#!/usr/local/bin/python2
# coding=UTF8
import math
from telnetlib import Telnet
import logging
import re

from swconfig import telnet_user, telnet_password


class Port:
    _factors = {
        'gpon': {
            't': 125,
            'psh': 8,
            'c': 0,
        },
        'ethernet': {
            't': 7,
            'psh': 6,
            'c': 0,
        },
    }

    def __init__(self, port):
        try:
            self.__index = int(port)
            self.__technology, self.__frame, self.__slot, self.__port = self.get_port_from_index(self.__index)
        except ValueError:
            port_data = re.match(
                r'^(?P<technology>\S*)(?P<frameid>0)/(?P<slotid>\d{1,2})/(?P<portid>\d{1,2})$', port)
            if port_data:
                self.__technology = port_data.group('technology')
                self.__frame = int(port_data.group('frameid'))
                self.__slot = int(port_data.group('slotid'))
                self.__port = int(port_data.group('portid'))
                self.__index = self.get_index(self.__technology, self.__frame, self.__slot, self.__port)
            else:
                raise ValueError("incorrect port number")

    def __repr__(self):
        return '{} (ifIndex: {})'.format(self, self.__index)

    def __str__(self):
        return '{}{}/{}/{}'.format(self.__technology, self.__frame, self.__slot, self.__port)

    @property
    def index(self):
        return self.__index

    @property
    def frame(self):
        return self.__frame

    @property
    def slot(self):
        return self.__slot

    @property
    def port(self):
        return self.__port

    @classmethod
    def get_index(cls, technology, frame, slot, port):
        if technology not in cls._factors:
            raise ValueError("incorrect technology")
        if frame > 0:
            raise ValueError("frameid can't be greater than 0")
        if slot > 22:
            raise ValueError("slotid can't be greater than 22")
        if port > 47:
            raise ValueError("portid can't be greater than 47")

        t = cls._factors[technology]['t']
        psh = cls._factors[technology]['psh']
        c = cls._factors[technology]['c']
        return (t << 25) + (frame << 19) + (slot << 13) + (port << psh) + c

    @classmethod
    def get_port_from_index(cls, index):
        technology = 'ethernet' if index < 4194304000 else 'gpon'

        # Frameid always 0. I did not find the case when frameid is grater than 0.
        frame = 0

        for slot in range(23):
            new_index = cls.get_index(technology, frame, slot, 0)
            if new_index > index:
                slot -= 1
                break

        for port in range(48):
            new_index = cls.get_index(technology, frame, slot, port)
            if new_index > index:
                port -= 1
                break

        return technology, frame, slot, port


def snr_diag_parser(incoming_value, host):
    """
    Приводит диагностику порта в формате SNR к виду похожему на формат D-Link.

    :param dict incoming_value: словарь с диагностикой от SNR
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словарь с диагностикой в формате D-Link
    """

    # словарик для сопоставления числового и строкового статусов
    statuses = {'well': 0,
                'open': 1,
                'short': 2,
                'abnormal': 3,
                'fail': 4}

    # получаем индекс порта и строку с результатами диагностики из входящих данных
    port_index, input_diag = incoming_value['cableDiag'].popitem()

    # паттерн для строк вида "(1, 2)          open\t\t          0"
    pair_pattern = re.compile(r'^(?P<pair>\(\d,\s\d\))\s+(?P<status>\S+)\s+(?P<length>\d+)$')

    vct_result = {'cdLinkStatus': incoming_value['ActualStatus']}

    diag_line_index = 0  # индекс строки с состоянием пары (для определения номера пары)
    for line in input_diag.splitlines():
        pair_match = pair_pattern.match(line)
        if pair_match:
            diag_line_index += 1
            vct_result['cdPair{}Status'.format(diag_line_index)] = {
                str(port_index): statuses[pair_match.group('status')]}
            vct_result['cdPair{}Length'.format(diag_line_index)] = {str(port_index): pair_match.group('length')}

    return vct_result


def dlink_clear_errors_on_port(incoming_value, host):
    """
    Посылает на коммутатор D-Link команды для сброса количества ошибок на порту.

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с результатом выполнения сброса
    """

    # получаем индекс порта и количество CRC ошибок
    port_index, input_crc_count = incoming_value['CRC'].popitem()

    try:
        conn = Telnet(host, port=23, timeout=3)

        # если подключение прошло успешно, то передаем логин/пароль пользователя
        conn.write(telnet_user.encode('ascii') + b'\n')
        conn.write(telnet_password.encode('ascii') + b'\n')

        # шлем команду на сброс счетчиков
        clear_command = 'clear counters ports {}'.format(port_index)
        conn.write(clear_command.encode('ascii') + b'\n')

        # разлогиниваемся
        conn.write(b'logout\n')
        logging.debug(conn.read_all())
    except Exception as err:
        logging.exception(err)
        return {'clear_errors': {str(port_index): 'Failed'}}
    else:
        return {'clear_errors': {str(port_index): 'Success'}}


def snr_clear_errors_on_port(incoming_value, host):
    """
    Посылает на коммутатор SNR команды для сброса количества ошибок на порту.

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с результатом выполнения сброса
    """

    # получаем индекс порта и количество CRC ошибок
    port_index, input_crc_count = incoming_value['CRC'].popitem()

    try:
        conn = Telnet(host, port=23, timeout=3)
        conn.read_until(b'login:', timeout=3)

        # если подключение прошло успешно, то передаем логин/пароль пользователя
        conn.write(telnet_user.encode('ascii') + b'\n')
        conn.write(telnet_password.encode('ascii') + b'\n')

        # шлем команду на сброс счетчиков
        clear_command = 'clear counters interface ethernet 1/0/{}'.format(port_index)
        conn.write(clear_command.encode('ascii') + b'\n')

        # разлогиниваемся
        conn.write(b'exit\n')
        logging.debug(conn.read_all())
    except Exception as err:
        logging.exception(err)
        return {'clear_errors': {str(port_index): 'Failed'}}
    else:
        return {'clear_errors': {str(port_index): 'Success'}}


def repair_big_indexes(incoming_value, host):
    """
    Устройства Huawei серии MA5600 из-за особенностей формирования индекса по SNMP отдают некоторые индексы
    отрицательными (не помещаются в Integer). Этот хелпер это исправляет. А так же отрезает данные с маленькими
    индексами (vlanif и прочие ненужные интерфейсы).

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с результатом выполнения сброса
    """

    new_port_indexes = {key_index: key_index for key_index, val_index in incoming_value['PortIndex'].iteritems() if
                        int(key_index) > 234881024}
    incoming_value['PortIndex'] = new_port_indexes
    return incoming_value


def remove_small_indexes(incoming_value, host):
    """
    Этот хелпер отрезает данные с маленькими индексами (vlanif и прочие ненужные интерфейсы).

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с результатом выполнения сброса
    """

    for dict_name, values_dict in incoming_value.iteritems():
        new_values = {key_index: val_index for key_index, val_index in incoming_value[dict_name].iteritems() if
                      int(key_index) > 234881024}
        incoming_value[dict_name] = new_values
    return incoming_value


def fake_board_index(incoming_value, host):
    """
    Этот хелпер заменяет индексы для плат в соответствии с логикой PortViewer2.

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с результатом выполнения сброса
    """

    boards_tech = {
        'H805GPFD': 'gpon',
        'H802SCUN': 'ethernet',
        'H801X2CS': 'ethernet',
    }

    new_data = {}

    for board_index, board_name in incoming_value['BoardDescr'].iteritems():
        board = re.match(r'(?P<model>\w*)_(?P<frameid>\d{1,2})_(?P<slotid>\d{1,2})', board_name)
        first_index = Port.get_index(boards_tech[board.group('model')], int(board.group('frameid')),
                                     int(board.group('slotid')), 0)
        print(first_index)
        pv_slotid = int(math.ceil(first_index / 12032.0))
        print(pv_slotid)
        new_data[str(pv_slotid)] = board.group('model')

    incoming_value['BoardDescr'] = new_data
    return incoming_value

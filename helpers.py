#!/usr/local/bin/python2
# coding=UTF8

import re
from telnetlib import Telnet
import logging

from swconfig import telnet_user, telnet_password


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
    new_port_indexes = {key_index: key_index for key_index, val_index in incoming_value['PortIndex'].iteritems()}
    incoming_value['PortIndex'] = new_port_indexes
    return incoming_value

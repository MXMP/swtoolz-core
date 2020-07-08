import math
from telnetlib import Telnet
import logging
import re
import time
import easysnmp
from easysnmp.exceptions import EasySNMPTimeoutError, EasySNMPError


from swconfig import telnet_user, telnet_password, users, snmp_retries, snmp_timeout, dyn_port_idx_update_interval

gDynamicSNMPIndex = {}


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
        if index < 234881024:
            raise ValueError("Wrong index")

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

    new_port_indexes = {key_index: key_index for key_index, val_index in incoming_value['PortIndex'].items() if
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

    for dict_name, values_dict in incoming_value.items():
        new_values = {key_index: val_index for key_index, val_index in incoming_value[dict_name].items() if
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
        'H801GPBC': 'gpon',
        'H802GPBD': 'gpon',
        'H805GPBD': 'gpon',
        'H806GPBH': 'gpon',
        'H807GPBH': 'gpon',
        'H802GPFD': 'gpon',
        'H805GPFD': 'gpon',
        'H801GPMD': 'gpon',
        'H807GPBD': 'gpon',
        'H802SCUN': 'ethernet',
        'H801X2CS': 'ethernet',
    }

    new_data = {}

    for board_index, board_name in incoming_value['BoardDescr'].items():
        board = re.match(r'(?P<model>\w*)_(?P<frameid>\d{1,2})_(?P<slotid>\d{1,2})', board_name)
        first_index = Port.get_index(boards_tech[board.group('model')], int(board.group('frameid')),
                                     int(board.group('slotid')), 0)
        pv_slotid = int(math.floor(first_index / 8192.0)) + 1
        new_data[str(pv_slotid)] = board.group('model')

    incoming_value['BoardDescr'] = new_data
    return incoming_value


def make_dynamic_map(incoming_value, host):
    """
    Этот формирует карту портов "DeviceMap" по индексам портов.

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с картой портов
    """

    ports = {}
    map = []

    for index in sorted(incoming_value['PortName'], key=int):
        try:
            port = Port(index)
        except ValueError:
            continue
        else:
            if port.slot not in ports:
                ports[port.slot] = []
            ports[port.slot].append(str(port.index))

    for slot in sorted(ports):
        map.append([ports[slot]])

    return {'DeviceMap': map}


def make_dynamic_map_for_6509(incoming_value, host):
    """
    Этот формирует карту портов "DeviceMap" по индексам портов для Cisco WS-C6509-E

    :param dict incoming_value: словарь с входящими данными
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словать с картой портов
    """

    ports = {}
    map = []

    for index, port_name in incoming_value['PortName'].items():
        if port_name.startswith('Gi') or port_name.startswith('Te'):
            try:
                slot, port_number = [int(n) for n in port_name[2:].split('/')]
            except ValueError:
                continue
            else:
                if slot not in ports:
                    ports[slot] = []
                ports[slot].append(str(index))

    for slot in sorted(ports):
        map.append([ports[slot][i:i+12] for i in range(0, len(ports[slot]), 12)])

    return {'DeviceMap': map}

def make_ports_for_nexus(incoming_value, host):
    map = {}
    for name in incoming_value:
        ports = {}
        for index, port_name in sorted(incoming_value[name].items()):
            if int(index)>=436207616:
                port_name = port_name.replace('Ethernet','Eth')
                port_idx = int((int(index) - 436207616)/4096) + 1
                if name == 'PortIndex':
                    ports[port_idx]=port_idx
                else:
                    ports[port_idx]=port_name
                map[name] = ports
    return map

def make_redback_ports(incoming_value, host):
#заполняем словарь типа порта одним и тем же значением (fiber)
    incoming_value['MediumType']=dict.fromkeys(range(1,25), 6)
    incoming_value['AdminSpeed']=incoming_value['ActualSpeed']
    incoming_value['AdminFlow']=dict.fromkeys(range(1,25), 1)
    return incoming_value

def update_dynamic_snmp_ports_qfx(host):
    ticks = time.time()
    if host not in gDynamicSNMPIndex or ticks-gDynamicSNMPIndex[host]['ticks']>dyn_port_idx_update_interval:
        ports={}
        session = easysnmp.Session(hostname=host, community=users['journal']['1'], version=2,
                               retries=snmp_retries, use_numeric=True, timeout=snmp_timeout)
        try:
        # Выполняем опрос параметров из default_info
            snmp_response = session.walk('.1.3.6.1.2.1.31.1.1.1.1')
        except EasySNMPTimeoutError as err:
            logging.exception(err)
            pass
        else:
            for x in snmp_response:
                match=re.search('[gx]e\-0\/0\/([0-9]+)$', x.value)
                if match:
                    ports[x.oid_index]=match.group(1)

        gDynamicSNMPIndex[host]={'ticks':ticks,'ports':ports}
        logging.debug(gDynamicSNMPIndex)
    else:
        logging.debug('cached')
    return



def make_ports_for_qfx5120(incoming_value, host):
    update_dynamic_snmp_ports_qfx(host)
    qfx5120ports=gDynamicSNMPIndex[host]['ports']
    map = {}
    for name in incoming_value:
        ports = {}
        for index, port_name in sorted(incoming_value[name].items()):
            try:
                journalkey = qfx5120ports.get(index)
                if journalkey is not None:
                    port_name = port_name.replace('Ethernet','Eth')
                    port_idx = journalkey
                    if name == 'PortIndex':
                        ports[port_idx]=port_idx
                    else:
                        ports[port_idx]=port_name
                    map[name] = ports
            except KeyError:
                logger.error("Can't find index {index}.")
    return map

def huawei_fdb(incoming_value, host):
    """
    Преобразовывает огромную HEX-STRING от шасси и разбивает ее по определенным правилам На удобочитаемую структуру.
    На выходе: ключи первого уровня - номера портов ONT, ключи второго уровря - номера виланов. Пример:
        "1": {
            "586": [
                "F8:4D:FC:22:3C:67"
                ]
        }

    :param str incoming_value: входящая HEX-STRING
    :param str host: ip-адрес устройства для которого выполняется запрос
    :return: структура с MAC-адресами
    """

    macs = {}
    _, all_macs = incoming_value['macs'].popitem()
    for i in range(0, len(all_macs), 20):
        item = all_macs[i:i + 20]
        if item != '00000000000000000000':
            mac_addr = ':'.join(split_nth(item[-12:], 2))
            port_id = int(item[2:4], 16)
            vlanid = int(item[4:8], 16)
            if port_id not in macs:
                macs[port_id] = {vlanid: [mac_addr]}
            else:
                if vlanid not in macs[port_id]:
                    macs[port_id][vlanid] = [mac_addr]
                else:
                    macs[port_id][vlanid].append(mac_addr)
    return {'macs': macs}


def split_nth(input_string, n):
    """ Просто разбивает строку на кусочки по `n` символов.

    :param str input_string: входная строка
    :param int n: по сколько символов разбивать строку
    :rtype: list
    :return: список подстрок по `n` символов
    """

    return [input_string[i:i + n] for i in range(0, len(input_string), n)]


def hex_string(input_string):
    """
    Возвращает HEX-STRING.

    :param str input_string: строка для преобразования в HEX
    :rtype: str
    :return: HEX-STRING
    """

    return ''.join([f'{ord(c):02X}' for c in input_string])


def ljust_string(input_string):
    """
    Добавляет нулей к входной строке до 16 символов. Используется в основоном для масок портов.

    :param input_string: входная строка
    :rtype: str
    :return: строка дополненная нулями до 16 символов
    """

    return hex_string(input_string).ljust(16, '0')


def mac(input_string):
    """
    Входную строку превращает в HEX-STRING и форматирует как MAC-адрес (через ':').

    :param str input_string: входная строка
    :rtype: str
    :return: MAC-адрес
    """

    return ':'.join(split_nth(hex_string(input_string), 2))


def make_items(input_dict):
    """
    Преобразует входной словарь с метриками в словарь с сущностями :)

    Пример:
    на входе
    {
        'sn': {'0': '485754432D9B039B', '1': '44443132B35CF35D'},
        'line-profile-name': {'0': 'activate', '1': 'line-P000-VLAN2200'},
        'srv-profile-name': {'0': 'activate', '1': 'srv-P000-VLAN2200'}
    }
    на выходе
    {
        '0': {
            'sn': '485754432D9B039B', 'line-profile-name': 'activate', 'srv-profile-name': 'activate'
        },
        '1': {
            'sn': '44443132B35CF35D', 'line-profile-name': 'line-P000-VLAN2200', 'srv-profile-name': 'srv-P000-VLAN2200'
        },
    }

    :param dict input_dict: входной словарь
    :rtype: dict
    :return: выходной словарь
    """

    items = {}

    for property_name, values_dict in input_dict.items():
        for ont_number, value in values_dict.items():
            if ont_number not in items:
                items[ont_number] = {}

            items[ont_number][property_name] = value

    return items


def huawei_get_inactive_onts(input_value, host=None):
    """
    Выбирает серийные номера ONT к которым привязаны line-profile и srv-profile с имененм "activate".

    :param dict input_value: входные данные
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словарь с серийниками "незарегистрированных" ONT
    """

    inactive_onts = {}
    onts = make_items(input_value)
    for ont_id, ont_info in onts.items():
        if ont_info['line-profile-name'] == 'activate' and ont_info['srv-profile-name'] == 'activate':
            inactive_onts[ont_id] = ont_info['sn']

    return {'sn': inactive_onts}


def huawei_get_service_ports(input_value, host=None):
    """
    Превращает несвязанные данные о сервисных портах в словарь с информацией о сервисных портах.

    :param dict input_value: входные данные
    :param str host: ip-адрес устройства для которого выполняется запрос
    :rtype: dict
    :return: словарь с сервисными портами
    """

    return {'service_ports': make_items(input_value)}


def str_from_index(input_string):
    """
    Возвращает человекопонятную строку из SNMP-индекса.

    Например, на входе - '108.105.110.101.45.80.48.48.48.45.86.76.65.78.50.48.48.48', на выходе - 'line-P000-VLAN2000'

    :param input_string:
    :return:
    """
    return ''.join([chr(int(p)) for p in input_string.split('.')])


def huawei_walk_profiles(input_value, host=None):
    """
    Ключами выходного словаря запроса профилей являются SNMP-индексы, мы их преобразовываем в строку и возвращаем в
    виде списка.

    :param input_value:
    :param host:
    :return:
    """
    for command_name, profiles_dict in input_value.items():
        return {command_name: [str_from_index(profile_index) for profile_index, _ in profiles_dict.items()]}

def eltex_walk_user_helper(input_val, host=None):
    if input_val.get('tableOfGroupUsers') is None:
        return {'tableOfGroupUsers': {}}
    keys = {
        '3' : "UserID",
        '4' : "RegState",
        '5' : "NumPlan",
        '6' : "Number",
        '7' : "IP",
        '8' : "Port",
        '9' : "SIP-Domain",
        '10' : "MaxActiveLines",
        '11' : "ActiveCallCount",
        '12' : "RegExpires",
    }
    result = {}
    for key, val in input_val['tableOfGroupUsers'].items():
        index = key.split('.')[0]
        if keys.get(index) is None:
            continue
        result[keys[index]] = val
    return {'tableOfGroupUsers': result}
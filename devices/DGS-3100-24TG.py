# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 20

# Карта портов устройства. Преставлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1','3','5','7','9', '11','13','15','17','19','21','23'],
	['2','4','6','8','10','12','14','16','18','20','22','24']
    ],
    [
	['51','53','55','57','59','61','63','65','67','69','71','73'],
	['52','54','56','58','60','62','64','66','68','70','72','74']
    ],
    [
	['101','103','105','107','109','111','113','115','117','119','121','123'],
	['102','104','106','108','110','112','114','116','118','120','122','124']
    ],
    [
	['151','153','155','157','159','161','163','165','167','169','171','173'],
	['152','154','156','158','160','162','164','166','168','170','172','174']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# Stackable - поддерживает ли устройство стекирование.
# Chassis - является ли устройство модульным шасси.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
    'SlotSize'   : '50',
    'ShiftIndex' : '0',
#    'MaxIndex'        : '64',
    'Stackable'  : 'True',
    'Chassis'    : 'False',
    },)

# Список рекомендуемых команд
Commands = ([
    'StackInfo',
    'MediumType',
    'ActualStatus',
    'ActualSpeed',
    'AdminStatus',
    'AdminSpeed',
    'AdminFlow',
    'get_PortIndex_U1U2',
    'get_PortIndex_U3U4',
#    'walk_PortIndex',
    ],)

# swIfTransceiverType
MediumType = ({
    '1' : 'copper',
    '2' : 'fiber',
    },)

# ifOperStatus
ActualStatus = ({
    '1' : 'linkup',
    '2' : 'linkdown',
    },)

# ifHighSpeed
ActualSpeed = ({
    '0'    : 'linkdown',
    '10'   : '10M',
    '100'  : '100M',
    '1000' : '1G',
    },)

# ifAdminStatus
AdminStatus = ({
    '1' : 'enabled',
    '2' : 'disabled',
    },)

# swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities (placeholder)
AdminSpeed = ({
    '0' : 'auto',
    },)

# swIfFlowControlMode
AdminFlow = ({
    '1' : 'enabled',
    '2' : 'disabled',
    '3' : 'auto',
    },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
    '0' : 'n/a',
    },)

walk_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.10.94.89.89.43.1.1.1		swIfIndex
    'PortIndex'       : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1',
    }

get_PortIndex_U1U2 = {
#    PortIndex           .1.3.6.1.4.1.171.10.94.89.89.43.1.1.1		swIfIndex
    'PortIndex.1'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.1',
    'PortIndex.2'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.2',
    'PortIndex.3'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.3',
    'PortIndex.4'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.4',
    'PortIndex.5'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.5',
    'PortIndex.6'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.6',
    'PortIndex.7'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.7',
    'PortIndex.8'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.8',
    'PortIndex.9'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.9',
    'PortIndex.10'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.10',
    'PortIndex.11'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.11',
    'PortIndex.12'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.12',
    'PortIndex.13'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.13',
    'PortIndex.14'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.14',
    'PortIndex.15'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.15',
    'PortIndex.16'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.16',
    'PortIndex.17'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.17',
    'PortIndex.18'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.18',
    'PortIndex.19'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.19',
    'PortIndex.20'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.20',
    'PortIndex.21'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.21',
    'PortIndex.22'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.22',
    'PortIndex.23'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.23',
    'PortIndex.24'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.24',
    'PortIndex.51'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.51',
    'PortIndex.52'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.52',
    'PortIndex.53'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.53',
    'PortIndex.54'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.54',
    'PortIndex.55'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.55',
    'PortIndex.56'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.56',
    'PortIndex.57'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.57',
    'PortIndex.58'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.58',
    'PortIndex.59'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.59',
    'PortIndex.60'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.60',
    'PortIndex.61'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.61',
    'PortIndex.62'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.62',
    'PortIndex.63'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.63',
    'PortIndex.64'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.64',
    'PortIndex.65'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.65',
    'PortIndex.66'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.66',
    'PortIndex.67'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.67',
    'PortIndex.68'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.68',
    'PortIndex.69'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.69',
    'PortIndex.70'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.70',
    'PortIndex.71'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.71',
    'PortIndex.72'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.72',
    'PortIndex.73'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.73',
    'PortIndex.74'    : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.74',
    }

get_PortIndex_U3U4 = {
#    PortIndex           .1.3.6.1.4.1.171.10.94.89.89.43.1.1.1		swIfIndex
    'PortIndex.101'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.101',
    'PortIndex.102'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.102',
    'PortIndex.103'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.103',
    'PortIndex.104'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.104',
    'PortIndex.105'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.105',
    'PortIndex.106'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.106',
    'PortIndex.107'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.107',
    'PortIndex.108'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.108',
    'PortIndex.109'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.109',
    'PortIndex.110'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.110',
    'PortIndex.111'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.111',
    'PortIndex.112'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.112',
    'PortIndex.113'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.113',
    'PortIndex.114'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.114',
    'PortIndex.115'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.115',
    'PortIndex.116'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.116',
    'PortIndex.117'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.117',
    'PortIndex.118'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.118',
    'PortIndex.119'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.119',
    'PortIndex.120'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.120',
    'PortIndex.121'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.121',
    'PortIndex.122'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.122',
    'PortIndex.123'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.123',
    'PortIndex.124'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.124',
    'PortIndex.151'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.151',
    'PortIndex.152'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.152',
    'PortIndex.153'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.153',
    'PortIndex.154'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.154',
    'PortIndex.155'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.155',
    'PortIndex.156'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.156',
    'PortIndex.157'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.157',
    'PortIndex.158'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.158',
    'PortIndex.159'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.159',
    'PortIndex.160'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.160',
    'PortIndex.161'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.161',
    'PortIndex.162'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.162',
    'PortIndex.163'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.163',
    'PortIndex.164'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.164',
    'PortIndex.165'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.165',
    'PortIndex.166'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.166',
    'PortIndex.167'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.167',
    'PortIndex.168'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.168',
    'PortIndex.169'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.169',
    'PortIndex.170'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.170',
    'PortIndex.171'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.171',
    'PortIndex.172'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.172',
    'PortIndex.173'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.173',
    'PortIndex.174'   : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.1.174',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.4.1.171.10.94.89.89.43.1.1.7		swIfTransceiverType
    'MediumType.'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.7.%s',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.'   : '.1.3.6.1.2.1.2.2.1.8.%s',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.'    : '.1.3.6.1.2.1.31.1.1.1.15.%s',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.'    : '.1.3.6.1.2.1.2.2.1.7.%s',
#    AdminSpeed          .1.3.6.1.4.1.171.10.94.89.89.43.1.1.40		swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities (placeholder)
#    'AdminSpeed.'     : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.40.%s',
#    AdminFlow           .1.3.6.1.4.1.171.10.94.89.89.43.1.1.14		swIfFlowControlMode
    'AdminFlow.'      : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.14.%s',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.171.10.94.89.89.43.1.1.7		swIfTransceiverType
    'MediumType'      : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.7',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus'    : '.1.3.6.1.2.1.2.2.1.8',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed'     : '.1.3.6.1.2.1.31.1.1.1.15',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus'     : '.1.3.6.1.2.1.2.2.1.7',
#    AdminSpeed          .1.3.6.1.4.1.171.10.94.89.89.43.1.1.40		swIfAdminSpeedDuplexAutoNegotiationLocalCapabilities (placeholder)
#    'AdminSpeed'      : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.40',
#    AdminFlow           .1.3.6.1.4.1.171.10.94.89.89.43.1.1.14		swIfFlowControlMode
    'AdminFlow'       : '.1.3.6.1.4.1.171.10.94.89.89.43.1.1.14',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_FDB_VLAN = {
#    FDB                 .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB'             : '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
    }

walk_VlanMap = {
#    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName'        : '.1.3.6.1.2.1.17.7.1.4.3.1.1',
#    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'EgressPorts'     : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_VlanEgressPorts = {
#    VEP                 .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'VEP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_VlanUntaggedPorts = {
#    VUP                 .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'VUP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.4',
    }

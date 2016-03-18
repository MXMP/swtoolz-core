# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Преставлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11','12','25','27'],
	['13','14','15','17','17','18','19','20','21','22','23','24','26','28']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# Stackable - поддерживает ли устройство стекирование.
# Chassis - является ли устройство модульным шасси.
StackInfo = ({
    'SlotSize'   : '48',
    'ShiftIndex' : '48',
    'MaxIndex'   : '100',
    'Stackable'  : 'False',
    'Chassis'    : 'False',
    },)

# Список рекомендуемых команд
Commands = ([
    'StackInfo',
    'MediumType',
    'ActualStatus',
    'ActualSpeed',
    'AdminStatus',
#    'AdminSpeed',
#    'AdminFlow',
    'BoardDescr',
    'get_PortIndex',
    'walk_ifName',
    ],)

# ifType
MediumType = ({
    '1'  : 'other',
    '6'  : 'copper',
    '24' : 'loopback',
    '53' : 'virtual',
    '131': 'tunnel',
    },)

# ifOperStatus
ActualStatus = ({
    '1' : 'linkup',
    '2' : 'linkdown',
    '3' : 'testing',
    '4' : 'unknown',
    '5' : 'dormant',
    '6' : 'notPresent',
    '7' : 'lowerLayerDown',
    },)

# ifHighSpeed
ActualSpeed = ({
    '0'    : 'linkdown',
    '10'   : '10M',
    '100'  : '100M',
    '1000' : '1G',
    '10000': '10G',
    },)

# ifAdminStatus
AdminStatus = ({
    '1' : 'enabled',
    '2' : 'disabled',
    '3' : 'testing',
    },)

# ifType (placeholder)
AdminSpeed = ({
    '1' : 'other',
    '6' : 'other',
    '24': 'other',
    '53': 'other',
    },)

# ifType (placeholder)
AdminFlow = ({
    '1' : 'disabled',
    '6' : 'disabled',
    '24': 'disabled',
    '53': 'disabled',
    },)

# UnitModuleName (placeholder)
BoardDescr = ({
    '1' : 'Eltex MES-2124',
    },)

walk_PortIndex = {
#    PortIndex           .1.3.6.1.2.1.2.2.1.1			ifIndex
    'PortIndex'       : '.1.3.6.1.2.1.2.2.1.1',
    }

get_PortIndex = {
#    PortIndex           .1.3.6.1.2.1.2.2.1.1			ifIndex
    'PortIndex.1'       : '.1.3.6.1.2.1.2.2.1.1.49',
    'PortIndex.2'       : '.1.3.6.1.2.1.2.2.1.1.50',
    'PortIndex.3'       : '.1.3.6.1.2.1.2.2.1.1.51',
    'PortIndex.4'       : '.1.3.6.1.2.1.2.2.1.1.52',
    'PortIndex.5'       : '.1.3.6.1.2.1.2.2.1.1.53',
    'PortIndex.6'       : '.1.3.6.1.2.1.2.2.1.1.54',
    'PortIndex.7'       : '.1.3.6.1.2.1.2.2.1.1.55',
    'PortIndex.8'       : '.1.3.6.1.2.1.2.2.1.1.56',
    'PortIndex.9'       : '.1.3.6.1.2.1.2.2.1.1.57',
    'PortIndex.10'       : '.1.3.6.1.2.1.2.2.1.1.58',
    'PortIndex.11'       : '.1.3.6.1.2.1.2.2.1.1.59',
    'PortIndex.12'       : '.1.3.6.1.2.1.2.2.1.1.60',
    'PortIndex.13'       : '.1.3.6.1.2.1.2.2.1.1.61',
    'PortIndex.14'       : '.1.3.6.1.2.1.2.2.1.1.62',
    'PortIndex.15'       : '.1.3.6.1.2.1.2.2.1.1.63',
    'PortIndex.16'       : '.1.3.6.1.2.1.2.2.1.1.64',
    'PortIndex.17'       : '.1.3.6.1.2.1.2.2.1.1.65',
    'PortIndex.18'       : '.1.3.6.1.2.1.2.2.1.1.66',
    'PortIndex.19'       : '.1.3.6.1.2.1.2.2.1.1.67',
    'PortIndex.20'       : '.1.3.6.1.2.1.2.2.1.1.68',
    'PortIndex.21'       : '.1.3.6.1.2.1.2.2.1.1.69',
    'PortIndex.22'       : '.1.3.6.1.2.1.2.2.1.1.70',
    'PortIndex.23'       : '.1.3.6.1.2.1.2.2.1.1.71',
    'PortIndex.24'       : '.1.3.6.1.2.1.2.2.1.1.72',
    'PortIndex.25'       : '.1.3.6.1.2.1.2.2.1.1.73',
    'PortIndex.26'       : '.1.3.6.1.2.1.2.2.1.1.74',
    'PortIndex.27'       : '.1.3.6.1.2.1.2.2.1.1.75',
    'PortIndex.28'       : '.1.3.6.1.2.1.2.2.1.1.76',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.2.1.2.2.1.3			ifType
    'MediumType.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8			ifOperStatus
    'ActualStatus.'   : '.1.3.6.1.2.1.2.2.1.8.%s',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15		ifHighSpeed
    'ActualSpeed.'    : '.1.3.6.1.2.1.31.1.1.1.15.%s',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7			ifAdminStatus
    'AdminStatus.'    : '.1.3.6.1.2.1.2.2.1.7.%s',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3			ifType (placeholder)
#    'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3			ifType (placeholder)
#    'AdminFlow.'      : '.1.3.6.1.2.1.2.2.1.3.%s',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18		ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.2.1.2.2.1.3			ifType
    'MediumType'      : '.1.3.6.1.2.1.2.2.1.3',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8			ifOperStatus
    'ActualStatus'    : '.1.3.6.1.2.1.2.2.1.8',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15		ifHighSpeed
    'ActualSpeed'     : '.1.3.6.1.2.1.31.1.1.1.15',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7			ifAdminStatus
    'AdminStatus'     : '.1.3.6.1.2.1.2.2.1.7',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3			ifType (placeholder)
#    'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3			ifType (placeholder)
#    'AdminFlow'       : '.1.3.6.1.2.1.2.2.1.3',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18		ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18		ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_ifName = {
#    PortName           .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName'       : '.1.3.6.1.2.1.31.1.1.1.1',
    }

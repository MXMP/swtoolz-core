# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    
       [
        ['1','3','5','7','9','11','13','15','17','19','21','23'],
        ['2','4','6','8','10','12','14','16','18','20','22','24'],
       ],[
        ['25','27','29','31','33','35','37','39','41','43','45','47'],
        ['26','28','30','32','34','36','38','40','42','44','46','48'],
       ],[
        ['49','51','53','55','57','59','61','63','65','67','69','71'],
        ['50','52','54','56','58','60','62','64','66','68','70','72'],
       ],[
        ['73','75','77','79','81','83','85','87','89','91','93','95'],
        ['74','76','78','80','82','84','86','88','90','92','94','96'],
       ],[
	['97','98','99','100','101','102','103','104']
       ]
    ],)

#DeviceMap = {
#    'helper': 'make_dynamic_map_for_nexus',
    # PortName   .1.3.6.1.2.1.31.1.1.1.1  ifName
#    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
#}


# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
    'SlotSize'   : '96',
#    'ShiftIndex' : '436207615',
    'ShiftIndex' : '0',
    'MaxIndex'   : '1014444403',
    },)

# Список рекомендуемых команд
Commands = ([
    'DeviceMap',
    'StackInfo',
    'MediumType',
    'ActualStatus',
    'ActualSpeed',
    'AdminStatus',
    'AdminSpeed',
    'AdminFlow',
    'BoardDescr',
    'walk_PortIndex',
    'walk_ifName',
    'walk_ifAlias',
    ],)

# ifType
MediumType = ({
    '1' : 'other',
    '6' : 'fiber',
    '24': 'loopback',
    '53': 'virtual',
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
    '40000': '40G',
    },)

# ifAdminStatus
AdminStatus = ({
    '1' : 'enabled',
    '2' : 'disabled',
    },)

# ifType (placeholder)
AdminSpeed = ({
    '1' : 'other',
    '6' : 'auto',
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
    '1' : 'N3K-C3132Q-40GX 96x10G',
    '2' : 'N3K-C3132Q-40GX 8x40G',
    },)

# walk_VlanEgressPorts (placeholder for Slava's Hardcode. not working but necessary)
walk_VlanEgressPorts = ({
    '0' : '',
    },)

get_HardwareRev = {
#    HardwareRev         .1.3.6.1.2.1.16.19.3.0				probeHardwareRev
    'HardwareRev.'    : '.1.3.6.1.2.1.16.19.3.0',
    }

walk_PortIndex = {
    'helper': 'make_ports_for_nexus32',
#    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex'       : '.1.3.6.1.2.1.2.2.1.1',
    }

get_SinglePort = {
    'helper': 'make_ports_for_nexus32',
#    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.'   : '.1.3.6.1.2.1.2.2.1.8.%s',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.'    : '.1.3.6.1.2.1.31.1.1.1.15.%s',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.'    : '.1.3.6.1.2.1.2.2.1.7.%s',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    'AdminFlow.'      : '.1.3.6.1.2.1.2.2.1.3.%s',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
    }

walk_AllPorts = {
    'helper': 'make_ports_for_nexus32',
#    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType'      : '.1.3.6.1.2.1.2.2.1.3',
#    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus'    : '.1.3.6.1.2.1.2.2.1.8',
#    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed'     : '.1.3.6.1.2.1.31.1.1.1.15',
#    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus'     : '.1.3.6.1.2.1.2.2.1.7',
#    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
#    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    'AdminFlow'       : '.1.3.6.1.2.1.2.2.1.3',
    }

walk_ifName = {
    'helper': 'make_ports_for_nexus32',
#    PortName            .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName'        : '.1.3.6.1.2.1.31.1.1.1.1',
    }

walk_ifAlias = {
    'helper': 'make_ports_for_nexus32',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

set_AdminStatus = [
#     .1.3.6.1.2.1.2.2.1.7						ifAdminStatus
    ['.1.3.6.1.2.1.2.2.1.7.%s', '', '%s', 'INTEGER'],
    ]

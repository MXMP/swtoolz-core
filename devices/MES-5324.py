# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 5

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '25', '26'],
                     ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '27', '28']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот.
# Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может
# начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
                 'SlotSize': '49',
                 'ShiftIndex': '0',
                 'MaxIndex': '49',
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
                'get_PortIndex',
                'PortName',
            ],)

# ifType
MediumType = ({
                  '1': 'other',
                  '6': 'fiber',
                  '24': 'loopback',
                  '53': 'virtual',
                  '131': 'tunnel',
              },)

# ifOperStatus
ActualStatus = ({
                    '1': 'linkup',
                    '2': 'linkdown',
                    '3': 'testing',
                    '4': 'unknown',
                    '5': 'dormant',
                    '6': 'notPresent',
                    '7': 'lowerLayerDown',
                },)

# ifHighSpeed
ActualSpeed = ({
                   '0': 'linkdown',
                   '10': '10M',
                   '100': '100M',
                   '1000': '1G',
                   '10000': '10G',
                   '40000': '40G',
               },)

# ifAdminStatus
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
               },)

# ifType (placeholder)
AdminSpeed = ({
                  '1': 'other',
                  '6': 'other',
                  '24': 'other',
                  '53': 'other',
              },)

# ifType (placeholder)
AdminFlow = ({
                 '1': 'disabled',
                 '6': 'disabled',
                 '24': 'disabled',
                 '53': 'disabled',
             },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'Eltex MES5324',
              },)

# ifName (placeholder)
PortName = ({
                '1': 'te1/0/1',
                '2': 'te1/0/2',
                '3': 'te1/0/3',
                '4': 'te1/0/4',
                '5': 'te1/0/5',
                '6': 'te1/0/6',
                '7': 'te1/0/7',
                '8': 'te1/0/8',
                '9': 'te1/0/9',
                '10': 'te1/0/10',
                '11': 'te1/0/11',
                '12': 'te1/0/12',
                '13': 'te1/0/13',
                '14': 'te1/0/14',
                '15': 'te1/0/15',
                '16': 'te1/0/16',
                '17': 'te1/0/17',
                '18': 'te1/0/18',
                '19': 'te1/0/19',
                '20': 'te1/0/20',
                '21': 'te1/0/21',
                '22': 'te1/0/22',
                '23': 'te1/0/23',
                '24': 'te1/0/24',
                '25': 'fo1/0/1',
                '26': 'fo1/0/2',
                '27': 'fo1/0/3',
                '28': 'fo1/0/4',
            },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
                       '0': 'n/a',
                   },)

walk_PortIndex = {
    #    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex': '.1.3.6.1.2.1.2.2.1.1',
}

get_PortIndex = {
    #    PortIndex           .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex.1': '.1.3.6.1.2.1.2.2.1.1.1',
    'PortIndex.2': '.1.3.6.1.2.1.2.2.1.1.2',
    'PortIndex.3': '.1.3.6.1.2.1.2.2.1.1.3',
    'PortIndex.4': '.1.3.6.1.2.1.2.2.1.1.4',
    'PortIndex.5': '.1.3.6.1.2.1.2.2.1.1.5',
    'PortIndex.6': '.1.3.6.1.2.1.2.2.1.1.6',
    'PortIndex.7': '.1.3.6.1.2.1.2.2.1.1.7',
    'PortIndex.8': '.1.3.6.1.2.1.2.2.1.1.8',
    'PortIndex.9': '.1.3.6.1.2.1.2.2.1.1.9',
    'PortIndex.10': '.1.3.6.1.2.1.2.2.1.1.10',
    'PortIndex.11': '.1.3.6.1.2.1.2.2.1.1.11',
    'PortIndex.12': '.1.3.6.1.2.1.2.2.1.1.12',
    'PortIndex.13': '.1.3.6.1.2.1.2.2.1.1.13',
    'PortIndex.14': '.1.3.6.1.2.1.2.2.1.1.14',
    'PortIndex.15': '.1.3.6.1.2.1.2.2.1.1.15',
    'PortIndex.16': '.1.3.6.1.2.1.2.2.1.1.16',
    'PortIndex.17': '.1.3.6.1.2.1.2.2.1.1.17',
    'PortIndex.18': '.1.3.6.1.2.1.2.2.1.1.18',
    'PortIndex.19': '.1.3.6.1.2.1.2.2.1.1.19',
    'PortIndex.20': '.1.3.6.1.2.1.2.2.1.1.20',
    'PortIndex.21': '.1.3.6.1.2.1.2.2.1.1.21',
    'PortIndex.22': '.1.3.6.1.2.1.2.2.1.1.22',
    'PortIndex.23': '.1.3.6.1.2.1.2.2.1.1.23',
    'PortIndex.24': '.1.3.6.1.2.1.2.2.1.1.24',
    'PortIndex.25': '.1.3.6.1.2.1.2.2.1.1.25',
    'PortIndex.26': '.1.3.6.1.2.1.2.2.1.1.26',
    'PortIndex.27': '.1.3.6.1.2.1.2.2.1.1.27',
    'PortIndex.28': '.1.3.6.1.2.1.2.2.1.1.28',
}

get_SinglePort = {
    #    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType.': '.1.3.6.1.2.1.2.2.1.3.%s',
    #    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.': '.1.3.6.1.2.1.2.2.1.8.%s',
    #    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.': '.1.3.6.1.2.1.31.1.1.1.15.%s',
    #    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.': '.1.3.6.1.2.1.2.2.1.7.%s',
    #    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
    #    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminFlow.'      : '.1.3.6.1.2.1.2.2.1.3.%s',
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.': '.1.3.6.1.2.1.31.1.1.1.18.%s',
}

walk_AllPorts = {
    #    MediumType          .1.3.6.1.2.1.2.2.1.3				ifType
    'MediumType': '.1.3.6.1.2.1.2.2.1.3',
    #    ActualStatus        .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus': '.1.3.6.1.2.1.2.2.1.8',
    #    ActualSpeed         .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed': '.1.3.6.1.2.1.31.1.1.1.15',
    #    AdminStatus         .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus': '.1.3.6.1.2.1.2.2.1.7',
    #    AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
    #    AdminFlow           .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    #    'AdminFlow'       : '.1.3.6.1.2.1.2.2.1.3',
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifAlias = {
    #    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifName = {
    #    PortName            .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
}

walk_FDB_VLAN = {
    #    FDB                 .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    #    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName': '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    #    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanEgressPorts = {
    #    VEP                 .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanUntaggedPorts = {
    #    VUP                 .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

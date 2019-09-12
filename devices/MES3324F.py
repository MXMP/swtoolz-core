# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 5

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '57', '59'],
                     ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '58', '60']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот.
# Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться,
# например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
                 'SlotSize': '108',
                 'ShiftIndex': '48',
                 'MaxIndex': '108',
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
                'getFirmwareVer'
            ],)

# swIfTransceiverType
MediumType = ({
                  '1': 'copper',
                  '2': 'fiber',
                  '3': 'copper', # comboRegular
                  '4': 'fiber', # comboFiberOptics
              },)

# ifOperStatus
ActualStatus = ({
                    '1': 'linkup',
                    '2': 'linkdown'
                },)

# ifHighSpeed
ActualSpeed = ({
                   '0': 'linkdown',
                   '10': '10M',
                   '100': '100M',
                   '1000': '1G',
                   '10000': '10G',
               },)

# ifAdminStatus
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
                   '3': 'testing'
               },)

# ifType (placeholder)
AdminSpeed = ({
                  '1': 'other',
                  '6': 'other',
                  '24': 'other',
                  '53': 'other',
              },)

# swIfFlowControlMode
AdminFlow = ({
                 '1': 'on',
                 '2': 'off',
                 '3': 'autoNegotiation',
                 '4': 'enabledRx',
                 '5': 'enabledTx'
             },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'Eltex MES3324F',
              },)

# ifName (placeholder)
PortName = ({
    '49': '1',
    '50': '2',
    '51': '3',
    '52': '4',
    '53': '5',
    '54': '6',
    '55': '7',
    '56': '8',
    '57': '9',
    '58': '10',
    '59': '11',
    '60': '12',
    '61': '13',
    '62': '14',
    '63': '15',
    '64': '16',
    '65': '17',
    '66': '18',
    '67': '19',
    '68': '20',
    '69': '21',
    '70': '22',
    '71': '23',
    '72': '24',
    '105': 'XG1',
    '106': 'XG2',
    '107': 'XG3',
    '108': 'XG4',
},)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = {
    # HardwareRev   .1.3.6.1.4.1.89.2.11.1   genGroupHWVersion
    'HardwareRev': '.1.3.6.1.4.1.89.2.11.1'
}

walk_PortIndex = {
    # PortIndex   .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex': '.1.3.6.1.2.1.2.2.1.1',
}

get_PortIndex = {
    # PortIndex     .1.3.6.1.2.1.2.2.1.1				ifIndex
    'PortIndex.1': '.1.3.6.1.2.1.2.2.1.1.49',
    'PortIndex.2': '.1.3.6.1.2.1.2.2.1.1.50',
    'PortIndex.3': '.1.3.6.1.2.1.2.2.1.1.51',
    'PortIndex.4': '.1.3.6.1.2.1.2.2.1.1.52',
    'PortIndex.5': '.1.3.6.1.2.1.2.2.1.1.53',
    'PortIndex.6': '.1.3.6.1.2.1.2.2.1.1.54',
    'PortIndex.7': '.1.3.6.1.2.1.2.2.1.1.55',
    'PortIndex.8': '.1.3.6.1.2.1.2.2.1.1.56',
    'PortIndex.9': '.1.3.6.1.2.1.2.2.1.1.57',
    'PortIndex.10': '.1.3.6.1.2.1.2.2.1.1.58',
    'PortIndex.11': '.1.3.6.1.2.1.2.2.1.1.59',
    'PortIndex.12': '.1.3.6.1.2.1.2.2.1.1.60',
    'PortIndex.13': '.1.3.6.1.2.1.2.2.1.1.61',
    'PortIndex.14': '.1.3.6.1.2.1.2.2.1.1.62',
    'PortIndex.15': '.1.3.6.1.2.1.2.2.1.1.63',
    'PortIndex.16': '.1.3.6.1.2.1.2.2.1.1.64',
    'PortIndex.17': '.1.3.6.1.2.1.2.2.1.1.65',
    'PortIndex.18': '.1.3.6.1.2.1.2.2.1.1.66',
    'PortIndex.19': '.1.3.6.1.2.1.2.2.1.1.67',
    'PortIndex.20': '.1.3.6.1.2.1.2.2.1.1.68',
    'PortIndex.21': '.1.3.6.1.2.1.2.2.1.1.69',
    'PortIndex.22': '.1.3.6.1.2.1.2.2.1.1.70',
    'PortIndex.23': '.1.3.6.1.2.1.2.2.1.1.71',
    'PortIndex.24': '.1.3.6.1.2.1.2.2.1.1.72',
    'PortIndex.te1': '.1.3.6.1.2.1.2.2.1.1.105',
    'PortIndex.te2': '.1.3.6.1.2.1.2.2.1.1.106',
    'PortIndex.te3': '.1.3.6.1.2.1.2.2.1.1.107',
    'PortIndex.te4': '.1.3.6.1.2.1.2.2.1.1.108',
}

get_SinglePort = {
    # MediumType    .1.3.6.1.4.1.89.43.1.1.7   swIfTransceiverType
    'MediumType.': '.1.3.6.1.4.1.89.43.1.1.7.%s',
    # ActualStatus    .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.': '.1.3.6.1.2.1.2.2.1.8.%s',
    # ActualSpeed    .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.': '.1.3.6.1.2.1.31.1.1.1.15.%s',
    # AdminStatus    .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus.': '.1.3.6.1.2.1.2.2.1.7.%s',
    # AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    # 'AdminSpeed.'     : '.1.3.6.1.2.1.2.2.1.3.%s',
    # AdminFlow    .1.3.6.1.4.1.89.43.1.1.14    swIfFlowControlMode
    'AdminFlow.': '.1.3.6.1.4.1.89.43.1.1.14.%s',
    # PortDescr    .1.3.6.1.2.1.31.1.1.1.18     ifAlias
    'PortDescr.': '.1.3.6.1.2.1.31.1.1.1.18.%s',
}

getFirmwareVer = {
    # 'FirmwareVer' .1.3.6.1.4.1.89.2.4    rndBrgVersion
    'FirmwareVer': '.1.3.6.1.4.1.89.2.4'
}

walk_AllPorts = {
    # MediumType   .1.3.6.1.4.1.89.43.1.1.7   swIfTransceiverType
    'MediumType': '.1.3.6.1.4.1.89.43.1.1.7',
    # ActualStatus   .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus': '.1.3.6.1.2.1.2.2.1.8',
    # ActualSpeed   .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed': '.1.3.6.1.2.1.31.1.1.1.15',
    # AdminStatus   .1.3.6.1.2.1.2.2.1.7				ifAdminStatus
    'AdminStatus': '.1.3.6.1.2.1.2.2.1.7',
    # AdminSpeed          .1.3.6.1.2.1.2.2.1.3				ifType (placeholder)
    # 'AdminSpeed'      : '.1.3.6.1.2.1.2.2.1.3',
    # AdminFlow   .1.3.6.1.4.1.89.43.1.1.14    swIfFlowControlMode
    'AdminFlow': '.1.3.6.1.4.1.89.43.1.1.14',
    # PortDescr   .1.3.6.1.2.1.31.1.1.1.18      ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifAlias = {
    # PortDescr   .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifName = {
    # PortName   .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
}

walk_FDB_VLAN = {
    # FDB   .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    # VlanName   .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName': '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    # EgressPorts   .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanEgressPorts = {
    # VEP   .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanUntaggedPorts = {
    # VUP   .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'hex_string:VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25'],
                     ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот.
# Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться,
# например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
                 'SlotSize': '26',
                 'ShiftIndex': '0',
                 'MaxIndex': 26,
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
                'PortName',
            ],)

# indicatesType
MediumType = ({
                  '1': 'other',
                  '2': 'hundredBaseTX',
                  '3': 'hundredBaseFX',
                  '4': 'thousandBaseSX',
                  '5': 'thousandBaseLX',
                  '6': 'copper',
                  '7': 'thousandBaseGBIC',
                  '8': 'fiber',
                  '9': 'hundredBaseFxScSingleMode',
                  '10': 'hundredBaseFxScMultiMode',
                  '11': 'thousandBaseCX',
                  '12': 'fiber',
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
               },)

# shutdown
AdminStatus = ({
                   '0': 'disabled',
                   '1': 'enabled',
               },)

# speedDuplex
AdminSpeed = ({
                  '0': 'auto',
                  '1': 'half10',
                  '2': 'full10',
                  '3': 'half100',
                  '4': 'full100',
                  '5': 'half1000',
                  '6': 'full1000',
                  '7': 'half-1000-M',
                  '8': 'half-1000-s',
                  '9': 'full-1000-M',
                  '10': 'full-1000-s',
                  '13': 'fx-100',
                  '14': 'fx-100-phy',
                  '15': 'fx-100-no-phy',
                  '16': 'neg-10-auto',
                  '17': 'neg-10-full',
                  '18': 'neg-10-half',
                  '19': 'neg-10-100-auto',
                  '20': 'neg-10-100-full',
                  '21': 'neg-10-100-half',
                  '22': 'neg-10-100-1000-full',
                  '23': 'neg-10-100-1000-half',
                  '24': 'neg-full-10g',
                  '25': 'full-10g',
                  '26': 'full-40g',
              },)

# flowControlStatus
AdminFlow = ({
                 '0': 'disabled',
                 '1': 'enabled',
             },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'SNR-S4550-24XQ-AC',
              },)

# ifName (placeholder)
PortName = ({
                '1': '1/0/1',
                '2': '1/0/2',
                '3': '1/0/3',
                '4': '1/0/4',
                '5': '1/0/5',
                '6': '1/0/6',
                '7': '1/0/7',
                '8': '1/0/8',
                '9': '1/0/9',
                '10': '1/0/10',
                '11': '1/0/11',
                '12': '1/0/12',
                '13': '1/0/13',
                '14': '1/0/14',
                '15': '1/0/15',
                '16': '1/0/16',
                '17': '1/0/17',
                '18': '1/0/18',
                '19': '1/0/19',
                '20': '1/0/20',
                '21': '1/0/21',
                '22': '1/0/22',
                '23': '1/0/23',
                '24': '1/0/24',
                '25': '1/1/1',
                '26': '1/2/1'
            },)

get_HardwareRev = {
    # HardwareRev    .1.3.6.1.4.1.40418.7.100.1.2   sysHardwareVersion
    'HardwareRev.': '.1.3.6.1.4.1.40418.7.100.1.2.0',
}

get_SoftwareVer = {
    # SoftwareVer    .1.3.6.1.4.1.40418.7.100.1.3   sysSoftwareVersion
    'SoftwareVer.': '.1.3.6.1.4.1.40418.7.100.1.3.0',
}

walk_PortIndex = {
    # PortIndex   .1.3.6.1.4.1.40418.7.100.3.2.1.1  portIndex
    'PortIndex': '.1.3.6.1.4.1.40418.7.100.3.2.1.1',
}

get_SinglePort = {
    # MediumType    .1.3.6.1.4.1.40418.7.100.3.2.1.17   indicatesType
    'MediumType.': '.1.3.6.1.4.1.40418.7.100.3.2.1.17.%s',
    # ActualStatus    .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus.': '.1.3.6.1.2.1.2.2.1.8.%s',
    # ActualSpeed    .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed.': '.1.3.6.1.2.1.31.1.1.1.15.%s',
    # AdminStatus    .1.3.6.1.4.1.40418.7.100.3.2.1.12  shutdown
    'AdminStatus.': '.1.3.6.1.4.1.40418.7.100.3.2.1.12.%s',
    # AdminSpeed    .1.3.6.1.4.1.40418.7.100.3.2.1.14   speedDuplex
    'AdminSpeed.': '.1.3.6.1.4.1.40418.7.100.3.2.1.14.%s',
    # AdminFlow    .1.3.6.1.4.1.40418.7.100.3.2.1.6 flowControlStatus
    'AdminFlow.': '.1.3.6.1.4.1.40418.7.100.3.2.1.6.%s',
    # PortDescr    .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.': '.1.3.6.1.2.1.31.1.1.1.18.%s',
}

walk_AllPorts = {
    # MediumType   .1.3.6.1.4.1.40418.7.100.3.2.1.17   indicatesType
    'MediumType': '.1.3.6.1.4.1.40418.7.100.3.2.1.17',
    # ActualStatus   .1.3.6.1.2.1.2.2.1.8				ifOperStatus
    'ActualStatus': '.1.3.6.1.2.1.2.2.1.8',
    # ActualSpeed   .1.3.6.1.2.1.31.1.1.1.15			ifHighSpeed
    'ActualSpeed': '.1.3.6.1.2.1.31.1.1.1.15',
    # AdminStatus    .1.3.6.1.4.1.40418.7.100.3.2.1.12  shutdown
    'AdminStatus': '.1.3.6.1.4.1.40418.7.100.3.2.1.12',
    # AdminSpeed   .1.3.6.1.4.1.40418.7.100.3.2.1.14   speedDuplex
    'AdminSpeed': '.1.3.6.1.4.1.40418.7.100.3.2.1.14',
    # AdminFlow   .1.3.6.1.4.1.40418.7.100.3.2.1.6  flowControlStatus
    # 'AdminFlow': '.1.3.6.1.4.1.40418.7.100.3.2.1.6',
    # PortDescr   .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifAlias = {
    # PortDescr   .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifName = {
    # PortName   .1.3.6.1.4.1.40418.7.100.3.2.1.2   portName
    'PortName': '.1.3.6.1.4.1.40418.7.100.3.2.1.2',
}

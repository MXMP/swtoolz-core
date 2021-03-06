# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23'],
                     ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '25', '26']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот.
# Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться,
# например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
                 'SlotSize': '64',
                 'ShiftIndex': '0',
                 'ComboDefMedType': 'copper',
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
                'PortType',
                'BoardDescr',
                'cdLinkStatus',
                'cdPairStatus',
                'get_PortIndex',
                'get_HardwareRev',
            ],)

# swL2PortInfoMediumType
MediumType = ({
                  '100': 'copper',
                  '101': 'fiber',
              },)

# swL2PortInfoLinkStatus
ActualStatus = ({
                    '1': 'other',
                    '2': 'linkup',
                    '3': 'linkdown',
                },)

# swL2PortInfoNwayStatus
ActualSpeed = ({
                   '1': 'linkdown',
                   '2': '10M-Half',
                   '3': '10M-Full',
                   '4': '100M-Half',
                   '5': '100M-Full',
                   '7': '1G-Full'
               },)

# swL2PortCtrlAdminState
AdminStatus = ({
                   '2': 'disabled',
                   '3': 'enabled',
               },)

# swL2PortCtrlNwayState
AdminSpeed = ({
                  '1': 'auto',
                  '2': '10M-Half',
                  '3': '10M-Full',
                  '4': '100M-Half',
                  '5': '100M-Full',
                  '7': '1G-Full',
                  '8': '1G-Full-master',
                  '9': '1G-Full-slave',
              },)

# swL2PortCtrlFlowCtrlState
AdminFlow = ({
                 '1': 'other',
                 '2': 'disabled',
                 '3': 'enabled',
             },)

# ifType
PortType = ({
                '1': 'other',
                '6': 'fastEthernet',
                '117': 'gigaEthernet',
            },)

# UnitModuleName (placeholder)
BoardDescr = ({
                  '1': 'DES-3200-26',
              },)

# swEtherCableDiagLinkStatus
cdLinkStatus = ({
                    '0': 'linkdown',
                    '1': 'linkup',
                    '2': 'other',
                },)

# swEtherCableDiagPairXStatus
cdPairStatus = ({
                    '0': 'ok',
                    '1': 'open',
                    '2': 'short',
                    '3': 'open-short',
                    '4': 'crosstalk',
                    '5': 'unknown',
                    '6': 'count',
                    '7': 'no-cable',
                    '8': 'other',
                },)

get_HardwareRev = {
    # HardwareRev    .1.3.6.1.2.1.16.19.3.0				probeHardwareRev
    'HardwareRev.': '.1.3.6.1.2.1.16.19.3.0',
}

walk_PortIndex = {
    # PortIndex   .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1		swL2PortInfoPortIndex
    'PortIndex': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1',
}

get_PortIndex = {
    # PortIndex        .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1      swL2PortInfoPortIndex
    'PortIndex..1':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.1.100',
    'PortIndex..2':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.2.100',
    'PortIndex..3':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.3.100',
    'PortIndex..4':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.4.100',
    'PortIndex..5':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.5.100',
    'PortIndex..6':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.6.100',
    'PortIndex..7':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.7.100',
    'PortIndex..8':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.8.100',
    'PortIndex..9':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.9.100',
    'PortIndex..10':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.10.100',
    'PortIndex..11':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.11.100',
    'PortIndex..12':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.12.100',
    'PortIndex..13':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.13.100',
    'PortIndex..14':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.14.100',
    'PortIndex..15':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.15.100',
    'PortIndex..16':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.16.100',
    'PortIndex..17':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.17.100',
    'PortIndex..18':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.18.100',
    'PortIndex..19':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.19.100',
    'PortIndex..20':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.20.100',
    'PortIndex..21':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.21.100',
    'PortIndex..22':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.22.100',
    'PortIndex..23':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.23.100',
    'PortIndex..24':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.24.100',
    'PortIndex..25c': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.25.100',
    'PortIndex..25f': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.25.101',
    'PortIndex..26c': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.26.100',
    'PortIndex..26f': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.1.26.101',
}

get_ifAlias = {
    # PortDescr        .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6      swL2PortCtrlDescription
    'PortDescr..1':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.1.100',
    'PortDescr..2':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.2.100',
    'PortDescr..3':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.3.100',
    'PortDescr..4':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.4.100',
    'PortDescr..5':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.5.100',
    'PortDescr..6':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.6.100',
    'PortDescr..7':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.7.100',
    'PortDescr..8':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.8.100',
    'PortDescr..9':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.9.100',
    'PortDescr..10':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.10.100',
    'PortDescr..11':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.11.100',
    'PortDescr..12':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.12.100',
    'PortDescr..13':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.13.100',
    'PortDescr..14':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.14.100',
    'PortDescr..15':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.15.100',
    'PortDescr..16':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.16.100',
    'PortDescr..17':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.17.100',
    'PortDescr..18':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.18.100',
    'PortDescr..19':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.19.100',
    'PortDescr..20':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.20.100',
    'PortDescr..21':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.21.100',
    'PortDescr..22':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.22.100',
    'PortDescr..23':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.23.100',
    'PortDescr..24':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.24.100',
    'PortDescr..25c': '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.25.100',
    'PortDescr..25f': '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.25.101',
    'PortDescr..26c': '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.26.100',
    'PortDescr..26f': '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.26.101',
}

get_ifName = {
    # PortName      .1.3.6.1.2.1.31.1.1.1.1      ifName
    'PortName.1':  '.1.3.6.1.2.1.31.1.1.1.1.1',
    'PortName.2':  '.1.3.6.1.2.1.31.1.1.1.1.2',
    'PortName.3':  '.1.3.6.1.2.1.31.1.1.1.1.3',
    'PortName.4':  '.1.3.6.1.2.1.31.1.1.1.1.4',
    'PortName.5':  '.1.3.6.1.2.1.31.1.1.1.1.5',
    'PortName.6':  '.1.3.6.1.2.1.31.1.1.1.1.6',
    'PortName.7':  '.1.3.6.1.2.1.31.1.1.1.1.7',
    'PortName.8':  '.1.3.6.1.2.1.31.1.1.1.1.8',
    'PortName.9':  '.1.3.6.1.2.1.31.1.1.1.1.9',
    'PortName.10': '.1.3.6.1.2.1.31.1.1.1.1.10',
    'PortName.11': '.1.3.6.1.2.1.31.1.1.1.1.11',
    'PortName.12': '.1.3.6.1.2.1.31.1.1.1.1.12',
    'PortName.13': '.1.3.6.1.2.1.31.1.1.1.1.13',
    'PortName.14': '.1.3.6.1.2.1.31.1.1.1.1.14',
    'PortName.15': '.1.3.6.1.2.1.31.1.1.1.1.15',
    'PortName.16': '.1.3.6.1.2.1.31.1.1.1.1.16',
    'PortName.17': '.1.3.6.1.2.1.31.1.1.1.1.17',
    'PortName.18': '.1.3.6.1.2.1.31.1.1.1.1.18',
    'PortName.19': '.1.3.6.1.2.1.31.1.1.1.1.19',
    'PortName.20': '.1.3.6.1.2.1.31.1.1.1.1.20',
    'PortName.21': '.1.3.6.1.2.1.31.1.1.1.1.21',
    'PortName.22': '.1.3.6.1.2.1.31.1.1.1.1.22',
    'PortName.23': '.1.3.6.1.2.1.31.1.1.1.1.23',
    'PortName.24': '.1.3.6.1.2.1.31.1.1.1.1.24',
    'PortName.25': '.1.3.6.1.2.1.31.1.1.1.1.25',
    'PortName.26': '.1.3.6.1.2.1.31.1.1.1.1.26',
}

get_SinglePort = {
    # MediumType        .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.2     swL2PortInfoMediumType
    'MediumType..c':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.2.%s.100',
    'MediumType..f':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.2.%s.101',
    # ActualStatus      .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus..c': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.4.%s.100',
    'ActualStatus..f': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.4.%s.101',
    # ActualSpeed       .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed..c':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.5.%s.100',
    'ActualSpeed..f':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.5.%s.101',
    # AdminStatus       .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3		swL2PortCtrlAdminState
    'AdminStatus..c':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3.%s.100',
    'AdminStatus..f':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3.%s.101',
    # AdminSpeed        .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed..c':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4.%s.100',
    'AdminSpeed..f':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4.%s.101',
    # AdminFlow         .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow..c':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.5.%s.100',
    'AdminFlow..f':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.5.%s.101',
    # PortDescr         .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6		swL2PortCtrlDescription
    'PortDescr..c':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.%s.100',
    'PortDescr..f':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6.%s.101',
    # PortType          .1.3.6.1.2.1.2.2.1.3				ifType
    'PortType.':       '.1.3.6.1.2.1.2.2.1.3.%s',
    # PortName          .1.3.6.1.2.1.31.1.1.1.1			ifName
    'PortName.':       '.1.3.6.1.2.1.31.1.1.1.1.%s',
}

walk_AllPorts = {
    # MediumType     .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.2		swL2PortInfoMediumType
    'MediumType':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.2',
    # ActualStatus   .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus': '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.4',
    # ActualSpeed    .1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.1.1.5',
    # AdminStatus    .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3		swL2PortCtrlAdminState
    'AdminStatus':  '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3',
    # AdminSpeed     .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed':   '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4',
    # AdminFlow      .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.5',
    # PortDescr      .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6		swL2PortCtrlDescription
    'PortDescr':    '.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.6',
}

walk_FDB_VLAN = {
    # FDB   .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    # VlanName                 .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName':               '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    # EgressPorts              .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanEgressPorts = {
    # VEP              .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_VlanUntaggedPorts = {
    # VUP              .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'hex_string:VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

# Ключи массива специально изменены для соответствия стандартам TIA!
# При таком изменении распиновка по парам у новых и старых моделей D-Link выглядит одинаково.
get_CableDiag = {
    # cdLinkStatus     .1.3.6.1.4.1.171.12.58.1.1.1.3			swEtherCableDiagLinkStatus
    'cdLinkStatus.':  '.1.3.6.1.4.1.171.12.58.1.1.1.3.%s',
    # cdPair1Status    .1.3.6.1.4.1.171.12.58.1.1.1.4			swEtherCableDiagPair1Status
    'cdPair2Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.4.%s',
    # cdPair2Status    .1.3.6.1.4.1.171.12.58.1.1.1.5			swEtherCableDiagPair2Status
    'cdPair3Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.5.%s',
    # cdPair3Status    .1.3.6.1.4.1.171.12.58.1.1.1.6			swEtherCableDiagPair3Status
    'cdPair1Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.6.%s',
    # cdPair4Status    .1.3.6.1.4.1.171.12.58.1.1.1.7			swEtherCableDiagPair4Status
    'cdPair4Status.': '.1.3.6.1.4.1.171.12.58.1.1.1.7.%s',
    # cdPair1Length    .1.3.6.1.4.1.171.12.58.1.1.1.8			swEtherCableDiagPair1Length
    'cdPair2Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.8.%s',
    # cdPair2Length    .1.3.6.1.4.1.171.12.58.1.1.1.9			swEtherCableDiagPair2Length
    'cdPair3Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.9.%s',
    # cdPair3Length    .1.3.6.1.4.1.171.12.58.1.1.1.10		swEtherCableDiagPair3Length
    'cdPair1Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.10.%s',
    # cdPair4Length    .1.3.6.1.4.1.171.12.58.1.1.1.11		swEtherCableDiagPair4Length
    'cdPair4Length.': '.1.3.6.1.4.1.171.12.58.1.1.1.11.%s',
}

get_Errors = {
    # CRC                   .1.3.6.1.2.1.16.1.1.1.8			etherStatsCRCAlignErrors
    'CRC.':                '.1.3.6.1.2.1.16.1.1.1.8.%s',
    # Undersize             .1.3.6.1.2.1.16.1.1.1.9			etherStatsUndersizePkts
    'Undersize.':          '.1.3.6.1.2.1.16.1.1.1.9.%s',
    # Oversize              .1.3.6.1.2.1.16.1.1.1.10			etherStatsOversizePkts
    'Oversize.':           '.1.3.6.1.2.1.16.1.1.1.10.%s',
    # Fragment              .1.3.6.1.2.1.16.1.1.1.11			etherStatsFragments
    'Fragment.':           '.1.3.6.1.2.1.16.1.1.1.11.%s',
    # Jabber                .1.3.6.1.2.1.16.1.1.1.12			etherStatsJabbers
    'Jabber.':             '.1.3.6.1.2.1.16.1.1.1.12.%s',
    # ExcessiveDefferal     .1.3.6.1.2.1.10.7.2.1.7			dot3StatsDeferredTransmissions
    'ExcessiveDefferal.':  '.1.3.6.1.2.1.10.7.2.1.7.%s',
    # LateCollision         .1.3.6.1.2.1.10.7.2.1.8			dot3StatsLateCollisions
    'LateCollision.':      '.1.3.6.1.2.1.10.7.2.1.8.%s',
    # ExcessiveCollision    .1.3.6.1.2.1.10.7.2.1.9			dot3StatsExcessiveCollisions
    'ExcessiveCollision.': '.1.3.6.1.2.1.10.7.2.1.9.%s',
    # SingleCollision       .1.3.6.1.2.1.10.7.2.1.4			dot3StatsSingleCollisionFrames
    'SingleCollision.':    '.1.3.6.1.2.1.10.7.2.1.4.%s',
    # Collision             .1.3.6.1.2.1.16.1.1.1.13			etherStatsCollisions
    'Collision.':          '.1.3.6.1.2.1.16.1.1.1.13.%s',
}

get_InOutOctets = {
    # InOctets     .1.3.6.1.2.1.31.1.1.1.6			ifHCInOctets
    'InOctets.':  '.1.3.6.1.2.1.31.1.1.1.6.%s',
    # OutOctets    .1.3.6.1.2.1.31.1.1.1.10			ifHCOutOctets
    'Outoctets.': '.1.3.6.1.2.1.31.1.1.1.10.%s',
}

clear_errors = {
    # Send telnet commands to device
    'helper': 'dlink_clear_errors_on_port',
    # CRC    .1.3.6.1.2.1.16.1.1.1.8    etherStatsCRCAlignErrors
    'CRC.': '.1.3.6.1.2.1.16.1.1.1.8.%s',
}

set_AdminStatus = [
    # .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3				swL2PortCtrlAdminState
    ['.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.3.%s', '100', '%s', 'INTEGER'],
]

set_AdminSpeed = [
    # .1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4				swL2PortCtrlNwayState
    ['.1.3.6.1.4.1.171.11.113.1.5.2.2.2.1.4.%s', '100', '%s', 'INTEGER'],
]

set_CableDiagInit = [
    # .1.3.6.1.4.1.171.12.58.1.1.1.12					swEtherCableDiagAction
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '%s', '1', 'INTEGER'],
]

set_SaveConfig = [
    # .1.3.6.1.4.1.171.12.1.2.6						agentSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.6', '0', '2', 'INTEGER'],
]

set_CreateVlan = [
    # .1.3.6.1.2.1.17.7.1.4.3.1.1					dot1qVlanStaticName
    ['.1.3.6.1.2.1.17.7.1.4.3.1.1', '{1}', '{2}', 'OCTETSTR'],
    # .1.3.6.1.2.1.17.7.1.4.3.1.2					dot1qVlanStaticEgressPorts
    ['.1.3.6.1.2.1.17.7.1.4.3.1.2', '{1}', '{3}', 'OCTETSTR'],
    # .1.3.6.1.2.1.17.7.1.4.3.1.5					dot1qVlanStaticRowStatus
    ['.1.3.6.1.2.1.17.7.1.4.3.1.5', '{1}', '4', 'INTEGER'],
]

set_IpifCfg = [
    # .1.3.6.1.4.1.171.11.113.1.5.2.1.2.2				swL2DevCtrlSystemIP
    ['.1.3.6.1.4.1.171.11.113.1.5.2.1.2.2', '0', '{1}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.113.1.5.2.1.2.3				swL2DevCtrlSubnetMask
    ['.1.3.6.1.4.1.171.11.113.1.5.2.1.2.3', '0', '{2}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.113.1.5.2.1.2.4				swL2DevCtrlDefaultGateway
    ['.1.3.6.1.4.1.171.11.113.1.5.2.1.2.4', '0', '{3}', 'IPADDR'],
    # .1.3.6.1.4.1.171.11.113.1.5.2.1.2.5				swL2DevCtrlManagementVlanId
    ['.1.3.6.1.4.1.171.11.113.1.5.2.1.2.5', '0', '{4}', 'INTEGER'],
]

set_DHCP_RemoteID = [
    # .1.3.6.1.4.1.171.12.42.3.2.5					swDHCPRelayOption82RemoteID
    ['.1.3.6.1.4.1.171.12.42.3.2.5', '0', '{1}', 'OCTETSTR'],
]

set_CfgDownload = [
    # .1.3.6.1.4.1.171.12.1.2.1.1.3					agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '{1}', 'IPADDR'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.5					agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', '{2}', 'OCTETSTR'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.7					agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '3', 'INTEGER'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.8					agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.9					agentBscSwFileBIncrement
    ['.1.3.6.1.4.1.171.12.1.2.1.1.9', '3', '1', 'INTEGER'],
]

set_CfgUpload = [
    # .1.3.6.1.4.1.171.12.1.2.1.1.3					agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3', '3', '{1}', 'IPADDR'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.5					agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5', '3', '{2}', 'OCTETSTR'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.7					agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7', '3', '2', 'INTEGER'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.8					agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8', '3', '3', 'INTEGER'],
    # .1.3.6.1.4.1.171.12.1.2.1.1.9					agentBscSwFileBIncrement
    ['.1.3.6.1.4.1.171.12.1.2.1.1.9', '3', '1', 'INTEGER'],
]

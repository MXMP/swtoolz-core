# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Преставлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1','3','5','7',],
	['2','4','6','8','9','10']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# Stackable - поддерживает ли устройство стекирование.
# Chassis - является ли устройство модульным шасси.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
    'SlotSize'        : '64',
    'ShiftIndex'      : '0',
#    'MaxIndex'        : '64',
    'Stackable'       : 'False',
    'Chassis'         : 'False',
    'ComboDefMedType' : 'copper',
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
    'PortType',
    'cdLinkStatus',
    'cdPairStatus',
    'BoardDescr',
    'get_PortIndex',
    'get_HardwareRev',
    ],)

# swL2PortInfoMediumType
MediumType = ({
    '100' : 'copper',
    '101' : 'fiber',
    },)

# swL2PortInfoLinkStatus
ActualStatus = ({
    '1' : 'other',
    '2' : 'linkup',
    '3' : 'linkdown',
    },)

# swL2PortInfoNwayStatus
ActualSpeed = ({
    '1' : 'linkdown',
    '2' : '10M-Half',
    '3' : '10M-Full',
    '4' : '100M-Half',
    '5' : '100M-Full',
    '7' : '1G-Full'
    },)

# swL2PortCtrlAdminState
AdminStatus = ({
    '2' : 'disabled',
    '3' : 'enabled',
    },)

# swL2PortCtrlNwayState
AdminSpeed = ({
    '1' : 'auto',
    '2' : '10M-Half',
    '3' : '10M-Full',
    '4' : '100M-Half',
    '5' : '100M-Full',
    '7' : '1G-Full',
    '8' : '1G-Full-master',
    '9' : '1G-Full-slave',
    },)

# swL2PortCtrlFlowCtrlState
AdminFlow = ({
    '1' : 'other',
    '2' : 'disabled',
    '3' : 'enabled',
    },)

# ifType
PortType = ({
    '0'   : 'other',
    '6'   : 'fastEthernet',
    '117' : 'gigaEthernet',
    },)

# UnitModuleName (placeholder)
BoardDescr = ({
    '1' : 'DES-3200-18',
    },)

# swEtherCableDiagLinkStatus
cdLinkStatus = ({
    '0' : 'linkdown',
    '1' : 'linkup',
    '2' : 'other',
    },)

# swEtherCableDiagPairXStatus
cdPairStatus = ({
    '0' : 'ok',
    '1' : 'open',
    '2' : 'short',
    '3' : 'open-short',
    '4' : 'crosstalk',
    '5' : 'unknown',
    '6' : 'count',
    '7' : 'no-cable',
    '8' : 'other',
    },)

get_HardwareRev = {
#    HardwareRev         .1.3.6.1.2.1.16.19.3.0				probeHardwareRev
    'HardwareRev.'    : '.1.3.6.1.2.1.16.19.3.0',
    }

walk_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1		swL2PortInfoPortIndex
    'PortIndex'       : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1',
    }

get_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1		swL2PortInfoPortIndex
    'PortIndex..1'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.1.100',
    'PortIndex..2'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.2.100',
    'PortIndex..3'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.3.100',
    'PortIndex..4'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.4.100',
    'PortIndex..5'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.5.100',
    'PortIndex..6'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.6.100',
    'PortIndex..7'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.7.100',
    'PortIndex..8'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.8.100',
    'PortIndex..9c'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.9.100',
    'PortIndex..9f'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.9.101',
    'PortIndex..10c'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.10.100',
    'PortIndex..10f'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.1.10.101',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2		swL2PortInfoMediumType
    'MediumType..c'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2.%s.100',
    'MediumType..f'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2.%s.101',
#    ActualStatus        .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus..c' : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.4.%s.100',
    'ActualStatus..f' : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.4.%s.101',
#    ActualSpeed         .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed..c'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5.%s.100',
    'ActualSpeed..f'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5.%s.101',
#    AdminStatus         .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3		swL2PortCtrlAdminState
    'AdminStatus..c'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3.%s.100',
    'AdminStatus..f'  : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3.%s.101',
#    AdminSpeed          .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed..c'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.%s.100',
    'AdminSpeed..f'   : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.%s.101',
#    AdminFlow           .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow..c'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5.%s.100',
    'AdminFlow..f'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5.%s.101',
#    PortDescr           .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.6		swL2PortCtrlDescription
    'PortDescr..c'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.6.%s.100',
    'PortDescr..f'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.6.%s.101',
#    PortType            .1.3.6.1.2.1.2.2.1.3				ifType
    'PortType.'       : '.1.3.6.1.2.1.2.2.1.3.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2		swL2PortInfoMediumType
    'MediumType'      : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.4		swL2PortInfoLinkStatus
    'ActualStatus'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.4',
#    ActualSpeed         .1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5		swL2PortInfoNwayStatus
    'ActualSpeed'     : '.1.3.6.1.4.1.171.11.113.1.1.2.2.1.1.5',
#    AdminStatus         .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3		swL2PortCtrlAdminState
    'AdminStatus'     : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3',
#    AdminSpeed          .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4		swL2PortCtrlNwayState
    'AdminSpeed'      : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4',
#    AdminFlow           .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5		swL2PortCtrlFlowCtrlState
    'AdminFlow'       : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.5',
#    PortDescr        :  .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.6		swL2PortCtrlDescription
    'PortDescr'       : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.6',
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

get_CableDiag = {
#    cdLinkStatus        .1.3.6.1.4.1.171.12.58.1.1.1.3			swEtherCableDiagLinkStatus
    'cdLinkStatus.'   : '.1.3.6.1.4.1.171.12.58.1.1.1.3.%s',
#    cdPair1Status       .1.3.6.1.4.1.171.12.58.1.1.1.4			swEtherCableDiagPair1Status
    'cdPair1Status.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.4.%s',
#    cdPair2Status       .1.3.6.1.4.1.171.12.58.1.1.1.5			swEtherCableDiagPair2Status
    'cdPair2Status.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.5.%s',
#    cdPair3Status       .1.3.6.1.4.1.171.12.58.1.1.1.6			swEtherCableDiagPair3Status
    'cdPair3Status.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.6.%s',
#    cdPair4Status       .1.3.6.1.4.1.171.12.58.1.1.1.7			swEtherCableDiagPair4Status
    'cdPair4Status.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.7.%s',
#    cdPair1Length       .1.3.6.1.4.1.171.12.58.1.1.1.8			swEtherCableDiagPair1Length
    'cdPair1Length.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.8.%s',
#    cdPair2Length       .1.3.6.1.4.1.171.12.58.1.1.1.9			swEtherCableDiagPair2Length
    'cdPair2Length.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.9.%s',
#    cdPair3Length       .1.3.6.1.4.1.171.12.58.1.1.1.10		swEtherCableDiagPair3Length
    'cdPair3Length.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.10.%s',
#    cdPair4Length       .1.3.6.1.4.1.171.12.58.1.1.1.11		swEtherCableDiagPair4Length
    'cdPair4Length.'  : '.1.3.6.1.4.1.171.12.58.1.1.1.11.%s',
    }

get_Errors = {
#    CRC                    .1.3.6.1.2.1.16.1.1.1.8			etherStatsCRCAlignErrors
    'CRC.'               : '.1.3.6.1.2.1.16.1.1.1.8.%s',
#    Undersize              .1.3.6.1.2.1.16.1.1.1.9			etherStatsUndersizePkts
    'Undersize.'         : '.1.3.6.1.2.1.16.1.1.1.9.%s',
#    Oversize               .1.3.6.1.2.1.16.1.1.1.10			etherStatsOversizePkts
    'Oversize.'          : '.1.3.6.1.2.1.16.1.1.1.10.%s',
#    Fragment               .1.3.6.1.2.1.16.1.1.1.11			etherStatsFragments
    'Fragment.'          : '.1.3.6.1.2.1.16.1.1.1.11.%s',
#    Jabber                 .1.3.6.1.2.1.16.1.1.1.12			etherStatsJabbers
    'Jabber.'            : '.1.3.6.1.2.1.16.1.1.1.12.%s',
#    ExcessiveDefferal      .1.3.6.1.2.1.10.7.2.1.7			dot3StatsDeferredTransmissions
    'ExcessiveDefferal.' : '.1.3.6.1.2.1.10.7.2.1.7.%s',
#    LateCollision          .1.3.6.1.2.1.10.7.2.1.8			dot3StatsLateCollisions
    'LateCollision.'     : '.1.3.6.1.2.1.10.7.2.1.8.%s',
#    ExcessiveCollision     .1.3.6.1.2.1.10.7.2.1.9			dot3StatsExcessiveCollisions
    'ExcessiveCollision.': '.1.3.6.1.2.1.10.7.2.1.9.%s',
#    SingleCollision        .1.3.6.1.2.1.10.7.2.1.4			dot3StatsSingleCollisionFrames
    'SingleCollision.'   : '.1.3.6.1.2.1.10.7.2.1.4.%s',
#    Collision              .1.3.6.1.2.1.16.1.1.1.13			etherStatsCollisions
    'Collision.'         : '.1.3.6.1.2.1.16.1.1.1.13.%s',
    }

get_InOutOctets = {
#    InOctets            .1.3.6.1.2.1.31.1.1.1.6			ifHCInOctets
    'InOctets.'       : '.1.3.6.1.2.1.31.1.1.1.6.%s',
#    OutOctets           .1.3.6.1.2.1.31.1.1.1.10			ifHCOutOctets
    'Outoctets.'      : '.1.3.6.1.2.1.31.1.1.1.10.%s',
    }

set_AdminStatus = [
#     .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3				swL2PortCtrlAdminState
    ['.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.3.%s', '100', '%s', 'INTEGER'],
    ]

set_AdminSpeed = [
#     .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4				swL2PortCtrlNwayState
    ['.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.%s', '100', '%s', 'INTEGER'],
    ]

set_CableDiagInit = [
#     .1.3.6.1.4.1.171.12.58.1.1.1.12					swEtherCableDiagAction
    ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '%s', '1', 'INTEGER'],
    ]

set_SaveConfig = [
#     .1.3.6.1.4.1.171.12.1.2.6						agentSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.6', '0', '2', 'INTEGER'],
    ]

set_CreateVlan = [
#     .1.3.6.1.2.1.17.7.1.4.3.1.1					dot1qVlanStaticName
    ['.1.3.6.1.2.1.17.7.1.4.3.1.1', '{1}', '{2}', 'OCTETSTR'],
#     .1.3.6.1.2.1.17.7.1.4.3.1.2					dot1qVlanStaticEgressPorts
    ['.1.3.6.1.2.1.17.7.1.4.3.1.2', '{1}', '{3}', 'OCTETSTR'],
#     .1.3.6.1.2.1.17.7.1.4.3.1.5					dot1qVlanStaticRowStatus
    ['.1.3.6.1.2.1.17.7.1.4.3.1.5', '{1}', '4', 'INTEGER'],
    ]

set_IpifCfg = [
#     .1.3.6.1.4.1.171.11.113.1.1.2.1.2.2				swL2DevCtrlSystemIP
    ['.1.3.6.1.4.1.171.11.113.1.1.2.1.2.2', '0', '{1}', 'IPADDR'],
#     .1.3.6.1.4.1.171.11.113.1.1.2.1.2.3				swL2DevCtrlSubnetMask
    ['.1.3.6.1.4.1.171.11.113.1.1.2.1.2.3', '0', '{2}', 'IPADDR'],
#     .1.3.6.1.4.1.171.11.113.1.1.2.1.2.4				swL2DevCtrlDefaultGateway
    ['.1.3.6.1.4.1.171.11.113.1.1.2.1.2.4', '0', '{3}', 'IPADDR'],
#     .1.3.6.1.4.1.171.11.113.1.1.2.1.2.5				swL2DevCtrlManagementVlanId
    ['.1.3.6.1.4.1.171.11.113.1.1.2.1.2.5', '0', '{4}', 'INTEGER'],
    ]

set_DHCP_RemoteID = [
#     .1.3.6.1.4.1.171.12.42.3.2.5					swDHCPRelayOption82RemoteID
    ['.1.3.6.1.4.1.171.12.42.3.2.5', '0', '{1}', 'OCTETSTR'],
    ]

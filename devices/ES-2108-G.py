timeout_mf = 1.0

DeviceMap = ([
                 [
                     ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                 ],
             ],)

StackInfo = ({
                 'SlotSize': '9',
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
                'get_PortIndex',
            ],)

# portOpModePortLinkUpType
MediumType = ({
                  '0': 'copper',
                  '1': 'copper',
                  '2': 'fiber',
              },)

# portOpModePortLinkUpType
ActualStatus = ({
                    '0': 'linkdown',
                    '1': 'linkup',
                    '2': 'linkup',
                },)

# ifHighSpeed
ActualSpeed = ({
                   '0': 'linkdown',
                   '10': '10M',
                   '100': '100M',
                   '1000': '1G',
               },)

# ifAdminStatus
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
               },)

# portOpModePortSpeedDuplex
AdminSpeed = ({
                  '0': 'auto',
                  '1': '10M-Half',
                  '2': '10M-Full',
                  '3': '100M-Half',
                  '4': '100M-Full',
                  '5': '1G-Full',
              },)

# portOpModePortFlowCntl
AdminFlow = ({
                 '0': 'disabled',
                 '1': 'enabled',
             },)

# portOpModePortModuleType
PortType = ({
                '0': 'fastEthernet',
                '1': 'gigaEthernet',
            },)

walk_PortIndex = {
    # PortIndex   .1.3.6.1.2.1.17.1.4.1.2    dot1dBasePortIfIndex
    'PortIndex': '.1.3.6.1.2.1.17.1.4.1.2',
}

get_PortIndex = {
    # PortIndex     .1.3.6.1.2.1.17.1.4.1.2     dot1dBasePortIfIndex
    'PortIndex.1': '.1.3.6.1.2.1.17.1.4.1.2.1',
    'PortIndex.2': '.1.3.6.1.2.1.17.1.4.1.2.2',
    'PortIndex.3': '.1.3.6.1.2.1.17.1.4.1.2.3',
    'PortIndex.4': '.1.3.6.1.2.1.17.1.4.1.2.4',
    'PortIndex.5': '.1.3.6.1.2.1.17.1.4.1.2.5',
    'PortIndex.6': '.1.3.6.1.2.1.17.1.4.1.2.6',
    'PortIndex.7': '.1.3.6.1.2.1.17.1.4.1.2.7',
    'PortIndex.8': '.1.3.6.1.2.1.17.1.4.1.2.8',
    'PortIndex.9': '.1.3.6.1.2.1.17.1.4.1.2.9',
}

get_ifName = {
    # PortName     .1.3.6.1.2.1.31.1.1.1.1  ifName
    'PortName.1': '.1.3.6.1.2.1.31.1.1.1.1.1',
    'PortName.2': '.1.3.6.1.2.1.31.1.1.1.1.2',
    'PortName.3': '.1.3.6.1.2.1.31.1.1.1.1.3',
    'PortName.4': '.1.3.6.1.2.1.31.1.1.1.1.4',
    'PortName.5': '.1.3.6.1.2.1.31.1.1.1.1.5',
    'PortName.6': '.1.3.6.1.2.1.31.1.1.1.1.6',
    'PortName.7': '.1.3.6.1.2.1.31.1.1.1.1.7',
    'PortName.8': '.1.3.6.1.2.1.31.1.1.1.1.8',
    'PortName.9': '.1.3.6.1.2.1.31.1.1.1.1.9',
}

get_SinglePort = {
    # MediumType      .1.3.6.1.4.1.890.1.5.8.19.19.1.1.5	portOpModePortLinkUpType
    'MediumType.':   '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.5.%s',
    # ActualStatus    .1.3.6.1.4.1.890.1.5.8.19.19.1.1.5    portOpModePortLinkUpType
    'ActualStatus.': '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.5.%s',
    # ActualSpeed     .1.3.6.1.2.1.31.1.1.1.15		        ifHighSpeed
    'ActualSpeed.':  '.1.3.6.1.2.1.31.1.1.1.15.%s',
    # AdminStatus     .1.3.6.1.2.1.2.2.1.7		            ifAdminStatus
    'AdminStatus.':  '.1.3.6.1.2.1.2.2.1.7.%s',
    # AdminSpeed      .1.3.6.1.4.1.890.1.5.8.19.19.1.1.1    portOpModePortSpeedDuplex
    'AdminSpeed.':   '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.1.%s',
    # AdminFlow       .1.3.6.1.4.1.890.1.5.8.19.19.1.1.2    portOpModePortFlowCntl
    'AdminFlow.':    '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.2.%s',
    # PortType        .1.3.6.1.4.1.890.1.5.8.19.19.1.1.4	portOpModePortModuleType
    'PortType.':     '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.4.%s',
    # PortName        .1.3.6.1.2.1.31.1.1.1.1               ifName
    'PortName.':     '.1.3.6.1.2.1.31.1.1.1.1.%s',
    # PortDescr       .1.3.6.1.4.1.890.1.5.8.19.19.1.1.3    portOpModePortName
    'PortDescr.':    '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.3.%s',
}

walk_AllPorts = {
    # MediumType     .1.3.6.1.4.1.890.1.5.8.19.19.1.1.5		portOpModePortLinkUpType
    'MediumType':   '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.5',
    # ActualStatus   .1.3.6.1.4.1.890.1.5.8.19.19.1.1.5		portOpModePortLinkUpType
    'ActualStatus': '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.5',
    # ActualSpeed    .1.3.6.1.2.1.31.1.1.1.15		        ifHighSpeed
    'ActualSpeed':  '.1.3.6.1.2.1.31.1.1.1.15',
    # AdminStatus    .1.3.6.1.2.1.2.2.1.7		            ifAdminStatus
    'AdminStatus':  '.1.3.6.1.2.1.2.2.1.7',
    # AdminSpeed     .1.3.6.1.4.1.890.1.5.8.19.19.1.1.1		portOpModePortSpeedDuplex
    'AdminSpeed':   '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.1',
    # AdminFlow      .1.3.6.1.4.1.890.1.5.8.19.19.1.1.2     portOpModePortFlowCntl
    'AdminFlow':    '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.2',
    # PortDescr      .1.3.6.1.4.1.890.1.5.8.19.19.1.1.3     portOpModePortName
    'PortDescr':    '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.3',
}

walk_ifAlias = {
    # PortDescr   .1.3.6.1.4.1.890.1.5.8.19.19.1.1.3    portOpModePortName
    'PortDescr': '.1.3.6.1.4.1.890.1.5.8.19.19.1.1.3',
}

walk_FDB_VLAN = {
    # FDB   .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB': '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
}

walk_VlanMap = {
    # VlanName                   .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName':                 '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    # EgressPorts                .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticEgressPorts
    'ljust_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

walk_VlanEgressPorts = {
    # VEP                .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticEgressPorts
    'ljust_string:VEP': '.1.3.6.1.2.1.17.7.1.4.3.1.4',
}

walk_VlanUntaggedPorts = {
    # VUP                .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticUntaggedPorts
    'ljust_string:VUP': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

get_Errors = {
    # CRC                   .1.3.6.1.2.1.16.1.1.1.8         etherStatsCRCAlignErrors
    'CRC.':                '.1.3.6.1.2.1.16.1.1.1.8.%s',
    # Undersize             .1.3.6.1.2.1.16.1.1.1.9			etherStatsUndersizePkts
    'Undersize.':          '.1.3.6.1.2.1.16.1.1.1.9.%s',
    # Oversize              .1.3.6.1.2.1.16.1.1.1.10		etherStatsOversizePkts
    'Oversize.':           '.1.3.6.1.2.1.16.1.1.1.10.%s',
    # Fragment              .1.3.6.1.2.1.16.1.1.1.11		etherStatsFragments
    'Fragment.':           '.1.3.6.1.2.1.16.1.1.1.11.%s',
    # Jabber                .1.3.6.1.2.1.16.1.1.1.12		etherStatsJabbers
    'Jabber.':             '.1.3.6.1.2.1.16.1.1.1.12.%s',
    # ExcessiveDefferal     .1.3.6.1.2.1.10.7.2.1.7			dot3StatsDeferredTransmissions
    'ExcessiveDefferal.':  '.1.3.6.1.2.1.10.7.2.1.7.%s',
    # LateCollision         .1.3.6.1.2.1.10.7.2.1.8			dot3StatsLateCollisions
    'LateCollision.':      '.1.3.6.1.2.1.10.7.2.1.8.%s',
    # ExcessiveCollision    .1.3.6.1.2.1.10.7.2.1.9			dot3StatsExcessiveCollisions
    'ExcessiveCollision.': '.1.3.6.1.2.1.10.7.2.1.9.%s',
    # SingleCollision       .1.3.6.1.2.1.10.7.2.1.4			dot3StatsSingleCollisionFrames
    'SingleCollision.':    '.1.3.6.1.2.1.10.7.2.1.4.%s',
    # Collision             .1.3.6.1.2.1.16.1.1.1.13		etherStatsCollisions
    'Collision.':          '.1.3.6.1.2.1.16.1.1.1.13.%s',
}

get_InOutOctets = {
    # InOctets     .1.3.6.1.2.1.31.1.1.1.6			ifHCInOctets
    'InOctets.':  '.1.3.6.1.2.1.31.1.1.1.6.%s',
    # OutOctets    .1.3.6.1.2.1.31.1.1.1.10			ifHCOutOctets
    'Outoctets.': '.1.3.6.1.2.1.31.1.1.1.10.%s',
}

set_AdminStatus = [
    # .1.3.6.1.2.1.2.2.1.7  ifAdminStatus
    ['.1.3.6.1.2.1.2.2.1.7', '{1}', '{2}', 'INTEGER'],
]

set_AdminSpeed = [
    # .1.3.6.1.4.1.890.1.5.8.19.19.1.1.1    portOpModePortSpeedDuplex
    ['.1.3.6.1.4.1.890.1.5.8.19.19.1.1.1', '{1}', '{2}', 'INTEGER'],
]

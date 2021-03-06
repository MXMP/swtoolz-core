# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Представлена в виде списков слотов. Каждый слот содержит список рядов.
# Каждый ряд содержит список портов.
DeviceMap = ([
                 [
                     ['1/1', '1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10', '1/11', '1/12'],
                     ['1/13', '1/14', '1/15', '1/16', '1/17', '1/18', '1/19', '1/20', '1/21', '1/22', '1/23', '1/24']
                 ],
                 [
                     ['2/1', '2/2', '2/3', '2/4', '2/5', '2/6', '2/7', '2/8', '2/9', '2/10', '2/11', '2/12'],
                     ['2/13', '2/14', '2/15', '2/16', '2/17', '2/18', '2/19', '2/20', '2/21', '2/22', '2/23', '2/24']
                 ],
                 [
                     ['3/1', '3/2', '3/3', '3/4', '3/5', '3/6', '3/7', '3/8', '3/9', '3/10', '3/11', '3/12'],
                     ['3/13', '3/14', '3/15', '3/16', '3/17', '3/18', '3/19', '3/20', '3/21', '3/22', '3/23', '3/24']
                 ],
                 [
                     ['4/1', '4/2', '4/3', '4/4', '4/5', '4/6', '4/7', '4/8', '4/9', '4/10', '4/11', '4/12'],
                     ['4/13', '4/14', '4/15', '4/16', '4/17', '4/18', '4/19', '4/20', '4/21', '4/22', '4/23', '4/24']
                 ],
                 [
                     ['5/1', '5/2', '5/3', '5/4', '5/5', '5/6', '5/7', '5/8', '5/9', '5/10', '5/11', '5/12'],
                     ['5/13', '5/14', '5/15', '5/16', '5/17', '5/18', '5/19', '5/20', '5/21', '5/22', '5/23', '5/24']
                 ],
                 [
                     ['6/1', '6/2', '6/3', '6/4', '6/5', '6/6', '6/7', '6/8', '6/9', '6/10', '6/11', '6/12'],
                     ['6/13', '6/14', '6/15', '6/16', '6/17', '6/18', '6/19', '6/20', '6/21', '6/22', '6/23', '6/24']
                 ],
                 [
                     ['7/1', '7/2', '7/3', '7/4', '7/5', '7/6', '7/7', '7/8', '7/9', '7/10', '7/11', '7/12'],
                     ['7/13', '7/14', '7/15', '7/16', '7/17', '7/18', '7/19', '7/20', '7/21', '7/22', '7/23', '7/24']
                 ],
                 [
                     ['8/1', '8/2', '8/3', '8/4', '8/5', '8/6', '8/7', '8/8', '8/9', '8/10', '8/11', '8/12'],
                     ['8/13', '8/14', '8/15', '8/16', '8/17', '8/18', '8/19', '8/20', '8/21', '8/22', '8/23', '8/24']
                 ],
             ],)

# SlotSize - количество индексов, отведенное на слот.
# Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться,
# например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
StackInfo = ({
                 'SlotSize': '256',
                 'ShiftIndex': '256',
                 #    'MaxIndex'        : '64',
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
                'BoardDescrShort',
                'walk_PortIndex',
                'walk_BoardDescr',
                'walk_ifName',
            ],)

# snSwPortInfoConnectorType
MediumType = ({
                  '1': 'other',
                  '2': 'copper',
                  '3': 'fiber',
              },)

# snSwPortInfoLinkStatus
ActualStatus = ({
                    '1': 'linkup',
                    '2': 'linkdown',
                },)

# snSwPortInfoSpeed
ActualSpeed = ({
                   '0': 'linkdown',
                   '1': 'auto',
                   '2': '10M',
                   '3': '100M',
                   '4': '1G',
                   '5': '1G-master',
                   '6': '155G',
                   '7': '10G',
               },)

# snSwPortInfoAdminStatus
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
               },)

# snSwPortInfoSpeed (placeholder)
AdminSpeed = ({
                  '0': 'linkdown',
                  '1': 'auto',
                  '2': '10M',
                  '3': '100M',
                  '4': '1G',
                  '5': '1G-master',
                  '6': '155G',
                  '7': '10G',
              },)

# snSwPortInfoFlowControl
AdminFlow = ({
                 '0': 'disabled',
                 '1': 'enabled',
             },)

# Пользовательские сокращения названий плат (модулей)
BoardDescrShort = ({
                       'J-FIxGMR4 JetCore Management Module, SYSIF 2': 'J-FIxGMR4',
                       'J-FIxG16 JetCore Gig Fiber Module, SYSIF 2': 'J-FIxG16',
                       'J-BxGMR4 JetCore Management Module, SYSIF 2': 'J-BxGMR4',
                       'J-BxG16 JetCore Gig Fiber Module, SYSIF 2': 'J-BxG16',
                       'B10G Fiber Switch Module, SYSIF 2': 'B10G',
                       'B2x10G Fiber Switch Module, SYSIF 2': 'B2x10G',
                       'SX-FI-2XG 2-port 10G Fiber': 'SX-FI-2XG',
                       'SX-FI-24HF 24-port Gig Fiber': 'SX-FI-24HF',
                       'SX-FIZMRXL6 0-port Management': 'SX-FIZMRXL6',
                       'TURBOIRON 2404(24-port  10G Fiber  + 4-port 1GC)': 'TI-2404: 24x10G(F)+4x1G(C)',
                   },)

# get_HardwareRev (placeholder for Slava's Hardcode. not working but necessary)
get_HardwareRev = ({
                       '0': 'n/a',
                   },)

# walk_VlanEgressPorts (placeholder for Slava's Hardcode. not working but necessary)
walk_VlanEgressPorts = ({
                            '0': '',
                        },)

walk_PortIndex = {
    #    PortIndex           .1.3.6.1.4.1.1991.1.1.3.3.1.1.1		snSwPortInfoPortNum
    'PortIndex': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.1',
}

walk_BoardDescr = {
    #    BoardBescr          .1.3.6.1.4.1.1991.1.1.2.2.1.1.2		snAgentBrdMainBrdDescription
    'BoardDescr': '.1.3.6.1.4.1.1991.1.1.2.2.1.1.2',
}

get_SinglePort = {
    #    MediumType          .1.3.6.1.4.1.1991.1.1.3.3.1.1.7		snSwPortInfoConnectorType
    'MediumType.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.7.%s',
    #    ActualStatus        .1.3.6.1.4.1.1991.1.1.3.3.1.1.9		snSwPortInfoLinkStatus
    'ActualStatus.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.9.%s',
    #    ActualSpeed         .1.3.6.1.4.1.1991.1.1.3.3.1.1.5		snSwPortInfoSpeed
    'ActualSpeed.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.5.%s',
    #    AdminStatus         .1.3.6.1.4.1.1991.1.1.3.3.1.1.8		snSwPortInfoAdminStatus
    'AdminStatus.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.8.%s',
    #    AdminSpeed          .1.3.6.1.4.1.1991.1.1.3.3.1.1.5		snSwPortInfoSpeed (placeholder)
    'AdminSpeed.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.5.%s',
    #    AdminFlow           .1.3.6.1.4.1.1991.1.1.3.3.1.1.35		snSwPortInfoFlowControl
    'AdminFlow.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.35.%s',
    #    PortDescr           .1.3.6.1.4.1.1991.1.1.3.3.1.1.24		snSwPortName
    'PortDescr.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.24.%s',
}

get_InMcastFrames_SinglePort = {
    #   InMcastFrames   1.3.6.1.4.1.1991.1.1.3.3.1.1.28 snSwPortStatsInMcastFrames
    'InMcastFrames.': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.28.%s',
}

get_NUnicastPkts_SinglePort = {
    #   ifInNUcastPkts  .1.3.6.1.2.1.2.2.1.12
    'IfInNUcastPkts.': '.1.3.6.1.2.1.2.2.1.12.%s',
}

walk_AllPorts = {
    #    MediumType          .1.3.6.1.4.1.1991.1.1.3.3.1.1.7		snSwPortInfoConnectorType
    'MediumType': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.7',
    #    ActualStatus        .1.3.6.1.4.1.1991.1.1.3.3.1.1.9		snSwPortInfoLinkStatus
    'ActualStatus': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.9',
    #    ActualSpeed         .1.3.6.1.4.1.1991.1.1.3.3.1.1.5		snSwPortInfoSpeed
    'ActualSpeed': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.5',
    #    AdminStatus         .1.3.6.1.4.1.1991.1.1.3.3.1.1.8		snSwPortInfoAdminStatus
    'AdminStatus': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.8',
    #    AdminSpeed          .1.3.6.1.4.1.1991.1.1.3.3.1.1.5		snSwPortInfoSpeed (placeholder)
    'AdminSpeed': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.5',
    #    AdminFlow           .1.3.6.1.4.1.1991.1.1.3.3.1.1.35.		snSwPortInfoFlowControl
    'AdminFlow': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.35',
    #    PortDescr           .1.3.6.1.4.1.1991.1.1.3.3.1.1.24		snSwPortName
    'PortDescr': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.24',
}

walk_ifAlias = {
    #    PortDescr           .1.3.6.1.4.1.1991.1.1.3.3.1.1.24		snSwPortName
    'PortDescr': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.24',
}

walk_ifName = {
    #    PortName            .1.3.6.1.4.1.1991.1.1.3.3.1.1.39		snSwPortDescr
    'PortName': '.1.3.6.1.4.1.1991.1.1.3.3.1.1.39',
}

walk_VlanMap = {
    #    VLanId              .1.3.6.1.4.1.1991.1.1.3.2.1.1.2		snVLanByPortVLanId
    'VLanId': '.1.3.6.1.4.1.1991.1.1.3.2.1.1.2',
    #    VLanName            .1.3.6.1.4.1.1991.1.1.3.2.1.1.25		snVLanByPortVLanName
    'VLanName': '.1.3.6.1.4.1.1991.1.1.3.2.1.1.25',
    #    RouterIntf          .1.3.6.1.4.1.1991.1.1.3.2.1.1.26		snVLanByPortRouterIntf
    'RouterIntf': '.1.3.6.1.4.1.1991.1.1.3.2.1.1.26',
    #    PortList            .1.3.6.1.4.1.1991.1.1.3.2.1.1.28		snVLanByPortPortList
    'PortList': '.1.3.6.1.4.1.1991.1.1.3.2.1.1.28',
    #    VlanName            .1.3.6.1.2.1.17.7.1.4.3.1.1			dot1qVlanStaticName
    'VlanName': '.1.3.6.1.2.1.17.7.1.4.3.1.1',
    #    EgressPorts         .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'hex_string:EgressPorts': '.1.3.6.1.2.1.17.7.1.4.3.1.2',
}

walk_IPifMap = {
    #    ipIfIndex           .1.3.6.1.2.1.4.20.1.2				ipAdEntIfIndex
    'ipIfIndex': '.1.3.6.1.2.1.4.20.1.2',
    #    ipNetMask           .1.3.6.1.2.1.4.20.1.3				ipAdEntNetMask
    'ipNetMask': '.1.3.6.1.2.1.4.20.1.3',
}

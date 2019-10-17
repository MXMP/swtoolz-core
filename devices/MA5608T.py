timeout_mf = 2.0

DeviceMap = {
    'helper': 'make_dynamic_map',
    # PortName   .1.3.6.1.2.1.31.1.1.1.1  ifName
    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
}

StackInfo = ({
                 'SlotSize': '8192',
                 'ShiftIndex': '0',
             },)

Commands = ([
                'StackInfo',
                'DeviceMap',
                'AdminStatus',
                'MediumType',
                'onu_eth_port_AdminStatus',
                'ActualStatus',
                'onu_eth_port_ActualStatus',
                'ActualSpeed',
                'AdminSpeed',
                'onu_eth_port_ActualSpeed',
                'walk_BoardDescr',
                'walk_PortIndex',
                'walk_ifName',
                'primary_status',
                'load_state',
                'xml_load_state',
            ],)

# hwXponDeviceOntControlPrimaryStatus   .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.6
primary_status = ({
                      '1': 'Normal',
                      '2': 'Abnormal',
                      '3': 'Restricted',
                      '4': 'Abnormal & Restricted',
                      '5': 'Autonomous',
                      '6': 'Management',
                      '7': 'Autonomous & Management',
                      '8': 'Autonomous & Restricted',
                      '9': 'Management & Abnormal',
                  },)

# hwXponOntInfoAppLoadState  .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.9
load_state = ({
                  '1': 'initstate',
                  '2': 'process %0',
                  '3': 'ftp load fail',
                  '4': 'loaded to mainboard process %10',
                  '5': 'loaded to ponboard process %20',
                  '6': 'loaded to ponboard fail',
                  '7': 'process %80',
                  '8': 'fail:user stop',
                  '9': 'fail:ont offline',
                  '10': 'fail:ont response fail',
                  '11': 'fail:ont response timeout',
                  '12': 'fail:pon inner error',
                  '13': 'process %100,ont restart',
                  '14': 'Process %100 the ont now is in survival mode',
                  '15': 'fail:system is busy because the ponboard\'s channel is occupied',
                  '16': 'fail:failed to verify the version information',
                  '17': 'fail:processing the loading task timed out',
                  '18': 'fail:ont file check failure',
                  '19': 'fail:code file validate failure',
                  '20': 'fail:system buffer is insufficient',
                  '21': 'fail:ont not support load',
                  '22': 'fail:ont storage space insufficient',
                  '23': 'fail:ont image file error',
                  '24': 'fail:ont image file existed',
                  '25': 'fail:ont activate image file fail',
                  '26': 'fail:ont commit image file fail',
                  '27': 'fail:ont image file crc error',
                  '28': 'fail:unknown reason',
              },)

# hwXponOntInfoXmlLoadState .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.10
xml_load_state = ({
                      '1': 'initstate',
                      '2': 'process %0',
                      '3': 'ftp load fail',
                      '4': 'loaded to mainboard process %10',
                      '5': 'loaded to ponboard process %20',
                      '6': 'loaded to ponboard fail',
                      '7': 'process %80',
                      '8': 'process %100',
                      '9': 'fail:user stop',
                      '10': 'fail:ont not support xml',
                      '11': 'fail:ont offline',
                      '12': 'fail:ont response unknown fail',
                      '13': 'fail:ont response timeout',
                      '14': 'fail:xml error ont will reconfigure fail',
                      '15': 'fail:xml format error',
                      '16': 'fail:xml content error',
                      '17': 'fail:ont find xml transfer error',
                      '18': 'fail:unknown error from ont',
                      '19': 'fail:unknown error from ponboard',
                      '20': 'fail:system is busy because the ponboard\'s channel is occupied',
                      '21': 'fail:unknown reason',
                  },)

# ifAdminStatus .1.3.6.1.2.1.2.2.1.7
AdminStatus = ({
                   '1': 'enabled',
                   '2': 'disabled',
                   '3': 'testing',
               },)

# hwGponDeviceOntEthernetOperateStatus  .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.5
onu_eth_port_AdminStatus = ({
                                '1': 'on',
                                '2': 'off',
                                '-1': 'invalid',
                            },)

# ifOperStatus  .1.3.6.1.2.1.2.2.1.8
ActualStatus = ({
                    '1': 'linkup',
                    '2': 'linkdown',
                    '3': 'testing',
                    '4': 'unknown',
                    '5': 'dormant',
                    '6': 'notPresent',
                    '7': 'lowerLayerDown',
                },)

# hwGponDeviceOntEthernetOnlineState    .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.22
onu_eth_port_ActualStatus = ({
                                 '1': 'linkup',
                                 '2': 'linkdown',
                                 '-1': 'invalid',
                             },)

# ifSpeed   .1.3.6.1.2.1.2.2.1.5
ActualSpeed = ({
                   '100000000': '100M',
                   '1000000000': '1G',
                   '2488320000': '2,5G',
               },)

# hwGponDeviceOntEthernetSpeed  .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.4
onu_eth_port_ActualSpeed = ({
                                '1': '10M (manual)',
                                '2': '100M (manual)',
                                '3': '1000M (manual)',
                                '4': 'linkdown (auto)',
                                '5': '10M (auto)',
                                '6': '100M (auto)',
                                '7': '1G (auto)',
                                '-1': 'invalid',
                            },)

# ifHighSpeed   .1.3.6.1.2.1.31.1.1.1.15
AdminSpeed = ({
                  '100': '100M',
                  '1000': '1G',
                  '2488': '2,5G',
              },)

# ifType    .1.3.6.1.2.1.2.2.1.3
MediumType = ({
                  '6': 'fiber',
                  '250': 'fiber',
              },)

walk_PortIndex = {
    'helper': 'repair_big_indexes',
    # PortIndex   .1.3.6.1.2.1.2.2.1.1  ifIndex
    'PortIndex': '.1.3.6.1.2.1.2.2.1.1',
}

walk_AllPorts = {
    'helper': 'remove_small_indexes',
    # ActualStatus   .1.3.6.1.2.1.2.2.1.8       ifOperStatus
    'ActualStatus': '.1.3.6.1.2.1.2.2.1.8',
    # ActualSpeed    .1.3.6.1.2.1.2.2.1.5       ifSpeed
    'ActualSpeed':  '.1.3.6.1.2.1.2.2.1.5',
    # AdminStatus    .1.3.6.1.2.1.2.2.1.7       ifAdminStatus
    'AdminStatus':  '.1.3.6.1.2.1.2.2.1.7',
    # AdminSpeed     .1.3.6.1.2.1.31.1.1.1.15   ifHighSpeed
    'AdminSpeed':   '.1.3.6.1.2.1.31.1.1.1.15',
    # PortDescr      .1.3.6.1.2.1.31.1.1.1.18   ifAlias
    'PortDescr':    '.1.3.6.1.2.1.31.1.1.1.18',
    # MediumType     .1.3.6.1.2.1.2.2.1.3       ifType
    'MediumType':   '.1.3.6.1.2.1.2.2.1.3',
}

walk_ifAlias = {
    # PortDescr   .1.3.6.1.2.1.31.1.1.1.18  ifAlias
    'PortDescr': '.1.3.6.1.2.1.31.1.1.1.18',
}

walk_ifName = {
    # PortName   .1.3.6.1.2.1.31.1.1.1.1  ifName
    'PortName': '.1.3.6.1.2.1.31.1.1.1.1',
}

get_SinglePort = {
    # ActualStatus    .1.3.6.1.2.1.2.2.1.8          ifOperStatus
    'ActualStatus.': '.1.3.6.1.2.1.2.2.1.8.%s',
    # ActualSpeed     .1.3.6.1.2.1.2.2.1.5          ifSpeed
    'ActualSpeed.':  '.1.3.6.1.2.1.2.2.1.5.%s',
    # AdminStatus     .1.3.6.1.2.1.2.2.1.7          ifAdminStatus
    'AdminStatus.':  '.1.3.6.1.2.1.2.2.1.7.%s',
    # AdminSpeed      .1.3.6.1.2.1.31.1.1.1.15      ifHighSpeed
    'AdminSpeed.':   '.1.3.6.1.2.1.31.1.1.1.15.%s',
    # PortDescr       .1.3.6.1.2.1.31.1.1.1.18      ifAlias
    'PortDescr.':    '.1.3.6.1.2.1.31.1.1.1.18.%s',
    # MediumType      .1.3.6.1.2.1.2.2.1.3          ifType
    'MediumType.':   '.1.3.6.1.2.1.2.2.1.3.%s',
}

# Установка описания для порта.
# На вход обязательно нужно передать: ifIndex GPON-порта и описание.
set_port_descr = [
    # .1.3.6.1.2.1.31.1.1.1.18  ifAlias
    ['.1.3.6.1.2.1.31.1.1.1.18', '{1}', '{2}', 'OCTETSTR'],
]

# Получение информации о ethernet-порту ONU.
# На вход обязательно нужно передать: ifIndex GPON-порта, порядковый номер ONU и номер порта на ONU.
get_onu_eth_port_info = {
    # onu_eth_port_ActualStatus      .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.22      hwGponDeviceOntEthernetOnlineState
    'onu_eth_port_ActualStatus...': '.1.3.6.1.4.1.2011.6.128.1.1.2.62.1.22.{1}.{2}.{3}',
    # onu_eth_port_ActualSpeed       .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.4       hwGponDeviceOntEthernetSpeed
    'onu_eth_port_ActualSpeed...':  '.1.3.6.1.4.1.2011.6.128.1.1.2.62.1.4.{1}.{2}.{3}',
    # onu_eth_port_AdminStatus       .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.5       hwGponDeviceOntEthernetOperateStatus
    'onu_eth_port_AdminStatus...':  '.1.3.6.1.4.1.2011.6.128.1.1.2.62.1.5.{1}.{2}.{3}',
}

# Включение/выключение Ethernet порта на ONU.
# На вход обязательно нужно передать: ifIndex GPON-порта, порядковый номер ONU, номер порта на ONU и нужный статус.
set_onu_eth_port_admin_status = [
    # .1.3.6.1.4.1.2011.6.128.1.1.2.62.1.5  hwGponDeviceOntEthernetOperateStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.2.62.1.5', '{1}.{2}.{3}', '{4}', 'INTEGER'],
]

# Получение ошибок на ethernet-порту ONU.
# На вход обязательно нужно передать: ifIndex GPON-порта, порядковый номер ONU и номер порта на ONU.
get_onu_eth_port_errors = {
    # recv_crc_align_errors                  .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.7                   hwGponOntEthernetStatisticRecvCRCAlignErrors
    'recv_crc_align_errors...':             '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.7.{1}.{2}.{3}',
    # recv_undersize_pkts                    .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.8                   hwGponOntEthernetStatisticRecvUndersizePkts
    'recv_undersize_pkts...':               '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.8.{1}.{2}.{3}',
    # recv_fragments                         .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.10                  hwGponOntEthernetStatisticRecvFragments
    'recv_fragments...':                    '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.10.{1}.{2}.{3}',
    # recv_jabbers                           .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.11                  hwGponOntEthernetStatisticRecvJabbers
    'recv_jabbers...':                      '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.11.{1}.{2}.{3}',
    # collisions                             .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.12                  hwGponOntEthernetStatisticCollisions
    'collisions...':                        '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.12.{1}.{2}.{3}',
    # recv_fcs_errors                        .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.19                  hwGponOntEthernetStatisticRecvFCSErrors
    'recv_fcs_errors...':                   '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.19.{1}.{2}.{3}',
    # send_excessive_collision               .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.20                  hwGponOntEthernetStatisticSendExcessiveCollision
    'send_excessive_collision...':          '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.20.{1}.{2}.{3}',
    # send_late_collision                    .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.21                  hwGponOntEthernetStatisticSendLateCollision
    'send_late_collision...':               '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.21.{1}.{2}.{3}',
    # recv_frame_too_longs                   .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.22                  hwGponOntEthernetStatisticRecvFrameTooLongs
    'recv_frame_too_longs...':              '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.22.{1}.{2}.{3}',
    # recv_buffer_overflowson                .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.23                  hwGponOntEthernetStatisticRecvBufferOverflowson
    'recv_buffer_overflowson...':           '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.23.{1}.{2}.{3}',
    # send_buffer_overflowson                .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.24                  hwGponOntEthernetStatisticSendBufferOverflowson
    'send_buffer_overflowson...':           '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.24.{1}.{2}.{3}',
    # send_single_collision_frame            .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.25                  hwGponOntEthernetStatisticSendSingleCollisionFrame
    'send_single_collision_frame...':       '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.25.{1}.{2}.{3}',
    # send_multiple_collisions_frame         .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.26                  hwGponOntEthernetStatisticSendMultipleCollisionsFrame
    'send_multiple_collisions_frame...':    '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.26.{1}.{2}.{3}',
    # send_deferred_transmission             .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.28                  hwGponOntEthernetStatisticDeferredTransmission
    'send_deferred_transmission...':        '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.28.{1}.{2}.{3}',
    # send_sqe_test_error                    .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.27                  hwGponOntEthernetStatisticSendSQETestError
    'send_sqe_test_error...':               '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.27.{1}.{2}.{3}',
    # send_internal_mac_transmit_error       .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.29                  hwGponOntEthernetStatisticInternalmacTransmitError
    'send_internal_mac_transmit_error...':  '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.29.{1}.{2}.{3}',
    # send_carrier_sense_error               .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.30                  hwGponOntEthernetStatisticSendCarrierSenseError
    'send_carrier_sense_error...':          '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.30.{1}.{2}.{3}',
    # recv_alignment_error                   .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.31                  hwGponOntEthernetStatisticRecvAlignmentError
    'recv_alignment_error...':              '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.31.{1}.{2}.{3}',
    # recv_internal_mac_receive_error        .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.32                  hwGponOntEthernetStatisticInternalMACReceiveError
    'recv_internal_mac_receive_error...':   '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.32.{1}.{2}.{3}',
    # delay_exceeded_discard                 .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.35                  hwGponOntEthernetStatisticDelayExceededDiscard
    'delay_exceeded_discard...':            '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.35.{1}.{2}.{3}',
    # recv_good_pkts_octets                  .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.42                  hwGponOntEthernetStatisticRecvGoodPktsOctets
    'recv_good_pkts_octets...':             '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.42.{1}.{2}.{3}',
    # send_good_pkts_octets                  .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.43                  hwGponOntEthernetStatisticSendGoodPktsOctets
    'send_good_pkts_octets...':             '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.43.{1}.{2}.{3}',
    # recv_bad_pkts_octets                   .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.44                  hwGponOntEthernetStatisticRecvBadPktsOctets
    'recv_bad_pkts_octets...':              '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.44.{1}.{2}.{3}',
    # send_bad_pkts_octets                   .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.45                  hwGponOntEthernetStatisticSendBadPktsOctets
    'send_bad_pkts_octets...':              '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.45.{1}.{2}.{3}',
    # forward_drop_events                    .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.47                  hwGponOntEthernetStatisticForwardDropEvents
    'forward_drop_events...':               '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.47.{1}.{2}.{3}',
    # send_pkts_oversize                     .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.54                  hwGponOntEthernetStatisticSendPktsOversize
    'send_pkts_oversize...':                '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.54.{1}.{2}.{3}',
    # recv_pkts_1519_to_oversize_octets      .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.55                  hwGponOntEthernetStatisticRecvPkts1519toOversizeOctets
    'recv_pkts_1519_to_oversize_octets...': '.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.55.{1}.{2}.{3}',
}

# Включение/выключение порта.
# На вход передать: ifIndex GPON-порта, статус порта (смотреть словарь AdminStatus).
set_AdminStatus = [
    # .1.3.6.1.2.1.2.2.1.7 ifAdminStatus
    ['.1.3.6.1.2.1.2.2.1.7', '{1}', '{2}', 'INTEGER'],
]

# Получение DDM с ONU.
# На вход обязательно нужно передать: ifIndex GPON-порта и порядковый номер ONU.
get_onu_ddm_info = {
    # onu_ddm_temperature     .1.3.6.1.4.1.2011.6.128.1.1.2.51.1.1      hwGponOntOpticalDdmTemperature
    'onu_ddm_temperature..': '.1.3.6.1.4.1.2011.6.128.1.1.2.51.1.1.{1}.{2}',
    # onu_ddm_voltage         .1.3.6.1.4.1.2011.6.128.1.1.2.51.1.5      hwGponOntOpticalDdmVoltage
    'onu_ddm_voltage..':     '.1.3.6.1.4.1.2011.6.128.1.1.2.51.1.5.{1}.{2}',
    # onu_ddm_bias            .1.3.6.1.4.1.2011.6.128.1.1.2.51.1.2      hwGponOntOpticalDdmBiasCurrent
    'onu_ddm_bias..':        '.1.3.6.1.4.1.2011.6.128.1.1.2.51.1.2.{1}.{2}',
    # onu_ddm_tx_power        .1.3.6.1.4.1.2011.6.128.1.1.2.51.1.3      hwGponOntOpticalDdmTxPower
    'onu_ddm_tx_power..':    '.1.3.6.1.4.1.2011.6.128.1.1.2.51.1.3.{1}.{2}',
    # onu_ddm_rx_power        .1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4      hwGponOntOpticalDdmRxPower
    'onu_ddm_rx_power..':    '.1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4.{1}.{2}',
}

walk_BoardDescr = {
    'helper': 'fake_board_index',
    # BoardBescr   .1.3.6.1.4.1.2011.6.3.3.2.1.3.0    hwSlotDesc
    'BoardDescr': '.1.3.6.1.4.1.2011.6.3.3.2.1.3.0',
}

walk_VlanMap = {
    # VLanId      .1.3.6.1.4.1.2011.5.6.1.1.1.1     hwVlanIndex
    'VLanId':    '.1.3.6.1.4.1.2011.5.6.1.1.1.1',
    # VLanName    .1.3.6.1.4.1.2011.5.6.1.1.1.2     hwVlanDescription
    'VLanName':  '.1.3.6.1.4.1.2011.5.6.1.1.1.2',
    # VlanPorts   .1.3.6.1.4.1.2011.5.6.1.1.1.3     hwVlanPorts
    'VlanPorts': '.1.3.6.1.4.1.2011.5.6.1.1.1.3',
}

# Получение краткой информации (серийный номер и описание) о всех ONU на устройстве
walk_onus = {
    # sn              .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3  hwGponDeviceOntSn
    'hex_string:sn': '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3',
    # description     .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9  hwGponDeviceOntDespt
    'description':   '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9',
}

# Получение информации о всех vlanif.
walk_vlanif = {
    # vlanid   .1.3.6.1.4.1.2011.5.6.1.2.1.2    hwVlanID
    'vlanid': '.1.3.6.1.4.1.2011.5.6.1.2.1.2',
    # ip       .1.3.6.1.4.1.2011.5.6.1.2.1.3    hwVlanIpAddress
    'ip':     '.1.3.6.1.4.1.2011.5.6.1.2.1.3',
    # mask     .1.3.6.1.4.1.2011.5.6.1.2.1.4    hwVlanIpAddressMask
    'mask':   '.1.3.6.1.4.1.2011.5.6.1.2.1.4',
}

# Создание vlanif.
# На вход обязательно нужно передать: vlanid, ip-address, subnet mask
create_vlanif = [
    # .1.3.6.1.4.1.2011.5.6.1.2.1.3     hwVlanIpAddress
    ['.1.3.6.1.4.1.2011.5.6.1.2.1.3', '{1}', '{2}', 'IPADDRESS'],
    # .1.3.6.1.4.1.2011.5.6.1.2.1.4     hwVlanIpAddressMask
    ['.1.3.6.1.4.1.2011.5.6.1.2.1.4', '{1}', '{3}', 'IPADDRESS'],
    # .1.3.6.1.4.1.2011.5.6.1.2.1.7     hwInterfaceRowStatus
    ['.1.3.6.1.4.1.2011.5.6.1.2.1.7', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.18.1.3.1.2    hwDhcpToL3GroupId
    ['.1.3.6.1.4.1.2011.5.18.1.3.1.2', '{1}', '0', 'INTEGER'],
]

# Удаление vlanif.
# На вход обязательно нужно передать: vlanid
delete_vlanif = [
    # .1.3.6.1.4.1.2011.5.6.1.2.1.7     hwInterfaceRowStatus
    ['.1.3.6.1.4.1.2011.5.6.1.2.1.7', '{1}', '6', 'INTEGER'],
]

# Получение краткой информации (серийный номер и описание) о всех ONU за портом.
# На вход обязательно нужно передать: ifIndex GPON-порта
walk_onus_by_port = {
    # sn              .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3      hwGponDeviceOntSn
    'hex_string:sn': '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3.{1}',
    # description     .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9      hwGponDeviceOntDespt
    'description':   '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9.{1}',
}

# Создание VLAN.
# На вход передаем: VLANID.
create_vlan = [
    # .1.3.6.1.4.1.2011.5.6.1.1.1.4     hwVlanType
    ['.1.3.6.1.4.1.2011.5.6.1.1.1.4', '{1}', '7', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.6.1.1.1.13    hwVlanRowStatus
    ['.1.3.6.1.4.1.2011.5.6.1.1.1.13', '{1}', '4', 'INTEGER'],
]

# Установить описание VLAN. Почему-то нельзя это указать при создании, пришлось выделить в отдельный метод.
# На вход передаем: VLANID и текстовое описание.
set_vlan_descr = [
    # .1.3.6.1.4.1.2011.5.6.1.1.1.2     hwVlanDescription
    ['.1.3.6.1.4.1.2011.5.6.1.1.1.2', '{1}', '{2}', 'OCTETSTR'],
]

# Удаление VLAN.
# На вход передаем: VLANID.
delete_vlan = [
    # .1.3.6.1.4.1.2011.5.6.1.1.1.13  hwVlanRowStatus
    ['.1.3.6.1.4.1.2011.5.6.1.1.1.13', '{1}', '6', 'INTEGER'],
]

# Выдает информацию о всех сервисных портах на OLT.
walk_service_ports = {
    'helper': 'huawei_get_service_ports',
    # slot_id   .1.3.6.1.4.1.2011.5.14.5.2.1.3      hwExtSrvFlowPara2
    'slot_id': '.1.3.6.1.4.1.2011.5.14.5.2.1.3',
    # port_id   .1.3.6.1.4.1.2011.5.14.5.2.1.4      hwExtSrvFlowPara3
    'port_id': '.1.3.6.1.4.1.2011.5.14.5.2.1.4',
    # ont_id    .1.3.6.1.4.1.2011.5.14.5.2.1.5      hwExtSrvFlowPara4
    'ont_id':  '.1.3.6.1.4.1.2011.5.14.5.2.1.5',
    # vlan_id   .1.3.6.1.4.1.2011.5.14.5.2.1.8      hwExtSrvFlowVlanid
    'vlan_id': '.1.3.6.1.4.1.2011.5.14.5.2.1.8',
}

walk_dhcp_mac = {
    # mac               .1.3.6.1.4.1.2011.5.18.1.31.1.6     hwDhcpUserMACAddress
    'mac:mac':         '.1.3.6.1.4.1.2011.5.18.1.31.1.6',
    # service_port_id   .1.3.6.1.4.1.2011.5.18.1.31.1.3     hwDhcpUserFlowID
    'service_port_id': '.1.3.6.1.4.1.2011.5.18.1.31.1.3',
    # ip                .1.3.6.1.4.1.2011.5.18.1.31.1.5     hwDhcpUserIpAddress
    'ip':              '.1.3.6.1.4.1.2011.5.18.1.31.1.5',
}

# Получение MAC-адресов за ONT.
# На вход нужно обязательно передать: ifIndex GPON-порта, ONTID.
walk_fdb = {
    'helper': 'huawei_fdb',
    #  mac                      .1.3.6.1.4.1.2011.6.128.1.1.2.130.1.8   hwXponDynamicMacAddr
    'hex_string:macs........': '.1.3.6.1.4.1.2011.6.128.1.1.2.130.1.8.{1}.1.0.3.{2}.47.0.0',
}

# Получение незарегистрированных ONU за GPON-портом. Незарегистрированными считаются ONT, к которым привязаны
# line-profile и srv-profile с именем "activate". Это сделано специально, мы приняли решение вешать дефолтный профиль
# на "незарегистрированные" ONT, что бы у них был доступ к локальным ресурсам.
#
# На вход обязательно нужно передать: ifIndex GPON-порта.
walk_unregistered_onus_on_port = {
    'helper': 'huawei_get_inactive_onts',
    # sn                  .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3  hwGponDeviceOntSn
    'hex_string:sn':     '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3.{1}',
    # line-profile-name   .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.7  hwGponDeviceOntLineProfName
    'line-profile-name': '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.7.{1}',
    # srv-profile-name    .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.8  hwGponDeviceOntServiceProfName
    'srv-profile-name':  '.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.8.{1}',
}

# Создание line-profile.
# На вход обязательно передаем: имя профиля.
create_lineprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.61.1.7  hwGponDeviceLineProfileRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.61.1.7', '{to_index:1}', '4', 'INTEGER'],
]

# Привязка DBA-profile к t-cont в line-profile.
# На вход обязательно передать: имя line-profile, имя DBA-profile.
set_tcont_dba_profile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.62.1.3  hwGponDeviceLineProfTcontCfgDbaProfileName
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.62.1.3', '{to_index_with_length:1}.4', '{2}', 'OCTETSTR'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.62.1.4  hwGponDeviceLineProfTcontCfgRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.62.1.4', '{to_index_with_length:1}.4', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6  hwGponDeviceLineProfileCommit
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6', '{to_index:1}', '1', 'INTEGER'],
]

# Привязка gem к t-cont в line-profile.
# На вход обязательно передать: имя line-profile, номер GEM, номер t-cont.
set_gem_tcont = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.63.1.4  hwGponDeviceLineProfGemCfgTcontIndex
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.63.1.4', '{to_index_with_length:1}.{2}', '{3}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.63.1.5  hwGponDeviceLineProfGemCfgServiceType
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.63.1.5', '{to_index_with_length:1}.{2}', '1', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.63.1.9  hwGponDeviceLineProfGemCfgRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.63.1.9', '{to_index_with_length:1}.{2}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6  hwGponDeviceLineProfileCommit
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6', '{to_index:1}', '1', 'INTEGER'],
]

# Создание gem-mapping.
# На вход обязательно передать: имя line-profile, номер GEM, mapping index, vlanid.
set_gem_mapping = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.64.1.4 hwGponDeviceLineProfMappingCfgMappingMode
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.64.1.4', '{to_index_with_length:1}.{2}.{3}', '1', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.64.1.8 hwGponDeviceLineProfMappingCfgVlanId
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.64.1.8', '{to_index_with_length:1}.{2}.{3}', '{4}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.64.1.10 hwGponDeviceLineProfMappingCfgRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.64.1.10', '{to_index_with_length:1}.{2}.{3}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6  hwGponDeviceLineProfileCommit
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.61.1.6', '{to_index:1}', '1', 'INTEGER'],
]

# Назначение native-vlan для ethernet-порта onu.
# На вход обязательно передать: ifIndex GPON-порта, ont_id, номер ethernet порта, vlanid.
set_onu_eth_port_native_vlan = [
    # .1.3.6.1.4.1.2011.6.145.1.1.1.26.1.1 hwGponOntPortNativeVlan
    ['.1.3.6.1.4.1.2011.6.145.1.1.1.26.1.1', '{1}.{2}.47.{3}', '{4}', 'INTEGER'],
]

delete_lineprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.61.1.7  hwGponDeviceLineProfileRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.61.1.7', '{to_index:1}', '6', 'INTEGER'],
]

# Создание srv-profile.
# На вход обязательно передаем: имя профиля.
create_srvprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.65.1.4   hwGponDeviceSrvProfileRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.65.1.4', '{to_index:1}', '4', 'INTEGER'],
]

# Список всех btv пользователей.
walk_igmp_users = {
    # index          .1.3.6.1.4.1.2011.6.28.16.1.24 hwDslamNtvUserIndex
    'index':        '.1.3.6.1.4.1.2011.6.28.16.1.24',
    # service-port   .1.3.6.1.4.1.2011.6.28.16.1.38 hwDslamNtvUserFlowID
    'service-port': '.1.3.6.1.4.1.2011.6.28.16.1.38',
}

# Создание btv пользователя.
# На вход обязательно передать: index пользователя, service-port id для мультикаста.
add_igmp_user = [
    # .1.3.6.1.4.1.2011.6.28.16.1.3 hwDslamNtvUserRowStatus
    ['.1.3.6.1.4.1.2011.6.28.16.1.3', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.28.16.1.38 hwDslamNtvUserFlowID
    ['.1.3.6.1.4.1.2011.6.28.16.1.38', '{1}', '{2}', 'INTEGER'],
]

# Удаление btv пользователя.
# На вход обязательно передать: index igmp-пользователя
delete_igmp_user = [
    # .1.3.6.1.4.1.2011.6.28.16.1.3 hwDslamNtvUserRowStatus
    ['.1.3.6.1.4.1.2011.6.28.16.1.3', '{1}', '6', 'INTEGER'],
]

# Добавление service-port в члены мультикаст-влана
# На вход обязательно передать: index пользователя (см. add_igmp_user)
add_multicast_member = [
    # .1.3.6.1.4.1.2011.6.28.124.1.1 hwDslamNtvMVlanMembershipStatus
    ['.1.3.6.1.4.1.2011.6.28.124.1.1', '50.{1}', '1', 'INTEGER'],
]

# Создание service-port.
# На вход обязательно передать: service-port index, номер слота, номер порта, ont_id, gem, vlanid.
create_service_port = [
    # .1.3.6.1.4.1.2011.5.14.5.2.1.2 hwExtSrvFlowPara1
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.2', '{1}', '0', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.3 hwExtSrvFlowPara2
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.3', '{1}', '{2}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.4 hwExtSrvFlowPara3
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.4', '{1}', '{3}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.5 hwExtSrvFlowPara4
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.5', '{1}', '{4}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.6 hwExtSrvFlowPara5
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.6', '{1}', '{5}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.7 hwExtSrvFlowParaType
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.7', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.8 hwExtSrvFlowVlanid
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.8', '{1}', '{6}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.11 hwExtSrvFlowMultiServiceType
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.11', '{1}', '1', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.12 hwExtSrvFlowMultiServiceUserPara
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.12', '{1}', '{6}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.15 hwExtSrvFlowRowStatus
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.15', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.18 hwExtSrvFlowTagTransform
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.18', '{1}', '2', 'INTEGER'],
]

# Удаление service-port.
# На вход обязательно передать: service-port index
delete_service_port = [
    # .1.3.6.1.4.1.2011.5.14.5.2.1.15 hwExtSrvFlowRowStatus
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.15', '{1}', '6', 'INTEGER'],
]

# Создание service-port для ТВ.
# На вход обязательно передать: service-port index, номер слота, номер порта, ont_id, gem.
create_multicast_service_port = [
    # .1.3.6.1.4.1.2011.5.14.5.2.1.2 hwExtSrvFlowPara1
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.2', '{1}', '0', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.3 hwExtSrvFlowPara2
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.3', '{1}', '{2}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.4 hwExtSrvFlowPara3
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.4', '{1}', '{3}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.5 hwExtSrvFlowPara4
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.5', '{1}', '{4}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.6 hwExtSrvFlowPara5
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.6', '{1}', '{5}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.7 hwExtSrvFlowParaType
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.7', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.8 hwExtSrvFlowVlanid
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.8', '{1}', '50', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.9 hwExtSrvFlowReceiveTrafficDescrIndex
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.9', '{1}', '8', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.10 hwExtSrvFlowTransmitTrafficDescrIndex
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.10', '{1}', '8', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.11 hwExtSrvFlowMultiServiceType
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.11', '{1}', '1', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.12 hwExtSrvFlowMultiServiceUserPara
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.12', '{1}', '50', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.15 hwExtSrvFlowRowStatus
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.15', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.5.2.1.18 hwExtSrvFlowTagTransform
    ['.1.3.6.1.4.1.2011.5.14.5.2.1.18', '{1}', '2', 'INTEGER'],
]

# Создание vlan translation в srvprofile.
# На вход обязательно передать: имя srv-profile, тип порта (для eth - 47), номер порта, vlanid, priority.
config_vlan_translation_srvprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.68.1.6  hwGponDeviceSrvProfPortVlanCfgPortVlanType
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.68.1.6', '{to_index_with_length:1}.{2}.{3}.{4}.-1.-1', '2', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.68.1.8  hwGponDeviceSrvProfPortVlanCfgPortSVlan
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.68.1.8', '{to_index_with_length:1}.{2}.{3}.{4}.-1.-1', '{4}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.68.1.5  hwGponDeviceSrvProfPortVlanCfgRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.68.1.5', '{to_index_with_length:1}.{2}.{3}.{4}.-1.-1', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.65.1.3  hwGponDeviceSrvProfileCommit
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.65.1.3', '{to_index:1}', '1', 'INTEGER'],
]

# Задаем основные параметыр для srv-profile.
# На вход обязательно передать: имя srv-profile.
config_srvprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.66.1.3 hwGponDeviceSrvProfileEthNum
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.66.1.3', '{to_index:1}', '254', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.66.1.11 hwGponDeviceSrvProfileMultiSrvTransmitMode
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.66.1.11', '{to_index:1}', '3', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.66.1.13 hwGponDeviceSrvProfileMulticastMode
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.66.1.13', '{to_index:1}', '2', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.66.1.14 hwGponDeviceSrvProfileUpIgmpTransmitMode
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.66.1.14', '{to_index:1}', '2', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.66.1.15 hwGponDeviceSrvProfileUpIgmpMsgTranslationVlan
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.66.1.15', '{to_index:1}', '50', 'INTEGER'],
    # .1.3.6.1.4.1.2011.6.128.1.1.3.65.1.3  hwGponDeviceSrvProfileCommit
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.65.1.3', '{to_index:1}', '1', 'INTEGER'],
]

delete_srvprofile = [
    # .1.3.6.1.4.1.2011.6.128.1.1.3.65.1.4   hwGponDeviceSrvProfileRowStatus
    ['.1.3.6.1.4.1.2011.6.128.1.1.3.65.1.4', '{to_index:1}', '6', 'INTEGER'],
]

# Включение автообнаружения на порту OLT.
# На вход обязательно нужно передать: ifIndex GPON-порта
enable_autofind = [
    # .1.3.6.1.4.1.2011.6.128.1.1.2.21.1.4 hwGponDeviceOltControlAutofindOntEnable
    ['.1.3.6.1.4.1.2011.6.128.1.1.2.21.1.4', '{1}', '1', 'INTEGER'],
]

# Включение auto-service-port на порту OLT.
# На вход передать: ifIndex GPON-порта, VLANID, onu-vlan-num, имя inbound-traffic-table, имя outbound-traffic-table.
# Аналог команды:
#   auto-service-port port 0 vlan 420 single-vlan onu-vlan-num 1 inbound traffic-table name activate
#   outbound traffic-table name activate
enable_auto_service_port = [
    # .1.3.6.1.4.1.2011.5.14.35.1.1 hwPortAutoServiceParaRowStatus
    ['.1.3.6.1.4.1.2011.5.14.35.1.1', '{1}', '4', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.35.1.2 hwPortAutoServiceParaType
    ['.1.3.6.1.4.1.2011.5.14.35.1.2', '{1}', '1', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.35.1.3 hwPortAutoServiceParaServiceVlan
    ['.1.3.6.1.4.1.2011.5.14.35.1.3', '{1}', '{2}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.35.1.5 hwPortAutoServiceParaOnuVlanNumber
    ['.1.3.6.1.4.1.2011.5.14.35.1.5', '{1}', '{3}', 'INTEGER'],
    # .1.3.6.1.4.1.2011.5.14.35.1.8 hwPortAutoServiceParaInboundTrafficTableName
    ['.1.3.6.1.4.1.2011.5.14.35.1.8', '{1}', '{4}', 'OCTETSTR'],
    # .1.3.6.1.4.1.2011.5.14.35.1.9 hwPortAutoServiceParaOutboundTrafficTableName
    ['.1.3.6.1.4.1.2011.5.14.35.1.9', '{1}', '{5}', 'OCTETSTR'],
]

# Получение информации о ONU.
# На вход обязательно нужно передать: ifIndex GPON-порта и порядковый номер ONU
get_onu_info = {
    # description        .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.5        hwXponOntInfoProductDescription
    'description..':    '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.5.{1}.{2}',
    # online             .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.1        hwXponOntInfoOnlineDuration
    'online..':         '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.1.{1}.{2}',
    # memory             .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.2        hwXponOntInfoMemoryOccupation
    'memory..':         '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.2.{1}.{2}',
    # cpu                .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.3        hwXponOntInfoCpuOccupation
    'cpu..':            '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.3.{1}.{2}',
    # primary_status     .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.6        hwXponDeviceOntControlPrimaryStatus
    'primary_status..': '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.6.{1}.{2}',
    # load_state         .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.9        hwXponOntInfoAppLoadState
    'load_state..':     '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.9.{1}.{2}',
    # distance           .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.12       hwXponOntLastDistance
    'distance..':       '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.12.{1}.{2}',
    # xml_load_state     .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.10       hwXponOntInfoXmlLoadState
    'xml_load_state..': '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.10.{1}.{2}',
    # xml_load_error     .1.3.6.1.4.1.2011.6.145.1.1.1.4.1.14       hwXponOntInfoXmlLoadErrorInfo
    'xml_load_error..': '.1.3.6.1.4.1.2011.6.145.1.1.1.4.1.14.{1}.{2}',
}

# Сброс статистики ethernet на порту ONU (трафик и ошибки).
# На вход обязательно нужно передать: ifIndex GPON-порта, порядковый номер ONU и номер порта на ONU.
clear_onu_eth_stats = [
    # .1.3.6.1.4.1.2011.6.128.1.1.4.25.1.60 hwGponOntEthernetStatisticClear
    ['.1.3.6.1.4.1.2011.6.128.1.1.4.25.1.60.{1}.{2}', '{3}', '1', 'INTEGER']
]

# Зарегистрировать ONT.
# Здесь мы не добавляем новый ONT, а просто подменяем названия профилей, т.к. у нас ONT регистрируются автоматически.
# На вход обязательно передаем: ifIndex GPON-порта, ont_id, line-profile-name, srv-profile-name, описание.
register_onu = [
    # .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.7 hwGponDeviceOntLineProfName
    ['.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.7', '{1}.{2}', '{3}', 'OCTETSTR'],
    # .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.8 hwGponDeviceOntServiceProfName
    ['.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.8', '{1}.{2}', '{4}', 'OCTETSTR'],
    # .1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9 hwGponDeviceOntDespt
    ['.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9', '{1}.{2}', '{5}', 'OCTETSTR'],
]

# Возвращает DslamInterfaceIfIndex для vlanif
# На вход обязательно передать: VLANID.
get_dslam_ifindex = {
    # dslam_ifindex    .1.3.6.1.4.1.2011.6.161.1.1.1.3  hwIpDslamInterfaceIfIndex
    'dslam_ifindex.': '.1.3.6.1.4.1.2011.6.161.1.1.1.3.4.{1}',
}

# Вешает ACL на интерфейс.
# На вход передать: DslamInterfaceIfIndex, направление (1-inbound, 2-outbound), номер профиля ACL.
set_acl_on_interface = [
    # .1.3.6.1.4.1.2011.6.47.48.1.5 hwFirewallPacketFilterRowStatus
    ['.1.3.6.1.4.1.2011.6.47.48.1.5.{1}.{2}', '{3}', '4', 'INTEGER'],
]

#!/usr/local/bin/python2
# coding=UTF8

import re


def snr_diag_parser(incoming_value):
    """
    Приводит диагностику порта в формате SNR к виду похожему на формат D-Link.

    :param dict incoming_value: словарь с диагностикой от SNR
    :rtype: dict
    :return: словарь с диагностикой в формате D-Link
    """

    # получаем индекс порта и строку с результатами диагностики из входящих данных
    port_index, input_diag = incoming_value['cableDiag'].popitem()

    # паттерн для строк вида "(1, 2)          open\t\t          0"
    pair_pattern = re.compile(r'^(?P<pair>\(\d,\s\d\))\s+(?P<status>\S+)\s+(?P<length>\d+)$')

    vct_result = {'cdLinkStatus': incoming_value['ActualStatus']}

    diag_line_index = 0  # индекс строки с состоянием пары (для определения номера пары)
    for line in input_diag.splitlines():
        pair_match = pair_pattern.match(line)
        if pair_match:
            diag_line_index += 1
            vct_result['cdPair{}Status'.format(diag_line_index)] = {str(port_index): pair_match.group('status')}
            vct_result['cdPair{}Length'.format(diag_line_index)] = {str(port_index): pair_match.group('length')}

    return vct_result

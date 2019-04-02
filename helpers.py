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

    vct_result = {'cdLinkStatus': {incoming_value['ActualStatus']}}

    for line_index, line in enumerate(input_diag.splitlines(), start=1):
        pair_match = pair_pattern.match(line)
        if pair_match:
            vct_result['cdPair{}Status'.format(line_index)] = {str(port_index): pair_match.group('status')}
            vct_result['cdPair{}Length'.format(line_index)] = {str(port_index): pair_match.group('length')}

    return vct_result

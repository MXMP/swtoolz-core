import importlib
import logging
import time
import urllib.parse
from ipaddress import ip_address

import easysnmp
from easysnmp.exceptions import EasySNMPTimeoutError, EasySNMPError
from aiohttp import web

import helpers
import swconfig


def get_model(sys_name, sys_descr, models_list):
    """
    Определяем модель по вхождению подстроки в значения sysDescr и sysName. Проверка идет до первого соответствия.
    Сначала проверяется sysName.

    :param list models_list: список словарей моделей, как в models_by_desc в конфиге
    :param str sys_descr: sysDescr, полученный с устройства
    :param str sys_name: sysName, полученный с устройства
    :return: идентификатор модели или None если совпадений не найдено
    """

    model = 'None'
    for item in models_list:
        for desc_model in item:
            if sys_name is not None:
                if desc_model in sys_name:
                    model = item[desc_model]
            if sys_descr is not None:
                if desc_model in sys_descr:
                    model = item[desc_model]
        if model != 'None':
            break

    return model


def parse_request(request, users):
    """
    Функция для преобразования URL в словарь и определения ошибок.
    В URL каждый параметр идет после символа '/'. Группы параметров разделяются символом '+'.
    Первые три параметра первой группы зарезервированы: /user, /target, /comm_index.
    Каждая группа параметров описывает одно задание.
    Первым параметром в каждой группе является имя словаря или функции в конфигурационном файле.
    Далее следуют параметры для постановки в этот словарь или функцию

    :param users:
    :param request:
    :return:
    """

    # Задаем структуру словаря, которую затем изменяем в процессе обработки
    json_req = {
        'user': request.match_info['user'],
        'target': request.match_info['target_ip'],
        'comm_index': request.match_info['comm_index'],
        'data': [],
        'errors': []}
    # Разделяем весь запрос на несколько групп. В каждой группе находится отдельное задание
    requests = request.match_info['commands'].split('+/')
    # Перебираем все задания/группы
    for i in range(len(requests)):
        # Получаем список параметров для текущего задания
        params = requests[i].split('/')

        # Генерируем список из параметров и добавляем в общий список верхнего уровня для 'data'
        # Параметр с нулевым индексом указывает на имя переменной в файле модуля для конкретного устройства
        # Остальные параметры могут подставляться в эту переменную
        json_req['data'].append({i: v for i, v in enumerate(params)})

    # Если пользователь не найден, добавляем соответствующий код в список ошибок
    if json_req['user'] not in users:
        json_req['errors'].append('User not found')
    else:
        # Если пользователь найден, но для него не найдено snmp-коммунити с соответствующим индексом, добавляем
        # соответствующий код в список ошибок
        if json_req['comm_index'] not in users[json_req['user']].keys():
            json_req['errors'].append('Snmp-community is not defined for this index')

    # Если IP-адрес имеет неправильный формат, добавляем соответствующий код в список ошибок
    try:
        ip_address(json_req['target'])
    except ValueError:
        json_req['errors'].append('IP-address is not correct')

    # Если список ошибок пустой, добавляем в него код '0' - OK (нет ошибок)
    if len(json_req['errors']) == 0:
        json_req['errors'].append('OK')
    return json_req


def str_to_index(input_str, with_length=False):
    """
    Переводит строку в SNMP-индекс. Если `with_length` равен True, то перед индексом добавляется длина строки.

    :param str input_str: строка для перевода
    :param bool with_length: нужно ли добавлять длину строки перед индексом
    :rtype: str
    :return: строка в виде SNMP-индекса
    """

    chars = [str(ord(ch)) for ch in input_str]
    index = '.'.join(chars)
    if with_length:
        return "{}.{}".format(len(input_str), index)
    return index


def quote_hex(input_str):
    """
    Добавляет к каждой паре символов '%' что бы показать что это HEX. Например для серийного номера.

    :param str input_str: строка для экранирования
    :rtype: str
    :return: экранированная строка
    """

    return '%'.join(helpers.split_nth(input_str, 2))


def prepare_oid(params, dataset):
    """
    Функция для подстановки параметров пользователя в OID. Последовательно заменяет '%s' на параметры с ключами кроме
    '0' (первый параметр)
    Также функция заменяет все {№} на элемент № из словаря с данными
    Вообще, это достаточно подозрительная функция и она уже сломала мне мозг, но этот вариант вроде приемлимый :)

    :param dict params: словарь с данными из запроса. Пример: {"1": "24", "0": "set_AdminStatus", "2": "2"}
    :param dataset: данные метода куда будем подставлять параметры
    :return:
    """

    # Перебираем и раскодируем значения элементов словаря, заменяя последовательности '%xx' на их односимвольный
    # эквивалент
    for key in params.keys():
        params[key] = urllib.parse.unquote(params[key])

    # При Walk/Get операциях вторым параметром передается строка, содержащая OID
    if isinstance(dataset, str):
        # Перебираем весь словарь с данными. Ключи при этом сортируем
        for i, k in enumerate(sorted(params.keys())[1:]):
            # Заменяем одну следующую последовательность '%s' на соответствующий элемент словаря
            dataset = dataset.replace('%s', params[k], 1)
            # Заменяем все последовательности '{№}' на соответствующий элемент словаря.
            # Здесь № - номер элемента в сортированном списке ключей
            # Например, все последовательности '{2}' заменяются на второй элемент словаря.
            # Это используется когда нужно подставить одно значение несколько раз
            dataset = dataset.replace('{%s}' % (i + 1), params[k])
            # Подстановка со специальными конвертерами:
            dataset = dataset.replace('{to_index:%s}' % (i + 1), str_to_index(params[k]))
            dataset = dataset.replace('{to_index_with_length:%s}' % (i + 1), str_to_index(params[k], True))
            dataset = dataset.replace('{hex:%s}' % (i + 1), quote_hex(params[k]))
        return dataset

    # При Set операциях вторым параметром передается список, содержащий tag, iid, value, type.
    # Пример: ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '1','1','INTEGER']
    if isinstance(dataset, list):
        # Указатель на элемент словаря из первого параметра. Используется, чтобы в каждом элементе dataset
        # не начинать перебор элементов my_dict сначала
        shft = 1
        # Перебираем список, причем ориентируемся на индекс, который затем потребуется для замены
        for indx, item in enumerate(dataset):
            # В каждом элементе списка делаем по одной замене столько раз, сколько встречается последовательность
            # '%s', при этом инкрементируем значение указателя
            for i in range(dataset[indx].count('%s')):
                # Если указатель не достиг максимально возможного значения, значит замена еще возможна
                if shft < len(params):
                    # Заменяем одну следующую последовательность '%s' на соответствующий элемент словаря.
                    # При замене ориентируемся на позицию shft
                    dataset[indx] = dataset[indx].replace('%s', params[sorted(params.keys())[shft:][0]], 1)
                    shft += 1
            # Для каждого элемента, который является строкой, выполняем такую же процедуру,
            # как если бы изначально получили строку в dataset
            for i, k in enumerate(sorted(params.keys())[1:]):
                # Заменяем все последовательности '{№}' на соответствующий элемент словаря.
                # Здесь № - номер элемента в сортированном списке ключей
                # Например, все последовательности '{2}' заменяются на второй элемент словаря.
                # Это используется когда нужно подставить одно значение несколько раз
                dataset[indx] = dataset[indx].replace('{%s}' % (i + 1), params[k])
                # Подстановка со специальными конвертерами:
                dataset[indx] = dataset[indx].replace('{to_index:%s}' % (i + 1), str_to_index(params[k]))
                dataset[indx] = dataset[indx].replace('{to_index_with_length:%s}' % (i + 1),
                                                      str_to_index(params[k], True))
                dataset[indx] = dataset[indx].replace('{hex:%s}' % (i + 1), quote_hex(params[k]))
        return dataset


def process_device(device_module, request_params, json_resp, target_ip, snmp_comm, model, request):
    # Пробуем получить из модуля множитель 'timeout_mf' и применить его. При неудаче
    # будет использован таймаут из файла конфигурации сервиса
    current_snmp_timeout = int(swconfig.snmp_timeout * getattr(device_module, 'timeout_mf', 1))

    # request_params - все, что содержится в ключе 'data' из запроса ('request'). Представлен в виде списка.
    # request_param - конкретный элемент списка, содержащий параметры конкретного запроса. Представлен в
    # виде словаря. В debug-лог пишется как 'URL Params'.
    # "data": [{"1": "2", "0": "swL2PortCtrlAdminState"}, {"0": ""}]
    # dataset - словарь вида {'Metric':'OID'}, список списков вида [['tag', 'iid', 'value', 'type']] или
    # кортеж со словарем внутри ({'2':'enable'},) из файла с таким же именем, как имя модели устройства (model)
    logging.debug(request_params)
    for request_param in request_params:
        try:
            method_name = request_param[0]
        except KeyError:
            continue

        # Пробуем извлечь параметр (метод) из файла модуля
        try:
            dataset = getattr(device_module, method_name)
        except AttributeError:
            if method_name == 'list':
                json_resp['data']['list'] = [str(d) for d in dir(device_module) if d[0] != '_']
            else:
                logging.error(f"Can't find param '{method_name}' from module '{model}'!")
        else:
            # Для режима отладки пишем в лог кто и что у нас запросил
            if swconfig.debug_mode:
                client_host, client_port = request.transport.get_extra_info('peername')
                logging.debug(f"Request from {client_host}:{client_port}."
                              f"Dataset: {str(dataset)}, URL Params: {str(request_param)}")
            current_snmp_retries = swconfig.snmp_retries
            # Если параметр находится в списке 'no_retries', сбрасываем для него число дополнительных попыток в 0
            if method_name in swconfig.no_retries:
                current_snmp_retries = 0

            # Создаем SNMP-сессию
            session = easysnmp.Session(hostname=target_ip, community=snmp_comm, version=2,
                                       retries=current_snmp_retries, use_numeric=True, timeout=current_snmp_timeout)

            # dataset может быть как словарем (для get/walk) так и списком (для set) и
            # кортежем (для неизменяемых пользовательских данных). Обрабатываем эти случаи отдельно
            if isinstance(dataset, dict):
                # Получаем функцию-хелпер и удаляем этот элемент, чтобы не мешался
                helper = None
                data_for_helper = {}
                try:
                    helper_name = dataset.get('helper')
                    del (dataset['helper'])
                    helper = getattr(helpers, helper_name)
                    logging.debug(f"Found {helper_name} helper function.")
                except KeyError:
                    pass
                except AttributeError:
                    logging.error(f"Can't find {helper_name} helper function.")

                # если хотя бы в одном названии параметра будет присутствовать точка, то выполняется GET-запрос
                get_notwalk = False
                for paramname in dataset:
                    if '.' in paramname:
                        get_notwalk = True
                        break

                snmp_oids_list = [prepare_oid(request_param.copy(), dataset[paramname]) for paramname in dataset]

                # выполняем SNMP-опрос
                snmp_method = session.get if get_notwalk else session.walk
                snmp_result = snmp_method(snmp_oids_list)

                for var in snmp_result:
                    # Убеждаемся, что ответ распознан, т.е. не None
                    if var.oid_index is not None:
                        # Получаем полный OID.
                        full_oid = f"{var.oid}.{var.oid_index}"
                        # Здесь k - имя параметра, по которому получим значение, а prep_k - имя ключа в 'data'. В
                        # случае walk-запроса значения k и prep_k равны, а в случае get имя prep_k обрезается до первой
                        # точки, не включая ее
                        for k in dataset:
                            # Если используем метод get, то получаем имя ключа из параметра k с начала до первой
                            # точки, не включая ее, и задаем трейлер
                            # Для метода опроса walk имя ключа будет равно параметру k, а трейлер должен быть пустым
                            if get_notwalk:
                                prep_k = k[0:k.find('.')]
                                trailer = '*'
                            else:
                                prep_k = k
                                trailer = '.'
                            # Значение trailer прибавляем для избежания ложного срабатывания при сравнении OID,
                            # например ...1.2.3.2 и ....1.2.3.20
                            # При Get-запросе full_oid всегда является "конечным", поскольку это "прицельный"
                            # запрос. Поэтому здесь используем "жесткий" трейлер = '*'
                            # Теперь будут сравниваться .1.2.3.2* и .1.2.3.20*.
                            # Первое значение уже не входит во второе, как было бы в предыдущем случае
                            # При Walk-запросе full_oid заранее неизвестен, поэтому используем "мягкий" трейлер =
                            # '.' (символ точки является частью OID)
                            # Также при Walk-запросе у нас есть отдельное требование - ветки должны быть одной длины
                            # Если оно выполнено, значит сравниваемые ветки разные и точку использовать допустимо.
                            # Ниже пример tmp_oid, которые "пересеклись" бы без трейлера
                            # full_oid: .1.3.6.1.2.1.31.1.1.1.18.1
                            # tmp_oid:  .1.3.6.1.2.1.31.1.1.1.18 (вместе с трейлером '.' входит в full_oid)
                            #
                            # full_oid: .1.3.6.1.2.1.31.1.1.1.1.1
                            # tmp_oid:  .1.3.6.1.2.1.31.1.1.1.1 (вместе с трейлером '.' входит в full_oid)

                            # Временный OID, полученный из конфигурационного файла, и в который уже подставлены
                            # пользовательские параметры
                            tmp_oid = prepare_oid(request_param.copy(), dataset[k])
                            # Проверяем, есть ли значение временного OID в полном OID
                            if tmp_oid + trailer in full_oid + trailer:
                                # Получаем оставшуюся часть от OID
                                remainder = full_oid.replace(tmp_oid + '.', '')
                                # Если используем метод get, оставшаяся часть будет равна iid
                                if get_notwalk:
                                    remainder = var.oid_index
                                    # Альтернативный вариант для использования нескольких
                                    # последних чисел OID в имени подраздела, например '7.100'
                                    if k.count('.') > 1:
                                        remainder = ".".join(full_oid.split(".")[-k.count('.'):])

                                # Разбиваем имя параметра по ':'. Если все разбилось, то в первой части будет
                                # "форматтер", который и применяем.
                                splitted_prep_k = prep_k.split(':')
                                if len(splitted_prep_k) == 2:
                                    try:
                                        formatter = getattr(helpers, splitted_prep_k[0])
                                        prep_k = splitted_prep_k[1]
                                        value = formatter(var.value)
                                    except AttributeError:
                                        logging.warning(f'Formatter {splitted_prep_k[0]} not found.')
                                        value = var.value
                                else:
                                    if var.value == 'NOSUCHINSTANCE':
                                        value = ''
                                    else:
                                        value = var.value

                                # Например в конфиге указан OID 1.2.3.2.1, tag будет 1.2.3.2.1.X, iid - Y (может
                                # быть пустым).
                                # Полный OID (full_oid) будет 1.2.3.2.1.X.Y
                                # Имя раздела (словаря) будет k, а подраздела (ключа метрики) - remainder
                                if helper and prep_k not in data_for_helper:
                                    data_for_helper[prep_k] = {}
                                elif prep_k not in json_resp['data']:
                                    json_resp['data'][prep_k] = {}

                                if helper:
                                    data_for_helper[prep_k][remainder] = value
                                else:
                                    json_resp['data'][prep_k][remainder] = value

                # вызываем функцию хелпер, если она была указана
                if helper:
                    json_resp['data'].update(helper(data_for_helper, target_ip))

            # Если dataset является списком, выполняем для него set-операции
            if isinstance(dataset, list):
                varlist = []
                for VarBindItem in dataset:
                    prepaired_oid = prepare_oid(request_param.copy(), VarBindItem[:])
                    full_prepaired_oid = '.'.join(prepaired_oid[0:2])
                    varlist.append((full_prepaired_oid, prepaired_oid[2], prepaired_oid[3],))

                try:
                    session.set_multiple(varlist)
                except EasySNMPError:
                    json_resp['data'][method_name] = False
                else:
                    json_resp['data'][method_name] = True

                time.sleep(swconfig.set_iter_delay)

            # Если dataset является кортежем, просто возвращаем его первый элемент. Это нужно для хранения
            # пользовательских словарей в конфиге swtoolz-core
            if isinstance(dataset, tuple):
                json_resp['data'][method_name] = dataset[0]

    return json_resp['data']


async def handle_get(request):
    answer = {
        'request': {
            'user': None,
            'target': None,
            'comm_index': None,
            'data': [],
            'errors': [],
        },
        'response': {
            'target': None,
            'sys_descr': None,
            'sys_uptime': None,
            'sys_name': None,
            'sys_location': None,
            'model': None,
            'query_time': None,
            'data': {},
        },
    }

    answer['request'].update(parse_request(request, swconfig.users))
    answer['response']['target'] = answer['request']['target']

    # Получаем SNMP-Community для устройства
    snmp_comm = swconfig.users[answer['request']['user']][answer['request']['comm_index']]

    # Создаем SNMP-сессию
    session = easysnmp.Session(hostname=answer['request']['target'], community=snmp_comm, version=2,
                               retries=swconfig.snmp_retries, use_numeric=True, timeout=swconfig.snmp_timeout)

    # Фиксируем текущее время
    start_time = time.time()
    try:
        # Выполняем опрос параметров из default_info
        snmp_default_params = session.get(list(swconfig.default_info.values()))
    except EasySNMPTimeoutError:
        # Устройство недоступно, выставляем модель в 'None'
        answer['response']['model'] = 'None'
    else:
        # Помещаем в словарь результаты опроса параметров из default_info
        for def_param_index, def_param in enumerate(swconfig.default_info):
            answer['response'][def_param] = snmp_default_params[def_param_index].value

        # Получаем идентификатор модели
        answer['response']['model'] = get_model(answer['response']['sys_name'], answer['response']['sys_descr'],
                                                swconfig.models_by_desc)

    # Если в списке команд (методов) есть зарезервированная команда (метод), то выполняем опрос
    # оборудования даже если оно недоступно
    forced = False
    for request_param in answer['request']['data']:
        if len(set(request_param.values()) & set(swconfig.forced_mtd)) > 0:
            forced = True

    # Работаем, если устройство доступно (определили модель) или выставлен флаг 'forced'
    if answer['response']['model'] != 'None' or forced:
        # Пробуем импортировать модуль, описывающий методы для данной модели
        try:
            device_module = importlib.import_module(answer['response']['model'])
            importlib.reload(device_module)
        except ImportError:
            logging.error(f"Can't import module '{answer['response']['model']}' for '{answer['request']['target']}'!")
        else:
            data_from_device = process_device(device_module, answer['request']['data'], answer['response'],
                                              answer['request']['target'], snmp_comm, answer['response']['model'],
                                              request)
            answer['response']['data'] = data_from_device

    # Время, затраченное на опрос
    answer['response']['query_time'] = str(int((time.time() - start_time) * 1000))

    return web.json_response(answer)

#!/usr/local/bin/python2
#coding=UTF8
#version 1.7.20 (2016.07.20)

import sys, socket, time, datetime, struct, logging, threading, netsnmp, string, json, urllib
from os import sep
from daemon import Daemon
from swconfig import interface_ip, port, sleep_int, stats_int, set_iter_delay, snmp_timeout
from swconfig import snmp_retries, no_retries, forced_mtd, logfile,  users, default_info
from swconfig import models_by_desc, http_header, debug_mode

logging.basicConfig(filename = logfile, level = logging.DEBUG, format = '%(asctime)s  %(message)s')

# Добавляем директорию 'devices' в список path. Это нужно, чтобы демон мог находить модули в этой директории
sys.path.append('%s%sdevices' % (sys.path[0], sep))

# Хорошая функция проверки правильности IP-адреса, взятая с 'переполненного стека'

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


# Функция для подстановки параметров пользователя в OID. Последовательно заменяет '%s' на параметры с ключами кроме '0' (первый параметр)
# Также функция заменяет все {№} на элемент № из словаря с данными
# Вообще, это достаточно подозрительная функция и она уже сломала мне мозг, но этот вариант вроде приемлимый :)
def prepare_oid(my_dict, my_data):
    # Первым параметром передается словарь с данными из запроса. Пример: {"1": "24", "0": "set_AdminStatus", "2": "2"}
    # Перебираем и раскодируем значения элементов словаря, заменяя последовательности '%xx' на их односимвольный эквивалент
    for key in my_dict.keys():
	my_dict[key] = urllib.unquote(my_dict[key])

    # При Walk/Get операциях вторым параметром передается строка, содержащая OID
    if isinstance(my_data, str):
	# Перебираем весь словарь с данными. Ключи при этом сортируем
	for i,k in enumerate(sorted(my_dict.keys())[1:]):
	    # Заменяем одну следующую последовательность '%s' на соответствующий элемент словаря
	    my_data = my_data.replace('%s', my_dict[k], 1)
	    # Заменяем все последовательности '{№}' на соответствующий элемент словаря. Здесь № - номер элемента в сортированном списке ключей
	    # Например, все последовательности '{2}' заменяются на второй элемент словаря. Это используется когда нужно подставить одно значение несколько раз
	    my_data = my_data.replace('{%s}' % (i+1), my_dict[k])
	return my_data

    # При Set операциях вторым параметром передается список, содержащий tag, iid, value, type. Пример: ['.1.3.6.1.4.1.171.12.58.1.1.1.12', '1','1','INTEGER']
    if isinstance(my_data, list):
	# Указатель на элемент словаря из первого параметра. Используется, чтобы в каждом элементе my_data не начинать перебор элементов my_dict сначала
	shft = 1
	# Перебираем список, причем ориентируемся на индекс, который затем потребуется для замены
	for indx,item in enumerate(my_data):
	    # В каждом элементе списка делаем по одной замене столько раз, сколько встречается последовательность '%s', при этом инкрементируем значение указателя
	    for i in range(my_data[indx].count('%s')):
		# Если указатель не достиг максимально возможного значения, значит замена еще возможна
		if shft < len(my_dict):
		    # Заменяем одну следующую последовательность '%s' на соответствующий элемент словаря. При замене ориентируемся на позицию shft
		    my_data[indx] = my_data[indx].replace('%s', my_dict[ sorted(my_dict.keys()) [shft:] [0] ], 1)
		    shft += 1
	    # Для каждого элемента, который является строкой, выполняем такую же процедуру, как если бы изначально получили строку в my_data
	    for i,k in enumerate(sorted(my_dict.keys())[1:]):
		# Заменяем все последовательности '{№}' на соответствующий элемент словаря. Здесь № - номер элемента в сортированном списке ключей
		# Например, все последовательности '{2}' заменяются на второй элемент словаря. Это используется когда нужно подставить одно значение несколько раз
		my_data[indx] = my_data[indx].replace('{%s}' % (i+1), my_dict[k])
	return my_data


# Функция для преобразования адресной строки в словарь и определения ошибок
# В адресной строке каждый параметр идет после символа '/'. Группы параметров разделяются символом '+'
# Первые три параметра первой группы зарезервированы: /user, /target, /comm_index.
# Каждая группа параметров описывает одно задание.
# Первым параметров в каждой группе является имя словаря или функции в конфигурационном файле
# Далее следуют параметры для постановки в этот словарь или функцию
def parse_request(request):
    # Задаем структуру словаря, которую затем изменяем в процессе обработки
    json_req = {'user':'', 'target':'', 'comm_index':'', 'data':[], 'errors':[]}
    # Разделяем весь запрос на несколько групп. В каждой группе находится отдельное задание
    requests = request.split('+')
    # Перебираем все задания/группы
    for i in range(len(requests)):
	# Получаем список параметров для текущего задания
	params = requests[i].split('/')
	# Сдвиг используемый чтобы отличать первую группу параметров от остальных
	shft = 0
	# Если работаем с первой группой параметров, то определяем пользователя, цель и индекс snmp-коммунити
	if i == 0:
	    # Первые три помещаем в словарь на зарезервированные места в том случае, если они определены
	    if len(params)>1:
		json_req['user'] = params[1]
	    if len(params)>2:
		json_req['target'] = params[2]
	    if len(params)>3:
		json_req['comm_index'] = params[3]
	    # Если параметров недостаточно, добавляем соответствующий код в список ошибок
	    else:
		json_req['errors'].append(1)
	    shft = 3
	# Генерируем список из параметров и добавляем в общий список верхнего уровня для 'data'
	# Параметр с нулевым индексом указывает на имя переменной в файле модуля для конкретного устройства
	# Остальные параметры могут подставляться в эту переменную
	json_req['data'].append(dict((str(p-shft-1),params[p]) for p in range(shft+1,len(params))))
    # -- Обработка ошибок --
    # Если пользователь не найден, добавляем соответствующий код в список ошибок
    if json_req['user'] not in users:
	json_req['errors'].append(2)
    else:
	# Если пользователь найден, но для него не найдено snmp-коммунити с соответствующим индексом, добавляем соответствующий код в список ошибок
	if json_req['comm_index'] not in users[json_req['user']].keys():
	    json_req['errors'].append(3)
    # Если IP-адрес имеет неправильный формат, добавляем соответствующий код в список ошибок
    if not is_valid_ipv4_address(json_req['target']):
	json_req['errors'].append(4)
    # Если список ошибок пустой, добавляем в него код '0' - OK (нет ошибок)
    if len(json_req['errors']) == 0:
	json_req['errors'].append(0)
    return json_req

# Родительсткий класс поллера, который запускается в отдельном потоке
class thrPoller(threading.Thread):
    def __init__(self, requests, client_ip, client_port, responses):
	threading.Thread.__init__(self)
	self.requests = requests
	self.client_ip = client_ip
	self.client_port = client_port
	self.responses = responses
	self.users = users
    def run(self):
	# Задаем структуру словаря, который будет добавляться в общий словарь ответов
	json_resp   = {'target':'', 'sys_descr':'', 'sys_uptime':'', 'sys_name':'', 'sys_location':'', 'model':'', 'query_time':'', 'data':{}}
	# Получаем IP адрес устройства
	target_ip   = self.requests[self.client_ip][self.client_port]['target']
	# Получаем список параметров (данные) для устройства
	data_params = self.requests[self.client_ip][self.client_port]['data']
	# Получаем SNMP-Community для устройства
	snmp_comm   = self.users[self.requests[self.client_ip][self.client_port]['user']][self.requests[self.client_ip][self.client_port]['comm_index']]
	# Формируем структуру varlist/varbind из параметров, перечисленных в default_info
	snmp_var    = netsnmp.VarList(*[ netsnmp.Varbind(default_info[def_param]) for def_param in default_info ])
	# Фиксируем текущее время
	start_time  = time.time()
	# Выполняем опрос устройства
	snmp_query  = netsnmp.snmpget(*snmp_var, Version = 2, DestHost = target_ip, Community = snmp_comm, Timeout = snmp_timeout, Retries = snmp_retries, UseNumeric = 1)
	# Время, затраченное на опрос
	snmp_query_time = str(int((time.time()-start_time)*1000))
	# Заполняем словарь данными
	json_resp['target']       = self.requests[self.client_ip][self.client_port]['target']
	# Помещаем в словарь результаты опроса параметров из default_info
	for def_param_index, def_param in enumerate(default_info):
	    json_resp[def_param] = snmp_query[def_param_index]
	# Определяем модель по вхождению подстроки в значения sysDescr и sysName
	# Проверка идет до первого соответствия. Сначала проверяется sysName
	model = 'None'
	for item in models_by_desc:
	    for desc_model in item:
		if json_resp['sys_name'] is not None:
		    if desc_model in json_resp['sys_name']:
			model = item[desc_model]
		if json_resp['sys_descr'] is not None:
		    if desc_model in json_resp['sys_descr']:
			model = item[desc_model]
	    if model != 'None':
		break
	json_resp['model']        = model
	json_resp['query_time']   = snmp_query_time

	# Если в списке команд (методов) есть зарезервированная команда (метод), то выполняем опрос оборудования даже если оно недоступно
	forced = False
	for data_param in data_params:
	    if len( set(data_param.values()) & set(forced_mtd) ) > 0:
		forced = True

	# Работаем, если устройство доступно (определили модель) или выставлен флаг 'forced'
	if model != 'None' or forced:
	    # Пробуем импортировать модуль, описывающий методы для данной модели
	    try:
		device = __import__(model)
		reload(device)
	    except:
		logging.info("WARNING: Can't import module '%s' for '%s'!", model, target_ip)
	    else:
		# Пробуем получить из модуля множитель 'timeout_mf' и применить его. При неудаче используем таймаут из файла конфигурации сервиса
		try:
		    timeout_mf = getattr(device, 'timeout_mf')
		    current_snmp_timeout = int(snmp_timeout * timeout_mf)
		except:
		    current_snmp_timeout = snmp_timeout
		# data_params - все, что содержится в ключе 'data' из запроса ('request'). Представлен в виде списка
		# data_param - конкретный элемент списка, содержащий параметры конкретного запроса. Представлен в виде словаря. В debug-лог пишется как 'URL Params'.
		# "data": [{"1": "2", "0": "swL2PortCtrlAdminState"}, {"0": ""}]
		# dataset - словарь вида {'Metric':'OID'}, список списков вида [['tag', 'iid', 'value', 'type']] или->
		# ->кортеж со словарем внутри ({'2':'enable'},) из файла с таким же именем, как имя модели устройства (model)
		for data_param in data_params:
		    if '0' in data_param:
			# Пробуем извлечь параметр (метод) из файла модуля
			try:
			    dataset = getattr(device, data_param['0'])
			except:
			    if data_param['0'] == 'list':
#				logging.info("INFO: Requested 'list' command from client %s:%s.", self.client_ip, self.client_port)
				json_resp['data']['list'] = [str(d) for d in dir(device) if d[0]!='_']
			    else:
				logging.info("WARNING: Can't find param '%s' from module '%s'!", data_param['0'], model)
			else:
			    # Для режима отладки пишем в лог кто и что у нас запросил
			    if debug_mode:
				logging.info("DEBUG: Request from %s:%s. Dataset: '%s', URL Params: %s", self.client_ip, self.client_port, str(dataset), str(data_param))
			    current_snmp_retries = snmp_retries
			    # Если параметр находится в списке 'no_retries', сбрасываем для него число дополнительных попыток в 0
			    if data_param['0'] in no_retries:
				current_snmp_retries = 0
			    # dataset может быть как словарем (для get/walk) так и списком (для set) и кортежем (для неизменяемых пользовательских данных). Обрабатываем эти случаи отдельно
			    if isinstance(dataset, dict):
				get_notwalk = False
				for paramname in dataset.keys():
				    if '.' in paramname:
					get_notwalk = True
				big_bada_boom = False
				snmp_var = netsnmp.VarList(*[ netsnmp.Varbind(prepare_oid(data_param.copy(), dataset[paramname])) for paramname in dataset.keys() ])
				# Формируем структуру varlist/varbind в зависимости о метода запроса (get или walk)
				if get_notwalk:
				    snmp_query   = netsnmp.snmpget(*snmp_var,Version = 2, DestHost = target_ip, Community = snmp_comm, Timeout = current_snmp_timeout, Retries = current_snmp_retries, UseNumeric = 1)
				else:
				    snmp_query   = netsnmp.snmpwalk(snmp_var,Version = 2, DestHost = target_ip, Community = snmp_comm, Timeout = current_snmp_timeout, Retries = current_snmp_retries, UseNumeric = 1)
				# ВНИМАНИЕ! Это обход бага. _Если в конфиге (модуле) задать OID задать без точки в самом начале_, то при формировании varlist/varbind может возникнуть проблема
				# Заключается она в том, что нельзя перебрать snmp_var, хотя по формальным признакам для этого нет препятствий
				# Плюс попутно возникают другие странности, например logging.info выбрасывает исключение
				# Отладка результатов не дала, похоже что это именно БАГ
				# Если задавать все OID, начинающиеся с точки, то все работает хорошо
				try:
				    for var_ in snmp_var:
					pass
				except:
				    big_bada_boom = True
				if not big_bada_boom:
				    for var_ in snmp_var:
					# Убеждаемся, что ответ распознан, т.е. не None
					if ( (var_.tag is not None) & (var_.iid is not None) ):
					    # Получаем полный OID. В ответе он разбит на части, находящиеся в tag и iid, которые мы склеиваем вместе
					    full_oid = var_.tag+'.'+var_.iid
					    # Здесь k - имя параметра, по которому получим значение, а prep_k - имя ключа в 'data'
					    # В случае walk-запроса значения k и prep_k равны, а в случае get имя prep_k обрезается до первой точки, не включая ее
					    for k in dataset:
						# Если используем метод get, то получаем имя ключа из параметра k с начала до первой точки, не включая ее, и задаем трейлер
						# Для метода опроса walk имя ключа будет равно параметру k, а трейлер должен быть пустым
						if get_notwalk:
						    prep_k = k[0:k.find('.')]
						    trailer = '*'
						else:
						    prep_k = k
						    trailer = '.'
						# Значение trailer прибавляем для избежания ложного срабатывания при сравнении OID, например ...1.2.3.2 и ....1.2.3.20
						# При Get-запросе full_oid всегда является "конечным", поскольку это "прицельный" запрос. Поэтому здесь используем "жесткий" трейлер = '*'
						# Теперь будут сравниваться .1.2.3.2* и .1.2.3.20*. Первое значение уже не входит во второе, как было бы в предыдущем случае
						# При Walk-запросе full_oid заранее неизвестен, поэтому используем "мягкий" трейлер = '.' (символ точки является частью OID)
						# Также при Walk-запросе у нас есть отдельное требование - ветки должны быть одной длины
						# Если оно выполнено, значит сравниваемые ветки разные и точку использовать допустимо. Ниже пример tmp_oid, которые "пересеклись" бы без трейлера
						# full_oid: .1.3.6.1.2.1.31.1.1.1.18.1, tmp_oid: .1.3.6.1.2.1.31.1.1.1.18 (вместе с трейлером '.' входит в full_oid)
						# full_oid: .1.3.6.1.2.1.31.1.1.1.1.1,  tmp_oid: .1.3.6.1.2.1.31.1.1.1.1  (вместе с трейлером '.' входит в full_oid)

						# Временный OID, полученный из конфигурационного файла, и в который уже подставлены пользовательские параметры
						tmp_oid = prepare_oid(data_param.copy(),dataset[k])
						# Проверяем, есть ли значение временного OID в полном OID
						if (tmp_oid+trailer in full_oid+trailer):
						    # Получаем оставшуюся часть от OID
						    remainder = full_oid.replace(tmp_oid+'.','')
						    # Если используем метод get, оставшаяся часть будет равна iid
						    if get_notwalk:
							remainder = var_.iid
							# Альтернативный вариант для использования нескольких последних чисел OID в имени подраздела, например '7.100'
							if k.count('.')>1:
							    remainder = ".".join(full_oid.split(".")[-k.count('.'):])
						    # Например в конфиге указан OID 1.2.3.2.1, tag будет 1.2.3.2.1.X, iid - Y (может быть пустым). Полный OID (full_oid) будет 1.2.3.2.1.X.Y
						    # Имя раздела (словаря) будет k, а подраздела (ключа метрики) - remainder
						    if (prep_k not in json_resp['data']):
							json_resp['data'][prep_k]={}
						    # Выполняем проверку на наличие непечатаемых символов. Если таких нет, возвращаем исходную строку, а иначе возвращаем hex-string
						    if var_.val == filter(lambda x: x in string.printable, var_.val):
							json_resp['data'][prep_k][remainder] = var_.val.replace('\"','')
						    else:
							json_resp['data'][prep_k][remainder] = var_.val.encode("hex")

			    # Если dataset является списком, выполняем для него set-операции
			    if isinstance(dataset, list):
				query = 'skipped'
				varlist = netsnmp.VarList(*[netsnmp.Varbind(*prepare_oid(data_param.copy(), VarBindItem[:])) for VarBindItem in dataset])
				query   = netsnmp.snmpset(*varlist, Version = 2, DestHost = target_ip, Community = snmp_comm, Timeout = current_snmp_timeout, Retries = current_snmp_retries, UseNumeric = 1)
				time.sleep(set_iter_delay)
				json_resp['data'][data_param['0']] = query

			    # Если dataset является кортежем, просто возвращаем его первый элемент. Это нужно для хранения пользовательских словарей в конфиге swtoolz-core
			    if isinstance(dataset, tuple):
				json_resp['data'][data_param['0']] = dataset[0]

	# --- Если для данного IP уже был получен ответ, обновляем словарь, а если нет - создаем
	if self.client_ip in self.responses.keys():
	    self.responses[self.client_ip].update({self.client_port:json_resp})
	else:
	    self.responses[self.client_ip]    =   {self.client_port:json_resp}

def main():
    logging.info("Daemon 'swtoolz-core' started...")

    err_codes = {
	0: "OK",
	1: "Missing mandatory parameters: /user, /target, /comm_index",
	2: "User is not found",
	3: "Snmp-community is not defined for this index",
	4: "IP-address is not correct",
	}

    # Создаем сокет для приема подключений
    tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Переводим сокет в неблокирующий режим и задаем опции для более быстрого освобождения ресурсов
    tcps.setblocking(0)
    tcps.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcps.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 0, 1))
    # Примечание: В варианте SO_LINGER 1 и 0 коннект не разрывается и поддерживается вечно при помощи Keep-Alive.

    # Список, содержащий клиентов
    clients = []
    # Данные в необработанном виде
    data_raw = ''
    # Словарь с запросами от клиентов
    requests = {}
    # Словарь с ответами от оборудования
    responses = {}

    # Счетчик ответов
    res_cnt = 0

    # Пробуем открыть сокет
    try:
	tcps.bind((interface_ip, port))
    # Обрабатываем возможную ошибку сокета (сокет уже занят), делаем запись в лог и завершаем работу:
    except socket.error as err:
	logging.info("ERROR: Socket Error: {}. Exiting...".format(err.args[1]))
	tcps.close()
	sys.exit(2)
    else:
	# При отсутствии ошибок начинаем прослушивать порт
	tcps.listen(2)

    # Инициализируем таймер для статистики
    timer = int(time.time())
    # Выполняем бесконечный цикл, в котором опрашиваем сокеты через небольшой интервал
    while True:
	# В конце каждого цикла (интервал определен пользователем) подводим итоги:
	if (int(time.time()) - timer >= stats_int):
	    timer = int(time.time())
	    logging.info("INFO: Requests processed for iteration - %s", res_cnt)
	    # Обнуляем счетчик ответов
	    res_cnt = 0
	    # В режиме отладки пишем в лог кол-во вопросов и ответов
	    if debug_mode:
		logging.info("DEBUG: Requests queue - %s, Responses queue - %s", sum(map(len,requests)), sum(map(len,responses)))
	    if len(clients)>0:
		logging.info("WARNING: Currently %s active connections. Possible %s dead clients", len(clients), len(dead_clients))
	# Пробуем принять подключение
	try:    connect, addr = tcps.accept()
	except: pass
	else:
	    # Переводим сокет в неблокирующий режим и говорим, чтобы при отключении освобождался быстрее (no linger) и добавляем в список
	    connect.setblocking(0)
	    connect.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 1))
	    clients.append(connect)
	# Список клиентов, передача данных к которым завершилась ошибкой
	dead_clients = []
	# Пробуем получить данные, IP-адрес и порт с каждого сокета, перебирая их
	for client_index, client in enumerate(clients):
	    try:
		data_raw = client.recv(512)
		client_ip, client_port = client.getpeername()
	    # Если данных нет возникнет ошибка, это нормально, ничего не трогаем
	    except: pass
	    else:
		# Если данные не пустые, начинаем их обрабатывать
		if (len(data_raw)>0):
		    # Разбиваем данные по строкам и перебираем их
		    for data_row in data_raw.split('\n'):
			if data_row[0:3] == 'GET':
			# Пробуем получить имя запрашиваемого ресурса (строка с параметрами)
			    try:
				request = data_raw.split(" ")[1]
			    except:
				request = ""
			    # Для режима отладки пишем в лог исходный запрос 'как есть'
			    if debug_mode:
				logging.info("DEBUG: Request from %s:%s - %s", client_ip, client_port, request)
			    # Формируем словарь вида {IP:{Port:Request}}
			    # Если для данного IP уже был определен запрос, обновляем словарь, а если нет - создаем
			    if client_ip in requests.keys():
				requests[client_ip].update({client_port:parse_request(request)})
			    else:
				requests[client_ip]    =   {client_port:parse_request(request)}

			    # Если ошибок нет, запускаем новую задачу по обработке запросов
			    if requests[client_ip][client_port]['errors'][0] == 0:
				# Создаем новый класс потоков
				thrNewTask = thrPoller(requests, client_ip, client_port, responses)
				# Задаем потоку имя вида 'thr_IP:Port'
				thrNewTask.setName("thr_%s:%s" % (client_ip, client_port))
				# Запускаем отдельный поток
				thrNewTask.start()
		    # Очищаем данные
		    data_raw = ''

	    # Структура словаря с ответом клиенту
	    answer = {'request':'','response':''}
	    # Признак мгновенного или отложенного ответа
	    # Если ошибок нет - ждем завершения задачи по опросу, если есть - отвечаем сразу
	    answer_immediately = False

	    # Инициализируем переменные
	    client_ip = None
	    client_port = None

	    # Пробуем получить IP-адрес и порт текущего клиента. Выше работали с теми, кто передает данные, а дальше работаем со всеми
	    try:
		client_ip, client_port = client.getpeername()
	    # При неудаче добавляем клиента в список неактивных клиентов, чтобы затем удалить из основного списка, который сейчас перебираем
	    except:
		dead_clients.append(client_index)
		if debug_mode:
		    logging.info('DEBUG: Some client lost in network...')

	    # Проверяем, есть ли IP-адрес данного клиента в словаре ответов
	    if client_ip in responses:
		# Проверяем, есть ли порт данного клиента в словаре ответов
		if client_port in responses[client_ip]:
		    # Добавляем полученый ответ в словарь для ответа
		    answer['response'] = responses[client_ip][client_port]
		    # Устанавливаем признак готовности ответа для клиента
		    answer_immediately = True
		    # Инкрементируем счетчик полученных ответов
		    res_cnt += 1
		    # Удаляем ответ для текущего подключения (по номеру порта) из соответствующего словаря
		    del responses[client_ip][client_port]
		    # Если для данного IP-адреса не осталось других данных, удаляем этот адрес из словаря
		    if len(responses[client_ip]) == 0:
			del responses[client_ip]

	    # Проверяем, есть ли IP-адрес данного клиента в словаре запросов
	    if client_ip in requests:
		# Проверяем, есть ли порт данного клиента в словаре запросов
		if client_port in requests[client_ip]:
		    # Добавляем исходный запрос в словарь для ответа
		    answer['request'] = requests[client_ip][client_port]
		    # Если запросе были ошибки отвечаем немедленно
		    if requests[client_ip][client_port]['errors'][0] != 0:
			answer_immediately = True
		    # Если получен ответ либо если есть ошибки, удаляем запросы для текущего подключения
		    if answer_immediately:
			# Удаляем запрос для текущего подключения (по номеру порта) из соответствующего словаря
			del requests[client_ip][client_port]
			# Если для данного IP-адреса не осталось других данных, удаляем этот адрес из словаря
			if len(requests[client_ip]) == 0:
			    del requests[client_ip]

	    # Если ответ получен (задача завершена) или в запросе были ошибки, отвечаем клиенту:
	    if answer_immediately:
		# Формируем json-строку с данными для ответа клиенту
		http_data = json.dumps(answer)
		# Правим заголовок HTTP для ответа клиенту
		new_header = http_header.replace("{$datetime}",str(datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'))).replace("{$datalen}",str(len(http_data)))
		if debug_mode:
		    # Отправляем ответ клиенту
		    logging.info("DEBUG: Send a answer to %s:%s...",client_ip,client_port)
		client.send(new_header+http_data+"\n")
		# Отключаем клиента. Принудительное отключение нужно потому, что на практике не удавалось добиться корректного отключения со стороны клиента.
		# Сессия поддерживалась бесконечное время при помощи Keep-Alive сообщений. Поэтому отключение производим вручную.
		# Для корректного отключения нужна настройка сокета SO_LINGER с параметрами, отличными от 1 и 0.
		client.close()
		dead_clients.append(client_index)
		# Устанавливаем признак, что ответы больше не нужны
		answer_immediately = False

	# Удаляем неактивных клиентов из основного списка клиентов
	for dead_client in dead_clients:
	    try:
		del clients[dead_client]
	    except:
		pass
	# Засыпаем на некоторый интервал чтобы не создавать нагрузку на систему
	time.sleep(sleep_int)

# ------- Служебный блок: создание и управление демоном -------

class MyDaemon(Daemon):
    def run(self):
        main()

if __name__ == "__main__":
    daemon = MyDaemon('/var/run/swtoolz-core.pid','/dev/null',logfile,logfile)
    if len(sys.argv) == 2:
        if   'start'     == sys.argv[1]:
            daemon.start()
        elif 'faststart' == sys.argv[1]:
            daemon.start()
        elif 'stop'      == sys.argv[1]:
            daemon.stop()
        elif 'restart'   == sys.argv[1]:
            daemon.restart()
        else:
            print "swtoolz-core: "+sys.argv[1]+" - unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

# ------- Конец служебного блока -------
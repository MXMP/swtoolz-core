# coding=UTF8
# IP-адрес интерфейса и порт
interface_ip = ""
port = 7577

# Пауза при опросе сокета в секундах
sleep_int = 0.01

# Интервал для статистики в файле журнала
stats_int = 300

# Пауза в секундах после set-операций
set_iter_delay = 0

# Таймаут ожидания ответа для SNMP-запроса (в секундах)
snmp_timeout = 3

# Количество дополнительных попыток для SNMP-запроса
# Значение '1' означает, что всего будет предпринято 2 попытки
snmp_retries = 0

# Список методов, для которых значение snmp_retries будет всегда считаться равным нулю
no_retries = ['set_SaveConfig']

# Список методов, которые будут вызваны даже если устройство недоступно
forced_mtd = ['Commands', 'OfflineDeviceMaps', 'set_CreateVlan', 'set_IpifCfg']

# Файл журнала
logfile = '/var/log/swtoolz-core.log'

# Пользователи и их наборы snmp-community
users = {
    'default': {'1' : 'public', '2' : 'private'},
    }

# Имена и OID'ы параметров, запрашиваемых у устройства в обязательном порядке
# По умолчанию спрашиваем sysDescr, sysUpTime, sysName, sysLocation
# Параметры sys_name и sys_descr зарезервированы и используются для определения модели устройства
default_info = {
    'sys_descr': '.1.3.6.1.2.1.1.1.0',
    'sys_uptime': '.1.3.6.1.2.1.1.3.0',
    'sys_name': '.1.3.6.1.2.1.1.5.0',
    'sys_location': '.1.3.6.1.2.1.1.6.0',
}

# Шаблон HTTP-заголовка для ответа клиенту
http_header = """HTTP/1.1 200 OK
Content-Type: application/json
Server: SWT-Core
Date: {$datetime}
Connection: close
Content-Length: {$datalen}

"""

# Режим отладки
debug_mode = False

telnet_user = 'script'
telnet_password = 'ljcnegcrhbgnf'

#время кеширования индексов SNMP
dyn_port_idx_update_interval=30

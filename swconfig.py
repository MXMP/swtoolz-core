#coding=UTF8
# Настройки интерфейса и порта
interface = ""
port      = 7377

# Пауза при опросе сокета в секундах
sleep_int = 0.01

# Интервал для статистики в файле журнала
stats_int = 300

# Пауза в секундах после set-операций
set_iter_delay = 0

# Таймаут ожидания ответа для SNMP-запроса (в микросекундах)
snmp_timeout  = 300000

# Количество дополнительных попыток для SNMP-запроса
# Значение '1' означает, что всего будет предпринято 2 попытки
snmp_retries  = 1

# Список методов, для которых значение snmp_retries будет всегда считаться равным нулю
no_retries = ['set_SaveConfig']

# Список методов, которые будут вызваны даже если устройство недоступно
forced_mtd = ['set_CreateVlan', 'set_IpifCfg']

# Файл журнала
logfile   = "/var/log/swtoolz-core.log"

# Пользователи и их наборы snmp-community
users = {
    'default'  : {'1' : 'public', '2' : 'private'},
    }

# Имена и OID'ы параметров, запрашиваемых у устройства в обязательном порядке
# По умолчанию спрашиваем sysDescr, sysUpTime, sysName, sysLocation
# Параметры sys_name и sys_descr зарезервированы и используются для определения модели устройства
default_info = {
    'sys_descr'    : '.1.3.6.1.2.1.1.1.0',
    'sys_uptime'   : '.1.3.6.1.2.1.1.3.0',
    'sys_name'     : '.1.3.6.1.2.1.1.5.0',
    'sys_location' : '.1.3.6.1.2.1.1.6.0',
    }

# Соответствие описаний моделей их названиям. Список проверяется до первого соответствия
# Ключ - подстрока, входящая в строки в sysDescr или sysName (имеет приоритет)
# Значение - локально значимое имя модели и соответствующего ей файла в ./devices
models_by_desc = [
    {'DES-3200-28/C1' : 'DES-3200-28_C1'},
    {'DES-3200-28'    : 'DES-3200-28'},
    {'DES-3200-18/C1' : 'DES-3200-18_C1'},
    {'DES-3200-18'    : 'DES-3200-18'},
    {'DES-3200-10'    : 'DES-3200-10'},
    {'DES-3028G'      : 'DES-3028G'},
    {'DES-3028'       : 'DES-3028'},
    {'DES-3026'       : 'DES-3026'},
    {'DGS-3100-24TG'  : 'DGS-3100-24TG'},
    {'DGS-3120-24SC/B': 'DGS-3120-24SC_B'},
    {'DGS-3120-24SC'  : 'DGS-3120-24SC'},
    {'DGS-3000-28SC'  : 'DGS-3000-28SC'},
    {'DGS-3000-24TC'  : 'DGS-3000-24TC'},
    {'DGS-3612G'      : 'DGS-3612G'},
    {'DGS-3627G'      : 'DGS-3627G'},
    {'BigIron RX'     : 'BigIron-RX'},
    {'BigIron 8000'   : 'Foundry'},
    {'BigIron 4000'   : 'Foundry'},
    {'FastIron 800'   : 'Foundry'},
    {'FastIron 400'   : 'Foundry'},
    {'FastIron SX 800': 'Foundry'},
    {'NetIron 800'    : 'Foundry'},
    {'IronWare'       : 'Foundry'},
    {'TurboIron-X24'  : 'Foundry'},
    {'c2950-MGMT'     : 'WS-C2950G-48-EI'},
    {'cat3550-12G'    : 'WS-C3550-12G'},
    {'Cat3550-12G'    : 'WS-C3550-12G'},
    {'Core7k-17'      : 'WS-C3550-12G'},
    {'Kalach_cat3550' : 'WS-C3550-12G'},
    {'Bereslavka-Cat' : 'WS-C3550-12G'},
    {'CiscoWisi'      : 'WS-C3560X-24'},
    {'AdmRack-c3750'  : 'WS-C3750-24PS-S'},
    {'Cat3750-48_TV'  : 'WS-C3750-48TS-S'},
    {'GGC-3750G-16TD' : 'WS-C3750G-16TD'},
    {'SCE8000'        : 'SCE8000'},
    {'Redback'        : 'Redback'},
    {'MES2124'        : 'MES-2124'},
    {'MES3124F'       : 'MES-3124F'},
    {'APC Web/SNMP'   : 'APC-Smart-UPS'},
    ]

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

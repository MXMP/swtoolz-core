# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Список рекомендуемых команд
Commands = ([
    "Commands",
    "set_groupResetCheck",
    "set_UserByNumber",
    "set_UserByNumplan",
    "walk_tableOfGroupUsers",
    "UserRegState",
],)

# Состояние регистрации
UserRegState = ({
    '0': "Unregistred",
    '1': 'Registred'
},)

# Сброс параметров поиска
set_groupResetCheck = [
    [".1.3.6.1.4.1.35265.1.29.39.2", '0', '1', 'INTEGER']
]

# Установка номера абонента для поиска
set_UserByNumber = [
    [".1.3.6.1.4.1.35265.1.29.39.10",'0','{1}', 'OCTETSTR']
]

# Установка плана нумерации
set_UserByNumplan = [
    ['.1.3.6.1.4.1.35265.1.29.39.9', '0', '0', 'INTEGER']
]

# Получение результата поиска
walk_tableOfGroupUsers = {
    'helper': 'eltex_walk_user_helper',
    'tableOfGroupUsers': '.1.3.6.1.4.1.35265.1.29.39.12.1'
}


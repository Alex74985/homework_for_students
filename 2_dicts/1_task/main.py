import os

from decimal import Decimal

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '\n'


def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_employees_info() -> list[str]:
    """Внешнее апи, которое возвращает вам список строк с данными по сотрудникам."""
    return read_file(os.path.join(
        BASE_DIR, '1_task', 'input_data.txt',
    )).split(SPLIT_SYMBOL)


def get_parsed_employees_info() -> list[dict[str, int | str]]:
    """Функция парсит данные, полученные из внешнего API и приводит их к стандартизированному виду."""
    _ = get_employees_info()
    parsed_employees_info = []

    # Ваш код ниже

    int_keys = ['id', 'age']
    decimal_key = ['salary']
    string_key = ['name', 'last_name', 'position']
    for s in _:
        emp = {}
        s = s.split(' ')
        keys = [s[i] for i in range(0, len(s), 2)]
        vals = [s[i] for i in range(1, len(s), 2)]

        for k in keys:
            if k in int_keys:
                emp[k] = int(vals[keys.index(k)])
            elif k in decimal_key:
                emp[k] = Decimal(vals[keys.index(k)])
            elif k in string_key:
                emp[k] = str(vals[keys.index(k)])

        parsed_employees_info.append(emp)

    return parsed_employees_info

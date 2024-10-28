import re


def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    formatted_phone_number = ""

    pattern_2 = r'(\+7|8|.?).*(\d{3}).*(\d{3}).*(\d{2}).*(\d{2})'

    formatted_phone_number = re.sub(r'[^\d]', '', phone_number)

    if len(formatted_phone_number) > 8:
        res = re.search(pattern_2, formatted_phone_number)
        part_1 = res.group(2)
        part_2 = res.group(3)
        part_3 = res.group(4)
        part_4 = res.group(5)
        formatted_phone_number = '8' + f' ({part_1}) ' + part_2 + '-' + part_3 + '-' + part_4

    return formatted_phone_number

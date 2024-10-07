import re


def format_phone(phone_number: str) -> str:
    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    formatted_phone_number = ""

    pattern = r'(?:\d)'
    standard_pattern = r'/(?:\+7|8)(?:\s\(\d{3}\)\s)(?:\d{3})(?:-\d{2}){2}/'
    pattern_1 = r'(?:\+7|8|.?).*(?:\d{3}).*(?:\d{3}).*(?:\d{2}).*(?:\d{2})'

    formatted_phone_number += re.search(pattern, phone_number).group(0)

    return formatted_phone_number

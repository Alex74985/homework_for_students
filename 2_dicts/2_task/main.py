import re


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """

    most_common = {}

    pattern = r'[а-яё]{3,}'

    text = re.findall(pattern, text.lower())

    unic = set(text)

    for word in unic:
        most_common[word] = text.count(word)

    most_common = dict(sorted(list(sorted(most_common.items(), key=lambda y: y[0])), key=lambda x: x[1], reverse=True)[:10])

    return most_common

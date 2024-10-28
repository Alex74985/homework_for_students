import re


def decode_numbers(numbers: str) -> str | None:
    """Пишите ваш код здесь."""

    keyboard = {
        0: ' ',
        1: '.', 11: ',', 111: '?', 1111: '!', 11111: ':', 111111: ';',
        2: 'а', 22: 'б', 222: 'в', 2222: 'г',
        3: 'д', 33: 'е', 333: 'ж', 3333: 'з',
        4: 'и', 44: 'й', 444: 'к', 4444: 'л',
        5: 'м', 55: 'н', 555: 'о', 5555: 'п',
        6: 'р', 66: 'с', 666: 'т', 6666: 'у',
        7: 'ф', 77: 'х', 777: 'ц', 7777: 'ч',
        8: 'ш', 88: 'щ', 888: 'ъ', 8888: 'ы',
        9: 'ь', 99: 'э', 999: 'ю', 9999: 'я'
    }

    q = re.findall(r'\d+', numbers)

    # q = list(map(lambda x: int(x), q))

    result = ""

    for el in q:
        if el == '00':
            result = None
            break
        else:
            el = int(el)
        if el in keyboard.keys() and str(el):
            result += keyboard[el]
        else:
            result = None
            break

    return result
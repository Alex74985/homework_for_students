import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()

    # Ваш код ниже, возвращайте уже отредактированный текст!

    wrong_article = wrong_article.split('\n')
    correct_article = []
    for sen in wrong_article:
        sen = ''.join(reversed(sen))
        sen = sen[len(sen)//2 + 1:]
        sen = sen.replace('WOOF-WOOF', 'cat')
        if sen != '':
            sen = sen.capitalize() + '.'
        correct_article.append(sen)

    correct_article = '\n'.join(correct_article)

    return correct_article

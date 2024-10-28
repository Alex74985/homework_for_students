"""Реализуйте необходимые функции ниже."""
from typing import Callable


def one(*args):
    return 1 if not len(args) else args[0](1)


def two(*args):
    return 2 if not len(args) else args[0](2)


def three(*args):
    return 3 if not len(args) else args[0](3)


def four(*args):
    return 4 if not len(args) else args[0](4)


def five(*args):
    return 5 if not len(args) else args[0](5)


def six(*args):
    return 6 if not len(args) else args[0](6)


def seven(*args):
    return 7 if not len(args) else args[0](7)


def eight(*args):
    return 8 if not len(args) else args[0](8)


def nine(*args):
    return 9 if not len(args) else args[0](9)


def zero(*args):
    return 0 if not len(args) else args[0](0)


def times(num):
    return lambda x: x * num


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def divided_by(num):
    return lambda x: x // num
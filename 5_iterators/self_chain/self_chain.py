import itertools
from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    obj = list(map(lambda x: list(x), iterables))
    for it in obj:
        for el in it:
            yield el


class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.obj = list(map(lambda x: list(x), iterables))
        self.i = 0
        self.j = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.i
        j = self.j
        if i == len(self.obj):
            raise StopIteration
        if j < len(self.obj[i]) - 1:
            self.j += 1
        else:
            self.i += 1
            self.j = 0
        return self.obj[i][j]


#
test = itertools.chain("1234", [1, 2, 3, 4], ["a", "b", 1], {1: 1, 2: 2})
#
ch = Chain("1234", [1, 2, 3, 4], ["a", "b", 1], {1: 10, 2: 20})
#
print(f'RC elements: ')
print(*list(map(lambda x: str(x) + ' --> ' + str(type(x)), test)), sep='\n')
print(f'MC elements: ')
print(*list(map(lambda x: str(x) + ' --> ' + str(type(x)), ch)), sep='\n')
#
# # print(ch.obj)
#
# for el in ch:
#     print(el)


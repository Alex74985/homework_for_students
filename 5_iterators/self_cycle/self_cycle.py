import itertools
from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    while True:
        for it in obj:
            yield it


class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = list(obj)
        self.i = 0

    def __next__(self):
        if self.i < len(self.obj):
            element = self.obj[self.i]
            self.i += 1
            return element
        else:
            self.i = 0
            element = self.obj[self.i]
            self.i += 1
            return element

    def __iter__(self):
        return self


test = ["1234", [1, 2, 3, 4], {1: 1, 2: 2, 3: 3}, {1, 2, 3, 4}, (1, 2, 3, 4)]
count = 8


for el in test:
    it = Cycle(el)
    rc = itertools.cycle(el)
    for i, e, in enumerate(zip(it, rc)):
        if i >= count:
            break
        print(i, '-->', list(map(lambda y: [type(y), y], e)))





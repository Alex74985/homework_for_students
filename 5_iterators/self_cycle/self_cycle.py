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
        self.obj = obj
        self.i = 1

    def __next__(self):
        if self.i <= len(self.obj):
            el = self.i
            self.i += 1
            return el
        else:
        #     raise StopIteration
            self.i = 1
            el = self.i
            self.i += 1
            return el

    def __iter__(self):
        return self


it = Cycle('1234')

count = 8

for i, el in enumerate(it):
    if i >= count:
        break
    print(el)

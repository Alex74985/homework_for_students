from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    if n < 1:
        raise ValueError('n must be at least one')
    while obj:
        if len(obj) >= n:
            b = tuple(obj[:n])
            obj = obj[n:]
        else:
            b = tuple(obj)
            obj = None
        yield b


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        """Реализуй этот класс."""
        self.obj = obj
        self.size = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.obj) >= self.i + self.size:
            el = tuple(self.obj[self.i:self.i + self.size])
            self.i += self.size
        else:
            el = tuple(self.obj[self.i:])
        return el



bat = batched('ABCDEFG', 3)

for el in bat:
    print(el)

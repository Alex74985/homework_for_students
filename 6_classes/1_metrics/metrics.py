import datetime
from typing import Protocol


class Saver(Protocol):
    def save(self) -> None:
        pass


class SaverTxt(Saver, Protocol):
    pass


class SaverCsv(Saver, Protocol):
    pass


class Statsd:
    def __init__(self, save: Saver, path, buffer_limit, init_line: str = None):
        """Реализуйте класс"""
        self._save = save
        self._path = path
        self._buffer_limit = buffer_limit
        self.stor = []*self._buffer_limit
        self._init_line = init_line
        self.i = 0

    def incr(self, m_name):
        data = datetime.UTC, m_name, 1
        self.stor[self.i] = data
        self.i += 1
        if self.check_buff():
            self.i = 0

    def decr(self, m_name):
        data = datetime.UTC, m_name, -1
        self.stor[self.i] = data
        self.i += 1
        if self.check_buff():
            self.i = 0

    def check_buff(self):
        if self.i == self._buffer_limit:
            self.save_call()
            self.clean_buff()
            return True

    def save_call(self):
        self._save.save()

    def clean_buff(self):
        self.stor = []*self._buffer_limit


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    txt = SaverTxt()
    s = Statsd(txt, path, buffer_limit)
    return s


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    init_line = ''
    csv = SaverCsv
    s = Statsd(csv, path, buffer_limit, init_line)
    return s


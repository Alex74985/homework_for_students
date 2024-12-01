import datetime
import re
from typing import Protocol
import csv
import os


class Saver(Protocol):
    def __init__(self, p):
        self.path = p
        pass

    def read(self):
        pass

    def save(self, data) -> None:
        pass

    def _create(self):
        pass

    def _check(self):
        pass


class SaverTxt:
    def __init__(self, p):
        self.path = p
        self._check()
        self._create()
        self.container = None

    def read(self):
        with open(self.path, 'r', newline='\n'):
            pass

    def save(self, data: list):
        self.container = data
        with open(self.path, 'a+') as file:
            for el in self.container:
                file.writelines([' '.join([str(_) for _ in el]), '\n'])

    def _create(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w+'):
                pass

    def _check(self):
        reg = r'\.(.*)'
        if re.search(reg, self.path).group(1) == 'txt':
            return True
        else:
            raise ValueError


class SaverCsv:
    def __init__(self, p):
        self.path = p
        self._check()
        self._create()
        self.container = None

    def read(self):
        with open(self.path, 'r', newline=''):
            pass

    def save(self, data: list):
        self.container = data
        with open(self.path, 'a+', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(self.container)

    def _create(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(['date', 'metric', 'value'])
        else:
            file = open(self.path, 'r', newline='')
            reader = csv.reader(file, delimiter=";")
            lines = [row for row in reader]
            if len(lines) == 0:
                file.close()
                with open(self.path, 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow(['date', 'metric', 'value'])
            file.close()


    def _check(self):
        reg = r'\.(.*)'
        if re.search(reg, self.path).group(1) == 'csv':
            return True
        else:
            raise ValueError


class Statsd:
    def __init__(self, save: Saver, buffer_limit: int, init_line: str = None):
        """Реализуйте класс"""
        self._saver = save
        self._buffer_limit = buffer_limit
        self.stor = [None]*self._buffer_limit
        self._init_line = init_line
        self.i = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stor[0] is not None:
            self._saver.save(self.stor[:self.stor.index(None)])

    def incr(self, m_name):
        data = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0000'), m_name, 1
        self.stor[self.i] = data
        self.i += 1
        if self.check_buff():
            self.i = 0

    def decr(self, m_name):
        data = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+0000'), m_name, -1
        self.stor[self.i] = data
        self.i += 1
        if self.check_buff():
            self.i = 0

    def check_buff(self):
        if self.i == self._buffer_limit:
            self._saver.save(self.stor)
            self.clean_buff()
            return True

    def clean_buff(self):
        self.stor = [None]*self._buffer_limit


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    saver = SaverTxt(path)
    s = Statsd(saver, buffer_limit)
    return s


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    init_line = ''
    saver = SaverCsv(path)
    s = Statsd(saver, buffer_limit, init_line)
    return s


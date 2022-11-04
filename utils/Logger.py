""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-22:10 """
import os
import time

from inspect import currentframe, stack, getmodule
import inspect

import colorama
from colorama import Fore, Style  # 命令行颜色字体库

colorama.init(autoreset=True)  # 使旧版cmd中命令行颜色字体生效, 并在print换行处自动还原默认颜色


class Logger:

    def __init__(self, filename: str = None, level: str = 'DEBUG'):
        le = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10}
        self.path = filename
        self.level = le[level]
        self.COLOR = {
            'red': Fore.LIGHTRED_EX,
            'yellow': Fore.YELLOW,
            'blue': Fore.LIGHTBLUE_EX,
            'green': Fore.GREEN,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
            'reset': Fore.RESET
        }
        self.levels = {
            'DEBUG': self.set('DEBUG', color='white', bright=True),
            'INFO': self.set('INFO', color='cyan', bright=True),
            'WARNING': self.set('WARNING', color='yellow', bright=True),
            'ERROR': self.set('ERROR', color='magenta', bright=True),
            'CRITICAL': self.set('CRITICAL', color='red', bright=True)
        }

    @property
    def _module(self):
        return getmodule(stack()[1][0])

    def write_log(self, value):
        if self.path is None:
            return
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(value + '\n')

    @property
    def _file(self):
        return self._module.__file__

    @property
    def _name(self):
        return self._module.__name__

    @property
    def _time(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @property
    def _color_time(self):
        return self.set(self._time, color='green')

    def set(self, value, color=None, bright=False):
        if bright:
            return self.COLOR[color] + Style.BRIGHT + value + Fore.RESET
        return self.COLOR[color] + value + Fore.RESET

    def debug(self, value):
        value = value if isinstance(value, str) else str(value)
        if self.level > 10:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        print(self._color_time, '[', self.levels['DEBUG'], ']', self.set(file_name, color='blue'),
              f':{line}', '|', self.set(value, color='white'))
        log = f"""{self._time} [DEBUG] {file_name}:{line} | {value}"""
        self.write_log(log)

    def info(self, value):
        value = value if isinstance(value, str) else str(value)
        if self.level > 20:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        print(self._color_time, '[', self.levels['INFO'], ']', self.set(file_name, color='blue'),
              f':{line}', '|', self.set(value, color='cyan'))
        log = f"""{self._time} [INFO] {file_name}:{line} | {value}"""
        self.write_log(log)

    def warning(self, value):
        value = value if isinstance(value, str) else str(value)
        if self.level > 30:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        print(self._color_time, '[', self.levels['WARNING'], ']', self.set(file_name, color='blue'),
              f':{line}', '|', self.set(value, color='yellow'))
        log = f"""{self._time} [WARNING] {file_name}:{line} | {value}"""
        self.write_log(log)

    def error(self, value):
        value = value if isinstance(value, str) else str(value)
        if self.level > 40:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        print(self._color_time, '[', self.levels['ERROR'], ']', self.set(file_name, color='blue'),
              f':{line}', '|', self.set(value, color='magenta'))
        log = f"""{self._time} [ERROR] {file_name}:{line} | {value}"""
        self.write_log(log)

    def critical(self, value):
        value = value if isinstance(value, str) else str(value)
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        print(self._color_time, '[', self.levels['CRITICAL'], ']', self.set(file_name, color='blue'),
              f':{line}', '|', self.set(value, color='red'))
        log = f"""{self._time} [CRITICAL] {file_name}:{line} | {value}"""
        self.write_log(log)


if __name__ == '__main__':
    logger = Logger()
    logger.debug('debug')
    logger.warning('warning')
    logger.info('info')
    logger.error('error')
    logger.critical('critical')

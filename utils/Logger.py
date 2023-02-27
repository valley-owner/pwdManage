""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-22:10 """
import datetime
import os

from inspect import currentframe, stack, getmodule
import inspect

import colorama
from colorama import Fore, Style  # 命令行颜色字体库

colorama.init(autoreset=True)  # 使旧版cmd中命令行颜色字体生效, 并在print换行处自动还原默认颜色


class Logger:

    def __init__(self, filename: str = None, level: str = 'DEBUG'):
        le = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10}
        self.__path = filename
        self.__level = le[level]
        self.__COLOR = {
            'red': Fore.LIGHTRED_EX,
            'yellow': Fore.YELLOW,
            'blue': Fore.LIGHTBLUE_EX,
            'green': Fore.GREEN,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
            'reset': Fore.RESET
        }
        self.__levels = {
            'DEBUG': self.__set('DEBUG', color='white', bright=True),
            'INFO': self.__set('INFO', color='cyan', bright=True),
            'WARNING': self.__set('WARNING', color='yellow', bright=True),
            'ERROR': self.__set('ERROR', color='magenta', bright=True),
            'CRITICAL': self.__set('CRITICAL', color='red', bright=True)
        }

    @property
    def _module(self):
        return getmodule(stack()[1][0])

    def __write_log(self, value):
        if self.__path is None:
            return
        with open(self.__path, 'a', encoding='utf-8') as file:
            file.write(value + '\n')

    @property
    def _file(self):
        return self._module.__file__

    @property
    def _name(self):
        return self._module.__name__

    @property
    def _time(self):
        return str(datetime.datetime.now())[5:]

    @property
    def _color_time(self):
        return self.__set(self._time, color='green')

    def __set(self, value, color=None, bright=False):
        if bright:
            return self.__COLOR[color] + Style.BRIGHT + value + Fore.RESET
        return self.__COLOR[color] + value + Fore.RESET

    @staticmethod
    def __format_msg(*msg):
        return ' '.join([str(item) for item in msg])

    def __print_msg(self, file_name, line, msg,
                    level='DEBUG', file_color='blue', msg_color='white'):
        print(self._color_time, '[', self.__levels[level], ']', self.__set(file_name, color=file_color),
              f':{line}', '|', self.__set(msg, color=msg_color))
        log = f"""{self._time} [{level}] {file_name}:{line} | {msg}"""
        self.__write_log(log)

    def debug(self, *msg):
        value = self.__format_msg(*msg)
        if self.__level > 10:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        self.__print_msg(file_name, line, value)

    def info(self, *msg):
        value = self.__format_msg(*msg)
        if self.__level > 20:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        self.__print_msg(file_name, line, value, level='INFO', msg_color='cyan')

    def warning(self, *msg):
        value = self.__format_msg(*msg)
        if self.__level > 30:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        self.__print_msg(file_name, line, value, level='WARNING', msg_color='yellow')

    def error(self, *msg):
        value = self.__format_msg(*msg)
        if self.__level > 40:
            return
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        self.__print_msg(file_name, line, value, level='ERROR', msg_color='magenta')

    def critical(self, *msg):
        value = self.__format_msg(*msg)
        file_name = os.path.split(inspect.getframeinfo(inspect.currentframe().f_back).filename)[1]
        line = str(currentframe().f_back.f_lineno)
        self.__print_msg(file_name, line, value, level='CRITICAL', msg_color='red')


if __name__ == '__main__':
    logger = Logger()
    logger.debug('debug')
    logger.warning('warning')
    logger.info('info')
    logger.error('error')
    logger.critical('critical')

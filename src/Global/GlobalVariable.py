""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-17:00 """
import os
import platform


class GlobalVar:
    """可以自动写入文件中的"""
    author = 'duckweed'
    version = '0.1.0'
    level = 'DEBUG'  # 'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10
    python_version = platform.python_version()
    auto_login = False
    username = None
    password = None
    key = None

    @classmethod
    def get_dict(cls):
        return {key: value for key, value in cls.__dict__.items() if key[0] != '_' and key != 'get_dict'}


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(os.getcwd())))

""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-20:48 """
import os
import time

from utils.baseObject import basePath


class GlobalPathDir(basePath):
    """文件夹"""
    # 根目录
    root_dir = os.path.dirname(os.path.abspath(__file__)) if os.name == 'nt' \
        else os.path.abspath(os.path.dirname(os.getcwd()))
    # 配置文件
    config_dir = root_dir + os.sep + 'config'
    # 日志
    log_dir = root_dir + os.sep + 'logs'
    # 密钥
    key_dir = root_dir + os.sep + 'key'


class GlobalPathFile(basePath):
    """文件"""
    # 数据库文件
    database_path = GlobalPathDir.config_dir + os.sep + 'data.db'
    # 文件及文件夹配置目录
    config_file_path = GlobalPathDir.config_dir + os.sep + 'path.json'
    # 配置文件
    config_path = GlobalPathDir.config_dir + os.sep + 'config.json'
    # 日志文件
    log_path = GlobalPathDir.log_dir + os.sep + f'{str(time.strftime("%Y-%m-%d"))}.log'
    # 私钥
    private_key = GlobalPathDir.key_dir + os.sep + 'private_key.pem'
    # 公钥
    public_key = GlobalPathDir.key_dir + os.sep + 'public_key.pem'





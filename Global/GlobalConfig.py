""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-21:04 """

from peewee import SqliteDatabase
from utils.dictToObj import DictToObj
from utils.jsonFile import read_json
from utils.baseObject import basePath
from utils.Logger import Logger
from path import GlobalPathFile, GlobalPathDir
from Global.GlobalVariable import GlobalVar


class GlobalConfig(basePath):
    """不能写入文件中的"""
    database = SqliteDatabase(GlobalPathFile.database_path)
    config = DictToObj(read_json(GlobalPathFile.config_path), path=GlobalPathFile.config_path) if \
        read_json(GlobalPathFile.config_path) is not None else \
        DictToObj(GlobalVar.get_dict(), path=GlobalPathFile.config_path)
    default_config = DictToObj(GlobalVar.get_dict(), path=GlobalPathFile.config_path)
    logger = Logger(GlobalPathFile.log_path, level=config.level if config.level else GlobalVar.level)
    dir_path = DictToObj(read_json(GlobalPathFile.config_file_path).get('dir_file'), path=GlobalPathFile.config_file_path) if \
        read_json(GlobalPathFile.config_file_path) is not None else \
        DictToObj(GlobalPathDir.get_dict(), path=GlobalPathFile.config_file_path)
    file_path = DictToObj(read_json(GlobalPathFile.config_file_path).get('path_file'), path=GlobalPathFile.config_file_path) if \
        read_json(GlobalPathFile.config_file_path) is not None else \
        DictToObj(GlobalPathFile.get_dict(), path=GlobalPathFile.config_file_path)
    user = None  # 保存用户信息


logger = GlobalConfig.logger


def get_config(value):
    if value in GlobalConfig.config:
        return GlobalConfig.config.get(value)
    if value not in GlobalConfig.default_config:
        return None
    GlobalConfig.config[value] = GlobalConfig.default_config.get(value)
    GlobalConfig.config.save()
    return GlobalConfig.default_config.get(value)


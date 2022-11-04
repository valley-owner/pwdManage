""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-17:48 """
import os

from utils.jsonFile import write_json
from Global.GlobalConfig import logger   # 日志
from Global.GlobalConfig import GlobalConfig
from utils.Encryption import RsaEncryption


class initData:

    def __init__(self):
        self.path_dir_all: dict = GlobalConfig.dir_path or {}
        self.path_file_all: dict = GlobalConfig.file_path or {}
        self.config: dict = GlobalConfig.config or {}

    def initPath(self):
        return {
            'dir_file': self.path_dir_all,
            'path_file': self.path_file_all}

    def initFile(self):
        logger.debug(f'初始化文件{GlobalConfig.file_path.config_file_path}')
        write_json(GlobalConfig.file_path.config_file_path, self.initPath())
        logger.debug(f'初始化文件{GlobalConfig.file_path.config_path}')
        write_json(GlobalConfig.file_path.config_path, self.config)

    def initDir(self):
        if self.path_dir_all is None:
            return
        for _, value in self.path_dir_all.items():
            # 判断目录是否存在
            if '.' in value:
                continue
            if not os.path.exists(value):
                logger.debug(f'创建文件夹 {value}')
                os.makedirs(value)

    @staticmethod
    def initKey():
        if not os.path.exists(GlobalConfig.file_path.public_key):
            logger.debug(f'未检测到公钥，进行创建{GlobalConfig.file_path.public_key}')
            Rsa = RsaEncryption()
            Rsa.createKey(is_save=True)
            logger.debug(f'{GlobalConfig.file_path.public_key} 创建成功')

    def init(self):
        self.initDir()
        self.initFile()
        logger.info(GlobalConfig.config.level)
        logger.info('作者: ' + GlobalConfig.config.author)
        logger.info('当前版本: ' + GlobalConfig.config.version)
        logger.info('python: ' + GlobalConfig.config.python_version)
        self.initKey()
        logger.info('文件初始化成功')


global_init = initData()


if __name__ == '__main__':
    print(global_init.config)

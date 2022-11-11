""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/27-15:47 """
import json
from datetime import datetime
from typing import Union

from peewee import Model, ModelBase
import peewee

from Global.GlobalConfig import logger, GlobalConfig


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = GlobalConfig.database


class Database(BaseModel):

    @classmethod
    def getModel(cls):
        return [item for item in cls.__subclasses__()]

    def getModelName(self):
        model = [item.__name__.lower() for item in self.getModel()]
        return model

    def createTable(self):
        model = self.getModel()
        logger.debug(f'初始化模型 {model}')
        GlobalConfig.database.create_tables(model)
        logger.debug('初始化模型完成')

    def deleteTable(self, key: Union[object, list, str]):
        logger.warning(f'删除表{key}')
        if isinstance(key, ModelBase):
            if key in self.getModel():
                GlobalConfig.database.drop_tables([key])
            else:
                raise f'{key} 表不存在'
        elif isinstance(key, list):
            [self.deleteTable(item) for item in key]
        elif isinstance(key, str):
            table_list = dict(zip(self.getModelName(), self.getModel()))
            if key in table_list:
                GlobalConfig.database.drop_tables([table_list[key]])
        else:
            raise f'{key} 只能是object, list, str'

    @property
    def get_table(self):
        table_list = dict(zip(self.getModelName(), self.getModel()))
        ret = []
        for item in table_list:
            index = [k for k, v in table_list[item].__dict__.items() if k[0] != '_' and k != 'DoesNotExist']
            R = {'table_name': item, 'field': index}
            ret.append(R)
        return ret

    def save_table(self, path: str = None, data: Union[list, dict] = None):
        t_path = path if path else 'table.json'
        t_table = data if data else self.get_table
        with open(t_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(t_table))

    @staticmethod
    def read_table(path: str = None):
        t_path = path if path else 'table.json'
        with open(t_path, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
        return data

    @staticmethod
    def get_cursor():
        return GlobalConfig.database.cursor()

    @staticmethod
    def execute_sql(sql, params=None):
        cursor = GlobalConfig.database.execute_sql(sql, params).fetchall()
        return cursor

    def __str__(self):
        return str(self.getModelName())

    def __repr__(self):
        return self.getModelName()


# 在下方且在base上方创建模型会自动生成表
class UserModel(Database):
    username = peewee.CharField(max_length=256, verbose_name='用户名')
    password = peewee.CharField(max_length=256, verbose_name='密码')
    add_time = peewee.DateTimeField(default=datetime.now, verbose_name='创建时间')


class PasswordMemoModel(Database):
    user = peewee.ForeignKeyField(UserModel, on_delete='CASCADE', verbose_name='用户')
    name = peewee.CharField(max_length=256, verbose_name='名字')
    account = peewee.CharField(max_length=256, verbose_name='账号')
    password = peewee.CharField(max_length=256, verbose_name='密码')
    key = peewee.TextField(verbose_name='密钥')
    remark = peewee.CharField(null=True, default='', max_length=256, verbose_name='备注')
    add_time = peewee.DateTimeField(default=datetime.now, verbose_name='创建时间')


base = Database()
base.createTable()

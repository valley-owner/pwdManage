""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/27-10:08 """
import json


class DictToObj(dict):

    def __init__(self, dict_: dict = None, path: str = None):
        self.path = path
        d = {} if dict_ is None else dict_
        super().__init__(d)
        if dict_ is not None:
            self.initDict(dict_)

    def __getattr__(self, key):
        if key not in self:
            return None
        else:
            value = self[key]
            if isinstance(value, dict):
                value = DictToObj(value)
            return value

    def __setattr__(self, key, value):
        if isinstance(value, dict):
            dict.__setattr__(self, key, DictToObj(value))
        elif isinstance(value, list):
            dict.__setattr__(self, key, self.__iterlist__(value))
        else:
            dict.__setattr__(self, key, value)
        self.update(self.__dict__)

    def initDict(self, dict_):
        for key, value in dict_.items():
            if key[0] != '_':
                if isinstance(value, dict):
                    self.__setattr__(key, DictToObj(value))
                elif isinstance(value, list):
                    self.__setattr__(key, self.__iterlist__(value))
                else:
                    self.__setattr__(key, value)

    def __iterlist__(self, items: list):
        ret = [DictToObj(j) if isinstance(j, dict) else j for j in items]
        ret = [self.__iterlist__(i) if isinstance(i, list) else i for i in ret]
        return ret

    @property
    def get_dict(self):
        return {key: value for key, value in self.__dict__.items() if key[0] != "_" and key != 'path'}

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(json.dumps({key: value for key, value in self.items()
                                   if key[0] != "_" and key != 'path'}, ensure_ascii=False))

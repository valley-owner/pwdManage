""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-20:16 """
import os
import json


def write_file(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))


def write_json(path: str, data: dict):
    """
    :param path: 要写入的文件路径
    :param data: 要写入的字典
    """
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, ensure_ascii=False))


def read_json(json_path: str):
    """
    :param json_path: json文件路径
    :return: 字典
    """
    if not os.path.exists(json_path):
        return None
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)


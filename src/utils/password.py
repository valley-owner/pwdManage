""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/11/2-20:28 """
import hashlib


def create_pwd(username, password):
    v = username[:5] + password
    md5 = hashlib.md5(v.encode()).hexdigest()
    return md5[2:]


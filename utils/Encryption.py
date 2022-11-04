""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/9/27-22:37 """
import os
import random
import base64
from typing import Union

from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5
from binascii import b2a_hex, a2b_hex

from path import GlobalPathFile


class AesEncryption:

    def __init__(self,
                 aes_key: Union[str, bytes],
                 key_size: int = 16,
                 iv: bytes = b'k\x0eX\x8d\xc1\xfb\xd3=4>\x86\x9ctF\xe43',
                 mode=AES.MODE_CFB,
                 is_ran_iv=False):
        """
        :param aes_key:  密钥
        :param mode: 加密模式，不建议修改
        :param key_size: 密钥key长度    必须为16,24或者32bytes的长度
        :param iv: iv偏移量，bytes类型, 默认随机生成
        """
        self.key_size = key_size
        self.key = self._set_key(aes_key)
        self.mode = mode
        if is_ran_iv:
            self.iv = Random.new().read(AES.block_size)
        else:
            self.iv = iv

    def _set_key(self, aes_key: Union[str, bytes]) -> bytes:
        """检测key的长度是否为16,24或者32bytes的长度"""
        if isinstance(aes_key, str):
            aes_key = aes_key.encode()
        if len(aes_key) > self.key_size:  # 如果密钥长度超过 AES_KEY_SIZE
            return aes_key[:self.key_size]  # 截取前面部分作为密钥并返回
        while len(aes_key) % self.key_size != 0:  # 不到 AES_KEY_SIZE 长度则补齐
            aes_key += '#'.encode()  # 补齐的字符可用任意字符代替
        return aes_key

    @staticmethod
    def check_data(metadata: Union[str, bytes]) -> bytes:
        """检测加密的数据类型"""
        data = metadata.encode() if isinstance(metadata, str) else metadata
        if not isinstance(metadata, str) and not isinstance(metadata, bytes):
            raise Exception(f'加密的数据必须为str或bytes,不能为{type(metadata)}')
        return data

    def encrypt(self, metadata: Union[str, bytes], is_decode=True) -> Union[bytes, str]:
        """ 加密函数 """
        metadata = self.check_data(metadata)
        cryptor = AES.new(self.key, self.mode, self.iv)
        if is_decode:
            return b2a_hex(cryptor.encrypt(metadata)).decode()
        return b2a_hex(cryptor.encrypt(metadata))

    def decrypt(self, metadata: Union[str, bytes], is_decode=True) -> Union[bytes, str]:
        """ 解密函数 """
        metadata = self.check_data(metadata)
        cryptor = AES.new(self.key, self.mode, self.iv)
        if is_decode:
            return cryptor.decrypt(a2b_hex(metadata)).decode()
        return cryptor.decrypt(a2b_hex(metadata))


class RsaEncryption:

    def __init__(self, private_key: bytes = None, public_key: bytes = None):
        self.private_key = private_key
        self.public_key = public_key

    def saveKey(self):
        """保存公私密钥"""
        with open(GlobalPathFile.private_key, "wb") as f:
            f.write(self.private_key)
        with open(GlobalPathFile.public_key, "wb") as f:
            f.write(self.public_key)

    def createKey(self, is_save=False):
        """创建公私密钥对"""
        f = RSA.generate(2048)
        self.private_key = f.exportKey("PEM")  # 生成私钥
        self.public_key = f.publickey().exportKey()  # 生成公钥
        if is_save:
            self.saveKey()
        return self.public_key, self.private_key

    def readPublicKey(self, path: str):
        """读取公钥"""
        with open(path, "rb") as file:
            self.public_key = file.read()
        return self.public_key

    def readPrivateKey(self, path: str):
        """读取私钥"""
        with open(path, "rb") as file:
            self.private_key = file.read()
        return self.private_key

    def encryption(self, text: str):
        """加密"""
        if self.public_key is None:
            raise ValueError('加密时公钥不能为空')
        text = text.encode('utf-8')  # 字符串指定编码（转为bytes）
        c_p = PKCS1_v1_5.new(RSA.importKey(self.public_key))  # 构建公钥对象
        t_e = c_p.encrypt(text)  # 加密（bytes）
        t_e_b = base64.b64encode(t_e).decode()  # base64编码，并转为字符串
        return t_e_b

    def decryption(self, en_text: str):
        """解密"""
        if self.private_key is None:
            raise ValueError('解密时公钥不能为空')
        b_text = en_text.encode('utf-8')  # 字符串指定编码（转为bytes）
        b64_text = base64.b64decode(b_text)  # base64解码
        cipher_private = PKCS1_v1_5.new(RSA.importKey(self.private_key))  # 构建私钥对象
        text_decrypted = cipher_private.decrypt(b64_text, Random.new().read)  # 解密（bytes）
        return text_decrypted.decode()  # 解码为字符串


class Encryption:

    @staticmethod
    def random_str(size=16):
        """生成随机字符串
        :param size: 字符串长度
        :return: 指定长度的随机字符串
        """
        chars = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        text = ''.join(random.choice(chars) for _ in range(size))
        return text

    @staticmethod
    def _createPublicRsa(public: Union[str, bytes]):
        """初始化一个Public，Rsa对象
        :param public: 公钥
        :return:  Rsa对象
        """
        if isinstance(public, str):
            Rsa = RsaEncryption()
            Rsa.readPublicKey(public)
        elif isinstance(public, bytes):
            Rsa = RsaEncryption(public_key=public)
        else:
            return {'code': 404, 'msg': '密钥不存在'}
        return Rsa

    @staticmethod
    def _createPrivateRsa(private: Union[str, bytes]):
        """初始化一个private，Rsa对象
        :param private: 私钥
        :return: 对象
        """
        if isinstance(private, str):
            Rsa = RsaEncryption()
            Rsa.readPrivateKey(private)
        elif isinstance(private, bytes):
            Rsa = RsaEncryption(private_key=private)
        else:
            return {'code': 404, 'msg': '密钥不存在'}
        return Rsa

    def _encrypt(self, text: Union[str, bytes], public: Union[str, bytes], iv: bytes = None, is_decode=True) -> dict:
        """加密
        :param text: 待加密的文本
        :param public: 公钥
        :return: 加密结果
        """
        Rsa = self._createPublicRsa(public)
        ran_key = self.random_str(size=16)
        Aes = AesEncryption(aes_key=ran_key) if iv is None else AesEncryption(aes_key=ran_key, iv=iv)
        en_text = Aes.encrypt(text, is_decode=is_decode)
        en_key = Rsa.encryption(ran_key)
        return {'code': 200, 'msg': '加密成功', 'data': en_text, "key": en_key}

    def _decrypt(self, data: Union[str, bytes], private: Union[str, bytes], key: str, iv=None, is_decode=True) -> dict:
        """解密
        :param data: 待解密数据
        :param private: 私钥
        :param key: 对称加密key
        :param iv: 对称加密iv, 默认固定，也可以随机生成
        :return: 返回加密结果字典
        """
        Rsa = self._createPrivateRsa(private)
        de_key = Rsa.decryption(key)
        Aes = AesEncryption(de_key) if iv is None else AesEncryption(de_key, iv=iv)
        text = Aes.decrypt(data, is_decode=is_decode)
        return {'code': 200, 'msg': '解密成功', 'data': text}

    def textEncrypt(self, data: Union[str, bytes], public: Union[str, bytes], iv: bytes = None) -> dict:
        """数据加密
        :param data: 待加密数据
        :param public: 公钥
        :param iv: 对称加密使用的iv
        :return: 加密结果
        """
        if data is None:
            return {'code': -1, 'error': '待加密数据为空'}
        if isinstance(public, str):
            if not os.path.exists(public):
                return {'code': -1, 'error': '密钥文件不存在'}
        elif isinstance(public, bytes):
            if len(public) < 10:
                return {'code': -1, 'error': '密钥错误'}
        d = data.encode() if isinstance(data, str) else data
        return self._encrypt(d, public, iv=iv, is_decode=True)

    def textDecrypt(self, data: Union[str, bytes], private: Union[str, bytes], key: str, iv=None) -> dict:
        if data is None:
            return {'code': -1, 'error': '待解密数据为空'}
        if isinstance(private, str):
            if not os.path.exists(private):
                return {'code': -1, 'error': '密钥文件不存在'}
        elif isinstance(private, bytes):
            if len(private) < 10:
                return {'code': -1, 'error': '密钥错误'}
        return self._decrypt(data, private, key, iv=iv, is_decode=True)

    def fileEncrypt(self, path: str, public: Union[str, bytes], iv: bytes = None,
                    save_path: str = None, partition: str = '###') -> dict:
        """数据加密
        :param path: 文件路径
        :param public: 公钥
        :param iv: 对称加密使用的iv
        :param save_path: 文件保存路径及文件名，不填默认使用path
        :param partition: 保存数据默认分割为 ###
        :return: 加密结果
        """
        if not os.path.exists(path):
            return {'code': -1, 'error': '待加密文件不存在'}
        if isinstance(public, str):
            if not os.path.exists(public):
                return {'code': -1, 'error': '密钥文件不存在'}
        elif isinstance(public, bytes):
            if len(public) < 10:
                return {'code': -1, 'error': '密钥错误'}
        with open(path, 'rb') as f:
            file_data = f.read()
        r_data = self._encrypt(file_data, public, iv=iv, is_decode=False)
        if save_path is not None:
            with open(save_path, 'wb') as fl:
                fl.write((r_data.get('data') + partition.encode() + r_data.get('key').encode()))
        else:
            with open(path, 'wb') as fl:
                fl.write((r_data.get('data') + partition.encode() + r_data.get('key').encode()))
        return r_data

    def fileDecrypt(self, path: str, private: Union[str, bytes],
                    iv=None,
                    save_path: str = None,
                    partition: str = '###') -> dict:
        if not os.path.exists(path):
            return {'code': -1, 'error': '待解密文件不存在'}
        if isinstance(private, str):
            if not os.path.exists(private):
                return {'code': -1, 'error': '密钥文件不存在'}
        elif isinstance(private, bytes):
            if len(private) < 10:
                return {'code': -1, 'error': '密钥错误'}
        with open(path, 'rb') as f:
            file_data = f.read()
        d, k = tuple(file_data.decode().split(partition))
        ret = self._decrypt(d, private, k, iv=iv, is_decode=False)
        if save_path is not None:
            with open(save_path, 'wb') as f:
                f.write(ret.get('data'))
        else:
            with open(path, 'wb') as f:
                f.write(ret.get('data'))
        return ret

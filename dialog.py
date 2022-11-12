""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/11/2-16:41 """
import random

import pyperclip
from PySide6 import QtCore
from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from Gui.insert_uic import Ui_Insert
from Gui.confirm_uic import Ui_Confirm

from Global.GlobalConfig import GlobalConfig
from utils.Encryption import Encryption

from model import PasswordMemoModel
from utils.password import create_pwd


logger = GlobalConfig.logger


class MouseDialog(QDialog):

    def __init__(self):
        super(MouseDialog, self).__init__()
        self.Point = None
        self.Move = False  # 设定bool为True

    def mousePressEvent(self, event):  # 事件开始
        self.Move = True  # 设定bool为True
        if event.button() == QtCore.Qt.LeftButton:
            self.Point = event.globalPosition().toPoint() - self.pos()  # 记录起始点坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 移动时间
        if QtCore.Qt.LeftButton and self.Move:  # 切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPosition().toPoint() - self.Point)  # 移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 结束事件
        self.Move = False

    def setWindowCenter(self):
        """设置窗口居中"""
        screen = QGuiApplication.primaryScreen().size()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def setBorderlessTransparency(self):
        """设置无边框, 去边框, 窗口背景透明"""
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 设置无边框
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明


class InsertDialog(MouseDialog):

    def __init__(self, parent=None):
        super(InsertDialog, self).__init__()
        self.parent = parent
        self.ui = Ui_Insert()
        self.ui.setupUi(self)
        self.setWindowCenter()  # 设置窗口居中
        self.setBorderlessTransparency()  # 设置无边框, 去边框, 窗口背景透明
        self.bind()

    def bind(self):
        # 生成随机密码
        self.ui.random_password.clicked.connect(self.create_password)
        # 提交数据
        self.ui.add_btn.clicked.connect(self.addDate)

    def create_password(self):
        chars = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789~!@#$%^'
        pwd = ''.join(random.choice(chars) for _ in range(random.randint(6, 16)))
        logger.debug(f'生成随机密码{pwd}')
        self.ui.password.setText(pwd)

    def addDate(self):
        name = self.ui.name.text()
        account = self.ui.account.text()
        password = self.ui.password.text()
        remark = self.ui.remark.text()
        if len(name) < 2:
            self.ui.name.setFocus()
            QMessageBox.warning(self, '不能为空', '需要给个名字哦！！！')
            return
        if len(account) < 2:
            self.ui.account.setFocus()
            QMessageBox.warning(self, '不能为空', '需要给填写个账号哦！！！')
            return
        if len(password) < 2:
            self.ui.password.setFocus()
            QMessageBox.warning(self, '不能为空', '需要填写密码哦！！！')
            return
        enc = Encryption()
        ret = enc.textEncrypt(password, public=GlobalConfig.file_path.public_key)
        if ret.get('code') != 200:
            logger.critical('数据加密失败')
            return
        pwd = ret.get('data')
        key = ret.get('key')
        user_id = GlobalConfig.user.id
        PasswordMemoModel.create(user=user_id, name=name, account=account, password=pwd,
                                 remark=remark, key=key)
        logger.debug(f'{name} {account} {password} {remark}')
        QMessageBox.information(self, '添加成功', f'{name} 已经添加到数据库！')
        if self.parent:
            self.parent.search_items()


class ConfirmDialog(MouseDialog):

    def __init__(self, parent=None, _type='delete', _id=None, _row=None):
        super(ConfirmDialog, self).__init__()
        self.parent = parent
        self._type = _type
        self._id = _id
        self._row = _row
        self.ui = Ui_Confirm()
        self.ui.setupUi(self)
        self.setWindowCenter()  # 设置窗口居中
        self.setBorderlessTransparency()  # 设置无边框, 去边框, 窗口背景透明
        self.bind()

    def bind(self):
        logger.debug(self._type)
        if self._type == 'delete':
            self.ui.validation.clicked.connect(self.delete_item)
        elif self._type == 'view':
            self.ui.validation.clicked.connect(self.view_password)
        else:
            logger.debug('其它')

    def validate_password(self):
        password = self.ui.password.text()
        username = GlobalConfig.user.username
        r_pwd = create_pwd(username, password)
        pwd = GlobalConfig.user.password
        if r_pwd == pwd:
            return True
        else:
            QMessageBox.warning(self, '验证失败', '登录密码错误，验证失败！！！')
        self.close()

    def delete_item(self):
        if self.validate_password():
            if self.parent.delete_items():
                QMessageBox.warning(self, '数据删除', '密码删除成功')
            else:
                QMessageBox.warning(self, '数据删除', '密码删除失败')
        self.close()

    def view_password(self):
        if self.validate_password():
            Password = PasswordMemoModel.select().where(PasswordMemoModel.id == int(self._id))
            if not Password.count():
                self.parent.statusInfo.emit('查询数据不存在!')
                logger.error(f'{self._id} 查询数据不存在')
                return
            Pwd = Password[0]
            password = Pwd.password
            key = Pwd.key
            enc = Encryption()
            logger.debug(GlobalConfig.file_path.private_key)
            ret = enc.textDecrypt(password, private=GlobalConfig.file_path.private_key, key=key)
            if ret.get('code') != 200:
                logger.critical(f'数据加密失败 {ret.get("error")}')
                self.parent.statusInfo.emit(f'数据加密失败 {ret.get("error")}')
                return
            pwd = ret.get('data')
            item_data = QTableWidgetItem(pwd)
            self.parent.ui.tableWidget.setItem(int(self._row), 3, item_data)  # 设置item信息
            self.parent.ui.tableWidget.item(int(self._row), 3).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.parent.statusInfo.emit(f'解密成功 密码{pwd}')
            pyperclip.copy(f"{pwd}")
            self.parent.statusInfo.emit(f'密码已经自动复制 {pwd}')
        self.close()

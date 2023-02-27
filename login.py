""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/31-15:00 """
import ctypes
import re

from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMessageBox
from PySide6.QtCore import Signal

from utils.baseObject import MouseEvent
from Gui.login_uic import Ui_Form
from model import UserModel
from Global.GlobalConfig import GlobalConfig, logger
from utils.Encryption import Encryption
from utils.password import create_pwd
from utils.file import readQss


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class LoginWindow(MouseEvent):
    ProgressBar = Signal(int)  # 进度条
    set_status = Signal(str)  # 设置状态

    def __init__(self, main_window=None):
        super(LoginWindow, self).__init__()
        self.main = main_window
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(readQss('./gui_style/login.qss'))
        self.setWindowIcon(QIcon("logo.ico"))
        self.th_status = None
        self.init_window()
        self.show()

    def init_window(self):
        logger.info('开始初始化窗口')
        self.setWindowCenter()  # 设置窗口居中
        self.setBorderlessTransparency()  # 设置无边框, 去边框, 窗口背景透明
        self.set_shadow(self.ui.out_frame)  # 设置外层阴影
        self.ui.tabWidget.setCurrentIndex(0)  # 设置页面显示登录
        self.bind()  # 绑定事件
        self.bind_signal()
        logger.info('窗口初始化完成')
        self.init_info()

    def init_info(self):
        if GlobalConfig.config.auto_login:
            username = GlobalConfig.config.username
            key = GlobalConfig.config.key
            pwd = GlobalConfig.config.password
            enc = Encryption()
            try:
                ret = enc.textDecrypt(pwd, private=GlobalConfig.file_path.private_key, key=key)
            except Exception as e:
                logger.critical('解密失败，请检查')
                logger.critical(str(e))
            else:
                password = ret.get('data')
                self.ui.login_account.setText(username)
                self.ui.login_password.setText(password)
                self.ui.login_auto.setChecked(True)
                logger.info('解密成功，自动填写密码')

    def bind(self):
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.register_btn.clicked.connect(self.register)

    def bind_signal(self):
        self.ProgressBar.connect(self.set_progress_bar)
        self.set_status.connect(self.set_status_signal)

    def set_status_signal(self, value: str):
        self.ui.status.setText(value)

    def set_progress_bar(self, progress: int):
        self.ui.progressBar.setValue(progress)

    def login(self):
        """登录"""
        self.ui.login_error.setText('')
        logger.info('开始登录')
        self.ui.login_btn.setEnabled(False)
        self.set_status.emit('正在登录中')
        self.ProgressBar.emit(10)
        account = self.ui.login_account.text()
        password = self.ui.login_password.text()
        auto_login = self.ui.login_auto.isChecked()
        pwd = create_pwd(account, password)
        select_ = UserModel.select().where(UserModel.username == account)
        self.ProgressBar.emit(30)

        def error(er_type='account'):
            if er_type == 'account':
                logger.warning('用户名不存在')
                self.ui.login_error.setText('用户名不存在')
            else:
                logger.warning('密码错误！')
                self.ui.login_error.setText('密码错误！')
            self.ui.login_account.setFocus()
            self.ui.login_btn.setEnabled(True)
            self.ProgressBar.emit(0)
            logger.warning('登录失败！')
            self.set_status.emit('登录失败')

        if not select_.count():
            error()
            return
        User = select_[0]
        if User.password != pwd:
            error(er_type='password')
            return
        self.ui.login_btn.setEnabled(True)
        self.ProgressBar.emit(100)
        self.set_status.emit('登录成功')
        logger.info('登录成功')
        if auto_login:
            logger.info('下次自动登录')
            self.autoLogin(account, password)
        else:
            logger.info('下次不自动登录')
            self.clearLogin()
        GlobalConfig.user = User
        if self.main:
            self.close()
            self.main.show()
            self.ProgressBar.emit(0)
            self.set_status.emit('')
        logger.info('登录成功')

    @staticmethod
    def clearLogin():
        GlobalConfig.config.auto_login = False
        GlobalConfig.config.username = None
        GlobalConfig.config.password = None
        GlobalConfig.config.key = None
        GlobalConfig.config.save()

    @staticmethod
    def autoLogin(account, password):
        enc = Encryption()
        ret = enc.textEncrypt(password, GlobalConfig.file_path.public_key)
        if ret.get('code') != 200:
            logger.critical('数据加密失败')
            return
        pwd = ret.get('data')
        key = ret.get('key')
        logger.info(f'加密成功')
        GlobalConfig.config.auto_login = True
        GlobalConfig.config.username = account
        GlobalConfig.config.password = pwd
        GlobalConfig.config.key = key
        GlobalConfig.config.save()

    def register(self):
        """注册"""
        self.ui.error_text.setText('')
        username = self.ui.register_account.text()
        password = self.ui.register_password.text()
        if not self.check_username(username) or not self.check_password(password):
            return
        select_ = UserModel.select().where(UserModel.username == username).count()
        if select_:
            logger.debug(f'{username} {select_}')
            self.ui.error_text.setText('用户名已经存在！')
            self.ui.register_account.setFocus()
            return
        pwd = create_pwd(username, password)
        UserModel.create(username=username, password=pwd)
        logger.info('注册成功')
        QMessageBox.information(self, '注册成功', '账号注册成功，密码无法修改，请务必妥善保管！')
        self.ui.tabWidget.setCurrentIndex(0)  # 设置页面显示登录
        self.ui.error_text.setText('')

    @staticmethod
    def set_shadow(frame):
        shadow = QGraphicsDropShadowEffect()  # 设置边框阴影
        shadow.setBlurRadius(20)
        shadow.setColor(QColor("#4444"))
        shadow.setOffset(0, 0)
        frame.setGraphicsEffect(shadow)

    def check_username(self, username):
        if not re.match(r'^[a-zA-Z0-9_-]{5,16}$', username):
            self.ui.error_text.setText('用户名只能为5-16位数字或字母！')
            self.ui.register_account.setFocus()
            logger.debug('用户名校验失败')
            return False
        return True

    def check_password(self, password):
        if len(password) < 6:
            self.ui.error_text.setText('密码长度不足，安全系数极低！')
            self.ui.register_password.setFocus()
            logger.debug('密码长度不足，安全系数极低！')
            return False
        return True


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    main = LoginWindow()  # 实例化主窗口
    app.exec()  # 避免程序执行到这一行后直接退出

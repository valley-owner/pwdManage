""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-16:50 """
import ctypes
import time
import os

from PySide6.QtCore import QSize, Signal, Qt, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QSizeGrip, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QCheckBox, QFileDialog, QWidget, QPushButton, QHBoxLayout
from peewee import SQL

from configInit import global_init
from utils.jsonFile import write_file

global_init.init()  # 必须在其它的先执行，否则涉及读写文件就报错

from Global.GlobalConfig import logger
from Global.GlobalConfig import GlobalConfig

from Gui.main_uic import Ui_manage
from Gui.pay_uic import Ui_Form as Pay_Ui
from dialog import InsertDialog, ConfirmDialog

from utils.baseObject import MouseEvent
from style import get_menu
from login import LoginWindow
from model import PasswordMemoModel


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class PayWindow(QWidget):

    def __init__(self):
        super(PayWindow, self).__init__()
        self.ui = Pay_Ui()
        self.ui.setupUi(self)
        flags = self.windowFlags()
        self.setWindowFlags(flags | Qt.WindowStaysOnTopHint)


class MainWindow(MouseEvent):
    ProgressBar = Signal(int)  # 进度条
    statusInfo = Signal(str)  # 左下角状态信息
    stateTime = Signal(str)  # 展示时间

    def __init__(self, payPage=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_manage()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("logo.ico"))
        self.login = LoginWindow(self)
        self.setWindowCenter()  # 设置窗口居中
        self.setBorderlessTransparency()  # 设置无边框, 去边框, 窗口背景透明
        self.extend = False  # 默认不扩展
        self.checkbox_list = []  # 搜索列表中的多选按钮
        self.selected_list = []  # 选择结果
        self.initWindow()
        self.bind()
        self.bind_signal()
        self.stateTime.emit(time.strftime('%Y/%m/%d %H:%M'))
        self.hide()
        self.pay = payPage

    def bind(self):
        # 扩展按钮点击事件
        self.ui.extend_btn.clicked.connect(self.extendEvent)
        # 菜单事件
        self.ui.manage_btn.clicked.connect(lambda: self.changePage(0))
        self.ui.setting_btn.clicked.connect(lambda: self.changePage(1))
        self.ui.about_btn.clicked.connect(lambda: self.changePage(2))
        # 菜单退出
        self.ui.exit_btn.clicked.connect(self.exitLogin)
        # 增加密码
        self.ui.add_btn.clicked.connect(self.insert_password)
        # 删除密码
        self.ui.del_btn.clicked.connect(lambda: self.validate_dialog(_type='delete'))
        # 查询
        self.ui.search.clicked.connect(self.search_items)
        # 下拉框
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxChanged)
        # 最大化
        self.ui.max_btn.clicked.connect(self.winSize)

    def winSize(self):
        """窗口最大化与最小化"""
        if self.isMaximized():
            self.showNormal()
            self.changeBtnIcon(self.ui.max_btn, ":/white/images/white/icon-max.svg", '最大化')
        else:
            self.showMaximized()
            self.changeBtnIcon(self.ui.max_btn, ":/white/images/white/icon-repeat.svg", '恢复')

    @staticmethod
    def changeBtnIcon(btn, img_path: str, text: str = None):
        icon = QIcon()
        icon.addPixmap(QPixmap(img_path), QIcon.Normal, QIcon.Off)
        btn.setIcon(icon)
        btn.setToolTip("<html><head/><body><p>" + text + "</p></body></html>")

    def bind_signal(self):
        self.ProgressBar.connect(self.set_progress_bar)
        self.statusInfo.connect(self.set_status_signal)
        self.stateTime.connect(self.set_state_time)

    def set_state_time(self, _time: str):
        self.ui.state_time.setText(_time)

    def set_status_signal(self, value: str):
        self.ui.status_info.setText(value)

    def set_progress_bar(self, progress: int):
        self.ui.progressBar.setValue(progress)

    def init_setting(self):
        self.ui.db_label.setText(str(GlobalConfig.file_path.database_path))
        self.ui.path_label.setText(str(GlobalConfig.file_path.config_file_path))
        self.ui.log_label.setText(str(GlobalConfig.file_path.log_path))
        self.ui.pub_key_label.setText(str(GlobalConfig.file_path.public_key))
        self.ui.priv_key_label.setText(str(GlobalConfig.file_path.private_key))
        self.ui.db_bth.clicked.connect(self.getDbFilePath)
        self.ui.path_btn.clicked.connect(self.getPathFilePath)
        self.ui.log_btn.clicked.connect(self.getLogFilePath)
        self.ui.public_btn.clicked.connect(self.getPublicFilePath)
        self.ui.private_btn.clicked.connect(self.getPrivateFilePath)

    def getDbFilePath(self):
        self.statusInfo.emit(f'选择数据库')
        file, _ = QFileDialog.getOpenFileName(self, '请选择数据库', GlobalConfig.dir_path.config_dir, 'sqlite file (*.db);')
        logger.debug(file)
        if file:
            path = str(file).replace('/', os.sep)
            self.ui.db_label.setText(path)
            GlobalConfig.file_path.database_path = path
            write_file(GlobalConfig.file_path.config_file_path, {'dir_file': GlobalConfig.dir_path,
                                                                 'path_file': GlobalConfig.file_path})
            self.statusInfo.emit(f'文件配置更新完成')
            self.select_init()

    def getPathFilePath(self):
        self.statusInfo.emit(f'选择配置文件')
        file, _ = QFileDialog.getOpenFileName(self, '请选择配置文件', GlobalConfig.dir_path.config_dir,
                                              'config file (*.json);')
        logger.debug(file)
        if file:
            path = str(file).replace('/', os.sep)
            self.ui.path_label.setText(path)
            GlobalConfig.file_path.config_file_path = path
            write_file(GlobalConfig.file_path.config_file_path, {'dir_file': GlobalConfig.dir_path,
                                                                 'path_file': GlobalConfig.file_path})
            self.statusInfo.emit(f'文件配置更新完成')
            self.select_init()

    def getLogFilePath(self):
        self.statusInfo.emit(f'选择日志文件')
        file, _ = QFileDialog.getOpenFileName(self, '请选择日志文件', GlobalConfig.dir_path.log_dir, 'config file (*.log);')
        logger.debug(file)
        if file:
            path = str(file).replace('/', os.sep)
            self.ui.log_label.setText(path)
            GlobalConfig.file_path.log_path = path
            write_file(GlobalConfig.file_path.config_file_path, {'dir_file': GlobalConfig.dir_path,
                                                                 'path_file': GlobalConfig.file_path})
            self.statusInfo.emit(f'文件配置更新完成')
            self.select_init()

    def getPublicFilePath(self):
        self.statusInfo.emit(f'选择公钥')
        file, _ = QFileDialog.getOpenFileName(self, '请选择公钥', GlobalConfig.dir_path.key_dir, 'config file (*.pem);')
        logger.debug(file)
        if file:
            path = str(file).replace('/', os.sep)
            self.ui.pub_key_label.setText(path)
            GlobalConfig.file_path.public_key = path
            write_file(GlobalConfig.file_path.config_file_path, {'dir_file': GlobalConfig.dir_path,
                                                                 'path_file': GlobalConfig.file_path})
            self.statusInfo.emit(f'文件配置更新完成')
            self.select_init()

    def getPrivateFilePath(self):
        self.statusInfo.emit(f'选择私钥')
        file, _ = QFileDialog.getOpenFileName(self, '请选择私钥', GlobalConfig.dir_path.key_dir, 'config file (*.pem);')
        logger.debug(file)
        if file:
            path = str(file).replace('/', os.sep)
            self.ui.priv_key_label.setText(path)
            GlobalConfig.file_path.private_key = path
            write_file(GlobalConfig.file_path.config_file_path, {'dir_file': GlobalConfig.dir_path,
                                                                 'path_file': GlobalConfig.file_path})
            self.statusInfo.emit(f'文件配置更新完成')
            self.select_init()

    def select_init(self):
        self.search_items()

    def initWindow(self):
        logger.debug('初始化主窗口')
        sizegrip = QSizeGrip(self.ui.set_size)  # 设置右下角可以缩放窗口
        sizegrip.setToolTip('放大缩小窗口')
        self.extend_show(False)
        self.changePage(0)
        self.setComboBox()
        self.ui.keyword.setEnabled(False)
        self.initTable()
        self.init_setting()
        # 定时任务
        self.timedTasks()

    def initTable(self):
        tab = self.ui.tableWidget
        tab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # x先自适应宽度
        tab.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        tab.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 单元格不可编辑
        tab.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        tab.setColumnWidth(0, 30)

    def timedTasks(self):
        """定时任务"""
        # 任务一展示时间
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000 * 60)
        # 展示捐赠页面
        QTimer.singleShot(1000 * 60 * 5, self.payShow)

    def payShow(self):
        self.pay.show()

    def showtime(self):
        """展示当前时间"""
        t = time.strftime('%Y/%m/%d %H:%M')
        self.stateTime.emit(t)

    def setComboBox(self):
        """初始化下拉选择框"""
        comboBox = self.ui.comboBox
        comboBox.addItems(['全部', '名字', '账号', '备注'])

    def changePage(self, page: int):
        logger.debug(f'切换页面{page}')
        self.statusInfo.emit('切换页面')
        btn = [self.ui.manage_btn, self.ui.setting_btn, self.ui.about_btn]
        btn_name = ['manage', 'setting', 'about']
        if self.extend:
            self.extend_show()
            btn[page].setStyleSheet(get_menu(btn_name[page], position='left', click=True))
        else:
            self.extend_show(False)
            btn[page].setStyleSheet(get_menu(btn_name[page], click=True))
        self.ui.stacked_page.setCurrentIndex(page)

    def extend_show(self, show: bool = True):
        self.extend = show
        menu_btn = [self.ui.extend_btn, self.ui.manage_btn, self.ui.setting_btn, self.ui.about_btn, self.ui.exit_btn]
        menu_name = ['extend', 'manage', 'setting', 'about', 'exit']
        if show:
            menu_text = ['扩展', '管理', '设置', '关于', '退出']
            self.ui.body_left.setMaximumSize(QSize(120, 16777215))
            self.ui.body_left.setMinimumSize(QSize(120, 16777215))
            for i in range(len(menu_text)):
                menu_btn[i].setText(menu_text[i])
                menu_btn[i].setStyleSheet(get_menu(menu_name[i], position='left'))
        else:
            self.ui.body_left.setMaximumSize(QSize(42, 16777215))
            self.ui.body_left.setMinimumSize(QSize(42, 16777215))
            for i in range(len(menu_name)):
                menu_btn[i].setText('')
                menu_btn[i].setStyleSheet(get_menu(menu_name[i]))

    def extendEvent(self):
        if self.extend:
            logger.debug('关闭菜单')
            self.statusInfo.emit('关闭菜单')
            self.extend_show(False)
        else:
            logger.debug('展开菜单')
            self.statusInfo.emit('展开菜单')
            self.extend_show()

    def exitLogin(self):
        logger.debug('退出主界面')
        self.statusInfo.emit('退出主界面')
        self.hide()
        self.login.show()

    def insert_password(self):
        dialog = InsertDialog(self)
        dialog.exec()

    def validate_dialog(self, _type='delete', _id=None, _row=None):
        delete_dialog = ConfirmDialog(self, _type, _id, _row)
        delete_dialog.exec()

    def delete_items(self):
        """删除数据"""
        del_list = self.selected_list
        if len(del_list) == 0:
            return False
        for i in del_list:
            PasswordMemoModel.delete().where(PasswordMemoModel.id == int(i)).execute()
        self.search_items()
        return True

    def search_items(self):
        self.checkbox_list = []  # 搜索列表中的多选按钮
        self.selected_list = []  # 选择结果
        condition = self.ui.comboBox.currentIndex()
        if condition != 0:
            key_word = self.ui.keyword.text()
            logger.debug(key_word)
            self.statusInfo.emit(f'正在搜索{key_word} ...')
            if len(key_word) == 0:
                self.statusInfo.emit('搜索关键词不能为空')
                self.ui.search.setFocus()
                return
            if condition == 1:
                logger.debug('按照名字查询')
                password_list = PasswordMemoModel.select().where(PasswordMemoModel.user == GlobalConfig.user.id,
                                                                 SQL(f"name like '%{key_word}%'"))
            elif condition == 2:
                logger.debug('按照账号查询')
                password_list = PasswordMemoModel.select().where(PasswordMemoModel.user == GlobalConfig.user.id,
                                                                 SQL(f"account like '%{key_word}%'"))
            elif condition == 3:
                logger.debug('按照备注查询')
                password_list = PasswordMemoModel.select().where(PasswordMemoModel.user == GlobalConfig.user.id,
                                                                 SQL(f"remark like '%{key_word}%'"))
            else:
                logger.critical('查询错误')
                return
        else:
            password_list = PasswordMemoModel.select().where(PasswordMemoModel.user == GlobalConfig.user.id)
        table = self.ui.tableWidget
        table.setRowCount(0)
        logger.debug(password_list.count())
        self.addTableItem(table, password_list)
        self.statusInfo.emit(f'搜索成功')

    def addTableItem(self, table, items: list):
        for item in items:
            logger.debug(item.id)
            RowCont = table.rowCount()
            table.insertRow(RowCont)  # 增加一行

            checkbox = QCheckBox()
            checkbox.setText(str(item.id))
            self.checkbox_list.append(checkbox)
            checkbox.stateChanged.connect(self.checkboxChanged)
            table.setCellWidget(RowCont, 0, checkbox)

            # 设置button
            table.setCellWidget(RowCont, 6, self.createButton())

            d_list = [QTableWidgetItem(item.name), QTableWidgetItem(item.account),
                      QTableWidgetItem(item.password), QTableWidgetItem(item.remark),
                      QTableWidgetItem(str(item.add_time).split('.')[0])]
            for it in range(len(d_list)):
                table.setItem(RowCont, it + 1, d_list[it])
                table.item(RowCont, it + 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table.resizeColumnsToContents()  # 设置自动列宽
        self.initTable()

    def createButton(self):
        widget = QWidget()
        see_btn = QPushButton('查看')
        see_btn.setStyleSheet('''QPushButton{
color:#000000;
text-align : center;
border:1px solid rgba(204, 204, 204, 150);
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 195, 200, 255), stop:0.403409 rgba(129, 213, 228, 255), stop:1 rgba(177, 184, 217, 255));
border-radius:12px;
}
QPushButton:hover {
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 227, 255), stop:0.403409 rgba(7, 228, 223, 255), stop:1 rgba(89, 191, 180, 255));
border-radius:12px;
}
QPushButton:pressed {
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 195, 200, 255), stop:0.403409 rgba(129, 213, 228, 255), stop:1 rgba(177, 184, 217, 255));
border-top:5px;
border-left:5px;
border-radius:12px;
}''')
        see_btn.setMaximumSize(QSize(80, 24))
        see_btn.setMinimumSize(QSize(80, 24))
        see_btn.clicked.connect(self.viewButton)
        hLayout = QHBoxLayout()
        hLayout.addWidget(see_btn)
        hLayout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(hLayout)
        return widget

    def viewButton(self):
        logger.debug('查看密码')
        button = self.sender()
        if button:
            row = self.ui.tableWidget.indexAt(button.parent().pos()).row()
            con = self.checkbox_list[int(row)]
            try:
                id_ = con.text()
            except RuntimeError as e:
                self.statusInfo.emit('查询失败请重启软件')
                logger.critical(e)
                return
            self.validate_dialog(_type='view', _id=int(id_), _row=int(row))

    def checkboxChanged(self):
        """表格中的按钮状态改变, 更新选中列表"""
        ret_list = []
        for i in self.checkbox_list:
            if i.isChecked():
                ret_list.append(i.text())
        logger.debug(ret_list)
        self.selected_list = ret_list

    def comboBoxChanged(self):
        com = self.ui.comboBox.currentIndex()
        if com == 0:
            self.ui.keyword.setEnabled(False)
        else:
            self.ui.keyword.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    pay = PayWindow()
    main = MainWindow(pay)  # 实例化主窗口
    app.exec()  # 避免程序执行到这一行后直接退出

""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/29-21:12 """
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication, QIcon, QPixmap
from PySide6.QtWidgets import QWidget


class MouseEvent(QWidget):

    def __init__(self):
        super(MouseEvent, self).__init__()
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


class basePath:

    @classmethod
    def get_dict(cls):
        return {key: value for key, value in cls.__dict__.items() if key[0] != '_' and key != 'get_dict'}
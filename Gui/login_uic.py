# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
from Gui import login_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(444, 550)
        Form.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.out_frame = QFrame(Form)
        self.out_frame.setObjectName(u"out_frame")
        self.out_frame.setMinimumSize(QSize(420, 500))
        self.out_frame.setMaximumSize(QSize(420, 500))
        self.out_frame.setStyleSheet(u"")
        self.out_frame.setFrameShape(QFrame.StyledPanel)
        self.out_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.out_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.minimize = QPushButton(self.out_frame)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(35, 30))
        self.minimize.setMaximumSize(QSize(35, 30))
        self.minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/button/images/black/icon-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.minimize)

        self.close = QPushButton(self.out_frame)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(35, 30))
        self.close.setMaximumSize(QSize(35, 30))
        self.close.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/button/images/black/icon-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.close)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.out_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icon/images/icon/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.out_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        self.label_2.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.in_frame = QFrame(self.out_frame)
        self.in_frame.setObjectName(u"in_frame")
        self.in_frame.setMinimumSize(QSize(298, 300))
        self.in_frame.setMaximumSize(QSize(298, 300))
        self.in_frame.setAutoFillBackground(False)
        self.in_frame.setStyleSheet(u"")
        self.in_frame.setFrameShape(QFrame.StyledPanel)
        self.in_frame.setFrameShadow(QFrame.Raised)
        self.in_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.in_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.in_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 300))
        self.tabWidget.setMaximumSize(QSize(300, 300))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(14)
        self.tabWidget.setFont(font1)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout = QVBoxLayout(self.login)
        self.verticalLayout.setSpacing(32)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 30, 9, 10)
        self.login_account = QLineEdit(self.login)
        self.login_account.setObjectName(u"login_account")
        self.login_account.setMinimumSize(QSize(0, 40))
        self.login_account.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        self.login_account.setFont(font2)
        self.login_account.setStyleSheet(u"")
        self.login_account.setMaxLength(64)

        self.verticalLayout.addWidget(self.login_account)

        self.login_password = QLineEdit(self.login)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setMinimumSize(QSize(0, 40))
        self.login_password.setMaximumSize(QSize(16777215, 40))
        self.login_password.setFont(font2)
        self.login_password.setMaxLength(64)
        self.login_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.login_password)

        self.login_btn = QPushButton(self.login)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 40))
        self.login_btn.setMaximumSize(QSize(16777215, 40))
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.login_btn)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.login_auto = QRadioButton(self.login)
        self.login_auto.setObjectName(u"login_auto")
        self.login_auto.setMinimumSize(QSize(100, 30))
        self.login_auto.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(10)
        self.login_auto.setFont(font3)
        self.login_auto.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.login_auto)

        self.login_error = QLabel(self.login)
        self.login_error.setObjectName(u"login_error")
        self.login_error.setMinimumSize(QSize(0, 30))
        self.login_error.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(11)
        self.login_error.setFont(font4)
        self.login_error.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.login_error)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.login, "")
        self.register = QWidget()
        self.register.setObjectName(u"register")
        self.verticalLayout_2 = QVBoxLayout(self.register)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, 10)
        self.register_account = QLineEdit(self.register)
        self.register_account.setObjectName(u"register_account")
        self.register_account.setMinimumSize(QSize(0, 40))
        self.register_account.setMaximumSize(QSize(16777215, 40))
        self.register_account.setFont(font2)
        self.register_account.setAutoFillBackground(False)
        self.register_account.setStyleSheet(u"")
        self.register_account.setMaxLength(64)
        self.register_account.setFrame(True)
        self.register_account.setCursorPosition(0)
        self.register_account.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.register_account.setClearButtonEnabled(False)

        self.verticalLayout_2.addWidget(self.register_account)

        self.register_password = QLineEdit(self.register)
        self.register_password.setObjectName(u"register_password")
        self.register_password.setMinimumSize(QSize(0, 40))
        self.register_password.setMaximumSize(QSize(16777215, 40))
        self.register_password.setFont(font2)
        self.register_password.setStyleSheet(u"")
        self.register_password.setMaxLength(64)
        self.register_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.register_password)

        self.register_btn = QPushButton(self.register)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setMinimumSize(QSize(0, 40))
        self.register_btn.setMaximumSize(QSize(16777215, 40))
        self.register_btn.setFont(font2)

        self.verticalLayout_2.addWidget(self.register_btn)

        self.error_text = QLabel(self.register)
        self.error_text.setObjectName(u"error_text")
        self.error_text.setMinimumSize(QSize(0, 30))
        self.error_text.setMaximumSize(QSize(16777215, 30))
        self.error_text.setFont(font4)
        self.error_text.setStyleSheet(u"")
        self.error_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error_text)

        self.tabWidget.addTab(self.register, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_4.addWidget(self.in_frame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.status = QLabel(self.out_frame)
        self.status.setObjectName(u"status")
        self.status.setFont(font2)
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.status)

        self.progressBar = QProgressBar(self.out_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.horizontalLayout.addWidget(self.out_frame)


        self.retranslateUi(Form)
        self.close.clicked.connect(Form.close)
        self.minimize.clicked.connect(Form.showMinimized)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.minimize.setText("")
        self.close.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.login_account.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.login_password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.login_auto.setText(QCoreApplication.translate("Form", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.login_error.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.register_account.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.register_password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.register_btn.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
        self.error_text.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register), QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.status.setText("")
    # retranslateUi


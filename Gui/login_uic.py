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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(420, 500))
        self.frame.setMaximumSize(QSize(420, 500))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(236, 239, 255);\n"
"border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(35, 30))
        self.pushButton.setMaximumSize(QSize(35, 30))
        self.pushButton.setStyleSheet(u"QPushButton { \n"
"border:none;\n"
" } \n"
"QPushButton:hover { \n"
"background-color: rgba(160, 160, 160, 80); \n"
"} \n"
"QPushButton:pressed {\n"
" background-color: rgb(255, 237, 252); \n"
"border-top:5px; \n"
"border-left:5px;\n"
" }")
        icon = QIcon()
        icon.addFile(u":/button/images/black/icon-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(35, 30))
        self.pushButton_2.setMaximumSize(QSize(35, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton { \n"
"border:none; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: rgb(255, 0, 0);\n"
" } \n"
"QPushButton:pressed {\n"
" background-color: rgb(255, 237, 252); \n"
"border-top:5px; \n"
"border-left:5px;\n"
" }")
        icon1 = QIcon()
        icon1.addFile(u":/button/images/black/icon-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icon/images/icon/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
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

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(298, 300))
        self.frame_2.setMaximumSize(QSize(298, 300))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 300))
        self.tabWidget.setMaximumSize(QSize(300, 300))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(14)
        self.tabWidget.setFont(font1)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget #tabWidget{\n"
"background-color: #ffffff;\n"
"border-radius: 12px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"\n"
"}\n"
"QWidget {\n"
"background-color: #ffffff;\n"
"border-radius: 12px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"}\n"
"\n"
"QTabWidget::pane{\n"
"	border:none;\n"
"	\n"
"}\n"
"QTabBar::tab{\n"
"	width:148px;\n"
"	height:40; \n"
"	margin:0px;\n"
"}\n"
"QTabBar::tab:first:!selected {\n"
"	color: rgba(0, 0, 0, 240);\n"
"	background-color: rgba(200,200,200, 120);\n"
"	Border-top-left-radius:12px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"	color: rgb(0, 0, 0);;\n"
"	background-color: #ffffff;\n"
"	Border-top-left-radius:12px;\n"
"	border-bottom-left-radius: 12px;\n"
"}\n"
"QTabBar::tab:last:!selected {\n"
"	color: rgba(0, 0, 0, 240);\n"
"	background-color: rgba(200,200,200, 120);\n"
"	Border-top-right-radius:12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}\n"
"QTabBar::tab:last:selected {\n"
"	color: rgb(0, 0, 0);;\n"
"	background-color: #ffffff;\n"
"	Border-top-"
                        "right-radius:12px;\n"
"	border-bottom-right-radius: 12px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"	color: #000000;\n"
"	background-color: #ffffff;\n"
"}\n"
"QTabBar::tab:selected {\n"
"	color: rgba(255, 255, 255, 180);\n"
"	background-color: rgb(97,0,0);\n"
"}\n"
"QTabWidget::tab-bar { \n"
"	alignment: center; \n"
"}\n"
"QPushButton{\n"
"	text-align : center;\n"
"	border:1px solid rgba(204, 204, 204, 150);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 195, 200, 255), stop:0.403409 rgba(129, 213, 228, 255), stop:1 rgba(177, 184, 217, 255));\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 227, 255), stop:0.403409 rgba(7, 228, 223, 255), stop:1 rgba(89, 191, 180, 255));\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 195, 200, 255), stop:0.403409 rgba(129, 213, 228, "
                        "255), stop:1 rgba(177, 184, 217, 255));\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:12px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: #f7f7f7;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 12px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"	padding-left: 12px; /* \u6587\u672c\u8ddd\u79bb\u5de6\u8fb9\u754c\u67095px */\n"
"	/*selection-background-color: #A0A0A0;  \u9009\u4e2d\u6587\u672c\u7684\u80cc\u666f\u989c\u8272 */\n"
"	/* selection-color: #ffffff;  \u9009\u4e2d\u6587\u672c\u7684\u989c\u8272 */\n"
"}\n"
"QLineEdit:focus{\n"
"	/* border: 1px solid rgb(0, 255, 255); */\n"
"	border-radius: 12px; /* \u8fb9\u6846\u5706\u89d2 */\n"
"}\n"
"QLineEdit[echoMode=\"2\"] { /* QLineEdit\u6709\u8f93\u5165\u63a9\u7801\u65f6\u7684\u72b6\u6001 */\n"
"	lineedit-password-character: 9679;\n"
"	lineedit-password-mask-delay: 2000;\n"
"}")
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
        self.login_auto.setStyleSheet(u"QRadioButton::indicator::unchecked {\n"
"	image: url(:/button/images/login/danxuan.svg);\n"
"}\n"
"QRadioButton::indicator::checked {\n"
"	image: url(:/button/images/login/danxuan-xuanzhong.svg);\n"
"}")

        self.horizontalLayout_5.addWidget(self.login_auto)

        self.login_error = QLabel(self.login)
        self.login_error.setObjectName(u"login_error")
        self.login_error.setMinimumSize(QSize(0, 30))
        self.login_error.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(11)
        self.login_error.setFont(font4)
        self.login_error.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 42, 0, 255), stop:0.238636 rgba(255, 140, 61, 255), stop:0.545455 rgba(255, 115, 139, 255), stop:1 rgba(255, 0, 144, 255));")

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
        self.error_text.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 42, 0, 255), stop:0.238636 rgba(255, 140, 61, 255), stop:0.545455 rgba(255, 115, 139, 255), stop:1 rgba(255, 0, 144, 255));")
        self.error_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.error_text)

        self.tabWidget.addTab(self.register, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.status = QLabel(self.frame)
        self.status.setObjectName(u"status")
        self.status.setFont(font2)
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.status)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    min-height: 8px;\n"
"    max-height: 8px;\n"
"    border-radius: 4px;\n"
"	background-color: rgb(236, 239, 255);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 227, 255), stop:0.403409 rgba(7, 228, 223, 255), stop:1 rgba(89, 191, 180, 255));\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(Form.showMinimized)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
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


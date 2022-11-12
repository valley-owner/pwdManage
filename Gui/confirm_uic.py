# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from Gui import login_rc

class Ui_Confirm(object):
    def setupUi(self, Confirm):
        if not Confirm.objectName():
            Confirm.setObjectName(u"Confirm")
        Confirm.resize(403, 268)
        self.verticalLayout = QVBoxLayout(Confirm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Confirm)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(380, 250))
        self.frame.setMaximumSize(QSize(380, 250))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(236, 239, 255);\n"
"border-radius: 30px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

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

        self.horizontalLayout_2.addWidget(self.pushButton)

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

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(310, 180))
        self.frame_2.setMaximumSize(QSize(310, 180))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
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
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78, 195, 200, 255), stop:0.403409 rgba(129, 213, 228, 255), stop:1 rgba(177, 184, 217, 255));\n"
"border-top:5px;\n"
"border-left:5px;\n"
"border-radius:12px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: #f7f7f7;\n"
"	border: none;\n"
"	outline: none;\n"
"	border-radius: 12px; /* \u8fb9\u6846"
                        "\u5706\u89d2 */\n"
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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 30, 5, 30)
        self.password = QLineEdit(self.frame_2)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(300, 40))
        self.password.setMaximumSize(QSize(300, 40))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet(u"")
        self.password.setMaxLength(64)

        self.verticalLayout_2.addWidget(self.password)

        self.validation = QPushButton(self.frame_2)
        self.validation.setObjectName(u"validation")
        self.validation.setMinimumSize(QSize(300, 40))
        self.validation.setMaximumSize(QSize(300, 40))
        self.validation.setFont(font)
        self.validation.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.validation)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Confirm)
        self.pushButton.clicked.connect(Confirm.showMinimized)
        self.pushButton_2.clicked.connect(Confirm.close)

        QMetaObject.connectSlotsByName(Confirm)
    # setupUi

    def retranslateUi(self, Confirm):
        Confirm.setWindowTitle(QCoreApplication.translate("Confirm", u"Dialog", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.password.setToolTip(QCoreApplication.translate("Confirm", u"\u5fc5\u586b\uff0c\u7528\u4e8e\u533a\u5206\u4e0d\u540c\u7684\u5bc6\u7801\uff0c\u65b9\u4fbf\u67e5\u8be2", None))
#endif // QT_CONFIG(tooltip)
        self.password.setPlaceholderText(QCoreApplication.translate("Confirm", u"\u8bf7\u8f93\u5165\u767b\u5f55\u5bc6\u7801", None))
        self.validation.setText(QCoreApplication.translate("Confirm", u"\u786e\u5b9a", None))
    # retranslateUi


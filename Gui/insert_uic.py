# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'insert.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from Gui import login_rc

class Ui_Insert(object):
    def setupUi(self, Insert):
        if not Insert.objectName():
            Insert.setObjectName(u"Insert")
        Insert.resize(403, 489)
        Insert.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Insert)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Insert)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(380, 470))
        self.frame.setMaximumSize(QSize(380, 470))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.frame)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(35, 30))
        self.minimize.setMaximumSize(QSize(35, 30))
        self.minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/button/images/black/icon-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimize)

        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(35, 30))
        self.close.setMaximumSize(QSize(35, 30))
        self.close.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/button/images/black/icon-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setPixmap(QPixmap(u":/icon/images/icon/logo.ico"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.NoAntialias)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.in_frame = QFrame(self.frame)
        self.in_frame.setObjectName(u"in_frame")
        self.in_frame.setMinimumSize(QSize(310, 330))
        self.in_frame.setMaximumSize(QSize(310, 330))
        self.in_frame.setStyleSheet(u"")
        self.in_frame.setFrameShape(QFrame.StyledPanel)
        self.in_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.in_frame)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 30, 5, 30)
        self.name = QLineEdit(self.in_frame)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(300, 40))
        self.name.setMaximumSize(QSize(300, 40))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        self.name.setFont(font1)
        self.name.setStyleSheet(u"")
        self.name.setMaxLength(256)

        self.verticalLayout_2.addWidget(self.name)

        self.account = QLineEdit(self.in_frame)
        self.account.setObjectName(u"account")
        self.account.setMinimumSize(QSize(300, 40))
        self.account.setMaximumSize(QSize(300, 40))
        self.account.setFont(font1)
        self.account.setStyleSheet(u"")
        self.account.setMaxLength(256)

        self.verticalLayout_2.addWidget(self.account)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.password = QLineEdit(self.in_frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(200, 40))
        self.password.setMaximumSize(QSize(200, 40))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"")
        self.password.setMaxLength(64)

        self.horizontalLayout.addWidget(self.password)

        self.random_password = QPushButton(self.in_frame)
        self.random_password.setObjectName(u"random_password")
        self.random_password.setMinimumSize(QSize(90, 40))
        self.random_password.setMaximumSize(QSize(90, 40))
        self.random_password.setFont(font1)
        self.random_password.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.random_password)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.remark = QLineEdit(self.in_frame)
        self.remark.setObjectName(u"remark")
        self.remark.setMinimumSize(QSize(300, 40))
        self.remark.setMaximumSize(QSize(300, 40))
        self.remark.setFont(font1)
        self.remark.setStyleSheet(u"")
        self.remark.setMaxLength(256)

        self.verticalLayout_2.addWidget(self.remark)

        self.add_btn = QPushButton(self.in_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(300, 40))
        self.add_btn.setMaximumSize(QSize(300, 40))
        self.add_btn.setFont(font1)
        self.add_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.add_btn)


        self.horizontalLayout_4.addWidget(self.in_frame)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Insert)
        self.minimize.clicked.connect(Insert.showMinimized)
        self.close.clicked.connect(Insert.close)

        QMetaObject.connectSlotsByName(Insert)
    # setupUi

    def retranslateUi(self, Insert):
        Insert.setWindowTitle(QCoreApplication.translate("Insert", u"Dialog", None))
        self.minimize.setText("")
        self.close.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("Insert", u"\u589e\u52a0\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.name.setToolTip(QCoreApplication.translate("Insert", u"\u5fc5\u586b\uff0c\u7528\u4e8e\u533a\u5206\u4e0d\u540c\u7684\u5bc6\u7801\uff0c\u65b9\u4fbf\u67e5\u8be2", None))
#endif // QT_CONFIG(tooltip)
        self.name.setPlaceholderText(QCoreApplication.translate("Insert", u"\u8bf7\u7ed9\u5bc6\u7801\u4e00\u4e2a\u540d\u5b57", None))
#if QT_CONFIG(tooltip)
        self.account.setToolTip(QCoreApplication.translate("Insert", u"\u5fc5\u586b", None))
#endif // QT_CONFIG(tooltip)
        self.account.setPlaceholderText(QCoreApplication.translate("Insert", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
#if QT_CONFIG(tooltip)
        self.password.setToolTip(QCoreApplication.translate("Insert", u"\u5fc5\u586b\uff0c\u968f\u673a\u5bc6\u7801\u4f1a\u5305\u542b\u7279\u6b8a\u7b26\u53f7\uff0c\u5efa\u8bae\u4f7f\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.password.setPlaceholderText(QCoreApplication.translate("Insert", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.random_password.setText(QCoreApplication.translate("Insert", u"\u968f\u673a\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.remark.setToolTip(QCoreApplication.translate("Insert", u"\u53ef\u9009\uff0c\u7ed9\u5bc6\u7801\u4e00\u4e2a\u5907\u6ce8\u4fe1\u606f\uff0c\u65b9\u4fbf\u68c0\u7d22", None))
#endif // QT_CONFIG(tooltip)
        self.remark.setPlaceholderText(QCoreApplication.translate("Insert", u"\u8bf7\u8f93\u5165\u5907\u6ce8", None))
        self.add_btn.setText(QCoreApplication.translate("Insert", u"\u589e\u52a0", None))
    # retranslateUi


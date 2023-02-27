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
        Confirm.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Confirm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Confirm)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(380, 250))
        self.frame.setMaximumSize(QSize(380, 250))
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
        icon = QIcon()
        icon.addFile(u":/button/images/black/icon-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.minimize)

        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(35, 30))
        self.close.setMaximumSize(QSize(35, 30))
        icon1 = QIcon()
        icon1.addFile(u":/button/images/black/icon-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.in_frame = QFrame(self.frame)
        self.in_frame.setObjectName(u"in_frame")
        self.in_frame.setMinimumSize(QSize(310, 180))
        self.in_frame.setMaximumSize(QSize(310, 180))
        self.in_frame.setStyleSheet(u"")
        self.in_frame.setFrameShape(QFrame.StyledPanel)
        self.in_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.in_frame)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 30, 5, 30)
        self.password = QLineEdit(self.in_frame)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(300, 40))
        self.password.setMaximumSize(QSize(300, 40))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet(u"")
        self.password.setMaxLength(64)
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password)

        self.validation = QPushButton(self.in_frame)
        self.validation.setObjectName(u"validation")
        self.validation.setMinimumSize(QSize(300, 40))
        self.validation.setMaximumSize(QSize(300, 40))
        self.validation.setFont(font)
        self.validation.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.validation)


        self.horizontalLayout_4.addWidget(self.in_frame)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Confirm)
        self.minimize.clicked.connect(Confirm.showMinimized)
        self.close.clicked.connect(Confirm.close)

        QMetaObject.connectSlotsByName(Confirm)
    # setupUi

    def retranslateUi(self, Confirm):
        Confirm.setWindowTitle(QCoreApplication.translate("Confirm", u"Dialog", None))
        self.minimize.setText("")
        self.close.setText("")
#if QT_CONFIG(tooltip)
        self.password.setToolTip(QCoreApplication.translate("Confirm", u"\u5fc5\u586b\uff0c\u7528\u4e8e\u533a\u5206\u4e0d\u540c\u7684\u5bc6\u7801\uff0c\u65b9\u4fbf\u67e5\u8be2", None))
#endif // QT_CONFIG(tooltip)
        self.password.setPlaceholderText(QCoreApplication.translate("Confirm", u"\u8bf7\u8f93\u5165\u767b\u5f55\u5bc6\u7801", None))
        self.validation.setText(QCoreApplication.translate("Confirm", u"\u786e\u5b9a", None))
    # retranslateUi


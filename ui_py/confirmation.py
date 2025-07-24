# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Confirmation(object):
    def setupUi(self, Confirmation):
        if not Confirmation.objectName():
            Confirmation.setObjectName(u"Confirmation")
        Confirmation.resize(250, 144)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Confirmation.sizePolicy().hasHeightForWidth())
        Confirmation.setSizePolicy(sizePolicy)
        Confirmation.setMaximumSize(QSize(300, 150))
        self.verticalLayout = QVBoxLayout(Confirmation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_label = QLabel(Confirmation)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.main_label.setFont(font)

        self.verticalLayout.addWidget(self.main_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_btn = QPushButton(Confirmation)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.ok_btn)

        self.cancel_btn = QPushButton(Confirmation)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Confirmation)

        QMetaObject.connectSlotsByName(Confirmation)
    # setupUi

    def retranslateUi(self, Confirmation):
        Confirmation.setWindowTitle(QCoreApplication.translate("Confirmation", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("Confirmation", u"Text", None))
        self.ok_btn.setText(QCoreApplication.translate("Confirmation", u"OK", None))
        self.cancel_btn.setText(QCoreApplication.translate("Confirmation", u"Cancel", None))
    # retranslateUi


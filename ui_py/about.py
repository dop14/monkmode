# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(318, 321)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.aboutFrame = QFrame(Form)
        self.aboutFrame.setObjectName(u"aboutFrame")
        self.aboutFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.aboutFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.aboutFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.about_text = QLabel(self.aboutFrame)
        self.about_text.setObjectName(u"about_text")
        font = QFont()
        font.setPointSize(12)
        self.about_text.setFont(font)

        self.verticalLayout_2.addWidget(self.about_text)


        self.verticalLayout.addWidget(self.aboutFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.about_text.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archive.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 150)
        Form.setMaximumSize(QSize(300, 200))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_label = QLabel(Form)
        self.main_label.setObjectName(u"main_label")
        font = QFont()
        font.setPointSize(14)
        self.main_label.setFont(font)

        self.verticalLayout_2.addWidget(self.main_label)

        self.archiveFrame = QFrame(Form)
        self.archiveFrame.setObjectName(u"archiveFrame")
        self.archiveFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.archiveFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.archiveFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.archived_combobox = QComboBox(self.archiveFrame)
        self.archived_combobox.setObjectName(u"archived_combobox")

        self.verticalLayout.addWidget(self.archived_combobox)


        self.verticalLayout_2.addWidget(self.archiveFrame)

        self.unarchive_btn = QPushButton(Form)
        self.unarchive_btn.setObjectName(u"unarchive_btn")
        self.unarchive_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.unarchive_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("Form", u"archived subjects", None))
        self.unarchive_btn.setText(QCoreApplication.translate("Form", u"unarchive", None))
    # retranslateUi


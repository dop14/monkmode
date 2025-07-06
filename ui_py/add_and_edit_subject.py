# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_and_edit_subject.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(249, 166)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_label = QLabel(Form)
        self.main_label.setObjectName(u"main_label")
        font = QFont()
        font.setPointSize(14)
        self.main_label.setFont(font)

        self.verticalLayout_2.addWidget(self.main_label)

        self.subject_frame = QFrame(Form)
        self.subject_frame.setObjectName(u"subject_frame")
        self.subject_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subject_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.subject_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.subject_name_label = QLabel(self.subject_frame)
        self.subject_name_label.setObjectName(u"subject_name_label")

        self.verticalLayout.addWidget(self.subject_name_label)

        self.subject_name_entry = QLineEdit(self.subject_frame)
        self.subject_name_entry.setObjectName(u"subject_name_entry")

        self.verticalLayout.addWidget(self.subject_name_entry)


        self.verticalLayout_2.addWidget(self.subject_frame)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout_2.addWidget(self.save_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("Form", u"create new subject", None))
        self.subject_name_label.setText(QCoreApplication.translate("Form", u"subject name", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"save", None))
    # retranslateUi


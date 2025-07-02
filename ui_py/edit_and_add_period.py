# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_and_add_period.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 347)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_label = QLabel(Form)
        self.main_label.setObjectName(u"main_label")
        font = QFont()
        font.setPointSize(16)
        self.main_label.setFont(font)

        self.verticalLayout_3.addWidget(self.main_label)

        self.focus_frame = QFrame(Form)
        self.focus_frame.setObjectName(u"focus_frame")
        self.focus_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.focus_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.focus_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.focus_name_label = QLabel(self.focus_frame)
        self.focus_name_label.setObjectName(u"focus_name_label")

        self.verticalLayout.addWidget(self.focus_name_label)

        self.focus_name_entry = QLineEdit(self.focus_frame)
        self.focus_name_entry.setObjectName(u"focus_name_entry")

        self.verticalLayout.addWidget(self.focus_name_entry)

        self.focus_time_label = QLabel(self.focus_frame)
        self.focus_time_label.setObjectName(u"focus_time_label")

        self.verticalLayout.addWidget(self.focus_time_label)

        self.focus_time_spinbox = QSpinBox(self.focus_frame)
        self.focus_time_spinbox.setObjectName(u"focus_time_spinbox")
        self.focus_time_spinbox.setMinimum(1)
        self.focus_time_spinbox.setMaximum(1000)

        self.verticalLayout.addWidget(self.focus_time_spinbox)


        self.verticalLayout_3.addWidget(self.focus_frame)

        self.short_break_frame = QFrame(Form)
        self.short_break_frame.setObjectName(u"short_break_frame")
        self.short_break_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.short_break_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.short_break_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.short_break_checkbox = QCheckBox(self.short_break_frame)
        self.short_break_checkbox.setObjectName(u"short_break_checkbox")

        self.horizontalLayout.addWidget(self.short_break_checkbox)

        self.short_break_spinbox = QSpinBox(self.short_break_frame)
        self.short_break_spinbox.setObjectName(u"short_break_spinbox")
        self.short_break_spinbox.setMinimum(1)
        self.short_break_spinbox.setMaximum(100)

        self.horizontalLayout.addWidget(self.short_break_spinbox)


        self.verticalLayout_3.addWidget(self.short_break_frame)

        self.long_break_frame = QFrame(Form)
        self.long_break_frame.setObjectName(u"long_break_frame")
        self.long_break_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.long_break_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.long_break_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.long_break_checkbox = QCheckBox(self.long_break_frame)
        self.long_break_checkbox.setObjectName(u"long_break_checkbox")

        self.horizontalLayout_2.addWidget(self.long_break_checkbox)

        self.long_break_spinbox = QSpinBox(self.long_break_frame)
        self.long_break_spinbox.setObjectName(u"long_break_spinbox")
        self.long_break_spinbox.setMinimum(1)
        self.long_break_spinbox.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.long_break_spinbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.long_break_after_label = QLabel(self.long_break_frame)
        self.long_break_after_label.setObjectName(u"long_break_after_label")

        self.verticalLayout_2.addWidget(self.long_break_after_label)

        self.long_break_after_spinbox = QSpinBox(self.long_break_frame)
        self.long_break_after_spinbox.setObjectName(u"long_break_after_spinbox")
        self.long_break_after_spinbox.setMinimum(2)
        self.long_break_after_spinbox.setMaximum(100)

        self.verticalLayout_2.addWidget(self.long_break_after_spinbox)


        self.verticalLayout_3.addWidget(self.long_break_frame)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout_3.addWidget(self.save_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("Form", u"create new focus period", None))
        self.focus_name_label.setText(QCoreApplication.translate("Form", u"focus period name", None))
        self.focus_time_label.setText(QCoreApplication.translate("Form", u"focus time", None))
        self.short_break_checkbox.setText(QCoreApplication.translate("Form", u"short break", None))
        self.long_break_checkbox.setText(QCoreApplication.translate("Form", u"long break", None))
        self.long_break_after_label.setText(QCoreApplication.translate("Form", u"long break after", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"save", None))
    # retranslateUi


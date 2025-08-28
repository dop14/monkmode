# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'focuswindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(320, 200))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.focusSetting = QFrame(Form)
        self.focusSetting.setObjectName(u"focusSetting")
        self.focusSetting.setMinimumSize(QSize(0, 0))
        self.focusSetting.setFrameShape(QFrame.Shape.StyledPanel)
        self.focusSetting.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.focusSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.session_label = QLabel(self.focusSetting)
        self.session_label.setObjectName(u"session_label")

        self.verticalLayout.addWidget(self.session_label)

        self.session_spinbox = QSpinBox(self.focusSetting)
        self.session_spinbox.setObjectName(u"session_spinbox")
        self.session_spinbox.setMinimum(1)

        self.verticalLayout.addWidget(self.session_spinbox)

        self.session_lenght_label = QLabel(self.focusSetting)
        self.session_lenght_label.setObjectName(u"session_lenght_label")

        self.verticalLayout.addWidget(self.session_lenght_label)


        self.verticalLayout_2.addWidget(self.focusSetting)

        self.start_focus_btn = QPushButton(Form)
        self.start_focus_btn.setObjectName(u"start_focus_btn")
        self.start_focus_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.start_focus_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.session_label.setText(QCoreApplication.translate("Form", u"Choose the number of sessions", None))
        self.session_lenght_label.setText(QCoreApplication.translate("Form", u"this will approximately take:", None))
        self.start_focus_btn.setText(QCoreApplication.translate("Form", u"start focus", None))
    # retranslateUi


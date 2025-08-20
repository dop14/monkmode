# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_default_weekly_focus.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

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

        self.changeweeklydefaultFrame = QFrame(Form)
        self.changeweeklydefaultFrame.setObjectName(u"changeweeklydefaultFrame")
        self.changeweeklydefaultFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.changeweeklydefaultFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.changeweeklydefaultFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.weekly_focus_goal_spinbox = QSpinBox(self.changeweeklydefaultFrame)
        self.weekly_focus_goal_spinbox.setObjectName(u"weekly_focus_goal_spinbox")
        self.weekly_focus_goal_spinbox.setMinimum(1)
        self.weekly_focus_goal_spinbox.setMaximum(168)

        self.horizontalLayout.addWidget(self.weekly_focus_goal_spinbox)

        self.hours_label = QLabel(self.changeweeklydefaultFrame)
        self.hours_label.setObjectName(u"hours_label")

        self.horizontalLayout.addWidget(self.hours_label)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.changeweeklydefaultFrame)

        self.save_btn = QPushButton(Form)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.save_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main_label.setText(QCoreApplication.translate("Form", u"change weekly focus goal", None))
        self.hours_label.setText(QCoreApplication.translate("Form", u"hours", None))
        self.save_btn.setText(QCoreApplication.translate("Form", u"save", None))
    # retranslateUi


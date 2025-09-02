# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(652, 725)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 620, 930))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.overallFrame = QFrame(self.scrollAreaWidgetContents)
        self.overallFrame.setObjectName(u"overallFrame")
        self.overallFrame.setMaximumSize(QSize(600, 300))
        self.overallFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.overallFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.overallFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.overallFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.focus_label = QLabel(self.overallFrame)
        self.focus_label.setObjectName(u"focus_label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.focus_label.setFont(font1)

        self.verticalLayout.addWidget(self.focus_label)

        self.total_focus_time = QLabel(self.overallFrame)
        self.total_focus_time.setObjectName(u"total_focus_time")

        self.verticalLayout.addWidget(self.total_focus_time)

        self.avarage_focus_time = QLabel(self.overallFrame)
        self.avarage_focus_time.setObjectName(u"avarage_focus_time")

        self.verticalLayout.addWidget(self.avarage_focus_time)

        self.longest_focus_session = QLabel(self.overallFrame)
        self.longest_focus_session.setObjectName(u"longest_focus_session")

        self.verticalLayout.addWidget(self.longest_focus_session)

        self.focus_sessions_completed = QLabel(self.overallFrame)
        self.focus_sessions_completed.setObjectName(u"focus_sessions_completed")

        self.verticalLayout.addWidget(self.focus_sessions_completed)

        self.streak_and_karma_label = QLabel(self.overallFrame)
        self.streak_and_karma_label.setObjectName(u"streak_and_karma_label")
        self.streak_and_karma_label.setFont(font1)

        self.verticalLayout.addWidget(self.streak_and_karma_label)

        self.daily_goal_achieved = QLabel(self.overallFrame)
        self.daily_goal_achieved.setObjectName(u"daily_goal_achieved")

        self.verticalLayout.addWidget(self.daily_goal_achieved)

        self.current_streak = QLabel(self.overallFrame)
        self.current_streak.setObjectName(u"current_streak")

        self.verticalLayout.addWidget(self.current_streak)

        self.longest_streak = QLabel(self.overallFrame)
        self.longest_streak.setObjectName(u"longest_streak")

        self.verticalLayout.addWidget(self.longest_streak)

        self.karma = QLabel(self.overallFrame)
        self.karma.setObjectName(u"karma")

        self.verticalLayout.addWidget(self.karma)

        self.karma_level = QLabel(self.overallFrame)
        self.karma_level.setObjectName(u"karma_level")

        self.verticalLayout.addWidget(self.karma_level)


        self.verticalLayout_2.addWidget(self.overallFrame)

        self.focusFrame = QFrame(self.scrollAreaWidgetContents)
        self.focusFrame.setObjectName(u"focusFrame")
        self.focusFrame.setMinimumSize(QSize(600, 300))
        self.focusFrame.setMaximumSize(QSize(600, 300))
        self.focusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.focusFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.focusFrame)

        self.subjectFrame = QFrame(self.scrollAreaWidgetContents)
        self.subjectFrame.setObjectName(u"subjectFrame")
        self.subjectFrame.setMinimumSize(QSize(600, 300))
        self.subjectFrame.setMaximumSize(QSize(600, 300))
        self.subjectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.subjectFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Overall statistics", None))
        self.focus_label.setText(QCoreApplication.translate("Form", u"Focus", None))
        self.total_focus_time.setText(QCoreApplication.translate("Form", u"total focus time:", None))
        self.avarage_focus_time.setText(QCoreApplication.translate("Form", u"avarage focus time:", None))
        self.longest_focus_session.setText(QCoreApplication.translate("Form", u"longest focus session:", None))
        self.focus_sessions_completed.setText(QCoreApplication.translate("Form", u"focus sessions completed:", None))
        self.streak_and_karma_label.setText(QCoreApplication.translate("Form", u"Streak & Karma", None))
        self.daily_goal_achieved.setText(QCoreApplication.translate("Form", u"daily goal achieved:", None))
        self.current_streak.setText(QCoreApplication.translate("Form", u"current streak:", None))
        self.longest_streak.setText(QCoreApplication.translate("Form", u"longest streak:", None))
        self.karma.setText(QCoreApplication.translate("Form", u"karma:", None))
        self.karma_level.setText(QCoreApplication.translate("Form", u"karma level:", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(655, 725)
        Form.setMinimumSize(QSize(650, 725))
        Form.setMaximumSize(QSize(655, 725))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 623, 2196))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.overallFrame = QFrame(self.scrollAreaWidgetContents)
        self.overallFrame.setObjectName(u"overallFrame")
        self.overallFrame.setMaximumSize(QSize(600, 420))
        self.overallFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.overallFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.overallFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.focus_label = QLabel(self.overallFrame)
        self.focus_label.setObjectName(u"focus_label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.focus_label.setFont(font)

        self.verticalLayout_2.addWidget(self.focus_label)

        self.total_focus_time = QLabel(self.overallFrame)
        self.total_focus_time.setObjectName(u"total_focus_time")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.total_focus_time.setFont(font1)

        self.verticalLayout_2.addWidget(self.total_focus_time)

        self.avg_daily_focus = QLabel(self.overallFrame)
        self.avg_daily_focus.setObjectName(u"avg_daily_focus")
        font2 = QFont()
        font2.setPointSize(10)
        self.avg_daily_focus.setFont(font2)

        self.verticalLayout_2.addWidget(self.avg_daily_focus)

        self.avg_weekly_focus = QLabel(self.overallFrame)
        self.avg_weekly_focus.setObjectName(u"avg_weekly_focus")
        self.avg_weekly_focus.setFont(font2)

        self.verticalLayout_2.addWidget(self.avg_weekly_focus)

        self.focus_sessions_completed = QLabel(self.overallFrame)
        self.focus_sessions_completed.setObjectName(u"focus_sessions_completed")
        self.focus_sessions_completed.setFont(font2)

        self.verticalLayout_2.addWidget(self.focus_sessions_completed)

        self.longest_focus_session = QLabel(self.overallFrame)
        self.longest_focus_session.setObjectName(u"longest_focus_session")
        self.longest_focus_session.setFont(font2)

        self.verticalLayout_2.addWidget(self.longest_focus_session)

        self.highest_daily_label = QLabel(self.overallFrame)
        self.highest_daily_label.setObjectName(u"highest_daily_label")
        self.highest_daily_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.highest_daily_label)

        self.highest_weekly_label = QLabel(self.overallFrame)
        self.highest_weekly_label.setObjectName(u"highest_weekly_label")
        self.highest_weekly_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.highest_weekly_label)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.streak_and_karma_label = QLabel(self.overallFrame)
        self.streak_and_karma_label.setObjectName(u"streak_and_karma_label")
        self.streak_and_karma_label.setFont(font)

        self.verticalLayout_10.addWidget(self.streak_and_karma_label)

        self.daily_goal_achieved = QLabel(self.overallFrame)
        self.daily_goal_achieved.setObjectName(u"daily_goal_achieved")
        self.daily_goal_achieved.setFont(font2)

        self.verticalLayout_10.addWidget(self.daily_goal_achieved)

        self.current_streak = QLabel(self.overallFrame)
        self.current_streak.setObjectName(u"current_streak")
        self.current_streak.setFont(font2)

        self.verticalLayout_10.addWidget(self.current_streak)

        self.longest_streak = QLabel(self.overallFrame)
        self.longest_streak.setObjectName(u"longest_streak")
        self.longest_streak.setFont(font2)

        self.verticalLayout_10.addWidget(self.longest_streak)

        self.karma = QLabel(self.overallFrame)
        self.karma.setObjectName(u"karma")
        self.karma.setFont(font2)

        self.verticalLayout_10.addWidget(self.karma)

        self.karma_level = QLabel(self.overallFrame)
        self.karma_level.setObjectName(u"karma_level")
        self.karma_level.setFont(font2)

        self.verticalLayout_10.addWidget(self.karma_level)


        self.horizontalLayout.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addWidget(self.overallFrame)

        self.no_data_message = QLabel(self.scrollAreaWidgetContents)
        self.no_data_message.setObjectName(u"no_data_message")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.no_data_message.setFont(font3)

        self.verticalLayout_11.addWidget(self.no_data_message, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer)

        self.focusFrame = QFrame(self.scrollAreaWidgetContents)
        self.focusFrame.setObjectName(u"focusFrame")
        self.focusFrame.setMinimumSize(QSize(600, 300))
        self.focusFrame.setMaximumSize(QSize(600, 300))
        self.focusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.focusFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.focusFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_2)

        self.subjectFrame = QFrame(self.scrollAreaWidgetContents)
        self.subjectFrame.setObjectName(u"subjectFrame")
        self.subjectFrame.setMinimumSize(QSize(600, 300))
        self.subjectFrame.setMaximumSize(QSize(600, 300))
        self.subjectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.subjectFrame)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_3)

        self.periodFrame = QFrame(self.scrollAreaWidgetContents)
        self.periodFrame.setObjectName(u"periodFrame")
        self.periodFrame.setMinimumSize(QSize(600, 300))
        self.periodFrame.setMaximumSize(QSize(600, 300))
        self.periodFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.periodFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.periodFrame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_4)

        self.subjectBarFrame = QFrame(self.scrollAreaWidgetContents)
        self.subjectBarFrame.setObjectName(u"subjectBarFrame")
        self.subjectBarFrame.setMinimumSize(QSize(600, 420))
        self.subjectBarFrame.setMaximumSize(QSize(600, 420))
        self.subjectBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectBarFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.subjectBarFrame)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_5)

        self.include_archived_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.include_archived_checkbox.setObjectName(u"include_archived_checkbox")
        font4 = QFont()
        font4.setPointSize(11)
        self.include_archived_checkbox.setFont(font4)
        self.include_archived_checkbox.setChecked(True)

        self.verticalLayout_11.addWidget(self.include_archived_checkbox)

        self.subjectAllBarFrame = QFrame(self.scrollAreaWidgetContents)
        self.subjectAllBarFrame.setObjectName(u"subjectAllBarFrame")
        self.subjectAllBarFrame.setMinimumSize(QSize(600, 420))
        self.subjectAllBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectAllBarFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.subjectAllBarFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.focus_label.setText(QCoreApplication.translate("Form", u"Focus", None))
        self.total_focus_time.setText(QCoreApplication.translate("Form", u"total focus time:", None))
        self.avg_daily_focus.setText(QCoreApplication.translate("Form", u"avg. daily focus:", None))
        self.avg_weekly_focus.setText(QCoreApplication.translate("Form", u"avg. weekly focus:", None))
        self.focus_sessions_completed.setText(QCoreApplication.translate("Form", u"focus sessions completed:", None))
        self.longest_focus_session.setText(QCoreApplication.translate("Form", u"longest focus session:", None))
        self.highest_daily_label.setText(QCoreApplication.translate("Form", u"highest daily focus:", None))
        self.highest_weekly_label.setText(QCoreApplication.translate("Form", u"highest weekly focus:", None))
        self.streak_and_karma_label.setText(QCoreApplication.translate("Form", u"Streak & Karma", None))
        self.daily_goal_achieved.setText(QCoreApplication.translate("Form", u"daily goal achieved:", None))
        self.current_streak.setText(QCoreApplication.translate("Form", u"current streak:", None))
        self.longest_streak.setText(QCoreApplication.translate("Form", u"longest streak:", None))
        self.karma.setText(QCoreApplication.translate("Form", u"karma:", None))
        self.karma_level.setText(QCoreApplication.translate("Form", u"karma level:", None))
        self.no_data_message.setText("")
        self.include_archived_checkbox.setText(QCoreApplication.translate("Form", u"include archived subjects", None))
    # retranslateUi


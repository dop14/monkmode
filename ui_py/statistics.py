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
        Form.resize(663, 658)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(40, 30, 571, 611))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 609))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.focus_label = QLabel(self.frame)
        self.focus_label.setObjectName(u"focus_label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.focus_label.setFont(font1)

        self.verticalLayout.addWidget(self.focus_label)

        self.total_focus_time = QLabel(self.frame)
        self.total_focus_time.setObjectName(u"total_focus_time")

        self.verticalLayout.addWidget(self.total_focus_time)

        self.avarage_focus_time = QLabel(self.frame)
        self.avarage_focus_time.setObjectName(u"avarage_focus_time")

        self.verticalLayout.addWidget(self.avarage_focus_time)

        self.longest_focus_session = QLabel(self.frame)
        self.longest_focus_session.setObjectName(u"longest_focus_session")

        self.verticalLayout.addWidget(self.longest_focus_session)

        self.focus_sessions_completed = QLabel(self.frame)
        self.focus_sessions_completed.setObjectName(u"focus_sessions_completed")

        self.verticalLayout.addWidget(self.focus_sessions_completed)

        self.streak_and_karma_label = QLabel(self.frame)
        self.streak_and_karma_label.setObjectName(u"streak_and_karma_label")
        self.streak_and_karma_label.setFont(font1)

        self.verticalLayout.addWidget(self.streak_and_karma_label)

        self.daily_goal_achieved = QLabel(self.frame)
        self.daily_goal_achieved.setObjectName(u"daily_goal_achieved")

        self.verticalLayout.addWidget(self.daily_goal_achieved)

        self.current_streak = QLabel(self.frame)
        self.current_streak.setObjectName(u"current_streak")

        self.verticalLayout.addWidget(self.current_streak)

        self.longest_streak = QLabel(self.frame)
        self.longest_streak.setObjectName(u"longest_streak")

        self.verticalLayout.addWidget(self.longest_streak)

        self.karma = QLabel(self.frame)
        self.karma.setObjectName(u"karma")

        self.verticalLayout.addWidget(self.karma)

        self.karma_level = QLabel(self.frame)
        self.karma_level.setObjectName(u"karma_level")

        self.verticalLayout.addWidget(self.karma_level)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

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
        self.label_7.setText(QCoreApplication.translate("Form", u"Focus time", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Subjects", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Heatmap history", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 943)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.actiondaily_goal = QAction(MainWindow)
        self.actiondaily_goal.setObjectName(u"actiondaily_goal")
        self.actiondark = QAction(MainWindow)
        self.actiondark.setObjectName(u"actiondark")
        self.actionlight = QAction(MainWindow)
        self.actionlight.setObjectName(u"actionlight")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionabout_2 = QAction(MainWindow)
        self.actionabout_2.setObjectName(u"actionabout_2")
        self.actionweekdays_only = QAction(MainWindow)
        self.actionweekdays_only.setObjectName(u"actionweekdays_only")
        self.actionwhole_week = QAction(MainWindow)
        self.actionwhole_week.setObjectName(u"actionwhole_week")
        self.actionnotify_when_session_starts = QAction(MainWindow)
        self.actionnotify_when_session_starts.setObjectName(u"actionnotify_when_session_starts")
        self.actionnotify_when_session_ends = QAction(MainWindow)
        self.actionnotify_when_session_ends.setObjectName(u"actionnotify_when_session_ends")
        self.actionview_focus_history = QAction(MainWindow)
        self.actionview_focus_history.setObjectName(u"actionview_focus_history")
        self.actionexport_data = QAction(MainWindow)
        self.actionexport_data.setObjectName(u"actionexport_data")
        self.actionclear_history = QAction(MainWindow)
        self.actionclear_history.setObjectName(u"actionclear_history")
        self.actionfocus_period = QAction(MainWindow)
        self.actionfocus_period.setObjectName(u"actionfocus_period")
        self.actionfocus_subject = QAction(MainWindow)
        self.actionfocus_subject.setObjectName(u"actionfocus_subject")
        self.mainLayout = QWidget(MainWindow)
        self.mainLayout.setObjectName(u"mainLayout")
        self.label = QLabel(self.mainLayout)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 50, 218, 58))
        font = QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self.mainLayout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 110, 351, 482))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.focusFrame = QFrame(self.layoutWidget)
        self.focusFrame.setObjectName(u"focusFrame")
        self.focusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.focusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.focusFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.timer_label = QLabel(self.focusFrame)
        self.timer_label.setObjectName(u"timer_label")
        font1 = QFont()
        font1.setPointSize(30)
        self.timer_label.setFont(font1)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.timer_label)

        self.start_focus_btn = QPushButton(self.focusFrame)
        self.start_focus_btn.setObjectName(u"start_focus_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_focus_btn.sizePolicy().hasHeightForWidth())
        self.start_focus_btn.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(18)
        self.start_focus_btn.setFont(font2)

        self.verticalLayout_3.addWidget(self.start_focus_btn)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.focus_pause_btn = QPushButton(self.focusFrame)
        self.focus_pause_btn.setObjectName(u"focus_pause_btn")
        self.focus_pause_btn.setEnabled(True)
        font3 = QFont()
        font3.setKerning(True)
        self.focus_pause_btn.setFont(font3)

        self.horizontalLayout_3.addWidget(self.focus_pause_btn)

        self.focus_stop_btn = QPushButton(self.focusFrame)
        self.focus_stop_btn.setObjectName(u"focus_stop_btn")

        self.horizontalLayout_3.addWidget(self.focus_stop_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_10.addWidget(self.focusFrame)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.periodFrame = QFrame(self.layoutWidget)
        self.periodFrame.setObjectName(u"periodFrame")
        self.periodFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.periodFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.periodFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.period_label = QLabel(self.periodFrame)
        self.period_label.setObjectName(u"period_label")
        font4 = QFont()
        font4.setPointSize(16)
        self.period_label.setFont(font4)

        self.verticalLayout_4.addWidget(self.period_label)

        self.period_combobox = QComboBox(self.periodFrame)
        self.period_combobox.addItem("")
        self.period_combobox.setObjectName(u"period_combobox")

        self.verticalLayout_4.addWidget(self.period_combobox)

        self.editperiod_btn = QPushButton(self.periodFrame)
        self.editperiod_btn.setObjectName(u"editperiod_btn")

        self.verticalLayout_4.addWidget(self.editperiod_btn)

        self.newperiod_btn = QPushButton(self.periodFrame)
        self.newperiod_btn.setObjectName(u"newperiod_btn")

        self.verticalLayout_4.addWidget(self.newperiod_btn)


        self.verticalLayout_8.addWidget(self.periodFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_2)

        self.dailyFrame = QFrame(self.layoutWidget)
        self.dailyFrame.setObjectName(u"dailyFrame")
        self.dailyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dailyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dailyFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.daily_label = QLabel(self.dailyFrame)
        self.daily_label.setObjectName(u"daily_label")
        self.daily_label.setFont(font4)

        self.verticalLayout_5.addWidget(self.daily_label)

        self.today_label = QLabel(self.dailyFrame)
        self.today_label.setObjectName(u"today_label")

        self.verticalLayout_5.addWidget(self.today_label)

        self.daily_goal_label = QLabel(self.dailyFrame)
        self.daily_goal_label.setObjectName(u"daily_goal_label")

        self.verticalLayout_5.addWidget(self.daily_goal_label)

        self.daily_progression_bar = QProgressBar(self.dailyFrame)
        self.daily_progression_bar.setObjectName(u"daily_progression_bar")
        self.daily_progression_bar.setValue(24)

        self.verticalLayout_5.addWidget(self.daily_progression_bar)


        self.verticalLayout_8.addWidget(self.dailyFrame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.subjectFrame = QFrame(self.layoutWidget)
        self.subjectFrame.setObjectName(u"subjectFrame")
        self.subjectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.subjectFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.subject_label = QLabel(self.subjectFrame)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setFont(font4)

        self.verticalLayout_6.addWidget(self.subject_label)

        self.subject_combobox = QComboBox(self.subjectFrame)
        self.subject_combobox.addItem("")
        self.subject_combobox.setObjectName(u"subject_combobox")

        self.verticalLayout_6.addWidget(self.subject_combobox)

        self.edit_subject_btn = QPushButton(self.subjectFrame)
        self.edit_subject_btn.setObjectName(u"edit_subject_btn")

        self.verticalLayout_6.addWidget(self.edit_subject_btn)

        self.newsubject_btn = QPushButton(self.subjectFrame)
        self.newsubject_btn.setObjectName(u"newsubject_btn")

        self.verticalLayout_6.addWidget(self.newsubject_btn)


        self.verticalLayout_9.addWidget(self.subjectFrame)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_3)

        self.weeklyFrame = QFrame(self.layoutWidget)
        self.weeklyFrame.setObjectName(u"weeklyFrame")
        self.weeklyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.weeklyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.weeklyFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.weekly_label = QLabel(self.weeklyFrame)
        self.weekly_label.setObjectName(u"weekly_label")
        self.weekly_label.setFont(font4)

        self.verticalLayout_7.addWidget(self.weekly_label)

        self.weekly_focus_label = QLabel(self.weeklyFrame)
        self.weekly_focus_label.setObjectName(u"weekly_focus_label")

        self.verticalLayout_7.addWidget(self.weekly_focus_label)

        self.weekly_goal_label = QLabel(self.weeklyFrame)
        self.weekly_goal_label.setObjectName(u"weekly_goal_label")

        self.verticalLayout_7.addWidget(self.weekly_goal_label)

        self.weekly_progression_bar = QProgressBar(self.weeklyFrame)
        self.weekly_progression_bar.setObjectName(u"weekly_progression_bar")
        self.weekly_progression_bar.setValue(24)

        self.verticalLayout_7.addWidget(self.weekly_progression_bar)


        self.verticalLayout_9.addWidget(self.weeklyFrame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.mainLayout)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuchange_default = QMenu(self.menuSettings)
        self.menuchange_default.setObjectName(u"menuchange_default")
        self.menutheme = QMenu(self.menuSettings)
        self.menutheme.setObjectName(u"menutheme")
        self.menuset_week = QMenu(self.menuSettings)
        self.menuset_week.setObjectName(u"menuset_week")
        self.menunotifications = QMenu(self.menuSettings)
        self.menunotifications.setObjectName(u"menunotifications")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        self.menuhistory = QMenu(self.menubar)
        self.menuhistory.setObjectName(u"menuhistory")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuhistory.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menuSettings.addAction(self.menuchange_default.menuAction())
        self.menuSettings.addAction(self.menuset_week.menuAction())
        self.menuSettings.addAction(self.menunotifications.menuAction())
        self.menuSettings.addAction(self.menutheme.menuAction())
        self.menuchange_default.addAction(self.actiondaily_goal)
        self.menuchange_default.addAction(self.actionfocus_period)
        self.menuchange_default.addAction(self.actionfocus_subject)
        self.menutheme.addAction(self.actiondark)
        self.menutheme.addAction(self.actionlight)
        self.menuset_week.addAction(self.actionweekdays_only)
        self.menuset_week.addAction(self.actionwhole_week)
        self.menunotifications.addAction(self.actionnotify_when_session_starts)
        self.menunotifications.addAction(self.actionnotify_when_session_ends)
        self.menuabout.addAction(self.actionabout)
        self.menuabout.addAction(self.actionabout_2)
        self.menuhistory.addAction(self.actionview_focus_history)
        self.menuhistory.addAction(self.actionexport_data)
        self.menuhistory.addAction(self.actionclear_history)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondaily_goal.setText(QCoreApplication.translate("MainWindow", u"daily focus goal", None))
        self.actiondark.setText(QCoreApplication.translate("MainWindow", u"dark", None))
        self.actionlight.setText(QCoreApplication.translate("MainWindow", u"light", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"how to use", None))
        self.actionabout_2.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.actionweekdays_only.setText(QCoreApplication.translate("MainWindow", u"weekdays only", None))
        self.actionwhole_week.setText(QCoreApplication.translate("MainWindow", u"whole week", None))
        self.actionnotify_when_session_starts.setText(QCoreApplication.translate("MainWindow", u"notify when session starts", None))
        self.actionnotify_when_session_ends.setText(QCoreApplication.translate("MainWindow", u"notify when session ends", None))
        self.actionview_focus_history.setText(QCoreApplication.translate("MainWindow", u"view focus history", None))
        self.actionexport_data.setText(QCoreApplication.translate("MainWindow", u"export data", None))
        self.actionclear_history.setText(QCoreApplication.translate("MainWindow", u"clear history", None))
        self.actionfocus_period.setText(QCoreApplication.translate("MainWindow", u"focus period", None))
        self.actionfocus_subject.setText(QCoreApplication.translate("MainWindow", u"focus subject", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"monkmode", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"25:00", None))
        self.start_focus_btn.setText(QCoreApplication.translate("MainWindow", u"focus", None))
        self.focus_pause_btn.setText(QCoreApplication.translate("MainWindow", u"pause/start", None))
        self.focus_stop_btn.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.period_label.setText(QCoreApplication.translate("MainWindow", u"focus period", None))
        self.period_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"pomodoro", None))

        self.editperiod_btn.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.newperiod_btn.setText(QCoreApplication.translate("MainWindow", u"create new period", None))
        self.daily_label.setText(QCoreApplication.translate("MainWindow", u"daily focus", None))
        self.today_label.setText(QCoreApplication.translate("MainWindow", u"today's focus:", None))
        self.daily_goal_label.setText(QCoreApplication.translate("MainWindow", u"daily focus goal:", None))
        self.subject_label.setText(QCoreApplication.translate("MainWindow", u"subject", None))
        self.subject_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"study", None))

        self.edit_subject_btn.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.newsubject_btn.setText(QCoreApplication.translate("MainWindow", u"create new subject", None))
        self.weekly_label.setText(QCoreApplication.translate("MainWindow", u"weekly focus", None))
        self.weekly_focus_label.setText(QCoreApplication.translate("MainWindow", u"this week's focus:", None))
        self.weekly_goal_label.setText(QCoreApplication.translate("MainWindow", u"weekly focus goal:", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"settings", None))
        self.menuchange_default.setTitle(QCoreApplication.translate("MainWindow", u"change default", None))
        self.menutheme.setTitle(QCoreApplication.translate("MainWindow", u"theme", None))
        self.menuset_week.setTitle(QCoreApplication.translate("MainWindow", u"set week", None))
        self.menunotifications.setTitle(QCoreApplication.translate("MainWindow", u"notifications", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.menuhistory.setTitle(QCoreApplication.translate("MainWindow", u"history", None))
    # retranslateUi


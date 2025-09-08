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
        MainWindow.resize(530, 745)
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
        self.actiondark.setCheckable(True)
        self.actionlight = QAction(MainWindow)
        self.actionlight.setObjectName(u"actionlight")
        self.actionlight.setCheckable(True)
        self.actionhowtouse = QAction(MainWindow)
        self.actionhowtouse.setObjectName(u"actionhowtouse")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionweekdays_only = QAction(MainWindow)
        self.actionweekdays_only.setObjectName(u"actionweekdays_only")
        self.actionweekdays_only.setCheckable(True)
        self.actionweekdays_only.setChecked(False)
        self.actionwhole_week = QAction(MainWindow)
        self.actionwhole_week.setObjectName(u"actionwhole_week")
        self.actionwhole_week.setCheckable(True)
        self.all_notifications = QAction(MainWindow)
        self.all_notifications.setObjectName(u"all_notifications")
        self.all_notifications.setCheckable(True)
        self.sound_break_start = QAction(MainWindow)
        self.sound_break_start.setObjectName(u"sound_break_start")
        self.sound_break_start.setCheckable(True)
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
        self.popup_focus_start = QAction(MainWindow)
        self.popup_focus_start.setObjectName(u"popup_focus_start")
        self.popup_focus_start.setCheckable(True)
        self.sound_focus_start = QAction(MainWindow)
        self.sound_focus_start.setObjectName(u"sound_focus_start")
        self.sound_focus_start.setCheckable(True)
        self.actiontips = QAction(MainWindow)
        self.actiontips.setObjectName(u"actiontips")
        self.actiontips.setCheckable(True)
        self.actiondaily_quotes = QAction(MainWindow)
        self.actiondaily_quotes.setObjectName(u"actiondaily_quotes")
        self.actiondaily_quotes.setCheckable(True)
        self.actionplay_sound_when_focus_completed = QAction(MainWindow)
        self.actionplay_sound_when_focus_completed.setObjectName(u"actionplay_sound_when_focus_completed")
        self.actionsounds = QAction(MainWindow)
        self.actionsounds.setObjectName(u"actionsounds")
        self.actionplay_sound_when_break_starts = QAction(MainWindow)
        self.actionplay_sound_when_break_starts.setObjectName(u"actionplay_sound_when_break_starts")
        self.actionplay_sound_when_focus_completed_2 = QAction(MainWindow)
        self.actionplay_sound_when_focus_completed_2.setObjectName(u"actionplay_sound_when_focus_completed_2")
        self.actionnotify_when_focus_session_starts = QAction(MainWindow)
        self.actionnotify_when_focus_session_starts.setObjectName(u"actionnotify_when_focus_session_starts")
        self.actionfocus_start = QAction(MainWindow)
        self.actionfocus_start.setObjectName(u"actionfocus_start")
        self.actionfocus_start.setCheckable(True)
        self.actionbreak_start = QAction(MainWindow)
        self.actionbreak_start.setObjectName(u"actionbreak_start")
        self.actionbreak_start.setCheckable(True)
        self.actionfocus_completed = QAction(MainWindow)
        self.actionfocus_completed.setObjectName(u"actionfocus_completed")
        self.actionfocus_completed.setCheckable(True)
        self.actionfocus_session_starts_popup = QAction(MainWindow)
        self.actionfocus_session_starts_popup.setObjectName(u"actionfocus_session_starts_popup")
        self.actionfocus_session_starts_popup.setCheckable(True)
        self.action_break_starts_popup = QAction(MainWindow)
        self.action_break_starts_popup.setObjectName(u"action_break_starts_popup")
        self.action_break_starts_popup.setCheckable(True)
        self.actionfocus_completed_popup = QAction(MainWindow)
        self.actionfocus_completed_popup.setObjectName(u"actionfocus_completed_popup")
        self.actionfocus_completed_popup.setCheckable(True)
        self.actiontips_and_quotes = QAction(MainWindow)
        self.actiontips_and_quotes.setObjectName(u"actiontips_and_quotes")
        self.actiontips_and_quotes.setCheckable(True)
        self.actionCOMING_SOON = QAction(MainWindow)
        self.actionCOMING_SOON.setObjectName(u"actionCOMING_SOON")
        self.actionCOMING_SOON_2 = QAction(MainWindow)
        self.actionCOMING_SOON_2.setObjectName(u"actionCOMING_SOON_2")
        self.actionCOMING_SOON_3 = QAction(MainWindow)
        self.actionCOMING_SOON_3.setObjectName(u"actionCOMING_SOON_3")
        self.actionCOMING_SOON_4 = QAction(MainWindow)
        self.actionCOMING_SOON_4.setObjectName(u"actionCOMING_SOON_4")
        self.actionreset_settings_to_default = QAction(MainWindow)
        self.actionreset_settings_to_default.setObjectName(u"actionreset_settings_to_default")
        self.actionshow_streaks = QAction(MainWindow)
        self.actionshow_streaks.setObjectName(u"actionshow_streaks")
        self.actionshow_streaks.setCheckable(True)
        self.all_notifications_2 = QAction(MainWindow)
        self.all_notifications_2.setObjectName(u"all_notifications_2")
        self.all_notifications_2.setCheckable(True)
        self.actionview_archived_subjects = QAction(MainWindow)
        self.actionview_archived_subjects.setObjectName(u"actionview_archived_subjects")
        self.actionweekly_focus_goal = QAction(MainWindow)
        self.actionweekly_focus_goal.setObjectName(u"actionweekly_focus_goal")
        self.mainLayout = QWidget(MainWindow)
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalLayout_10 = QVBoxLayout(self.mainLayout)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.focusFrame = QFrame(self.mainLayout)
        self.focusFrame.setObjectName(u"focusFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.focusFrame.sizePolicy().hasHeightForWidth())
        self.focusFrame.setSizePolicy(sizePolicy1)
        self.focusFrame.setMinimumSize(QSize(490, 150))
        self.focusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.focusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.focusFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.small_focus_window = QPushButton(self.focusFrame)
        self.small_focus_window.setObjectName(u"small_focus_window")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.small_focus_window.sizePolicy().hasHeightForWidth())
        self.small_focus_window.setSizePolicy(sizePolicy2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowNew))
        self.small_focus_window.setIcon(icon)

        self.verticalLayout_3.addWidget(self.small_focus_window, 0, Qt.AlignmentFlag.AlignRight)

        self.timer_label = QLabel(self.focusFrame)
        self.timer_label.setObjectName(u"timer_label")
        font = QFont()
        font.setPointSize(36)
        font.setBold(False)
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.timer_label)

        self.period_type_label = QLabel(self.focusFrame)
        self.period_type_label.setObjectName(u"period_type_label")

        self.verticalLayout_3.addWidget(self.period_type_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.start_focus_btn = QPushButton(self.focusFrame)
        self.start_focus_btn.setObjectName(u"start_focus_btn")
        sizePolicy2.setHeightForWidth(self.start_focus_btn.sizePolicy().hasHeightForWidth())
        self.start_focus_btn.setSizePolicy(sizePolicy2)
        self.start_focus_btn.setMinimumSize(QSize(200, 65))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.start_focus_btn.setFont(font1)

        self.verticalLayout_3.addWidget(self.start_focus_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.focus_pause_btn = QPushButton(self.focusFrame)
        self.focus_pause_btn.setObjectName(u"focus_pause_btn")
        self.focus_pause_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.focus_pause_btn.sizePolicy().hasHeightForWidth())
        self.focus_pause_btn.setSizePolicy(sizePolicy2)
        self.focus_pause_btn.setMinimumSize(QSize(60, 0))
        font2 = QFont()
        font2.setKerning(True)
        self.focus_pause_btn.setFont(font2)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.focus_pause_btn.setIcon(icon1)
        self.focus_pause_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.focus_pause_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.focus_resume_btn = QPushButton(self.focusFrame)
        self.focus_resume_btn.setObjectName(u"focus_resume_btn")
        sizePolicy2.setHeightForWidth(self.focus_resume_btn.sizePolicy().hasHeightForWidth())
        self.focus_resume_btn.setSizePolicy(sizePolicy2)
        self.focus_resume_btn.setMinimumSize(QSize(60, 0))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.focus_resume_btn.setIcon(icon2)
        self.focus_resume_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.focus_resume_btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.focus_stop_btn = QPushButton(self.focusFrame)
        self.focus_stop_btn.setObjectName(u"focus_stop_btn")
        sizePolicy2.setHeightForWidth(self.focus_stop_btn.sizePolicy().hasHeightForWidth())
        self.focus_stop_btn.setSizePolicy(sizePolicy2)
        self.focus_stop_btn.setMinimumSize(QSize(60, 0))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.focus_stop_btn.setIcon(icon3)
        self.focus_stop_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.focus_stop_btn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.focusFrame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.periodFrame = QFrame(self.mainLayout)
        self.periodFrame.setObjectName(u"periodFrame")
        sizePolicy2.setHeightForWidth(self.periodFrame.sizePolicy().hasHeightForWidth())
        self.periodFrame.setSizePolicy(sizePolicy2)
        self.periodFrame.setMinimumSize(QSize(230, 140))
        self.periodFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.periodFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.periodFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.period_label = QLabel(self.periodFrame)
        self.period_label.setObjectName(u"period_label")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.period_label.setFont(font3)

        self.verticalLayout.addWidget(self.period_label)

        self.period_combobox = QComboBox(self.periodFrame)
        self.period_combobox.setObjectName(u"period_combobox")
        font4 = QFont()
        font4.setPointSize(11)
        self.period_combobox.setFont(font4)

        self.verticalLayout.addWidget(self.period_combobox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.newperiod_btn = QPushButton(self.periodFrame)
        self.newperiod_btn.setObjectName(u"newperiod_btn")
        sizePolicy1.setHeightForWidth(self.newperiod_btn.sizePolicy().hasHeightForWidth())
        self.newperiod_btn.setSizePolicy(sizePolicy1)
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.newperiod_btn.setIcon(icon4)

        self.horizontalLayout.addWidget(self.newperiod_btn)

        self.editperiod_btn = QPushButton(self.periodFrame)
        self.editperiod_btn.setObjectName(u"editperiod_btn")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.editperiod_btn.setIcon(icon5)

        self.horizontalLayout.addWidget(self.editperiod_btn)

        self.delete_period_btn = QPushButton(self.periodFrame)
        self.delete_period_btn.setObjectName(u"delete_period_btn")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.delete_period_btn.setIcon(icon6)

        self.horizontalLayout.addWidget(self.delete_period_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addWidget(self.periodFrame)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.dailyFrame = QFrame(self.mainLayout)
        self.dailyFrame.setObjectName(u"dailyFrame")
        sizePolicy2.setHeightForWidth(self.dailyFrame.sizePolicy().hasHeightForWidth())
        self.dailyFrame.setSizePolicy(sizePolicy2)
        self.dailyFrame.setMinimumSize(QSize(230, 140))
        self.dailyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dailyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dailyFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.daily_label = QLabel(self.dailyFrame)
        self.daily_label.setObjectName(u"daily_label")
        self.daily_label.setFont(font3)

        self.verticalLayout_5.addWidget(self.daily_label)

        self.today_label = QLabel(self.dailyFrame)
        self.today_label.setObjectName(u"today_label")
        font5 = QFont()
        font5.setPointSize(10)
        self.today_label.setFont(font5)

        self.verticalLayout_5.addWidget(self.today_label)

        self.daily_goal_label = QLabel(self.dailyFrame)
        self.daily_goal_label.setObjectName(u"daily_goal_label")
        self.daily_goal_label.setFont(font5)

        self.verticalLayout_5.addWidget(self.daily_goal_label)

        self.daily_progression_bar = QProgressBar(self.dailyFrame)
        self.daily_progression_bar.setObjectName(u"daily_progression_bar")
        self.daily_progression_bar.setValue(24)

        self.verticalLayout_5.addWidget(self.daily_progression_bar)


        self.verticalLayout_8.addWidget(self.dailyFrame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.subjectFrame = QFrame(self.mainLayout)
        self.subjectFrame.setObjectName(u"subjectFrame")
        sizePolicy2.setHeightForWidth(self.subjectFrame.sizePolicy().hasHeightForWidth())
        self.subjectFrame.setSizePolicy(sizePolicy2)
        self.subjectFrame.setMinimumSize(QSize(239, 140))
        self.subjectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.subjectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.subjectFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subject_label = QLabel(self.subjectFrame)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setFont(font3)

        self.verticalLayout_2.addWidget(self.subject_label)

        self.subject_combobox = QComboBox(self.subjectFrame)
        self.subject_combobox.setObjectName(u"subject_combobox")
        self.subject_combobox.setFont(font4)

        self.verticalLayout_2.addWidget(self.subject_combobox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newsubject_btn = QPushButton(self.subjectFrame)
        self.newsubject_btn.setObjectName(u"newsubject_btn")
        self.newsubject_btn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.newsubject_btn)

        self.edit_subject_btn = QPushButton(self.subjectFrame)
        self.edit_subject_btn.setObjectName(u"edit_subject_btn")
        self.edit_subject_btn.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.edit_subject_btn)

        self.archive_subject_btn = QPushButton(self.subjectFrame)
        self.archive_subject_btn.setObjectName(u"archive_subject_btn")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.archive_subject_btn.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.archive_subject_btn)

        self.delete_subject_btn = QPushButton(self.subjectFrame)
        self.delete_subject_btn.setObjectName(u"delete_subject_btn")
        self.delete_subject_btn.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.delete_subject_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_9.addWidget(self.subjectFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.statsFrame = QFrame(self.mainLayout)
        self.statsFrame.setObjectName(u"statsFrame")
        sizePolicy2.setHeightForWidth(self.statsFrame.sizePolicy().hasHeightForWidth())
        self.statsFrame.setSizePolicy(sizePolicy2)
        self.statsFrame.setMinimumSize(QSize(239, 140))
        self.statsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.statsFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stats_label = QLabel(self.statsFrame)
        self.stats_label.setObjectName(u"stats_label")
        self.stats_label.setFont(font3)

        self.verticalLayout_7.addWidget(self.stats_label, 0, Qt.AlignmentFlag.AlignTop)

        self.this_week_focus = QLabel(self.statsFrame)
        self.this_week_focus.setObjectName(u"this_week_focus")
        self.this_week_focus.setFont(font5)

        self.verticalLayout_7.addWidget(self.this_week_focus)

        self.current_streak_label = QLabel(self.statsFrame)
        self.current_streak_label.setObjectName(u"current_streak_label")
        self.current_streak_label.setFont(font5)

        self.verticalLayout_7.addWidget(self.current_streak_label)

        self.show_all = QPushButton(self.statsFrame)
        self.show_all.setObjectName(u"show_all")

        self.verticalLayout_7.addWidget(self.show_all)


        self.verticalLayout_9.addWidget(self.statsFrame)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.horizontalSpacer_2)

        self.quoteFrame = QFrame(self.mainLayout)
        self.quoteFrame.setObjectName(u"quoteFrame")
        sizePolicy2.setHeightForWidth(self.quoteFrame.sizePolicy().hasHeightForWidth())
        self.quoteFrame.setSizePolicy(sizePolicy2)
        self.quoteFrame.setMinimumSize(QSize(300, 0))
        self.quoteFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.quoteFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.quoteFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.quote_label = QLabel(self.quoteFrame)
        self.quote_label.setObjectName(u"quote_label")
        sizePolicy2.setHeightForWidth(self.quote_label.sizePolicy().hasHeightForWidth())
        self.quote_label.setSizePolicy(sizePolicy2)
        self.quote_label.setMinimumSize(QSize(0, 0))
        self.quote_label.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(9)
        self.quote_label.setFont(font6)
        self.quote_label.setWordWrap(True)
        self.quote_label.setMargin(0)

        self.verticalLayout_4.addWidget(self.quote_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_10.addWidget(self.quoteFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.mainLayout)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuchange_default = QMenu(self.menuSettings)
        self.menuchange_default.setObjectName(u"menuchange_default")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        self.menuarchive = QMenu(self.menubar)
        self.menuarchive.setObjectName(u"menuarchive")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuarchive.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menuSettings.addAction(self.menuchange_default.menuAction())
        self.menuSettings.addAction(self.actiontips_and_quotes)
        self.menuSettings.addAction(self.all_notifications_2)
        self.menuchange_default.addAction(self.actiondaily_goal)
        self.menuchange_default.addAction(self.actionfocus_period)
        self.menuchange_default.addAction(self.actionfocus_subject)
        self.menuabout.addAction(self.actionabout)
        self.menuabout.addAction(self.actionhowtouse)
        self.menuabout.addSeparator()
        self.menuarchive.addAction(self.actionview_archived_subjects)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondaily_goal.setText(QCoreApplication.translate("MainWindow", u"daily focus goal", None))
        self.actiondark.setText(QCoreApplication.translate("MainWindow", u"dark", None))
        self.actionlight.setText(QCoreApplication.translate("MainWindow", u"light", None))
        self.actionhowtouse.setText(QCoreApplication.translate("MainWindow", u"how to use", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.actionweekdays_only.setText(QCoreApplication.translate("MainWindow", u"weekdays only", None))
        self.actionwhole_week.setText(QCoreApplication.translate("MainWindow", u"whole week", None))
        self.all_notifications.setText(QCoreApplication.translate("MainWindow", u"turn off all notifications", None))
        self.sound_break_start.setText(QCoreApplication.translate("MainWindow", u"play sound when focus period starts", None))
        self.actionview_focus_history.setText(QCoreApplication.translate("MainWindow", u"view focus history", None))
        self.actionexport_data.setText(QCoreApplication.translate("MainWindow", u"export data", None))
        self.actionclear_history.setText(QCoreApplication.translate("MainWindow", u"clear focus history", None))
        self.actionfocus_period.setText(QCoreApplication.translate("MainWindow", u"focus period", None))
        self.actionfocus_subject.setText(QCoreApplication.translate("MainWindow", u"focus subject", None))
        self.popup_focus_start.setText(QCoreApplication.translate("MainWindow", u"notify when focus period starts", None))
        self.sound_focus_start.setText(QCoreApplication.translate("MainWindow", u"notify when break period starts", None))
        self.actiontips.setText(QCoreApplication.translate("MainWindow", u"tips", None))
        self.actiondaily_quotes.setText(QCoreApplication.translate("MainWindow", u"daily quotes", None))
        self.actionplay_sound_when_focus_completed.setText(QCoreApplication.translate("MainWindow", u"play sound when focus completed", None))
        self.actionsounds.setText(QCoreApplication.translate("MainWindow", u"play sound when focus session starts", None))
        self.actionplay_sound_when_break_starts.setText(QCoreApplication.translate("MainWindow", u"play sound when break starts", None))
        self.actionplay_sound_when_focus_completed_2.setText(QCoreApplication.translate("MainWindow", u"play sound when focus completed", None))
        self.actionnotify_when_focus_session_starts.setText(QCoreApplication.translate("MainWindow", u"notify when focus session starts", None))
        self.actionfocus_start.setText(QCoreApplication.translate("MainWindow", u"focus session starts", None))
        self.actionbreak_start.setText(QCoreApplication.translate("MainWindow", u"break starts", None))
        self.actionfocus_completed.setText(QCoreApplication.translate("MainWindow", u"focus completed", None))
        self.actionfocus_session_starts_popup.setText(QCoreApplication.translate("MainWindow", u"focus session starts", None))
        self.action_break_starts_popup.setText(QCoreApplication.translate("MainWindow", u"break starts", None))
        self.actionfocus_completed_popup.setText(QCoreApplication.translate("MainWindow", u"focus completed", None))
        self.actiontips_and_quotes.setText(QCoreApplication.translate("MainWindow", u"show daily quote", None))
        self.actionCOMING_SOON.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.actionCOMING_SOON_2.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.actionCOMING_SOON_3.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.actionCOMING_SOON_4.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.actionreset_settings_to_default.setText(QCoreApplication.translate("MainWindow", u"reset settings to default", None))
        self.actionshow_streaks.setText(QCoreApplication.translate("MainWindow", u"show streaks", None))
        self.all_notifications_2.setText(QCoreApplication.translate("MainWindow", u"turn off focus notifications", None))
        self.actionview_archived_subjects.setText(QCoreApplication.translate("MainWindow", u"view archived subjects", None))
        self.actionweekly_focus_goal.setText(QCoreApplication.translate("MainWindow", u"weekly focus goal", None))
        self.small_focus_window.setText("")
        self.timer_label.setText("")
        self.period_type_label.setText("")
        self.start_focus_btn.setText(QCoreApplication.translate("MainWindow", u"focus", None))
        self.focus_pause_btn.setText("")
        self.focus_resume_btn.setText("")
        self.focus_stop_btn.setText("")
        self.period_label.setText(QCoreApplication.translate("MainWindow", u"focus period", None))
        self.newperiod_btn.setText("")
        self.editperiod_btn.setText("")
        self.delete_period_btn.setText("")
        self.daily_label.setText(QCoreApplication.translate("MainWindow", u"daily focus", None))
        self.today_label.setText(QCoreApplication.translate("MainWindow", u"today's focus:", None))
        self.daily_goal_label.setText(QCoreApplication.translate("MainWindow", u"daily focus goal:", None))
        self.subject_label.setText(QCoreApplication.translate("MainWindow", u"subject", None))
        self.newsubject_btn.setText("")
        self.edit_subject_btn.setText("")
        self.archive_subject_btn.setText("")
        self.delete_subject_btn.setText("")
        self.stats_label.setText(QCoreApplication.translate("MainWindow", u"statistics", None))
        self.this_week_focus.setText(QCoreApplication.translate("MainWindow", u"this week's focus:", None))
        self.current_streak_label.setText(QCoreApplication.translate("MainWindow", u"current streak:", None))
        self.show_all.setText(QCoreApplication.translate("MainWindow", u"show all", None))
        self.quote_label.setText("")
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"settings", None))
        self.menuchange_default.setTitle(QCoreApplication.translate("MainWindow", u"change default", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
        self.menuarchive.setTitle(QCoreApplication.translate("MainWindow", u"archive", None))
    # retranslateUi


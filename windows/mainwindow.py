from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl, Qt, QTimer
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
from windows.edit_period_window import EditPeriodWindow
from windows.confirmation_window import ConfirmationWindow
from windows.new_subject_window import NewSubjectWindow
from windows.edit_subject_window import EditSubjectWindow
from windows.change_default import ChangeDefault
from windows.small_focus_window import SmallFocusWindow
from windows.about import AboutWindow
from windows.statistics import Statistics
from core.popup_notification import PopupNotification
from core.timer import FocusTimer
from core.menu_bar import MenuBar
from core.icons import IconManager
from database.db_manager import get_period_names, get_subject_names, get_current_streak, save_daily_goal, get_user_stats, update_user_stats
from database.db_manager import get_default_period_name, get_default_subject_name, get_user_preferences, get_today_focus, get_this_week_focus, get_today_quote, check_streak_log
from utils import get_db_path
import requests
import shutil, os

class MainWindow(QMainWindow):
    APP_VERSION = "v1.2.1"

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)
        self.setWindowTitle("monkmode")
        self.adjustSize()  
        self.showNormal()

        self.is_timer_active = False
        self.is_delay_timer = False

        self.setup_ui()

    def setup_ui(self):
        # Create windows and managers
        self.small_window = SmallFocusWindow(self)
        self.icons = IconManager()
        
        # Create menubar and theme
        preferences = get_user_preferences()
        self.menubar = MenuBar(preferences, self, self.small_window, self.icons)
        self.theme = self.menubar.theme_name
        
        # Apply theme dependent icons
        if (self.menubar.theme_name == "monkmode_light"):
            self.icons.build("black")
            self.icons.apply_icons(self, self.small_window)
        else:
            self.icons.build("white")
            self.icons.apply_icons(self, self.small_window)

        # Check for updates after a small delay
        QTimer.singleShot(1500, self.check_latest_release)

        # Initalize streak data
        check_streak_log()
        self.check_longest_streak()
        self.show_streak()
        
        # Initialize UI state
        self.hide_buttons()
        self.update_period_combobox()
        self.update_subject_combobox()
        self.update_daily_focus()
        self.update_weekly_focus()
        self.update_progression_bar()
        self.load_today_quote()
        self.update_daily_focus_goal()

        # Connecting buttons to actions
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)
        
        self.ui.newperiod_btn.clicked.connect(lambda:self.start_add_window("period"))
        self.ui.editperiod_btn.clicked.connect(lambda:self.start_edit_window("period"))
        self.ui.delete_period_btn.clicked.connect(lambda:self.start_delete_window("period"))

        self.ui.newsubject_btn.clicked.connect(lambda:self.start_add_window("subject"))
        self.ui.edit_subject_btn.clicked.connect(lambda:self.start_edit_window("subject"))
        self.ui.archive_subject_btn.clicked.connect(lambda:self.start_archive_window())
        self.ui.delete_subject_btn.clicked.connect(lambda:self.start_delete_window("subject"))

        self.ui.focus_stop_btn.clicked.connect(self.stop_focus_confirmation)
        self.ui.small_focus_window.clicked.connect(self.start_small_focus_window)

        # Tooltips
        self.ui.newperiod_btn.setToolTip("create new period")
        self.ui.editperiod_btn.setToolTip("edit period")
        self.ui.delete_period_btn.setToolTip("delete period")
        self.ui.newsubject_btn.setToolTip("create new subject")
        self.ui.edit_subject_btn.setToolTip("edit subject")
        self.ui.archive_subject_btn.setToolTip("archive subject")
        self.ui.delete_subject_btn.setToolTip("delete subject")
        self.ui.focus_stop_btn.setToolTip("stop focus")
        self.ui.focus_pause_btn.setToolTip("pause focus")
        self.ui.focus_resume_btn.setToolTip("resume focus")
        self.ui.small_focus_window.setToolTip("small view")

        # Menu actions
        self.ui.actiondaily_goal.triggered.connect(self.menubar.change_default_daily)
        self.ui.actionfocus_period.triggered.connect(lambda:self.start_change_default_window("period"))
        self.ui.actionfocus_subject.triggered.connect(lambda:self.start_change_default_window("subject"))
        self.ui.all_notifications_2.triggered.connect(self.menubar.all_notifications_clicked)
        self.ui.actionview_archived_subjects.triggered.connect(self.menubar.archive_clicked)
        self.ui.actiontips_and_quotes.triggered.connect(self.menubar.tips_and_quotes_clicked)
        self.ui.show_all.clicked.connect(self.start_statistics_window)
        self.ui.actionabout.triggered.connect(self.start_about_window)
        self.ui.actionhowtouse.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/dop14/monkmode")))

        # Theme switching
        self.ui.monkmode_dark.triggered.connect(lambda: self.menubar.change_theme("monkmode_dark"))
        self.ui.monkmode_light.triggered.connect(lambda: self.menubar.change_theme("monkmode_light"))
        self.ui.focus_fire.triggered.connect(lambda: self.menubar.change_theme("focus_fire"))
        self.ui.zen_garden.triggered.connect(lambda: self.menubar.change_theme("zen_garden"))
        self.ui.deep_focus.triggered.connect(lambda: self.menubar.change_theme("deep_focus"))
        self.ui.dawn_ritual.triggered.connect(lambda: self.menubar.change_theme("dawn_ritual"))

    def closeEvent(self, event):
        # If no timer is active
        if self.is_timer_active == False:
            reply = QMessageBox.question(
                self,
                "quit",
                "Are you sure you want to quit?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                self.backup_db()
                event.accept()  
            else:
                event.ignore() 
        # If timer is active
        else:
            self.focus_timer.stop()
            reply = QMessageBox.question(
                self,
                "quit",
                "Are you sure you want to quit while in focus?<br>This will save, but end your current progress.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
                )

            if reply == QMessageBox.Yes:
                if self.is_delay_timer == True:
                    event.accept()
                # Save the data
                else:
                    self.focus_timer.save_focus_stopped_session()
                    self.focus_ended()
                    self.backup_db()
                    event.accept()

            elif reply == QMessageBox.No:
                # If delay timer is currently active
                if self.is_delay_timer == True:
                    event.ignore()
                else:
                    self.focus_timer.resume()
                    event.ignore()

    def start_focus_window(self):
        self.focus_window = FocusWindow(self)
        self.focus_window.exec()

    def start_add_window(self, type):
        if type == "period":
            self.add_window = NewPeriodWindow(self)
            self.add_window.exec()
        elif type == "subject":
            self.add_window = NewSubjectWindow(self)
            self.add_window.exec()

    def start_edit_window(self, type):
        if type == "period":
            self.edit_window = EditPeriodWindow(self)
            self.edit_window.exec()
        elif type == "subject":
            self.edit_window = EditSubjectWindow(self)
            self.edit_window.exec()

    def start_delete_window(self, setting_type):
        if setting_type == "period":
            if self.ui.period_combobox.currentText() == self.default_period_name:
                self.error_window = ConfirmationWindow(self,"The default focus setting cannot be deleted.", setting_type)
                self.error_window.exec()
            else:
                self.del_window = ConfirmationWindow(self, f"Do you really want to delete <b>{self.ui.period_combobox.currentText()}</b> focus period setting?<br>This action cannot be undone.", setting_type)
                self.del_window.exec()

        elif setting_type == "subject":
            if self.ui.subject_combobox.currentText() == self.default_subject_name:
                self.error_window = ConfirmationWindow(self, "The default subject cannot be deleted.", setting_type)
                self.error_window.exec()
            else:
                self.del_window = ConfirmationWindow(self, f"Do you really want to delete <b>{self.ui.subject_combobox.currentText()}</b> subject?<br>If you might use it later, use <b>archive</b> instead of <b>delete</b>.<br>This action cannot be undone.", setting_type)
                self.del_window.exec()

    def start_archive_window(self):
        if self.ui.subject_combobox.currentText() == self.default_subject_name:
            self.error_window = ConfirmationWindow(self,"The default subject cannot be archived.", "archive_subject")
            self.error_window.exec()
        else:
            self.del_window = ConfirmationWindow(self, f"Do you really want to archive <b>{self.ui.subject_combobox.currentText()}</b> subject?<br>You can unarchive it later.", "archive_subject")
            self.del_window.exec()

    def start_change_default_window(self, setting_type):
        if setting_type == "period":
            self.change_def_window = ChangeDefault(self, "period")
            self.change_def_window.exec()
        elif setting_type == "subject":
            self.change_def_window = ChangeDefault(self, "subject")
            self.change_def_window.exec()

    def start_small_focus_window(self):
        self.small_window.show()
        self.showMinimized()

    def start_statistics_window(self):
        self.statistics_window = Statistics(self)
        self.statistics_window.exec()

    def start_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def check_latest_release(self):
        try:
            response = requests.get("https://api.github.com/repos/dop14/monkmode/releases/latest", timeout=5)
            response.raise_for_status()
            data = response.json()
            latest_version = data["tag_name"]
        
            if latest_version != MainWindow.APP_VERSION:

                self.notification = PopupNotification(f"monkmode {latest_version} is now available!<br><a href='https://github.com/dop14/monkmode/releases/latest'>Download update</a>",10000)
                self.notification.show_notification()

        except requests.exceptions.RequestException as e:
            print("Version API failed:", e)

    def start_timer(self, period, subject, user_sessions):
        self.is_timer_active = True

        # Set UI
        self.ui.start_focus_btn.hide()
        self.ui.timer_label.show()
        self.ui.focus_pause_btn.show()
        self.ui.focus_stop_btn.show()
        self.ui.small_focus_window.show()
        self.disable_and_enable_gui(True)
        
        # Create and start the timer
        self.focus_timer = FocusTimer(period, subject, user_sessions, self, self.small_window)

        # Connect buttons to actions
        self.ui.focus_pause_btn.clicked.connect(self.focus_timer.pause)
        self.ui.focus_resume_btn.clicked.connect(self.focus_timer.resume)
    
    def stop_focus_confirmation(self):
        self.focus_timer.stop()

        reply = QMessageBox.question(
            self,
            "stopping focus session",
            "Are you sure you want stop the focus session?<br>This will save, but end your current progress.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.focus_timer.save_focus_stopped_session()
            self.small_window.default_values()
            self.focus_ended()

        elif reply == QMessageBox.No:
            self.focus_timer.resume()

    def disable_and_enable_gui(self, bool_value):
        self.ui.periodFrame.setDisabled(bool_value)
        self.ui.subjectFrame.setDisabled(bool_value)
        self.ui.dailyFrame.setDisabled(bool_value)
        self.ui.statsFrame.setDisabled(bool_value)
        self.ui.menubar.setDisabled(bool_value)
        self.ui.quoteFrame.setDisabled(bool_value)

    def hide_buttons(self):
        self.ui.timer_label.hide()
        self.ui.focus_pause_btn.hide()
        self.ui.focus_stop_btn.hide()
        self.ui.focus_resume_btn.hide()
        self.ui.period_type_label.hide()
        self.ui.small_focus_window.hide()

    def focus_ended(self):
        self.is_timer_active = False

        # Set UI
        self.small_window.focus_over()
        self.hide_buttons()
        self.ui.timer_label.setText("")
        self.ui.start_focus_btn.show()
        self.preferences = get_user_preferences()
        if self.preferences["tips_and_quotes"] == True:
            self.ui.quote_label.show()
        self.ui.start_focus_btn.setDisabled(False)
        self.disable_and_enable_gui(False)

        # Update focus values
        self.update_focus()
        self.check_daily_goal()
        self.show_streak()

    def update_daily_focus_goal(self):
        preferences = get_user_preferences()
        self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")
        self.update_progression_bar()

    def update_progression_bar(self):
        preferences = get_user_preferences()

        focus_goal_minutes = preferences["default_daily_focus_goal"] * 60
        today_focus_minutes = get_today_focus() / 60
        self.daily_progress = int((today_focus_minutes / focus_goal_minutes) * 100)
        self.daily_progress = min(self.daily_progress,100)
        self.ui.daily_progression_bar.setValue(self.daily_progress)
    
    def update_daily_focus(self):
        today_focus = get_today_focus()
        today_focus_minutes = 0
        if today_focus == 0:
            self.ui.today_label.setText(f"today's focus: <b>0 minutes</b>")
        elif today_focus < 3600:
            today_focus_minutes = int(today_focus / 60)
            self.ui.today_label.setText(f"today's focus: <b>{today_focus_minutes} minutes</b>")
        else:
            hours = today_focus // 3600
            minutes = (today_focus % 3600) // 60
            if minutes == 0:
                self.ui.today_label.setText(f"today's focus: <b>{hours} hours</b>")
            else:
                self.ui.today_label.setText(f"today's focus: <b>{hours} hours {minutes} minutes</b>")
        
    def update_weekly_focus(self):
        current_week_focus = get_this_week_focus()
        if current_week_focus < 3600:
            current_week_focus_minutes = int(current_week_focus / 60)
            self.ui.this_week_focus.setText(f"this week's focus:<b> {current_week_focus_minutes} minutes</b>")
        else:
            hours = current_week_focus // 3600
            minutes = (current_week_focus % 3600) // 60
            if minutes == 0:
                self.ui.this_week_focus.setText(f"this week's focus:<b> {hours} hours </b>")
            else:
                self.ui.this_week_focus.setText(f"this week's focus:<b> {hours} hours {minutes} minutes</b>")
    
    def show_streak(self):
        current_streak = get_current_streak()
        self.ui.current_streak_label.setText(f"current streak: <b>{current_streak} days</b>")

    def check_longest_streak(self):
        current_streak = get_current_streak()
        user_stats = get_user_stats()
        longest_streak = user_stats[3]

        if current_streak > longest_streak:
            new_stats = {
                        "total_focus_time_mins": user_stats[0],
                        "focus_sessions_completed": user_stats[1],
                        "longest_focus_session": user_stats[2],
                        "longest_streak": current_streak
                    }
            update_user_stats(new_stats)

    def check_daily_goal(self):
        if self.daily_progress == 100:
            save_daily_goal()
            self.check_longest_streak()

    def update_focus(self):
        self.update_daily_focus()
        self.update_weekly_focus()
        self.update_progression_bar()

    def update_period_combobox(self):
        # Load all period settings into combobox
        periods = get_period_names()
        self.ui.period_combobox.addItems(periods)

        # Set default period setting
        self.default_period_name = get_default_period_name()
        period_index = self.ui.period_combobox.findText(self.default_period_name)
        if period_index != -1:
            self.ui.period_combobox.setCurrentIndex(period_index)
    
    def update_subject_combobox(self):
        # Load all subject settings into combobox
        subjects = get_subject_names()
        self.ui.subject_combobox.addItems(subjects)

        # Set default subject setting
        self.default_subject_name = get_default_subject_name()
        subject_index = self.ui.subject_combobox.findText(self.default_subject_name)
        if subject_index != -1:
            self.ui.subject_combobox.setCurrentIndex(subject_index)

    def load_today_quote(self):
        preferences = get_user_preferences()
        if preferences["tips_and_quotes"] == 1:
            self.ui.quoteFrame.show()
            quote, author = get_today_quote()
            self.ui.quote_label.setAlignment(Qt.AlignCenter)
            self.ui.quote_label.setText(f"\"<i>{quote}</i>\"<br>— {author}")
        else:
            self.ui.quoteFrame.hide()

    def backup_db(self):
        db_path = get_db_path() 
        
        if not os.path.exists(db_path):
            print(f"No database found at {db_path}, skipping backup.")
            return
        
        # Create backup in the same folder as the database
        backup_folder = os.path.dirname(db_path) 
        backup_path = os.path.join(backup_folder, "monkmode_backup.db")
        
        try:
            shutil.copy(db_path, backup_path)
            print(f"Backup created: {backup_path}")
        except Exception as e:
            print(f"Failed to backup database: {e}")

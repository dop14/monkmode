from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
from windows.edit_period_window import EditPeriodWindow
from windows.confirmation_window import ConfirmationWindow
from windows.new_subject_window import NewSubjectWindow
from windows.edit_subject_window import EditSubjectWindow
from windows.change_default import ChangeDefault
from windows.small_focus_window import SmallFocusWindow
from windows.statistics import Statistics
from PySide6.QtGui import QIcon
import datetime
from core.timer import FocusTimer
from core.menu_bar import MenuBar
from core.thememanager import ThemeManager
from database.db_manager import get_period_names, get_subject_names, get_current_streak, save_daily_goal, get_user_stats, update_user_stats
from database.db_manager import get_default_period_name, get_default_subject_name, get_user_preferences, get_today_focus, get_this_week_focus, get_today_quote, check_streak_log
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)
        self.setWindowTitle("monkmode")

        self.small_window = SmallFocusWindow(self)
        self.showNormal()
        self.is_timer_active = False
        self.is_delay_timer = False

        # Check the streak_log
        check_streak_log()

        # Check the longest_streak
        self.check_longest_streak()

        # Show streak
        self.show_streak()

        # Hide buttons
        self.hide_buttons()
        
        # Load period combobox values
        self.update_period_combobox()

        # Load subject combobox values
        self.update_subject_combobox()

        # Load user preferences
        preferences = get_user_preferences()
        self.menubar = MenuBar(preferences, self)

        # Load today's focus and this week's focus
        self.update_daily_focus()

        # Load weekly and monthly focus
        self.update_weekly_monthly_focus()

        # Load daily and weekly progression bar
        self.update_progression_bar()
        
        # Load today's quote
        self.load_today_quote()

        # Load daily focus goal
        self.update_daily_focus_goal()

        # When focus button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)
        
        # When add period button is clicked
        self.ui.newperiod_btn.clicked.connect(lambda:self.start_add_window("period"))
        self.ui.newperiod_btn.setToolTip("create new period")

        # When edit period button is clicked
        self.ui.editperiod_btn.clicked.connect(lambda:self.start_edit_window("period"))
        self.ui.editperiod_btn.setToolTip("edit period")

        # When delete period button is clicked
        self.ui.delete_period_btn.clicked.connect(lambda:self.start_delete_window("period"))
        self.ui.delete_period_btn.setToolTip("delete period")

        # When add subject button is clicked
        self.ui.newsubject_btn.clicked.connect(lambda:self.start_add_window("subject"))
        self.ui.newsubject_btn.setToolTip("create new subject")

        # When edit subject button is clicked
        self.ui.edit_subject_btn.clicked.connect(lambda:self.start_edit_window("subject"))
        self.ui.edit_subject_btn.setToolTip("edit subject")

        # When archive subject button is clicked
        self.ui.archive_subject_btn.clicked.connect(lambda:self.start_archive_window("subject"))
        self.ui.archive_subject_btn.setToolTip("archive subject")

        # When delete subject button is clicked
        self.ui.delete_subject_btn.clicked.connect(lambda:self.start_delete_window("subject"))
        self.ui.delete_subject_btn.setToolTip("delete subject")

        # If stop button is clicked
        self.ui.focus_stop_btn.clicked.connect(self.stop_focus_confirmation)

        # If small focus window button is clicked
        self.ui.small_focus_window.clicked.connect(self.start_small_focus_window)

        # Tooltips for focus buttons
        self.ui.focus_stop_btn.setToolTip("stop focus")
        self.ui.focus_pause_btn.setToolTip("pause focus")
        self.ui.focus_resume_btn.setToolTip("resume focus")
        self.ui.small_focus_window.setToolTip("small view")

        # When change default daily focus button is clicked
        self.ui.actiondaily_goal.triggered.connect(self.menubar.change_default_daily)

        # When change default period button is clicked
        self.ui.actionfocus_period.triggered.connect(lambda:self.start_change_default_window("period"))

        # When change default subject is clicked
        self.ui.actionfocus_subject.triggered.connect(lambda:self.start_change_default_window("subject"))

        # When turn off notifications clicked
        self.ui.all_notifications_2.triggered.connect(self.menubar.all_notifications_clicked)

        # When view archived button is clicked
        self.ui.actionview_archived_subjects.triggered.connect(self.menubar.archive_clicked)

        # When tips and quotes button is clicked
        self.ui.actiontips_and_quotes.triggered.connect(self.menubar.tips_and_quotes_clicked)

        # When show all statistics button is clicked
        self.ui.show_all.clicked.connect(self.start_statistics_window)
    
    # If app is closed
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
        # If the a period setting is being deleted
        if setting_type == "period":
            # If the chosen element is the default one
            if self.ui.period_combobox.currentText() == self.default_period_name:
                self.error_window = ConfirmationWindow(self,"The default focus setting cannot be deleted.",setting_type)
                self.error_window.exec()
            # Else if deletable
            else:
                self.del_window = ConfirmationWindow(self,f"Do you really want to delete <b>{self.ui.period_combobox.currentText()}</b> focus period setting?<br>This action cannot be undone.",setting_type)
                self.del_window.exec()
        # Else if a subject setting is being deleted
        elif setting_type == "subject":
            # If the chosen element is the default one
            if self.ui.subject_combobox.currentText() == self.default_subject_name:
                self.error_window = ConfirmationWindow(self,"The default subject cannot be deleted.",setting_type)
                self.error_window.exec()
            # Else if deletable
            else:
                self.del_window = ConfirmationWindow(self,f"Do you really want to delete <b>{self.ui.subject_combobox.currentText()}</b> subject?<br>If you might use it later, use <b>archive</b> instead of <b>delete</b>.<br>This action cannot be undone.",setting_type)
                self.del_window.exec()

    def start_archive_window(self, setting_type):
        if self.ui.subject_combobox.currentText() == self.default_subject_name:
            self.error_window = ConfirmationWindow(self,"The default subject cannot be archived.","archive_subject")
            self.error_window.exec()
            # Else if deletable
        else:
            self.del_window = ConfirmationWindow(self,f"Do you really want to archive <b>{self.ui.subject_combobox.currentText()}</b> subject?<br>You can unarchive it later.","archive_subject")
            self.del_window.exec()

    # Change default subject or period window
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
    
    # Starting timer
    def start_timer(self, period, subject, user_sessions):
        # Timer is active
        self.is_timer_active = True

        # Hide button
        self.ui.start_focus_btn.hide()

        # Show buttons
        self.ui.timer_label.show()
        self.ui.focus_pause_btn.show()
        self.ui.focus_stop_btn.show()
        self.ui.small_focus_window.show()

        # Disable things on mainwindow
        self.disable_and_enable_gui(True)

        # Create FocusTimer
        self.focus_timer = FocusTimer(period, subject, user_sessions, self, self.small_window)

        # If pause button clicked
        self.ui.focus_pause_btn.clicked.connect(self.focus_timer.pause)

        # If resume button is clicked
        self.ui.focus_resume_btn.clicked.connect(self.focus_timer.resume)
    
    # Confirmation for stopping the focus
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
            # Save the data
            self.focus_timer.save_focus_stopped_session()
            
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
        # Timer is inactive
        self.is_timer_active = False

        # Hide timer label, pause/resume and stop
        self.hide_buttons()

        # Clear timer_label
        self.ui.timer_label.setText("")

        # Show focus button
        self.ui.start_focus_btn.show()

        self.preferences = get_user_preferences()
        if self.preferences["tips_and_quotes"] == True:
            self.ui.quote_label.show()

        # Enable GUI
        self.disable_and_enable_gui(False)

        # Update focus times
        self.update_focus()

        # Check if daily goal was achieved
        self.check_daily_goal()

    # Update the daily and weekly focus goal if the user changes the default values
    def update_daily_focus_goal(self):
        preferences = get_user_preferences()

        self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")

        self.update_progression_bar()

    # Update the progression bars
    def update_progression_bar(self):
        preferences = get_user_preferences()

        focus_goal_minutes = preferences["default_daily_focus_goal"] * 60
        today_focus_minutes = get_today_focus() / 60
        self.daily_progress = int((today_focus_minutes / focus_goal_minutes) * 100)
        self.daily_progress = min(self.daily_progress,100)
        self.ui.daily_progression_bar.setValue(self.daily_progress)
    
    def update_daily_focus(self):
         # Load today's focus
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
        
    def update_weekly_monthly_focus(self):
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

        user_stats = get_user_stats()
        longest_streak = user_stats[3]

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

            
    # Update the daily, weekly, monthly focus if user finished a focus session
    def update_focus(self):
        # update focus labels
        self.update_daily_focus()

        # update weekly and monthly focus
        self.update_weekly_monthly_focus()

        # update progression bar
        self.update_progression_bar()

    # Update period combobox values
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
            quote, author = get_today_quote()
            self.ui.quote_label.setText(f"\"<i>{quote}</i>\"<br>— {author}")
            self.ui.quoteFrame.show()
        else:
            self.ui.quoteFrame.hide()

# Application entry point
def main():
    app = QApplication(sys.argv)
    app.setPalette(ThemeManager.load_dark_palette())
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon("logo/monkmode.png"))
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
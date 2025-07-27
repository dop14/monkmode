from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
from windows.edit_period_window import EditPeriodWindow
from windows.confirmation_window import ConfirmationWindow
from windows.new_subject_window import NewSubjectWindow
from windows.edit_subject_window import EditSubjectWindow
from windows.change_default import ChangeDefault
import datetime
from core.timer import FocusTimer
from core.menu_bar import MenuBar
from core.thememanager import ThemeManager
from database.db_manager import get_period_names, get_subject_names
from database.db_manager import get_default_period_name, get_default_subject_name, get_user_preferences, get_today_focus, get_this_week_focus, get_today_quote
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)
        self.setWindowTitle("monkmode")

        self.is_timer_active = False

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
        self.update_daily_weekly_focus()

        # Load daily and weekly progression bar
        self.update_progression_bar()
        
        # Load today's quote
        self.load_today_quote()

        # Load daily focus goal
        # If weekdays only
        if preferences["week_mode"] == "weekdays":
            today = datetime.date.today()
            # And if its a weekend
            if today.weekday() >= 5:
                # Set goal to 0 hours
                self.ui.daily_goal_label.setText("daily focus goal: <b>0 hours</b>")
            # else if not weekend
            else:
                # set to default
                self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")
        # Else set to default
        else:
            self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")

        # Load weekly focus
        if preferences["week_mode"] == "weekdays":
            self.week_mode = 5
        else:
            self.week_mode = 7
        weekly_goal = preferences["default_daily_focus_goal"] * self.week_mode
        self.ui.weekly_goal_label.setText(f"weekly focus goal: <b>{weekly_goal} hours</b>")

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

        # Tooltips for focus buttons
        self.ui.focus_stop_btn.setToolTip("stop focus")
        self.ui.focus_pause_btn.setToolTip("pause focus")
        self.ui.focus_resume_btn.setToolTip("resume focus")

        # When change default daily focus button is clicked
        self.ui.actiondaily_goal.triggered.connect(self.menubar.change_default_daily)

        # When change default period button is clicked
        self.ui.actionfocus_period.triggered.connect(lambda:self.start_change_default_window("period"))

        # When change default subject is clicked
        self.ui.actionfocus_subject.triggered.connect(lambda:self.start_change_default_window("subject"))

        # When weekdays only clicked
        self.ui.actionweekdays_only.triggered.connect(self.menubar.change_to_weekdays)
        
        # When whole week clicked
        self.ui.actionwhole_week.triggered.connect(self.menubar.change_to_wholeweek)

        # When turn off notifications clicked
        self.ui.all_notifications_2.triggered.connect(self.menubar.all_notifications_clicked)

        # When view archived button is clicked
        self.ui.actionview_archived_subjects.triggered.connect(self.menubar.archive_clicked)

        # When tips and quotes button is clicked
        self.ui.actiontips_and_quotes.triggered.connect(self.menubar.tips_and_quotes_clicked)
    
    # If app is closed
    def closeEvent(self, event):
        # If no timer is active
        if self.is_timer_active == False:
            reply = QMessageBox.question(
                self,
                "Quit",
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
                "Quit",
                "Are you sure you want to quit while in focus?<br>This will save, but end your current progress.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
                )

            if reply == QMessageBox.Yes:
                # Save the data
                self.focus_timer.save_focus_stopped_session()
                event.accept()

            elif reply == QMessageBox.No:
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
    
    # Starting timer
    def start_timer(self, period, subject, user_sessions):
        # Timer is active
        self.is_timer_active = True

        # Hide button
        self.ui.start_focus_btn.hide()
        self.ui.quote_label.hide()

        # Show buttons
        self.ui.timer_label.show()
        self.ui.focus_pause_btn.show()
        self.ui.focus_stop_btn.show()

        # Disable things on mainwindow
        self.disable_and_enable_gui(True)

        # Create FocusTimer
        self.focus_timer = FocusTimer(period, subject, user_sessions, self)
        self.focus_timer.start()

        # If pause button clicked
        self.ui.focus_pause_btn.clicked.connect(self.focus_timer.pause)

        # If resume button is clicked
        self.ui.focus_resume_btn.clicked.connect(self.focus_timer.resume)
    
    # Confirmation for stopping the focus
    def stop_focus_confirmation(self):
        self.focus_timer.stop()
        reply = QMessageBox.question(
            self,
            "Stopping focus session",
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
        self.ui.weeklyFrame.setDisabled(bool_value)
        self.ui.menubar.setDisabled(bool_value)

    def hide_buttons(self):
        self.ui.timer_label.hide()
        self.ui.focus_pause_btn.hide()
        self.ui.focus_stop_btn.hide()
        self.ui.focus_resume_btn.hide()
        self.ui.period_type_label.hide()

    def focus_ended(self):
        # Timer is inactive
        self.is_timer_active = False

        # Hide timer label, pause/resume and stop
        self.hide_buttons()

        # Clear timer_label
        self.ui.timer_label.setText("")

        # Show focus button
        self.ui.start_focus_btn.show()
        self.ui.quote_label.show

        # Enable GUI
        self.disable_and_enable_gui(False)

        # Update focus times
        self.update_focus()

    # Update the daily and weekly focus goal if the user changes the default values
    def update_daily_weekly_focus_goal(self):
        preferences = get_user_preferences()

        if preferences["week_mode"] == "weekdays":
            today = datetime.date.today()
            
            # And if its a weekend
            if today.weekday() >= 5:
                # Set goal to 0 hours
                self.ui.daily_goal_label.setText("daily focus goal: <b>0 hours</b>")
            # else if not weekend
            else:
                # set to default
                self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")
        # Else set to default
        else:
            self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")
        
        if preferences["week_mode"] == "weekdays":
            week_mode = 5
        else:
            week_mode = 7
        
        weekly_goal = preferences["default_daily_focus_goal"] * week_mode
        self.ui.weekly_goal_label.setText(f"weekly focus goal: <b>{weekly_goal} hours</b>")

        self.update_progression_bar()

    # Update the progression bars
    def update_progression_bar(self):
        preferences = get_user_preferences()
        focus_goal_minutes = preferences["default_daily_focus_goal"] * 60
        today_focus_minutes = get_today_focus() / 60
        daily_progress = int((today_focus_minutes / focus_goal_minutes) * 100)
        daily_progress = min(daily_progress,100)
        self.ui.daily_progression_bar.setValue(daily_progress)

        if preferences["week_mode"] == "weekdays":
            self.week_mode = 5
        else:
            self.week_mode = 7
        weekly_focus_goal_minutes = (preferences["default_daily_focus_goal"] * 60) * self.week_mode
        focus_this_week_minutes = get_this_week_focus() / 60
        weekly_progress = int((focus_this_week_minutes / weekly_focus_goal_minutes) * 100)
        weekly_progress = min(weekly_progress,100)
        self.ui.weekly_progression_bar.setValue(weekly_progress)
    
    def update_daily_weekly_focus(self):
         # Load today's focus
        today_focus = get_today_focus()
        today_focus_minutes = 0
        if today_focus == 0:
            self.ui.today_label.setText(f"today's focus: <b>0 minutes</b>")
        elif today_focus < 3600:
            today_focus_minutes = int(today_focus / 60)
            self.ui.today_label.setText(f"today's focus: <b>{today_focus_minutes} minutes</b>")
        else:
            today_focus_hours = (today_focus / 60) / 60
            self.ui.today_label.setText(f"today's focus: <b>{today_focus_hours} hours</b>")

        # Load this week's focus
        focus_this_week = get_this_week_focus()
        focus_this_week_minutes = 0
        if focus_this_week == 0:
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>0 minutes</b>")
        elif focus_this_week < 3600:
            focus_this_week_minutes = int(focus_this_week / 60)
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>{focus_this_week_minutes} minutes</b>")
        else:
            focus_this_week_hours = round((focus_this_week / 60) / 60,2)
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>{focus_this_week_hours} hours</b>")

    # Update the daily and weekly focus if user finished a focus session
    def update_focus(self):
        # update focus labels
        self.update_daily_weekly_focus()

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
            self.ui.quote_label.setText(f"\"{quote}\"\n— {author}")
            self.ui.quote_label.show()
        else:
            self.ui.quote_label.hide()

# Application entry point
def main():
    app = QApplication(sys.argv)
    app.setPalette(ThemeManager.load_dark_palette())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
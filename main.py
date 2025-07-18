from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
from windows.edit_period_window import EditPeriodWindow
from windows.confirmation_window import ConfirmationWindow
from windows.new_subject_window import NewSubjectWindow
from windows.edit_subject_window import EditSubjectWindow
import datetime
from core.timer import FocusTimer
from core.menu_bar import MenuBar
from database.db_manager import get_period_names, get_subject_names
from database.db_manager import get_default_period_name, get_default_subject_name, get_user_preferences, get_today_focus, get_this_week_focus
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

        # Load all period settings into combobox
        periods = get_period_names()
        self.ui.period_combobox.addItems(periods)

        # Set default period setting
        self.default_period_name = get_default_period_name()
        period_index = self.ui.period_combobox.findText(self.default_period_name)
        if period_index != -1:
            self.ui.period_combobox.setCurrentIndex(period_index)

        # Load all subject settings into combobox
        subjects = get_subject_names()
        self.ui.subject_combobox.addItems(subjects)

        # Set default subject setting
        self.default_subject_name = get_default_subject_name()
        subject_index = self.ui.subject_combobox.findText(self.default_subject_name)
        if subject_index != -1:
            self.ui.subject_combobox.setCurrentIndex(subject_index)

        # Load user preferences
        preferences = get_user_preferences()
        self.menubar = MenuBar(preferences, self)

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

        # Load daily focus goal
        self.ui.daily_goal_label.setText(f"daily focus goal: <b>{preferences["default_daily_focus_goal"]} hours</b> ")

        # Load this week's focus
        focus_this_week = get_this_week_focus()
        focus_this_week_minutes = 0
        if focus_this_week == 0:
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>0 minutes</b>")
        elif focus_this_week < 3600:
            focus_this_week_minutes = int(focus_this_week / 60)
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>{focus_this_week_minutes} minutes</b>")
        else:
            focus_this_week_hours = (focus_this_week / 60) / 60
            self.ui.weekly_focus_label.setText(f"this week's focus: <b>{focus_this_week_hours} hours</b>")

        # Load weekly focus
        if preferences["week_mode"] == "weekdays":
            self.week_mode = 5
        else:
            self.week_mode = 7
        weekly_goal = preferences["default_daily_focus_goal"] * self.week_mode
        self.ui.weekly_goal_label.setText(f"weekly focus goal: <b>{weekly_goal} hours</b>")

        # Load daily and weekly progression bar
        self.update_progression_bar()

        # When focus button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)
        
        # When add period button is clicked
        self.ui.newperiod_btn.clicked.connect(lambda:self.start_add_window("period"))

        # When edit period button is clicked
        self.ui.editperiod_btn.clicked.connect(lambda:self.start_edit_window("period"))

        # When delete period button is clicked
        self.ui.delete_period_btn.clicked.connect(lambda:self.start_delete_window("period"))

        # When add subject button is clicked
        self.ui.newsubject_btn.clicked.connect(lambda:self.start_add_window("subject"))

        # When edit subject button is clicked
        self.ui.edit_subject_btn.clicked.connect(lambda:self.start_edit_window("subject"))

        # When delete subject button is clicked
        self.ui.delete_subject_btn.clicked.connect(lambda:self.start_delete_window("subject"))

        # If stop button is clicked
        self.ui.focus_stop_btn.clicked.connect(self.stop_focus_confirmation)

        # When change default daily focus button is clicked
        self.ui.actiondaily_goal.triggered.connect(self.menubar.change_default_daily)
    
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
                "Are you sure you want to quit while in focus? This will save, but end your current progress.",
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
                self.error_window = ConfirmationWindow(self,"The default focus setting cannot be deleted.<br>To change the default value, go to Settings → Change Default → Focus Period.",setting_type)
                self.error_window.exec()
            # Else if deletable
            else:
                self.del_window = ConfirmationWindow(self,f"Do you really want to delete <b>{self.ui.period_combobox.currentText()}</b> focus period setting?<br>This action cannot be undone.",setting_type)
                self.del_window.exec()
        # Else if a subject setting is being deleted
        elif setting_type == "subject":
            # If the chosen element is the default one
            if self.ui.subject_combobox.currentText() == self.default_subject_name:
                self.error_window = ConfirmationWindow(self,"The default subject cannot be deleted.<br>To change the default value, go to Settings → Change Default → Focus Subject.",setting_type)
                self.error_window.exec()
            # Else if deletable
            else:
                self.del_window = ConfirmationWindow(self,f"Do you really want to delete <b>{self.ui.subject_combobox.currentText()}</b> subject?<br>This action cannot be undone.",setting_type)
                self.del_window.exec()
    
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
            "Are you sure you want stop the focus session? This will save, but end your current progress.",
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
        self.ui.streakFrame.setDisabled(bool_value)
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

        # Enable GUI
        self.disable_and_enable_gui(False)


        # Update today's focus, daily progression bar, weekly focus, weekly progression bar

    # Update the daily and weekly focus goal if the user changes the default values
    def update_daily_weekly_focus_goal(self):
        preferences = get_user_preferences()
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

        weekly_focus_goal_minutes = (preferences["default_daily_focus_goal"] * 60) * self.week_mode
        focus_this_week_minutes = get_this_week_focus() / 60
        weekly_progress = int((focus_this_week_minutes / weekly_focus_goal_minutes) * 100)
        weekly_progress = min(weekly_progress,100)
        self.ui.weekly_progression_bar.setValue(weekly_progress)

    
    # Update the daily and weekly focus if user finished a focus session
    def update_today_weekly_focus(self):
        pass
        # update today's focus

        # update this week's focus

        # update progression bar


        
        
# Application entry point
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
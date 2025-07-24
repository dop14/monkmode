from windows.change_def_daily_focus import ChangeDefDailyFocus
from windows.archive_window import ArchiveWindow
from database.db_manager import update_user_preferences, get_user_preferences

class MenuBar:
    def __init__(self, preferences, main_window):
        self.preferences = preferences
        self.main_window = main_window

        self.load_default_checkbox_values()

    # Check buttons according to preferences (DEFAULT)
    def load_default_checkbox_values(self):
        # Set week
        self.preferred_week = self.preferences["week_mode"]
        if self.preferred_week == "weekdays":
            self.main_window.ui.actionweekdays_only.setChecked(True)
            self.main_window.ui.actionwhole_week.setChecked(False)
        else:
            self.main_window.ui.actionwhole_week.setChecked(True)
            self.main_window.ui.actionweekdays_only.setChecked(False)
        
        # All notifications off/on
        self.all_notifications = self.preferences["all_notifications_off"]
        if self.all_notifications == False:
            self.main_window.ui.all_notifications_2.setChecked(False)
        else:
            self.main_window.ui.all_notifications_2.setChecked(True)

        # theme
        self.theme = self.preferences["theme"]
        # TODO: when DESIGN is coming up

        # tips
        self.tips_and_quotes = self.preferences["tips_and_quotes"]
        if self.tips_and_quotes == 1:
            self.main_window.ui.actiontips_and_quotes.setChecked(True)


    # Connect buttons to classes
    def change_default_daily(self):
        self.change_def = ChangeDefDailyFocus(self.preferences, self)
        self.change_def.show()

    def change_to_weekdays(self):
        # Logic if its already checked
        if self.main_window.ui.actionweekdays_only.isChecked() == False:
            self.main_window.ui.actionweekdays_only.setChecked(True)
            return
        else:
            self.main_window.ui.actionwhole_week.setChecked(False)

            # save to db
            user_preferences = get_user_preferences()
            user_preferences["week_mode"] = "weekdays" 
            update_user_preferences(user_preferences,user_preferences["id"])
            
            # update progression bar
            self.main_window.update_daily_weekly_focus_goal()
            self.main_window.update_progression_bar()

    def change_to_wholeweek(self):
        # Logic if its already checked
        if self.main_window.ui.actionwhole_week.isChecked() == False:
            self.main_window.ui.actionwhole_week.setChecked(True)
            return
        else:
            self.main_window.ui.actionweekdays_only.setChecked(False)

            user_preferences = get_user_preferences()
            user_preferences["week_mode"] = "wholeweek"
            update_user_preferences(user_preferences, user_preferences["id"])

            # update progression bar
            self.main_window.update_daily_weekly_focus_goal()
            self.main_window.update_progression_bar()

    def all_notifications_clicked(self):
        if self.main_window.ui.all_notifications_2.isChecked():
            user_preferences = get_user_preferences()
            user_preferences["all_notifications_off"] = 1
            update_user_preferences(user_preferences, user_preferences["id"])
        else:
            user_preferences = get_user_preferences()
            user_preferences["all_notifications_off"] = 0
            update_user_preferences(user_preferences, user_preferences["id"])\
            
    def archive_clicked(self):
        self.archived_window = ArchiveWindow(self)
        self.archived_window.show()

    def refresh_daily_weekly_focus(self):
        self.main_window.update_daily_weekly_focus_goal()

    def refresh_subject_combobox(self):
        self.main_window.ui.subject_combobox.clear()
        self.main_window.update_subject_combobox()

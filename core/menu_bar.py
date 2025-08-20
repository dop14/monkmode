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
        self.change_def = ChangeDefDailyFocus(self)
        self.change_def.show()

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

    def refresh_daily_focus(self):
        self.main_window.update_daily_focus_goal()

    def refresh_subject_combobox(self):
        self.main_window.ui.subject_combobox.clear()
        self.main_window.update_subject_combobox()

    def tips_and_quotes_clicked(self):
        if self.main_window.ui.actiontips_and_quotes.isChecked():
            preferences = get_user_preferences()
            new_preferences = preferences
            new_preferences["tips_and_quotes"] = True
            update_user_preferences(new_preferences, new_preferences["id"])
        else:
            preferences = get_user_preferences()
            new_preferences = preferences
            new_preferences["tips_and_quotes"] = False
            update_user_preferences(new_preferences, new_preferences["id"])

        self.main_window.load_today_quote()

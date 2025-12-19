from windows.change_def_daily_focus import ChangeDefDailyFocus
from windows.archive_window import ArchiveWindow
from core.theme_manager import ThemeManager
from database.db_manager import update_user_preferences, get_user_preferences

class MenuBar:
    def __init__(self, preferences, main_window):
        self.preferences = preferences
        self.main_window = main_window

        self.tm = ThemeManager()
        self.themes = ["focus_fire", "zen_garden", "deep_focus", 
                      "dawn_ritual", "minimal_monk", "monkmode_dark", 
                      "monkmode_light"]
        
        self.load_default_checkbox_values()

    # Check buttons according to preferences (DEFAULT)
    def load_default_checkbox_values(self):
        # All notifications off/on
        self.all_notifications = self.preferences["all_notifications_off"]
        if self.all_notifications == False:
            self.main_window.ui.all_notifications_2.setChecked(False)
        else:
            self.main_window.ui.all_notifications_2.setChecked(True)

        # Tips
        self.tips_and_quotes = self.preferences["tips_and_quotes"]
        if self.tips_and_quotes == 1:
            self.main_window.ui.actiontips_and_quotes.setChecked(True)

        # Check the currently chosen theme
        theme_name = self.tm.get_theme_name()
        for name in self.themes:
            if name == theme_name:
                action = getattr(self.main_window.ui, name)
                action.setChecked(True)

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

    def change_theme(self, theme):
        # Set the chosen theme
        self.tm.set_theme(theme)

        # Uncheck all other themes
        for name in self.themes:
            if name != theme:
                action = getattr(self.main_window.ui, name)
                action.setChecked(False)

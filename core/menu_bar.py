from windows.change_def_daily_focus import ChangeDefDailyFocus

class MenuBar:
    def __init__(self, preferences, main_window):
        self.preferences = preferences
        self.main_window = main_window

        self.load_default_checkbox_values()

    # Check buttons according to preferences (DEFAULT)
    def load_default_checkbox_values(self):
        # Set week
        self.preferred_week = self.preferences[2]
        if self.preferred_week == "weekdays":
            self.main_window.ui.actionweekdays_only.setChecked(True)
            self.main_window.ui.actionwhole_week.setChecked(False)
        else:
            self.main_window.ui.actionwhole_week.setChecked(True)
            self.main_window.ui.actionweekdays_only.setChecked(False)
        
        # All notifications off/on
        self.all_notifications = self.preferences[3]
        if self.all_notifications == 1:
            self.main_window.ui.all_notifications.setChecked(False)

        # theme
        self.theme = self.preferences[4]
        # TODO: when DESIGN is coming up

        # tips
        self.tips_and_quotes = self.preferences[5]
        if self.tips_and_quotes == 1:
            self.main_window.ui.actiontips_and_quotes.setChecked(True)


    # Connect buttons to classes
    def change_default_daily(self):
        self.change_def = ChangeDefDailyFocus(self.preferences, self)
        self.change_def.show()


    #self.main_window.ui.actionfocus_period.clicked.connect(lambda:ChangeDefault("period"))
        # Load in to the combobox the current default period setting
        # If the user changed it, save it to the db
    #self.main_window.ui.actionfocus_subject.clicked.connect(lambda:ChangeDefault("subject"))
        # Load in to the combobox the current default subject setting
        # If the user changed it, save it to the db
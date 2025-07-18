from PySide6.QtWidgets import QDialog
from ui_py.change_default_daily_focus import Ui_Form
from database.db_manager import update_user_preferences, get_user_preferences

class ChangeDefDailyFocus(QDialog):
    def __init__(self, preferences, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.preferences = preferences
        self.main_window = main_window

        # Load the default value the spinbox
        self.default_daily = self.preferences["default_daily_focus_goal"]
        self.ui.daily_focus_goal_spinbox.setValue(self.default_daily)

        # When save button is clicked
        self.ui.save_btn.clicked.connect(lambda:self.save(main_window))

    def save(self,main_window):
        if self.ui.daily_focus_goal_spinbox.value() == self.default_daily:
            self.close()
        else:
            # save to dictionary
            self.new_preferences = get_user_preferences()
            self.new_preferences["default_daily_focus_goal"] = self.ui.daily_focus_goal_spinbox.value()

            # pass dictionary to db to update
            update_user_preferences(self.new_preferences, self.new_preferences["id"])

            # Refresh calculation for dailt goal, weekly goal
            main_window.refresh_daily_weekly_focus()

            # close
            self.close()
from PySide6.QtWidgets import QDialog
from ui_py.change_default_daily_focus import Ui_Form

class ChangeDefDailyFocus(QDialog):
    def __init__(self, preferences, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.preferences = preferences
        self.main_window = main_window

        # Load the default value the spinbox
        self.default_daily = self.preferences[1]
        self.ui.daily_focus_goal_spinbox.setValue(self.default_daily)

        # When save button is clicked
        self.ui.save_btn.clicked.connect(self.save)

    def save(self):
        if self.ui.daily_focus_goal_spinbox.value() == self.default_daily:
            # Refresh calculation for dailt goal, weekly goal
            self.close()
        else:
            pass
            # save to db

            # Refresh calculation for dailt goal, weekly goal

            # close

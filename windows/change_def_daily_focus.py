from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.change_default_daily_focus import Ui_Form
from database.db_manager import update_user_preferences, get_user_preferences
from utils import get_resource_path

class ChangeDefDailyFocus(QDialog):
    def __init__(self, main_window):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("settings")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))

        self.main_window = main_window

        # Load the default value to spinbox
        self.preferences = get_user_preferences()
        self.default_daily = self.preferences["default_daily_focus_goal"]
        self.ui.daily_focus_goal_spinbox.setValue(self.default_daily)

        # Signal
        self.ui.save_btn.clicked.connect(lambda:self.save(main_window))

    def save(self, main_window):
        if self.ui.daily_focus_goal_spinbox.value() == self.default_daily:
            self.close()
        else:
            self.new_preferences = get_user_preferences()
            self.new_preferences["default_daily_focus_goal"] = self.ui.daily_focus_goal_spinbox.value()

            update_user_preferences(self.new_preferences, self.new_preferences["id"])
            
            # Refresh UI
            main_window.refresh_daily_focus()
            self.default_daily = self.new_preferences["default_daily_focus_goal"]
            self.ui.daily_focus_goal_spinbox.setValue(self.default_daily)

            self.close()
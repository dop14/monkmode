from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.change_default import Ui_Form
from database.db_manager import get_default_period_name, get_default_subject_name, get_period_names, get_subject_names, change_def_period, change_def_subject
from utils import get_resource_path

class ChangeDefault(QDialog):
    def __init__(self, main_window, setting_type):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("settings")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))

        self.main_window = main_window
        self.setting_type = setting_type

        self.setup_ui()

    def setup_ui(self):
        if self.setting_type == "period":
            self.ui.main_label.setText("change default period")

            # Load all periods
            periods = get_period_names()
            self.ui.default_combobox.addItems(periods)

            # Set default period setting
            self.default_period_name = get_default_period_name()
            period_index = self.ui.default_combobox.findText(self.default_period_name)
            if period_index != -1:
                self.ui.default_combobox.setCurrentIndex(period_index)
            
            # Signal
            self.ui.save_btn.clicked.connect(self.save_period)

        elif self.setting_type == "subject":
            self.ui.main_label.setText("change default subject")

            # Load all periods
            subjects = get_subject_names()
            self.ui.default_combobox.addItems(subjects)

            # Set default period setting
            self.default_subject_name = get_default_subject_name()
            subject_index = self.ui.default_combobox.findText(self.default_subject_name)
            if subject_index != -1:
                self.ui.default_combobox.setCurrentIndex(subject_index)
            
            # Signal
            self.ui.save_btn.clicked.connect(self.save_subject)
        
    def save_period(self):
        self.chosen_period = self.ui.default_combobox.currentText().strip()
        if self.default_period_name == self.chosen_period:
            self.close()
        else:
            change_def_period(self.chosen_period)
            
            # Refresh combobox on main window
            self.main_window.ui.period_combobox.clear()
            self.main_window.update_period_combobox()

            self.close()

    def save_subject(self):
        self.chosen_subject = self.ui.default_combobox.currentText().strip()
        if self.default_subject_name == self.chosen_subject:
            self.close()
        else:
            change_def_subject(self.chosen_subject)

            # Refresh combobox on main window
            self.main_window.ui.subject_combobox.clear()
            self.main_window.update_subject_combobox()
            
            self.close()

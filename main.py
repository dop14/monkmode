from PySide6.QtWidgets import QApplication, QMainWindow
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
from windows.edit_period_window import EditPeriodWindow
from windows.confirmation_window import ConfirmationWindow
from PySide6.QtCore import Qt
from database.db_manager import get_period_names, get_subject_names
from database.db_manager import get_default_period_name, get_default_subject_name
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hide buttons
        self.ui.timer_label.hide()
        self.ui.focus_pause_btn.hide()
        self.ui.focus_stop_btn.hide()

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
        default_subject_name = get_default_subject_name()
        subject_index = self.ui.subject_combobox.findText(default_subject_name)
        if subject_index != -1:
            self.ui.subject_combobox.setCurrentIndex(subject_index)

        # Load today's focus

        # Load daily focus goal

        # Load this week's focus

        # Load weekly focus

        # When focus button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)
        
        # When add period button is clicked
        self.ui.newperiod_btn.clicked.connect(self.start_add_window)

        # When edit period button is clicked
        self.ui.editperiod_btn.clicked.connect(self.start_edit_window)

        # When delete period button is clicked
        self.ui.delete_period_btn.clicked.connect(lambda:self.start_delete_window("period"))
    
    def start_focus_window(self):
        self.focus_window = FocusWindow(self)
        self.focus_window.exec()

    def start_add_window(self):
        self.add_window = NewPeriodWindow(self)
        self.add_window.exec()

    def start_edit_window(self):
        self.edit_window = EditPeriodWindow(self)
        self.edit_window.exec()

    def start_delete_window(self, setting_type):
        # Check if the currentext is not equal to default
        if self.ui.period_combobox.currentText() == self.default_period_name:
            self.error_window = ConfirmationWindow(self,"The default focus setting cannot be deleted.<br>To change the default value, go to Settings → Change Default → Focus Period.",setting_type)
            self.error_window.exec()
        else:
            self.del_window = ConfirmationWindow(self,f"Do you really want to delete <b>{self.ui.period_combobox.currentText()}</b> focus period setting?<br>This action cannot be undone.",setting_type)
            self.del_window.exec()

# Application entry point
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
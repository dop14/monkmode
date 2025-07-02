from PySide6.QtWidgets import QApplication, QMainWindow
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
from windows.new_period_window import NewPeriodWindow
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
        default_period_name = get_default_period_name()
        period_index = self.ui.period_combobox.findText(default_period_name)
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
    
    def start_focus_window(self):
        self.focus_window = FocusWindow(self)
        self.focus_window.exec()

    def start_add_window(self):
        self.add_window = NewPeriodWindow(self)
        self.add_window.exec()

# Application entry point
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
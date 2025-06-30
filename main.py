from PySide6.QtWidgets import QApplication, QMainWindow
from ui_py.mainwindow import Ui_MainWindow
from windows.focus_window import FocusWindow
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

        # Load period settings into combobox
            # Set default

        # Load subject settings into combobox
            # Set default

        # Load today's focus

        # Load daily focus goal

        # Load this week's focus

        # Load weekly focus

        # When focus button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)
    
    def start_focus_window(self):
        self.focus_window = FocusWindow(self)
        self.focus_window.exec()

# Application entry point
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
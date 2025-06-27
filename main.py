from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QWidget
from ui_py.mainwindow import Ui_MainWindow
from ui_py.focuswindow import Ui_Form
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.focus_ui = Ui_Form()
        self.ui.setupUi(self)

        # Hide buttons
        self.ui.timer_label.hide()
        self.ui.focus_pause_btn.hide()
        self.ui.focus_stop_btn.hide()

        # Click action
        self.ui.start_focus_btn.clicked.connect(self.start_focus_window)

    def start_focus_window(self):
        self.focus_window = QWidget()
        self.focus_ui.setupUi(self.focus_window)
        self.focus_window.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
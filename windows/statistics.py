from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form

class Statistics(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("statistics")
        self.main_window = main_window
    
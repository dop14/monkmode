from PySide6.QtWidgets import QDialog
from ui_py.edit_and_add_period import Ui_Form

class NewPeriodWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
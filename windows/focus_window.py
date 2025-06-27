from PySide6.QtWidgets import QDialog
from ui_py.focuswindow import Ui_Form

class FocusWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)

        # send the current period setting
        # call the session lenght each time user changes the spinbox
        # show it to the user with the period setting (25-5-15)


        # start focus
            # error handling (session can not be 0)
            # calls timer.py
            # show pasue/resume button
            # show reset button
        
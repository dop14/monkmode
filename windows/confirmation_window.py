from PySide6.QtWidgets import QDialog
from ui_py.confirmation import Ui_Confirmation

class ConfirmationWindow(QDialog):
    def __init__(self, main_window, text, type):
        super().__init__()
        self.ui = Ui_Confirmation()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Confirmation")

        # If user wants to delete the default setting
        if text == "The default focus setting cannot be deleted.<br>To change the default value, go to Settings → Change Default → Focus Period.":
            self.ui.cancel_btn.hide()
            self.ui.ok_btn.clicked.connect(self.close)
        # Else if not the default one
        else:
            self.ui.cancel_btn.clicked.connect(self.close)
            self.ui.ok_btn.clicked.connect(lambda:self.delete_setting(type))
            
        # Set the main label text to input text
        self.ui.main_label.setText(text)

    def delete_setting(self, type):
        if type == "period":
            # call delete_period db function
            # refresh mainwindow page
            print("Period deleted")
            # close window
            self.close()
        else:
            # call delete_subject db function
            print("Subject deleted")
            # refresh mainwindow page
            # close window
            self.close()
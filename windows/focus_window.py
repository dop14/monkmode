from PySide6.QtWidgets import QDialog
from ui_py.focuswindow import Ui_Form
from database.db_manager import calculate_session_length

class FocusWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)

        # Get the current period from mainwindow
        self.current_period = main_window.ui.period_combobox.currentText()

        # Calculate session lenght for the minimum session (1)
        length = calculate_session_length(self.ui.session_spinbox.value(),self.current_period)
        self.ui.session_lenght_label.setText(f"this will approximately take {length[0]} minutes\nfocus sessions: {self.ui.session_spinbox.value()}, short breaks: {length[1]}, long breaks: {length[2]}")

        # Calculate session length every time the spinbox value changes
        self.ui.session_spinbox.valueChanged.connect(self.spinbox_value_changed)

        # If start focus is button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus)

    def spinbox_value_changed(self):
        length = calculate_session_length(self.ui.session_spinbox.value(),self.current_period)
        # if the return value is 3
        if len(length) == 3:
            self.ui.session_lenght_label.setText(f"this will approximately take {length[0]} minutes\nfocus sessions: {self.ui.session_spinbox.value()}, short breaks: {length[1]}, long breaks: {length[2]}")
        else:
            self.ui.session_lenght_label.setText(f"this will approximately take {length[0]} hours and {length[1]} minutes\nfocus sessions: {self.ui.session_spinbox.value()}, short breaks: {length[2]}, long breaks: {length[3]}")
        
    def start_focus(self):
       # calling timer.py
       pass

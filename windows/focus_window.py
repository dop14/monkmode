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
        self.current_subject = main_window.ui.subject_combobox.currentText()

        # Show for default value (1)
        self.spinbox_value_changed()

        # Calculate session length every time the spinbox value changes
        self.ui.session_spinbox.valueChanged.connect(self.spinbox_value_changed)

        # If start focus is button is clicked
        self.ui.start_focus_btn.clicked.connect(self.start_focus)

    def spinbox_value_changed(self):
        length = calculate_session_length(self.ui.session_spinbox.value(),self.current_period)
        # if the return value is 3
        if len(length) == 3:
            self.ui.session_lenght_label.setText(
                f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b><br>"
                f"Total session duration: <b>{length[0]} minutes</b><br><br>"
                f"Session breakdown:<br>"
                f"• Focus sessions: <b>{self.ui.session_spinbox.value()}</b><br>"
                f"• Short breaks: <b>{length[1]}</b><br>"
                f"• Long breaks: <b>{length[2]}</b>"
            )

        else:
            self.ui.session_lenght_label.setText(f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b> for <b>{length[0]}</b> hours and <b>{length[1]}</b> minutes<br>focus sessions: {self.ui.session_spinbox.value()}, short breaks: {length[2]}, long breaks: {length[3]}")
            self.ui.session_lenght_label.setText(
                f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b><br>"
                f"Total session duration: <b>{length[0]} hours and {length[1]} minutes</b><br><br>"
                f"Session breakdown:<br>"
                f"• Focus sessions: <b>{self.ui.session_spinbox.value()}</b><br>"
                f"• Short breaks: <b>{length[2]}</b><br>"
                f"• Long breaks: <b>{length[3]}</b>"
            )
    def start_focus(self):
       # calling timer.py
       pass

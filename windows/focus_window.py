from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.focuswindow import Ui_Form
from database.db_manager import calculate_session_length, get_period_data, get_subject_data
from utils import get_resource_path

class FocusWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("focus")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))

        self.main_window = main_window
        
        # Get the chosen period and subject
        self.current_period = self.main_window.ui.period_combobox.currentText()
        self.current_subject = self.main_window.ui.subject_combobox.currentText()

        # Show the default value
        self.spinbox_value_changed()

        # Signals
        self.ui.session_spinbox.valueChanged.connect(self.spinbox_value_changed)
        self.ui.start_focus.clicked.connect(self.start_focus)

    def spinbox_value_changed(self):
        length = calculate_session_length(self.ui.session_spinbox.value(), self.current_period)
        # Text for minutes
        if len(length) == 3:
            self.ui.session_lenght_label.setText(
                f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b><br>"
                f"Total duration: <b>{length[0]} minutes</b><br><br>"
                f"Session breakdown:<br>"
                f"• Focus sessions: <b>{self.ui.session_spinbox.value()}</b><br>"
                f"• Short breaks: <b>{length[1]}</b><br>"
                f"• Long breaks: <b>{length[2]}</b>"
            )
        # Text for hours and minutes
        else:
            self.ui.session_lenght_label.setText(f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b> for <b>{length[0]}</b> hours and <b>{length[1]}</b> minutes<br>focus sessions: {self.ui.session_spinbox.value()}, short breaks: {length[2]}, long breaks: {length[3]}")
            self.ui.session_lenght_label.setText(
                f"You will be focusing on <b>{self.current_subject}</b>, with <b>{self.current_period}</b><br>"
                f"Total duration: <b>{length[0]} hours and {length[1]} minutes</b><br><br>"
                f"Session breakdown:<br>"
                f"• Focus sessions: <b>{self.ui.session_spinbox.value()}</b><br>"
                f"• Short breaks: <b>{length[2]}</b><br>"
                f"• Long breaks: <b>{length[3]}</b>"
            )

    def start_focus(self):
       period_data = get_period_data(self.current_period)
       subject_data = get_subject_data(self.current_subject)
       
       self.main_window.start_timer(period_data, subject_data, self.ui.session_spinbox.value())     
         
       self.close()

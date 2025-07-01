from PySide6.QtWidgets import QDialog
from ui_py.edit_and_add_period import Ui_Form
from database.db_manager import get_period_names

class NewPeriodWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)

        # Set default values for checkboxes and spinboxes
        self.ui.short_break_checkbox.setChecked(True)
        self.ui.short_break_checkbox.stateChanged.connect(self.short_break_checkbox_changed)

        self.ui.long_break_checkbox.stateChanged.connect(self.long_break_checkbox_changed)
        self.ui.long_break_spinbox.setDisabled(True)
        self.ui.long_break_after_spinbox.setDisabled(True)

        # When save button is clicked
        self.ui.save_btn.clicked.connect(self.error_handling)

    # Set checkbox logic
    def short_break_checkbox_changed(self):
        if not self.ui.short_break_checkbox.isChecked():
            self.ui.short_break_spinbox.setDisabled(True)
        else:
            self.ui.short_break_spinbox.setDisabled(False)
        
            # If checkbox is False
                # Disable edit options
    def long_break_checkbox_changed(self):
        if not self.ui.long_break_checkbox.isChecked():
            self.ui.long_break_spinbox.setDisabled(True)
            self.ui.long_break_after_spinbox.setDisabled(True)
        else:
            self.ui.long_break_spinbox.setDisabled(False)
            self.ui.long_break_after_spinbox.setDisabled(False)

    # Handle errors 
    def error_handling(self):
        period_names = get_period_names()
        self.ui.focus_name_entry.setStyleSheet("")
        self.ui.focus_name_entry.setToolTip("")
        # If name is empty:
        if self.ui.focus_name_entry.text().strip() == "":
            self.ui.focus_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.focus_name_entry.setPlaceholderText("Required field!")
        elif self.ui.focus_name_entry.text().strip() in period_names:
            self.ui.focus_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.focus_name_entry.setPlaceholderText("Field has to unique")
            self.ui.focus_name_entry.setToolTip("Field has to be unique")
        else:
            self.save_inputs()

    def save_inputs(self):
        pass
        # Collect inputs into dict
        # Call save_period_settings(data) db function
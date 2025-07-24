from PySide6.QtWidgets import QDialog
from ui_py.add_and_edit_period import Ui_Form
from database.db_manager import get_period_names, save_period_settings, get_default_period_name

class NewPeriodWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("monkmode")

        # Set default values for checkboxes and spinboxes
        self.ui.short_break_checkbox.setChecked(True)
        self.ui.short_break_checkbox.stateChanged.connect(self.short_break_checkbox_changed)

        self.ui.long_break_checkbox.stateChanged.connect(self.long_break_checkbox_changed)
        self.ui.long_break_spinbox.setDisabled(True)
        self.ui.long_break_after_spinbox.setDisabled(True)
        self.ui.long_break_after_label.setDisabled(True)
        self.ui.long_break_minutes_label.setDisabled(True)
        self.ui.focus_sessions_label.setDisabled(True)

        # When save button is clicked
        self.ui.save_btn.clicked.connect(lambda: self.error_handling(main_window))

    # Set checkbox logic
    def short_break_checkbox_changed(self):
        if not self.ui.short_break_checkbox.isChecked():
            self.ui.short_break_spinbox.setDisabled(True)
            self.ui.short_break_minutes_label.setDisabled(True)
        else:
            self.ui.short_break_spinbox.setDisabled(False)
            self.ui.short_break_minutes_label.setDisabled(False)

    def long_break_checkbox_changed(self):
        if not self.ui.long_break_checkbox.isChecked():
            self.ui.long_break_spinbox.setDisabled(True)
            self.ui.long_break_after_spinbox.setDisabled(True)
            self.ui.long_break_after_label.setDisabled(True)
            self.ui.long_break_minutes_label.setDisabled(True)
            self.ui.focus_sessions_label.setDisabled(True)
        else:
            self.ui.long_break_spinbox.setDisabled(False)
            self.ui.long_break_after_spinbox.setDisabled(False)
            self.ui.long_break_after_label.setDisabled(False)
            self.ui.focus_sessions_label.setDisabled(False)
            self.ui.long_break_minutes_label.setDisabled(False)

    # Handle errors 
    def error_handling(self, main_window):
        period_names = get_period_names()

        # Delete previous errors
        self.ui.focus_name_entry.setStyleSheet("")
        self.ui.focus_name_entry.setToolTip("")
        self.ui.focus_name_entry.setPlaceholderText("")

        # If name is empty:
        if self.ui.focus_name_entry.text().strip() == "":
            self.ui.focus_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.focus_name_entry.setPlaceholderText("Required field!")
        # Or if name is not unique
        elif self.ui.focus_name_entry.text().strip() in period_names:
            self.ui.focus_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.focus_name_entry.setText("")
            self.ui.focus_name_entry.setPlaceholderText("Field has to be unique")
            self.ui.focus_name_entry.setToolTip("Field has to be unique")
        # Else no errors
        else:
            self.save_inputs(main_window)

    def save_inputs(self, main_window):
        # Handle checkbox logic
        if not self.ui.short_break_checkbox.isChecked():
            self.short_break_time = 0
        else:
            self.short_break_time = self.ui.short_break_spinbox.value()

        if not self.ui.long_break_checkbox.isChecked():
            self.long_break_time = 0
            self.long_break_after = 0
        else:
            self.long_break_time = self.ui.long_break_spinbox.value()
            self.long_break_after = self.ui.long_break_after_spinbox.value()

        # Collect inputs into dict
        self.new_period_data = {
            "name": self.ui.focus_name_entry.text(),
            "focus_time": self.ui.focus_time_spinbox.value(),
            "short_break_enabled": self.ui.short_break_checkbox.isChecked(),
            "short_break_time": self.short_break_time,
            "long_break_enabled": self.ui.long_break_checkbox.isChecked(),
            "long_break_time": self.long_break_time,
            "long_break_after": self.long_break_after
        }

        # Save the new period setting
        save_period_settings(self.new_period_data)

        # Refresh the combobox
        self.refresh_period_combobox(main_window)

        # Close window
        self.close()

    # Refresh mainwindow
    def refresh_period_combobox(self, main_window):
        periods = get_period_names()
        main_window.ui.period_combobox.clear()
        main_window.ui.period_combobox.addItems(periods)

        # Set the chosen as last added period
        last_added_period = self.ui.focus_name_entry.text().strip()
        period_index = main_window.ui.period_combobox.findText(last_added_period)
        if period_index != -1:
            main_window.ui.period_combobox.setCurrentIndex(period_index)

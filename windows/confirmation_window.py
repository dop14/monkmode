from PySide6.QtWidgets import QDialog
from ui_py.confirmation import Ui_Confirmation
from database.db_manager import get_period_data, delete_period_settings, get_period_names, get_default_period_name, delete_subject_settings, get_subject_data, get_subject_names, get_default_subject_name, archive_subject_settings
from PySide6.QtGui import QIcon
from utils import get_resource_path

class ConfirmationWindow(QDialog):
    def __init__(self, main_window, text, type):
        super().__init__()

        # Setup UI
        self.ui = Ui_Confirmation()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
        
        self.main_window = main_window
        self.text = text
        self.type = type

        self.setup_ui()

    def setup_ui(self):
        # Error for deleting the default setting
        if self.text == "The default focus setting cannot be deleted." or self.text == "The default subject cannot be deleted." or self.text == "The default subject cannot be archived.":
            self.ui.cancel_btn.hide()
            self.ui.ok_btn.clicked.connect(self.close)
            self.setWindowTitle("error")
        # Archiving a subject
        elif self.type == "archive_subject":
            self.ui.cancel_btn.clicked.connect(self.close)
            self.ui.ok_btn.clicked.connect(self.archive_subject)
            self.setWindowTitle("confirmation")
        # Deleting a period or subject
        else:
            self.ui.cancel_btn.clicked.connect(self.close)
            self.ui.ok_btn.clicked.connect(self.delete_setting)
            self.setWindowTitle("confirmation")
            
        # Set the main label text to input text
        self.ui.main_label.setText(self.text)

    def delete_setting(self):
        if self.type == "period":
            # Get the id of the chosen period
            self.current_period = self.main_window.ui.period_combobox.currentText()
            period_data = get_period_data(self.current_period)

            # Delete from database
            delete_period_settings(period_data["id"])

            # Refresh main window
            self.refresh_period_combobox()

            self.close()

        elif self.type == "subject":
            # Get the id of the chosen subject
            self.current_subject = self.main_window.ui.subject_combobox.currentText()
            subject_data = get_subject_data(self.current_subject)

            # Delete from database
            delete_subject_settings(subject_data[0])

            # Refresh main window
            self.refresh_subject_combobox()
    
            self.close()

    def archive_subject(self):
        # Get the id of the chosen subject
        self.current_subject = self.main_window.ui.subject_combobox.currentText()
        subject_data = get_subject_data(self.current_subject)

        # Delete from database
        archive_subject_settings(subject_data[0])

        # Refresh main window
        self.refresh_subject_combobox()
        
        self.close()

    # Refresh the period combobox on main window
    def refresh_period_combobox(self):
        periods = get_period_names()
        self.main_window.ui.period_combobox.clear()
        self.main_window.ui.period_combobox.addItems(periods)

        # Set the default setting
        default_period_name = get_default_period_name()
        period_index = self.main_window.ui.period_combobox.findText(default_period_name)
        if period_index != -1:
            self.main_window.ui.period_combobox.setCurrentIndex(period_index)

    # Refresh the subject combobox on main_window
    def refresh_subject_combobox(self):
        subjects = get_subject_names()
        self.main_window.ui.subject_combobox.clear()
        self.main_window.ui.subject_combobox.addItems(subjects)

        # Set the default setting
        default_subject_name = get_default_subject_name()
        period_index = self.main_window.ui.subject_combobox.findText(default_subject_name)
        if period_index != -1:
            self.main_window.ui.subject_combobox.setCurrentIndex(period_index)
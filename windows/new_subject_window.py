from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.add_and_edit_subject import Ui_Form
from database.db_manager import get_subject_names, save_subject_settings
from utils import get_resource_path

class NewSubjectWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("monkmode")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))

        self.main_window = main_window

        # Signal
        self.ui.save_btn.clicked.connect(self.error_handling)

    def error_handling(self):
        subjects = get_subject_names()

        # Delete previous errors
        self.ui.subject_name_entry.setStyleSheet("")
        self.ui.subject_name_entry.setToolTip("")
        self.ui.subject_name_entry.setPlaceholderText("")

        # Empty string error
        if self.ui.subject_name_entry.text().strip() == "":
            self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.subject_name_entry.setPlaceholderText("Required field!")
        # String not unique error
        elif self.ui.subject_name_entry.text().strip() in subjects:
            self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
            self.ui.subject_name_entry.setText("")
            self.ui.subject_name_entry.setPlaceholderText("Field has to be unique")
            self.ui.subject_name_entry.setToolTip("Field has to be unique")
        else:
            # Save data and refresh combobox
            save_subject_settings(self.ui.subject_name_entry.text().strip())
            self.refresh_subject_combobox()
            self.close()
        
        
    def refresh_subject_combobox(self):
        subjects = get_subject_names()
        self.main_window.ui.subject_combobox.clear()
        self.main_window.ui.subject_combobox.addItems(subjects)

        # Set the chosen as last added
        last_added_subject = self.ui.subject_name_entry.text().strip()
        subject_index = self.main_window.ui.subject_combobox.findText(last_added_subject)
        if subject_index != -1:
            self.main_window.ui.subject_combobox.setCurrentIndex(subject_index)

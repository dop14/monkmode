from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.add_and_edit_subject import Ui_Form
from database.db_manager import get_subject_names, get_subject_data, update_subject_settings
from utils import get_resource_path

class EditSubjectWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("monkmode")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
        self.ui.main_label.setText("edit subject")

        self.main_window = main_window

        self.load_inputs()

        # Signal
        self.ui.save_btn.clicked.connect(self.error_handling)

    # Load name into entry
    def load_inputs(self):
        self.old_subject_name = self.main_window.ui.subject_combobox.currentText()
        self.ui.subject_name_entry.setText(self.old_subject_name)

    def error_handling(self):
        # if new name is the same as old
        if self.old_subject_name == self.ui.subject_name_entry.text().strip():
            self.close()
        else:
            # String is empty error
            subjects = get_subject_names()
            if self.ui.subject_name_entry.text().strip() == "":
                self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
                self.ui.subject_name_entry.setPlaceholderText("Required field!")
            # String is not unique error
            elif self.ui.subject_name_entry.text().strip() in subjects:
                self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
                self.ui.subject_name_entry.setText("")
                self.ui.subject_name_entry.setPlaceholderText("Field has to be unique")
                self.ui.subject_name_entry.setToolTip("Field has to be unique")
            else:
                subject_data = get_subject_data(self.main_window.ui.subject_combobox.currentText())
                update_subject_settings(subject_data[0],self.ui.subject_name_entry.text().strip())
                self.refresh_subject_combobox()
                self.close()
        
    def refresh_subject_combobox(self):
        subjects = get_subject_names()
        self.main_window.ui.subject_combobox.clear()
        self.main_window.ui.subject_combobox.addItems(subjects)

        # Set the current as last edited
        last_subject_name = self.ui.subject_name_entry.text().strip()
        subject_index = self.main_window.ui.subject_combobox.findText(last_subject_name)
        if subject_index != -1:
            self.main_window.ui.subject_combobox.setCurrentIndex(subject_index)
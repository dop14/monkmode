from PySide6.QtWidgets import QDialog
from ui_py.add_and_edit_subject import Ui_Form
from database.db_manager import get_subject_names, get_default_subject_name, get_subject_data, update_subject_settings

class EditSubjectWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("monkmode")

        self.ui.main_label.setText("edit subject")

        self.load_inputs(main_window)

        # Action for save button
        self.ui.save_btn.clicked.connect(lambda: self.error_handling(main_window))

    # Load name into entry
    def load_inputs(self, main_window):
        self.old_subject_name = main_window.ui.subject_combobox.currentText()
        self.ui.subject_name_entry.setText(self.old_subject_name)

    def error_handling(self, main_window):
        # if no changes were made
        if self.old_subject_name == self.ui.subject_name_entry.text().strip():
            self.close()
        # else changes were made
        else:
            # If the name is empty
            subjects = get_subject_names()
            if self.ui.subject_name_entry.text().strip() == "":
                self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
                self.ui.subject_name_entry.setPlaceholderText("Required field!")
            # Else if the name is not unique
            elif self.ui.subject_name_entry.text().strip() in subjects:
                self.ui.subject_name_entry.setStyleSheet("border: 1px solid red;")
                self.ui.subject_name_entry.setText("")
                self.ui.subject_name_entry.setPlaceholderText("Field has to be unique")
                self.ui.subject_name_entry.setToolTip("Field has to be unique")
            # Else no errors
            else:
                # Update in database
                subject_data = get_subject_data(main_window.ui.subject_combobox.currentText())
                update_subject_settings(subject_data[0],self.ui.subject_name_entry.text().strip())

                # Refresh combobox on main_window
                self.refresh_subject_combobox(main_window)

                # Close window
                self.close()
        
    def refresh_subject_combobox(self, main_window):
        subjects = get_subject_names()
        main_window.ui.subject_combobox.clear()
        main_window.ui.subject_combobox.addItems(subjects)

        # Set the current as last edited
        last_subject_name = self.ui.subject_name_entry.text().strip()
        subject_index = main_window.ui.subject_combobox.findText(last_subject_name)
        if subject_index != -1:
            main_window.ui.subject_combobox.setCurrentIndex(subject_index)
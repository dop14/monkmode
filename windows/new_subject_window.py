from PySide6.QtWidgets import QDialog
from ui_py.add_and_edit_subject import Ui_Form
from database.db_manager import get_subject_names, save_subject_settings, get_default_subject_name

class NewSubjectWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("monkmode")

        # Action for save button
        self.ui.save_btn.clicked.connect(lambda: self.error_handling(main_window))

    # Error handling 
    def error_handling(self, main_window):

        self.ui.subject_name_entry.setStyleSheet("")
        self.ui.subject_name_entry.setToolTip("")
        self.ui.subject_name_entry.setPlaceholderText("")

        subjects = get_subject_names()
        # If the name is empty
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
            # Save to database
            save_subject_settings(self.ui.subject_name_entry.text().strip())

            # Refresh combobox on main_window
            self.refresh_subject_combobox(main_window)

            # Close window
            self.close()
        
        
    def refresh_subject_combobox(self, main_window):
        subjects = get_subject_names()
        main_window.ui.subject_combobox.clear()
        main_window.ui.subject_combobox.addItems(subjects)

        # Set the chosen as last added
        last_added_subject = self.ui.subject_name_entry.text().strip()
        subject_index = main_window.ui.subject_combobox.findText(last_added_subject)
        if subject_index != -1:
            main_window.ui.subject_combobox.setCurrentIndex(subject_index)

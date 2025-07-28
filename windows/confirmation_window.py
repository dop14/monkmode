from PySide6.QtWidgets import QDialog
from ui_py.confirmation import Ui_Confirmation
from database.db_manager import get_period_data, delete_period_settings, get_period_names, get_default_period_name, delete_subject_settings, get_subject_data, get_subject_names, get_default_subject_name, archive_subject_settings

class ConfirmationWindow(QDialog):
    def __init__(self, main_window, text, type):
        super().__init__()
        self.ui = Ui_Confirmation()
        self.ui.setupUi(self)
        self.setModal(True)

        # If user wants to delete the default setting
        if text == "The default focus setting cannot be deleted." or text == "The default subject cannot be deleted." or text == "The default subject cannot be archived.":
            self.ui.cancel_btn.hide()
            self.ui.ok_btn.clicked.connect(self.close)
            self.setWindowTitle("error")
        # Else if not the default one
        elif type == "archive_subject":
            self.ui.cancel_btn.clicked.connect(self.close)
            self.ui.ok_btn.clicked.connect(lambda:self.archive_subject(main_window,type))
            self.setWindowTitle("confirmation")
        else:
            self.ui.cancel_btn.clicked.connect(self.close)
            self.ui.ok_btn.clicked.connect(lambda:self.delete_setting(main_window,type))
            self.setWindowTitle("confirmation")
            
        # Set the main label text to input text
        self.ui.main_label.setText(text)

    def delete_setting(self, main_window, type):
        if type == "period":
            # Get the id of the chosen period
            self.current_period = main_window.ui.period_combobox.currentText()
            period_data = get_period_data(self.current_period)

            # Delete from database
            delete_period_settings(period_data["id"])

            # Refresh the main window
            self.refresh_period_combobox(main_window)

            # close window
            self.close()

        elif type == "subject":
            # Get the id of the chosen subject
            self.current_subject = main_window.ui.subject_combobox.currentText()
            subject_data = get_subject_data(self.current_subject)

            # Delete from database
            delete_subject_settings(subject_data[0])

            # Refresh the main window
            self.refresh_subject_combobox(main_window)
            # Close window
            self.close()

    def archive_subject(self, main_window, type):
        # Get the id of the chosen subject
        self.current_subject = main_window.ui.subject_combobox.currentText()
        subject_data = get_subject_data(self.current_subject)

        # Delete from database
        archive_subject_settings(subject_data[0])

        # Refresh the main window
        self.refresh_subject_combobox(main_window)
        
        # Close window
        self.close()

    # Refresh the period combobox on main_window
    def refresh_period_combobox(self, main_window):
        periods = get_period_names()
        main_window.ui.period_combobox.clear()
        main_window.ui.period_combobox.addItems(periods)

        # Set the default again
        default_period_name = get_default_period_name()
        period_index = main_window.ui.period_combobox.findText(default_period_name)
        if period_index != -1:
            main_window.ui.period_combobox.setCurrentIndex(period_index)

    # Refresh the subject combobox on main_window
    def refresh_subject_combobox(self, main_window):
        subjects = get_subject_names()
        main_window.ui.subject_combobox.clear()
        main_window.ui.subject_combobox.addItems(subjects)

        # Set the default again
        default_subject_name = get_default_subject_name()
        period_index = main_window.ui.subject_combobox.findText(default_subject_name)
        if period_index != -1:
            main_window.ui.subject_combobox.setCurrentIndex(period_index)
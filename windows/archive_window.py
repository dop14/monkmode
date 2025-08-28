from PySide6.QtWidgets import QDialog
from ui_py.archive import Ui_Form
from PySide6.QtGui import QIcon
from database.db_manager import get_archived_subject_names, unarchive_subject_settings, get_subject_data

class ArchiveWindow(QDialog):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("archive")
        
        self.setWindowIcon(QIcon("logo/monkmode.png"))
        self.parent_window = parent_window

        self.load_archived_subjects()

        self.ui.unarchive_btn.clicked.connect(lambda:self.unarchive_subject(self.ui.archived_combobox.currentText()))

    def load_archived_subjects(self):
    # Load all subject settings into combobox
        self.ui.archived_combobox.clear()
        archived_subjects = get_archived_subject_names()
        self.ui.archived_combobox.addItems(archived_subjects)

    def unarchive_subject(self, unarchived_subject):
        if unarchived_subject == "":
            self.close()
            return
        subject_data = get_subject_data(unarchived_subject)
        unarchive_subject_settings(subject_data[0])

        # refresh combobox on archive window
        self.load_archived_subjects()

        # refersh combobox on mainwindow
        self.parent_window.refresh_subject_combobox()

        # close window
        self.close()


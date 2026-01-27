from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.archive import Ui_Form
from database.db_manager import get_archived_subject_names, unarchive_subject_settings, get_subject_data
from utils import get_resource_path

class ArchiveWindow(QDialog):
    def __init__(self, parent_window):
        super().__init__()
    
        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("archive")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))

        self.parent_window = parent_window

        self.load_archived_subjects()

        # Signal
        self.ui.unarchive_btn.clicked.connect(lambda:self.unarchive_subject(self.ui.archived_combobox.currentText()))

    def load_archived_subjects(self):
        self.ui.archived_combobox.clear()
        archived_subjects = get_archived_subject_names()
        self.ui.archived_combobox.addItems(archived_subjects)

    def unarchive_subject(self, unarchived_subject):
        if unarchived_subject == "":
            self.close()
            return
        subject_data = get_subject_data(unarchived_subject)
        unarchive_subject_settings(subject_data[0])

        # Refresh the combobox on current window and on main window
        self.load_archived_subjects()
        self.parent_window.refresh_subject_combobox()

        self.close()


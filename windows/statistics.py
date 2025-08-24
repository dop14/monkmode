from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form
from database.db_manager import get_user_stats, get_avg_focus

class Statistics(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("statistics")
        self.main_window = main_window

        self.show_stats()

    def show_stats(self):
        stats = get_user_stats()
        avg_focus = get_avg_focus()
        
        # Set label values

        self.ui.total_focus_time.setText(f"total focus time: {int(stats[0] / 60)} minutes")
        self.ui.focus_sessions_completed.setText(f"focus sessions completed: {int(stats[1])}")
        self.ui.longest_focus_session.setText(f"longest focus session: {int(stats[2] / 60)} minutes")
        self.ui.avarage_focus_time.setText(f"avarage focus time: {avg_focus}")
    
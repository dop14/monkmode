from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form
from database.db_manager import get_user_stats, get_avg_focus, get_daily_goal_achieved, get_current_streak

class Statistics(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("statistics")
        self.main_window = main_window

        self.show_stats()
        self.show_karma_and_streaks()

    def show_stats(self):
        stats = get_user_stats()
        avg_focus = get_avg_focus()
        
        # Set label values
        if stats[0] > 3600:
            focus_mins = stats[0]
            hours = focus_mins // 3600
            minutes = (focus_mins % 3600) // 60
            self.ui.total_focus_time.setText(f"total focus time: <b>{hours} hours and {minutes} minutes</b>")
        else:
            self.ui.total_focus_time.setText(f"total focus time: <b>{int(stats[0] / 60)} minutes</b>")

        self.ui.focus_sessions_completed.setText(f"focus sessions completed: <b>{int(stats[1])}</b>")
        if stats[2] > 3600:
            longest_focus_mins = stats[2]
            hours = longest_focus_mins // 3600
            minutes = (longest_focus_mins % 3600) // 60
            self.ui.longest_focus_session.setText(f"longest focus session: <b>{hours} hours and {minutes} minutes</b>")
        else:
            self.ui.longest_focus_session.setText(f"longest focus session: <b>{int(stats[2] / 60)} minutes</b>")

        if avg_focus:
            self.ui.avarage_focus_time.setText(f"avarage focus time: <b>{int(avg_focus / 60)} minutes</b>")
        else:
            self.ui.avarage_focus_time.setText(f"avarage focus time: <b>no data</b>")

    def show_karma_and_streaks(self):
        daily_goal = get_daily_goal_achieved()
        self.ui.daily_goal_achieved.setText(f"daily goal achieved: <b>{daily_goal}</b>")

        current_streak = get_current_streak()
        self.ui.current_streak.setText(f"current streak: <b>{current_streak} days</b>")
    
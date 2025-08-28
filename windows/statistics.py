from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form
from database.db_manager import get_user_stats, get_avg_focus, get_daily_goal_achieved, get_current_streak, get_current_karma

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
        self.longest_streak = stats[3]
        avg_focus = get_avg_focus()
        
        # Set label values
        if stats[0] > 3600:
            focus_mins = stats[0]
            hours = focus_mins // 3600
            minutes = (focus_mins % 3600) // 60
            if minutes == 0:
                self.ui.total_focus_time.setText(f"total focus time: <b>{hours} hours")
            else:
                self.ui.total_focus_time.setText(f"total focus time: <b>{hours} hours and {minutes} minutes</b>")
        else:
            self.ui.total_focus_time.setText(f"total focus time: <b>{int(stats[0] / 60)} minutes</b>")

        self.ui.focus_sessions_completed.setText(f"focus sessions completed: <b>{int(stats[1])}</b>")
        if stats[2] > 3600:
            longest_focus_mins = stats[2]
            hours = longest_focus_mins // 3600
            minutes = (longest_focus_mins % 3600) // 60
            if minutes == 0:
                self.ui.longest_focus_session.setText(f"longest focus session: <b>{hours} hours</b>")
            else:
                self.ui.longest_focus_session.setText(f"longest focus session: <b>{hours} hours and {minutes} minutes</b>")
        else:
            self.ui.longest_focus_session.setText(f"longest focus session: <b>{int(stats[2] / 60)} minutes</b>")

        if avg_focus < 3600:
            self.ui.avarage_focus_time.setText(f"avarage focus time: <b>{int(avg_focus / 60)} minutes</b>")
        elif avg_focus > 3600:
            hours = avg_focus // 3600
            minutes = (avg_focus % 3600) // 60
            if minutes == 0:
                self.ui.avarage_focus_time.setText(f"avarage focus time: <b>{hours} hours</b>")
            else:
                self.ui.avarage_focus_time.setText(f"avarage focus time: <b>{hours} hours and {minutes} minutes</b>")
        else:
            self.ui.avarage_focus_time.setText(f"avarage focus time: <b>no data</b>")

    def show_karma_and_streaks(self):
        daily_goal = get_daily_goal_achieved()
        self.ui.daily_goal_achieved.setText(f"daily goal achieved: <b>{daily_goal}</b>")

        current_streak = get_current_streak()
        self.ui.current_streak.setText(f"current streak: <b>{current_streak} days</b>")

        self.ui.longest_streak.setText(f"longest streak: <b>{self.longest_streak} days</b>")

        self.current_karma = get_current_karma()
        self.ui.karma.setText(f"karma: <b>{int(self.current_karma)}%</b>")
        self.ui.karma.setToolTip("your consistency in the past 3 months")
        self.show_karma_level()
 
    def show_karma_level(self):
        if self.current_karma <= 15:
            karma_level = "☁️ Novice - Unsui (雲水)"
            tooltip_text = "Clouds and water. You're a novice monk wandering and learning."
        elif self.current_karma <= 31:
            karma_level = "🌱 Apprentice - Shami (沙弥)"
            tooltip_text = "Apprentice monk. Beginning to build consistent practice and focus."
        elif self.current_karma <= 47:
            karma_level = "🏹 Disciplined - Shugyōsha (修行者)"
            tooltip_text = "Dedicated practitioner. Developing strong habits and perseverance."
        elif self.current_karma <= 63:
            karma_level = "🕯️ Seeker - Shuso (首座)"
            tooltip_text = "Head trainee. Taking responsibility and deepening your practice."
        elif self.current_karma <= 79:
            karma_level = "📜 Teacher - Osho (和尚)"
            tooltip_text = "Teacher monk. Able to guide others with consistent discipline."
        elif self.current_karma <= 90:
            karma_level = "🪷 Master - Roshi (老師)"
            tooltip_text = "Master monk. Highly skilled, respected as an example of focus."
        else:
            karma_level = "🌞 Enlightened - Satori (悟り)"
            tooltip_text = "Enlightened. Peak dedication and mastery; ultimate level of focus."
        
        self.ui.karma_level.setText(f"karma level: <b>{karma_level}</b>")
        self.ui.karma_level.setToolTip(tooltip_text)

    
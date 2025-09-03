from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form
from database.db_manager import get_user_stats, get_avg_focus, get_daily_goal_achieved, get_current_streak, get_current_karma, get_focus_data, get_subject_data_stats, get_period_data_stats, get_subject_time_data
from PySide6.QtGui import QIcon
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QVBoxLayout
import textwrap

class Statistics(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("statistics")
        self.setWindowIcon(QIcon("logo/monkmode.png"))
        self.main_window = main_window

        self.show_stats()
        self.show_karma_and_streaks()
        self.plot_focus_chart()
        self.plot_subject_chart()
        self.plot_period_distribution()
        self.plot_subject_bar_chart()

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

        if avg_focus != None:
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

    def plot_focus_chart(self):
        # Get data
        rows = get_focus_data()

        # Prepare data
        row_dict = {row[0]: row[1]/60 for row in rows}  # seconds -> minutes
        all_days = [datetime.today() - timedelta(days=i) for i in reversed(range(30))]
        all_durations = [row_dict.get(d.strftime('%Y-%m-%d'), 0) for d in all_days]

        # Create Matplotlib figure and canvas
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(all_days, all_durations, color='blue', linewidth=2)
        ax.set_title('daily focus time (last 30 days)',fontweight="bold")
        ax.set_ylabel('focus duration (minutes)')
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        canvas.setMaximumSize(600, 300)

        layout = self.ui.focusFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.focusFrame.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    layout.removeWidget(widget)
                    widget.setParent(None)

        layout.addWidget(canvas, 0)


        # Add canvas to the focusFrame layout
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.ui.focusFrame.setLayout(layout)

    def plot_subject_chart(self):
        # Get data
        rows = get_subject_data_stats()

        # Prepare labels and values
        labels = [row[0] for row in rows]
        durations = [row[1]/60 for row in rows]  # seconds -> minutes

        # Create pie chart with same size as line chart
        fig, ax = plt.subplots(figsize=(6.2, 3.2))  # same as line chart
        wedges, texts, autotexts = ax.pie(
            durations,
            autopct='%1.1f%%',  # show percentages inside
            startangle=90,
            textprops={'fontsize': 8}  # make % text small enough to always fit
        )

        # Add legend for subject names
        ax.legend(
            wedges,
            labels,
            title="subjects",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=8
        )

        # Bold title
        ax.set_title('focus time distribution by subject (last 30 days)', fontweight="bold")

        canvas = FigureCanvas(fig)
        canvas.setMaximumSize(620, 320)  # same max size as line chart

        # Embed in subjectFrame
        layout = self.ui.subjectFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.subjectFrame.setLayout(layout)
        else:
            # Clear previous widgets
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    layout.removeWidget(widget)
                    widget.setParent(None)

        layout.addWidget(canvas, 0)  # add canvas with no stretch

    def plot_period_distribution(self):
        # Get data
        rows = get_period_data_stats()

        # If no data, clear frame and exit
        layout = self.ui.periodFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.periodFrame.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                if w:
                    layout.removeWidget(w)
                    w.setParent(None)

        if not rows:
            return

        # Prepare labels and values (seconds -> minutes)
        labels = [r[0] for r in rows]
        durations = [r[1] / 60 for r in rows]

        # Create pie chart (same size as subject pie chart)
        fig, ax = plt.subplots(figsize=(6.2, 3.2))
        wedges, texts, autotexts = ax.pie(
            durations,
            autopct='%1.1f%%',    # keep percentages inside
            startangle=90,
            textprops={'fontsize': 8}
        )

        # Add legend on the side
        ax.legend(
            wedges,
            labels,
            title="periods",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=8
        )

        # Bold title
        ax.set_title('focus time distribution by period (last 30 days)', fontweight="bold")

        canvas = FigureCanvas(fig)
        canvas.setMaximumSize(620, 320)  # match subject + line chart sizes

        layout.addWidget(canvas, 0)


    def plot_subject_bar_chart(self):
        # Get data
        rows = get_subject_time_data()

        # Ensure layout exists and clear old chart
        layout = self.ui.subjectBarFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.subjectBarFrame.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                if w:
                    layout.removeWidget(w)
                    w.setParent(None)

        if not rows:
            return

        # Prepare labels and values
        labels = [r[0] for r in rows]
        durations = [r[1] / 60 for r in rows]  # seconds → minutes

        # Pick distinct colors (using a matplotlib colormap)
        cmap = plt.get_cmap("tab20")  # up to 20 distinct colors
        colors = [cmap(i % 20) for i in range(len(labels))]

        labels = [textwrap.fill(l, 10) for l in labels]

        # Create bar chart
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(labels, durations, color=colors)
        ax.set_ylabel("focus time (minutes)")
        ax.set_title("focus time per subject (last 30 days)", fontweight="bold")
        plt.xticks(rotation=45, ha="right")

        # Give more space at bottom for labels
        fig.subplots_adjust(bottom=0.3)

        # Embed into Qt
        canvas = FigureCanvas(fig)
        canvas.setMaximumSize(600, 450)
        layout.addWidget(canvas, 0)
    
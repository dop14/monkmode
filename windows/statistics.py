from PySide6.QtWidgets import QDialog
from ui_py.statistics import Ui_Form
from database.db_manager import get_user_stats, get_most_productive_day, get_avg_daily_focus, get_avg_weekly_focus, get_daily_goal_achieved, get_current_streak, get_current_karma, get_focus_data, get_highest_weekly_focus, get_subject_data_stats, get_period_data_stats, get_subject_time_data, get_subject_time_data_all_include_archived, get_subject_time_data_all_not_include_archived, get_highest_daily_focus
from PySide6.QtGui import QIcon
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QVBoxLayout
import textwrap
from utils import get_resource_path
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates
from core.theme_manager import ThemeManager
from matplotlib.ticker import MaxNLocator

class Statistics(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("statistics")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
        self.main_window = main_window

        self.ui.no_data_message.hide()
        self.tm = ThemeManager()
        self.set_chart_theme()

        self.show_stats()
        self.show_karma_and_streaks()
        self.plot_focus_chart()
        self.plot_subject_chart()
        self.plot_period_distribution()
        self.plot_subject_bar_chart()
        self.plot_subject_bar_chart_allhistory()
        self.set_tooltips()

        self.ui.include_archived_checkbox.stateChanged.connect(self.plot_subject_bar_chart_allhistory)

    def show_stats(self):
        stats = get_user_stats()
        self.longest_streak = stats[3]
        avg_daily_focus = get_avg_daily_focus()
        avg_weekly_focus = get_avg_weekly_focus()
        highest_daily_focus = get_highest_daily_focus()
        highest_weekly_focus = get_highest_weekly_focus()
        most_productive_day = get_most_productive_day()

        # Set most productive day
        if most_productive_day:
            self.ui.most_prod_day.setText(f"most productive day of the week: <b>{most_productive_day}</b>")
        else:
            self.ui.most_prod_day.setText(f"most productive day of the week: <b>no data</b>")

        # Set label values
        if stats[0] > 3600:
            focus_mins = stats[0]
            hours = focus_mins // 3600
            minutes = (focus_mins % 3600) // 60
            if minutes == 0:
                self.ui.total_focus_time.setText(f"total focus time: <b>{hours} hours")
            else:
                self.ui.total_focus_time.setText(f"total focus time: <b>{hours} hours {minutes} minutes</b>")
        else:
            self.ui.total_focus_time.setText(f"total focus time: <b>{int(stats[0] / 60)} minutes</b>")

        self.ui.focus_sessions_completed.setText(f"focus sessions completed: <b>{int(stats[1])}</b>")

        if highest_daily_focus != None:
            if highest_daily_focus < 3600:
                self.ui.highest_daily_label.setText(f"highest daily focus: <b>{int(highest_daily_focus / 60)} minutes</b>")
            elif highest_daily_focus > 3600:
                hours = highest_daily_focus // 3600
                minutes = (highest_daily_focus % 3600) // 60
                if minutes == 0:
                    self.ui.highest_daily_label.setText(f"highest daily focus: <b>{hours} minutes</b>")
                else:
                    self.ui.highest_daily_label.setText(f"highest daily focus: <b>{hours} hours {minutes} minutes</b>")
            else:
                self.ui.highest_daily_label.setText(f"highest daily focus: <b>no data</b>")
        else:
            self.ui.highest_daily_label.setText(f"highest daily focus: <b>no data</b>")


        if highest_weekly_focus != None:
            if highest_weekly_focus < 3600:
                self.ui.highest_weekly_label.setText(f"highest weekly focus: <b>{int(highest_weekly_focus / 60)} minutes</b>")
            elif highest_weekly_focus > 3600:
                hours = highest_weekly_focus // 3600
                minutes = (highest_weekly_focus % 3600) // 60
                if minutes == 0:
                    self.ui.highest_weekly_label.setText(f"highest weekly focus: <b>{hours} minutes</b>")
                else:
                    self.ui.highest_weekly_label.setText(f"highest weekly focus: <b>{hours} hours {minutes} minutes</b>")
            else:
                self.ui.highest_weekly_label.setText(f"highest weekly focus: <b>no data</b>")
        else:
            self.ui.highest_weekly_label.setText(f"highest weekly focus: <b>no data</b>")

        if avg_daily_focus  != None:
            if avg_daily_focus  < 3600:
                self.ui.avg_daily_focus.setText(f"avg. daily focus: <b>{int(avg_daily_focus / 60)} minutes</b>")
            elif avg_daily_focus  > 3600:
                hours = avg_daily_focus  // 3600
                minutes = (avg_daily_focus  % 3600) // 60
                if minutes == 0:
                    self.ui.avg_daily_focus.setText(f"avg. daily focus: <b>{int(hours)} minutes</b>")
                else:
                    self.ui.avg_daily_focus.setText(f"avg. daily focus: <b>{int(hours)} hours {int(minutes)} minutes</b>")
            else:
                self.ui.avg_daily_focus.setText(f"avg. daily focus: <b>no data</b>")
        else:
            self.ui.avg_daily_focus.setText(f"avg. daily focus: <b>no data</b>")

        if avg_weekly_focus  != None:
            if avg_weekly_focus  < 3600:
                self.ui.avg_weekly_focus.setText(f"avg. weekly focus: <b>{int(avg_weekly_focus / 60)} minutes</b>")
            elif avg_weekly_focus  > 3600:
                hours = avg_weekly_focus  // 3600
                minutes = (avg_weekly_focus  % 3600) // 60
                if minutes == 0:
                    self.ui.avg_weekly_focus.setText(f"avg. weekly focus: <b>{int(hours)} minutes</b>")
                else:
                    self.ui.avg_weekly_focus.setText(f"avg. weekly focus: <b>{int(hours)} hours {int(minutes)} minutes</b>")
            else:
                self.ui.avg_weekly_focus.setText(f"avg. weekly focus: <b>no data</b>")
        else:
            self.ui.avg_weekly_focus.setText(f"avg. weekly focus: <b>no data</b>")

    def show_karma_and_streaks(self):
        daily_goal = get_daily_goal_achieved()
        self.ui.daily_goal_achieved.setText(f"daily goal achieved: <b>{daily_goal}</b>")

        current_streak = get_current_streak()
        self.ui.current_streak.setText(f"current streak: <b>{current_streak} days</b>")

        self.ui.longest_streak.setText(f"longest streak: <b>{self.longest_streak} days</b>")

        self.current_karma = get_current_karma()
        self.ui.karma.setText(f"karma: <b>{int(self.current_karma)}%</b>")
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

    def set_tooltips(self):
        self.ui.total_focus_time.setToolTip("Total time spent in focus.")
        self.ui.avg_daily_focus.setToolTip("Average focus time per day across all tracked days.")
        self.ui.avg_weekly_focus.setToolTip("Average focus time per week across all tracked weeks.")
        self.ui.focus_sessions_completed.setToolTip("Number of focus sessions completed.")
        self.ui.highest_daily_label.setToolTip("Your highest focus time achieved in a single day.")
        self.ui.highest_weekly_label.setToolTip("Your highest focus time achieved in a single week.")
        self.ui.daily_goal_achieved.setToolTip("Number of days you've met your daily focus goal.")
        self.ui.current_streak.setToolTip("Current streak of consecutive days meeting your goal. Weekdays are required; weekends are optional.")
        self.ui.longest_streak.setToolTip("Your longest streak of consecutive days meeting your goal.")
        self.ui.karma.setToolTip("Score reflecting your consistency in meeting focus goals over the past 2 months.")
        self.ui.most_prod_day.setToolTip("The day of the week when you average the most focus time per session.")

    def set_chart_theme(self):
        self.colors = self.tm.current_theme
        plt.rcParams.update({
            'figure.facecolor': self.colors['card'],
            'axes.facecolor': self.colors['card'],
            'axes.edgecolor': self.colors['text_secondary'],
            'axes.labelcolor': self.colors['text'],
            'text.color': self.colors['text'],
            'xtick.color': self.colors['text'],
            'ytick.color': self.colors['text'],
            'grid.color': self.colors['text_secondary'],
            'legend.facecolor': self.colors['card'],
            'legend.edgecolor': self.colors['text_secondary']
        })
        #self.ui.subjectFrame.setStyleSheet(f"background-color:{self.colors["background"]}")
        self.ui.include_archived_checkbox.setStyleSheet(f"background-color:{self.colors["background"]}")

    # Line chart
    def plot_focus_chart(self):
        self.ui.focusFrame.show()

        # Get data
        rows = get_focus_data()

        if not rows:
            self.ui.focusFrame.hide()
            self.ui.no_data_message.show()
            self.ui.no_data_message.setText(
                "Your statistics will appear here after you complete a focus session."
            )
            return

        # Prepare data: map date -> hours
        row_dict = {row[0]: row[1] / 3600 for row in rows}  # convert seconds to hours

        # Generate last 30 days
        all_days = [datetime.today() - timedelta(days=i) for i in reversed(range(30))]
        all_durations = [row_dict.get(d.strftime('%Y-%m-%d'), 0) for d in all_days]

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(6, 3))

        # Fill area under line for better visibility
        if self.tm.get_theme_name() == "monkmode_dark":
            ax.plot(all_days, all_durations, color="white", linewidth=2)
        elif self.tm.get_theme_name() == "monkmode_light":
             ax.plot(all_days, all_durations, color="black", linewidth=2)
        else:
            ax.plot(all_days, all_durations, color=self.colors["accent"], linewidth=2)

        # Titles and labels
        ax.set_title('daily focus time (last 30 days)', fontweight="bold")
        ax.set_ylabel('focus duration (hours)')

        # Grid for easier reading
        ax.grid(True, linestyle='--', alpha=0.5)

        # Format x-axis with intervals
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))       # every 7 days
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))    # e.g., Oct 13
        ax.tick_params(axis='x', rotation=45, labelsize=8)              # rotate & smaller font

        # Y-axis ticks
        max_val = max(all_durations)
        
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5, prune="lower"))
        ax.set_ylim(0, max(0.5, max_val))

        fig.tight_layout()

        # Embed in Qt canvas
        canvas = ScrollFriendlyCanvas(fig)
        canvas.setMaximumSize(600, 300)
        canvas.setStyleSheet("""
            background: transparent;
            border: none;
        """)

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


    # Pie chart #1
    def plot_subject_chart(self):
        # Show the frame if previously hidden
        self.ui.subjectFrame.show()
        
        # Get data
        rows = get_subject_data_stats()

        # If no data, hide the frame
        if not rows:
            self.ui.subjectFrame.hide()
            return

        # Sort by duration descending (if not already sorted)
        rows.sort(key=lambda x: x[1], reverse=True)

        # Limit to top 10 subjects
        top_rows = rows[:10]

        # Prepare labels and values
        labels = [row[0] for row in top_rows]
        durations = [row[1] / 60 for row in top_rows]  # convert seconds to minutes if needed

        # Create pie chart
        fig, ax = plt.subplots(figsize=(6, 3))
        wedges, texts, autotexts = ax.pie(
            durations,
            autopct=autopct_filter,
            startangle=90,
            textprops={'fontsize': 7}
        )

        plt.close(fig)

        # Add legend 
        ax.legend(
            wedges,
            labels,
            title="subjects",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=8
        )

        ax.set_title('focus time distribution by subject (last 30 days, top 10)', fontweight="bold")

        canvas = ScrollFriendlyCanvas(fig)
        canvas.setMaximumSize(600, 300)
        canvas.setStyleSheet("""
            background: transparent;
            border: none;
        """)

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

        layout.addWidget(canvas, 0)

    # Pie chart #2
    def plot_period_distribution(self):
        self.ui.periodFrame.show()

        # Get data
        rows = get_period_data_stats()

        if not rows:
            self.ui.periodFrame.hide()
            return

        # Sort by duration descending (if not already sorted)
        rows.sort(key=lambda x: x[1], reverse=True)

        # Limit to top 10 periods
        top_rows = rows[:10]

        # Prepare labels and values
        labels = [r[0] for r in top_rows]
        durations = [r[1] / 60 for r in top_rows]  # convert seconds → minutes

        # Create pie chart 
        fig, ax = plt.subplots(figsize=(6, 3))
        wedges, texts, autotexts = ax.pie(
            durations,
            autopct=autopct_filter,
            startangle=90,
            textprops={'fontsize': 7}
        )

        plt.close(fig)

        # Add legend 
        ax.legend(
            wedges,
            labels,
            title="periods",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=8
        )

        ax.set_title('focus time distribution by period (last 30 days, top 10)', fontweight="bold")

        # Prepare frame layout
        layout = self.ui.periodFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.periodFrame.setLayout(layout)
        else:
            # Clear old widgets
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                if w:
                    layout.removeWidget(w)
                    w.setParent(None)

        # Add chart canvas
        canvas = ScrollFriendlyCanvas(fig)
        canvas.setMaximumSize(600, 300)
        canvas.setStyleSheet("""
            background: transparent;
            border: none;
        """)

        layout.addWidget(canvas, 0)
    
    # Bar chart #1
    def plot_subject_bar_chart(self):
        self.ui.subjectBarFrame.show()

        # Get data
        rows = get_subject_time_data()

        if not rows:
            self.ui.subjectBarFrame.hide()
            return

        # Sort by duration descending (if not already sorted)
        rows.sort(key=lambda x: (-x[1], x[0]))

        # Limit to top 15 subjects
        top_rows = rows[:20]

        # Prepare labels and values
        labels = [r[0] for r in top_rows]
        durations = [r[1] / 3600 for r in top_rows]  # convert seconds → hours

        # Pick unique colors (tab20 supports 20 distinct colors)
        cmap = plt.get_cmap("tab20")
        colors = [cmap(i) for i in range(len(labels))]

        # Wrap long labels for better display
        labels = [textwrap.fill(l, 10) for l in labels]

        # Create bar chart
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(labels, durations, color=colors)

        ax.set_ylabel("focus time (hours)")
        ax.set_title("focus time per subject (last 30 days, top 20)", fontweight="bold")

        plt.xticks(rotation=45, ha="center", fontsize=8.5)

        # Adjust Y-axis tick spacing dynamically
        max_val = max(durations)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5, prune="lower"))
        ax.set_ylim(0, max(0.5, max_val))
        fig.subplots_adjust(bottom=0.3)

        plt.close(fig)

        # Clear existing layout before adding new chart
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

        # Add chart to layout
        canvas = ScrollFriendlyCanvas(fig)
        canvas.setMaximumSize(600, 300)
        canvas.setStyleSheet("""
            background: transparent;
            border: none;
        """)
        layout.addWidget(canvas, 0)


    # Bar chart #2
    def plot_subject_bar_chart_allhistory(self):
        self.ui.subjectAllBarFrame.show()
        self.ui.include_archived_checkbox.show()

        # Get data depending on the checkbox
        if self.ui.include_archived_checkbox.isChecked():
            rows = get_subject_time_data_all_include_archived()
        else:
            rows = get_subject_time_data_all_not_include_archived()

        if not rows:
            self.ui.subjectAllBarFrame.hide()
            self.ui.include_archived_checkbox.hide()
            return

        # Sort by duration descending, then alphabetically for tie-breaking
        rows.sort(key=lambda x: (-x[1], x[0]))

        # Limit to top 20 subjects
        top_rows = rows[:20]

        # Prepare labels and values
        labels = [r[0] for r in top_rows]
        durations = [r[1] / 3600 for r in top_rows]  # convert seconds → hours

        # Pick unique colors from tab20 (20 distinct colors)
        cmap = plt.get_cmap("tab20")
        colors = [cmap(i) for i in range(len(labels))]

        # Wrap long labels for readability
        labels = [textwrap.fill(l, 10) for l in labels]

        # Create bar chart
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(labels, durations, color=colors)
        ax.set_ylabel("focus time (hours)")
        ax.set_title("focus time per subject (all history, top 20)", fontweight="bold")

        plt.xticks(rotation=45, ha="center",fontsize=8.5)

        # Dynamic Y-axis tick spacing
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5, prune="lower"))

        max_val = max(durations)
        ax.set_ylim(0, max(0.5, max_val))
        fig.subplots_adjust(bottom=0.3)

        plt.close(fig)

        # Ensure layout exists and clear old chart
        layout = self.ui.subjectAllBarFrame.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.subjectAllBarFrame.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                w = layout.itemAt(i).widget()
                if w:
                    layout.removeWidget(w)
                    w.setParent(None)

        # Add chart canvas to layout
        canvas = ScrollFriendlyCanvas(fig)
        canvas.setMaximumSize(600, 300)
        canvas.setStyleSheet("""
            background: transparent;
            border: none;
        """)
        layout.addWidget(canvas, 0)

# If less then 4% on pie chart then dont show
def autopct_filter(pct):
    return f'{pct:.1f}%' if pct >= 4 else ''

class ScrollFriendlyCanvas(FigureCanvas):
    def wheelEvent(self, event):
        # Forward scroll events to parent scroll area
        if self.parent():
            self.parent().wheelEvent(event)

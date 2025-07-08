from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QMessageBox

class FocusTimer(QObject):
    def __init__(self, period, subject, user_sessions, main_window):
        super().__init__()
        self.period = period
        self.subject = subject
        self.main_window = main_window

        self.sessions_left = user_sessions
        self.long_break_after = self.period["long_break_after"]
        self.is_long_break = 0

        self.remaining_time = period["focus_time"] * 60

        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)

    def start(self):
        self.timer.start(1000)

    def short_break_timer(self):
        pass

    def long_break_timer(self):
        pass

    def pause(self):
        self.timer.stop()
        self.main_window.ui.focus_pause_btn.hide()
        self.main_window.ui.focus_resume_btn.show()

    def resume(self):
        self.timer.start(1000)
        self.main_window.ui.focus_resume_btn.hide()
        self.main_window.ui.focus_pause_btn.show()

    def stop(self):
        pass
    
    def _tick(self):
        self.remaining_time-=1
        self.main_window.update_timer_label(self.remaining_time)

        if self.remaining_time <= 0:
            self.timer.stop()
            self.sessions_left-=1

    def save_focus_sessions(self):
        pass
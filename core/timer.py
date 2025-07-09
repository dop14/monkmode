from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QMessageBox

class FocusTimer(QObject):
    def __init__(self, period, subject, user_sessions, main_window):
        super().__init__()
        self.period = period
        self.subject = subject
        self.main_window = main_window
        
        self.total_sessions = user_sessions
        self.sessions_left = user_sessions # How many session we have left
        self.long_break_after = self.period["long_break_after"] # After how many focus sessions do we have a long break
        self.completed_focus_sessions = 0 # How many focus sessions we've completed
        self.is_break = False # Are we on a break?

        # Start focus session (the first is always a focus session)
        self.remaining_time = period["focus_time"] * 60
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.main_window.ui.period_type_label.show()
        self.main_window.ui.period_type_label.setText(f"Focus period ({self.completed_focus_sessions+1} of {self.total_sessions})")

    def start_focus_session(self):
        self.is_break = False
        self.remaining_time = self.period["focus_time"] * 60
        self.main_window.ui.period_type_label.setText(f"Focus period ({self.completed_focus_sessions+1} of {self.total_sessions})")
        self.timer.start(1000)

    def start_break_session(self):
        self.is_break = True
        # If long break is next
        if self.completed_focus_sessions % self.long_break_after == 0:
            self.remaining_time = self.period["long_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"Break ({self.completed_focus_sessions} of {self.total_sessions-1})")
        # If short break is next
        else:
            self.remaining_time = self.period["short_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"Break ({self.completed_focus_sessions} of {self.total_sessions-1})")
        self.timer.start(1000)

    def _tick(self):
        self.remaining_time-=1
        self.main_window.update_timer_label(self.remaining_time)
        
        # If the timer has stopped
        if self.remaining_time <= 0:
            # Stop the timer
            self.pause()
            # If we're in a break
            if self.is_break:
                # Start the focus session
                self.start_focus_session()
            # If we're not in a break
            else:
                self.completed_focus_sessions+=1
                self.sessions_left-=1
                # If no sessions left
                if self.sessions_left == 0:
                    self.main_window.focus_ended()
                    return
                # Start a break session
                self.start_break_session()
                
    def start(self):
        self.timer.start(1000)

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.main_window.ui.focus_pause_btn.hide()
            self.main_window.ui.focus_resume_btn.show()

    def resume(self):
        self.timer.start(1000)
        self.main_window.ui.focus_resume_btn.hide()
        self.main_window.ui.focus_pause_btn.show()

    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
    
    def save_focus_session(self):
        # save focus sessions via self.completed_focus_sessions
        pass

    def save_focus_session_stopped(self):
        # save focus sessions via focus_time = total_time - remaning_time
        pass

    def play_sound(self):
        pass
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QMessageBox
from database.db_manager import save_focus_session_db, get_user_preferences
from core.sound_player import SoundPlayer

class FocusTimer(QObject):
    def __init__(self, period, subject, user_sessions, main_window):
        super().__init__()
        self.period = period
        self.subject = subject
        self.main_window = main_window
        
        self.total_sessions = user_sessions
        self.sessions_left = user_sessions 
        self.long_break_after = self.period["long_break_after"] 
        self.completed_focus_sessions = 0 
        self.is_break = False 

        preferences = get_user_preferences()
        self.notifications = preferences["all_notifications_off"]

        # Start focus session (the first is always a focus session)
        if not self.notifications:
            self.play_sound("focus")
        self.remaining_time = period["focus_time"] * 60
        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)
        self.main_window.ui.period_type_label.show()
        self.main_window.ui.period_type_label.setText(f"Focus session ({self.completed_focus_sessions+1} of {self.total_sessions})")

    def start_focus_session(self):
        self.is_break = False
        self.remaining_time = self.period["focus_time"] * 60
        self.main_window.ui.period_type_label.setText(f"Focus session ({self.completed_focus_sessions+1} of {self.total_sessions})")
        self.timer.start(1000)

    def start_break_session(self):
        self.is_break = True
        # If long break is next
        if self.long_break_after != 0 and self.completed_focus_sessions % self.long_break_after == 0 and self.long_break_after:
            self.remaining_time = self.period["long_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"Break ({self.completed_focus_sessions} of {self.total_sessions-1})")
        # If short break is next
        else:
            self.remaining_time = self.period["short_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"Break ({self.completed_focus_sessions} of {self.total_sessions-1})")
        self.timer.start(1000)

    def _tick(self):
        self.remaining_time-=1
        self.update_timer_label(self.remaining_time)
        
        # If the timer has stopped
        if self.remaining_time <= 0:
            # Stop the timer
            self.stop()
            # If we're in a break
            if self.is_break:
                # Play sound if notifications are on
                if not self.notifications:
                    self.play_sound("focus")
                # Start the focus session
                self.start_focus_session()
            # If we're not in a break
            else:
                self.completed_focus_sessions+=1
                self.sessions_left-=1
                self.save_focus_session()
                # If no sessions left
                if self.sessions_left == 0:
                    # TODO: play end sound
                    self.main_window.focus_ended()
                    return
                # Play sound if notifications are on
                if not self.notifications:
                    self.play_sound("break")
                # Start a break session
                self.start_break_session()
    
    def update_timer_label(self, remaining_time):
        # Format it to hours, minutes, seconds
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Show time
        self.main_window.ui.timer_label.setText(f"{hours}:{minutes}:{seconds}")
                
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
        self.focus_time = self.period["focus_time"] * 60
    
        # save data to db
        focus_session = {
            "subject_id": self.subject[0],
            "period_id": self.period["id"],
            "duration":  self.focus_time,
        }
        
        # call db function
        save_focus_session_db(focus_session)

    def save_focus_stopped_session(self):
        self.focus_time = self.period["focus_time"] * 60
        focus_time_unfinished_session = self.focus_time - self.remaining_time
        # If user spent more than one minute in focus in the unfinished session
        if not self.is_break and focus_time_unfinished_session > 60:
                # save data to db
                focus_session = {
                    "subject_id": self.subject[0],
                    "period_id": self.period["id"],
                    "duration": focus_time_unfinished_session,
                }
            

                # call db function
                save_focus_session_db(focus_session)
     
    def play_sound(self, sound_type):
        self.sound = SoundPlayer(sound_type)
        self.sound.play()

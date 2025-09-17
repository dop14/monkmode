from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QMessageBox
from database.db_manager import save_focus_session_db, get_user_preferences, get_user_stats, update_user_stats
from core.sound_player import SoundPlayer
from core.popup_notification import PopupNotification

class FocusTimer(QObject):
    def __init__(self, period, subject, user_sessions, main_window, small_window):
        super().__init__()
        self.period = period
        self.subject = subject
        self.main_window = main_window
        self.small_window = small_window
        
        self.total_sessions = user_sessions
        self.sessions_left = user_sessions 
        self.long_break_after = self.period["long_break_after"] 
        self.completed_focus_sessions = 0 
        self.is_break = False 
        self.focus_lenght = self.period["focus_time"] 
    
        preferences = get_user_preferences()
        self.notifications = preferences["all_notifications_off"]

        self.main_window.ui.start_focus_btn.setDisabled(True)

        self.remaining_time = 0
        self.focus_delay()


        self.timer = QTimer()
        self.timer.timeout.connect(self._tick)

    def start_focus_session(self):
        self.is_break = False
        self.main_window.is_delay_timer = False

        self.main_window.ui.focus_pause_btn.show()
        self.main_window.ui.focus_stop_btn.show()
        self.main_window.ui.small_focus_window.show()
        self.main_window.ui.period_type_label.setText(f"focus session ({self.completed_focus_sessions+1} of {self.total_sessions})")
        self.small_window.ui.session_label.setText(f"focus session ({self.completed_focus_sessions+1} of {self.total_sessions})")
        self.main_window.ui.period_type_label.show()
        self.main_window.ui.timer_label.setStyleSheet("font-size: 46px;")
    
        if not self.notifications:
            self.play_sound("focus")
            self.show_popup("focus")

        self.remaining_time = self.period["focus_time"] * 60
        self.update_timer_label(self.remaining_time)
        self.timer.start(1000)

    def start_break_session(self):
        self.is_break = True
        self.main_window.is_delay_timer = False

        self.main_window.ui.focus_pause_btn.show()
        self.main_window.ui.focus_stop_btn.show()
        self.main_window.ui.small_focus_window.show()
        self.main_window.ui.period_type_label.show()
        self.main_window.ui.timer_label.setStyleSheet("font-size: 46px;")

        if not self.notifications:
            self.play_sound("break")
            self.show_popup("break")
        # If long break is next
        if self.long_break_after != 0 and self.completed_focus_sessions % self.long_break_after == 0 and self.long_break_after:
            self.remaining_time = self.period["long_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"break ({self.completed_focus_sessions} of {self.total_sessions-1})")
            self.small_window.ui.session_label.setText(f"break ({self.completed_focus_sessions} of {self.total_sessions-1})")
            self.update_timer_label(self.remaining_time)
        # If short break is next
        else:
            self.remaining_time = self.period["short_break_time"] * 60
            self.main_window.ui.period_type_label.setText(f"break ({self.completed_focus_sessions} of {self.total_sessions-1})")
            self.small_window.ui.session_label.setText(f"break ({self.completed_focus_sessions} of {self.total_sessions-1})")
            self.update_timer_label(self.remaining_time)
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
                # Start the focus session
                self.focus_delay()
            # If we're not in a break
            else:
                self.completed_focus_sessions+=1
                self.sessions_left-=1
                self.save_focus_session()
                # If no sessions left
                if self.sessions_left == 0:
                    if not self.notifications:
                        self.play_sound("break")
                        self.show_popup("end")
                    self.main_window.focus_ended()
                    return
                # Start a break session
                self.break_delay()
    
    def update_timer_label(self, remaining_time):
        # Format it to hours, minutes, seconds
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # If less than an hour
        if remaining_time < 3600:
            self.main_window.ui.timer_label.setText(f"{minutes:02}:{seconds:02}")
            self.small_window.ui.time_label.setText(f"{minutes:02}:{seconds:02}") 
        else:
            self.main_window.ui.timer_label.setText(f"{hours}:{minutes:02}:{seconds:02}")
            self.small_window.ui.time_label.setText(f"{hours}:{minutes:02}:{seconds:02}")

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
        
        # Save statistics
        old_stats = get_user_stats()
        # collect data 
        if self.focus_time > old_stats[2]:
            self.longest_session = self.focus_time
        else:
            self.longest_session = old_stats[2]

        new_stats = {
            "total_focus_time_mins": old_stats[0] + self.focus_time,
            "focus_sessions_completed": old_stats[1] + 1,
            "longest_focus_session": self.longest_session,
            "longest_streak": old_stats[3]
        }

        update_user_stats(new_stats)

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

                # Save statistics
                old_stats = get_user_stats()
                # check if this was longest session
                if focus_time_unfinished_session > old_stats[2]:
                    self.longest_session = focus_time_unfinished_session
                else:
                    self.longest_session = old_stats[2]

                # save new stats
                new_stats = {
                    "total_focus_time_mins": old_stats[0] + focus_time_unfinished_session,
                    "focus_sessions_completed": old_stats[1],
                    "longest_focus_session": self.longest_session,
                    "longest_streak": old_stats[3]
                }
                update_user_stats(new_stats)

    def play_sound(self, sound_type):
        self.sound = SoundPlayer(sound_type)
        self.sound.play()

    def show_popup(self, popup_type):
        if popup_type == "focus":
            self.popup = PopupNotification("Focus session has started!")
            self.popup.show_notification()
            
        elif popup_type == "break":
            self.popup = PopupNotification("Break session has started!")
            self.popup.show_notification()
        else:
            self.popup = PopupNotification("Focus done! Great job.")
            self.popup.show_notification()

    def focus_delay(self):
        self.main_window.is_delay_timer = True
        self.focus_delay_time = 5

        self.small_window.delay_starts()

        if not self.notifications:
            self.popup = PopupNotification(f"Focus session starts in {self.focus_delay_time}")
            self.popup.show_notification()

        self.main_window.ui.timer_label.setText(f"Focus session starts in {self.focus_delay_time}")

        self.small_window.ui.time_label.setText(f"Focus in {self.focus_delay_time}")

        self.main_window.ui.timer_label.setStyleSheet("font-size: 20px;")
        self.main_window.ui.focus_pause_btn.hide()
        self.main_window.ui.focus_stop_btn.hide()
        self.main_window.ui.period_type_label.hide()
        self.main_window.ui.small_focus_window.hide()
        
        self.focus_timer_delayed = QTimer()
        self.focus_timer_delayed.start(1000)
        self.focus_timer_delayed.timeout.connect(self.focus_delay_tick)

    def focus_delay_tick(self):
        self.focus_delay_time -=1
        self.main_window.ui.timer_label.setText(f"Focus session starts in {self.focus_delay_time}")

        self.small_window.ui.time_label.setText(f"Focus in {self.focus_delay_time}")

        if not self.notifications:
            self.popup.update_message(f"Focus session starts in {self.focus_delay_time}")

        if self.focus_delay_time == 0:
            self.focus_timer_delayed.stop()
            self.small_window.delay_ends()
            self.start_focus_session()

    def break_delay(self):
        self.main_window.is_delay_timer = True
        self.break_delay_time = 5

        self.small_window.delay_starts()

        if not self.notifications:
            self.popup = PopupNotification(f"Break starts in {self.break_delay_time}")
            self.popup.show_notification()

        self.main_window.ui.timer_label.setText(f"Break starts in {self.break_delay_time}")

        self.small_window.ui.time_label.setText(f"Break in {self.break_delay_time}")


        self.main_window.ui.timer_label.setStyleSheet("font-size: 20px;")
        self.main_window.ui.focus_pause_btn.hide()
        self.main_window.ui.focus_stop_btn.hide()
        self.main_window.ui.period_type_label.hide()
        self.main_window.ui.small_focus_window.hide()

        self.break_timer_delayed = QTimer()
        self.break_timer_delayed.start(1000)
        self.break_timer_delayed.timeout.connect(self.break_delay_tick)

    def break_delay_tick(self):
        self.break_delay_time -=1   
        self.main_window.ui.timer_label.setText(f"Break starts in {self.break_delay_time}")

        self.small_window.ui.time_label.setText(f"Break in {self.break_delay_time}")

        if not self.notifications:
            self.popup.update_message(f"Break starts in {self.break_delay_time}")

        if self.break_delay_time == 0:
            self.break_timer_delayed.stop()
            self.small_window.delay_ends()
            self.start_break_session()





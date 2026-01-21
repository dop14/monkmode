import qtawesome as qta

class IconManager:
    def __init__(self):
         self.icons = {}
    
    def build(self, color):
        self.icons["add"] = qta.icon('fa5s.plus',color=color)  
        self.icons["edit"] = qta.icon('fa5s.edit',color=color)
        self.icons["delete"] = qta.icon('fa5s.trash',color=color) 
        self.icons["archive"] = qta.icon('fa5s.archive',color=color)  

        self.icons["pause"] = qta.icon('fa5s.pause',color=color)  
        self.icons["resume"] = qta.icon('fa5s.play',color=color) 
        self.icons["stop"] = qta.icon('fa5s.stop',color=color)   

        self.icons["fullscreen"] = qta.icon('fa5s.expand',color=color)  
        self.icons["smallscreen"] = qta.icon('fa5s.compress',color=color)         

    def apply_icons(self, main_window, small_window):
        # Main window icons
        main_window.ui.newperiod_btn.setIcon(self.icons["add"])
        main_window.ui.editperiod_btn.setIcon(self.icons["edit"])
        main_window.ui.delete_period_btn.setIcon(self.icons["delete"])

        main_window.ui.newsubject_btn.setIcon(self.icons["add"])
        main_window.ui.edit_subject_btn.setIcon(self.icons["edit"])
        main_window.ui.delete_subject_btn.setIcon(self.icons["delete"])
        main_window.ui.archive_subject_btn.setIcon(self.icons["archive"])

        main_window.ui.focus_pause_btn.setIcon(self.icons["pause"])
        main_window.ui.focus_resume_btn.setIcon(self.icons["resume"])
        main_window.ui.focus_stop_btn.setIcon(self.icons["stop"])
        main_window.ui.small_focus_window.setIcon(self.icons["smallscreen"])

        # Small view icons
        small_window.ui.back_to_main_btn.setIcon(self.icons["fullscreen"])
        small_window.ui.small_pause_btn.setIcon(self.icons["pause"])
        small_window.ui.small_resume_btn.setIcon(self.icons["resume"])
        small_window.ui.small_stop_btn.setIcon(self.icons["stop"])

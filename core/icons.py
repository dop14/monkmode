import qtawesome as qta

class IconManager:
    def __init__(self, main_window, small_window):
        # UI icons
        self.add_icon = qta.icon('fa5s.plus')             
        self.edit_icon = qta.icon('fa5s.edit')             
        self.delete_icon = qta.icon('fa5s.trash')          
        self.archive_icon = qta.icon('fa5s.archive')      

        # Media controls
        self.pause_icon = qta.icon('fa5s.pause')           
        self.resume_icon = qta.icon('fa5s.play')           
        self.stop_icon = qta.icon('fa5s.stop')             

        # Screen controls
        self.fullscreen_icon = qta.icon('fa5s.expand')     
        self.smallscreen_icon = qta.icon('fa5s.compress')  

        self.set_icons(main_window, small_window)

    def set_icons(self, main_window, small_window):
        # Main window icons
        main_window.ui.newperiod_btn.setIcon(self.add_icon)
        main_window.ui.editperiod_btn.setIcon(self.edit_icon)
        main_window.ui.delete_period_btn.setIcon(self.delete_icon)

        main_window.ui.newsubject_btn.setIcon(self.add_icon)
        main_window.ui.edit_subject_btn.setIcon(self.edit_icon)
        main_window.ui.delete_subject_btn.setIcon(self.delete_icon)
        main_window.ui.archive_subject_btn.setIcon(self.archive_icon)

        main_window.ui.focus_pause_btn.setIcon(self.pause_icon)
        main_window.ui.focus_resume_btn.setIcon(self.resume_icon)
        main_window.ui.focus_stop_btn.setIcon(self.stop_icon)
        main_window.ui.small_focus_window.setIcon(self.smallscreen_icon)

        # Small view icons
        small_window.ui.back_to_main_btn.setIcon(self.fullscreen_icon)
        small_window.ui.small_pause_btn.setIcon(self.pause_icon)
        small_window.ui.small_resume_btn.setIcon(self.resume_icon)
        small_window.ui.small_stop_btn.setIcon(self.stop_icon)

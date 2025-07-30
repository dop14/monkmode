from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from ui_py.small_focus_window import Ui_Form

class SmallFocusWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("small view")
        self.main_window = main_window
        self.setWindowFlags(
            Qt.Window | 
            Qt.WindowStaysOnTopHint
        )

        self.top_right_position()

        # Hide buttons
        self.ui.hidden_text.hide()
        self.ui.small_resume_btn.hide()
        self.ui.show_time_btn.hide()

        # Button actions
        self.ui.back_to_main_btn.clicked.connect(self.closeEvent)
        self.ui.small_pause_btn.clicked.connect(self.pause_timer)
        self.ui.small_resume_btn.clicked.connect(self.resume_timer)
        self.ui.small_stop_btn.clicked.connect(self.stop_timer)
        self.ui.unshow_time_btn.clicked.connect(self.unshow_time)
        self.ui.show_time_btn.clicked.connect(self.show_time)
        
    def top_right_position(self):
        screen_geometry = self.screen().availableGeometry()
        window_size = self.size()
        x = screen_geometry.right() - window_size.width() - 20  
        y = screen_geometry.top() + 20                          
        self.move(x, y)

    def closeEvent(self, event):
        self.close()
        self.main_window.showNormal()

    def pause_timer(self):
        self.main_window.focus_timer.pause()
        self.ui.small_pause_btn.hide()
        self.ui.small_resume_btn.show()
    
    def resume_timer(self):
        self.main_window.focus_timer.resume()
        self.ui.small_pause_btn.show()
        self.ui.small_resume_btn.hide()

    def stop_timer(self):
        self.close()
        self.main_window.showNormal()
        self.main_window.stop_focus_confirmation()

    def unshow_time(self):
        self.ui.unshow_time_btn.hide()
        self.ui.show_time_btn.show()

        self.ui.time_label.hide()
        self.ui.hidden_text.show()

    def show_time(self):
        self.ui.show_time_btn.hide()
        self.ui.unshow_time_btn.show()

        self.ui.hidden_text.hide()
        self.ui.time_label.show()


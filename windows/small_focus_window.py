from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from ui_py.small_focus_window import Ui_Form
from PySide6.QtGui import QIcon, QPixmap
from utils import get_resource_path

class SmallFocusWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("small view")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
        self.main_window = main_window
        self.setWindowFlags(
            Qt.Window | 
            Qt.WindowStaysOnTopHint
        )

        self.top_right_position()
        
        self.monk_image()
        self.image_label.hide()

        self.ui.time_label.mousePressEvent = self.toggle_timer_image
        self.image_label.mousePressEvent = self.toggle_timer_image


        # Button actions
        self.ui.back_to_main_btn.clicked.connect(self.closeEvent)
        self.ui.small_pause_btn.clicked.connect(self.pause_timer)
        self.ui.small_resume_btn.clicked.connect(self.resume_timer)
        self.ui.small_stop_btn.clicked.connect(self.stop_timer)
        
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

    def toggle_timer_image(self, event):
        if self.ui.time_label.isVisible():
            self.ui.time_label.hide()
            self.image_label.show()
        else:
            self.image_label.hide()
            self.ui.time_label.show()

    # Hiding buttons in small focus window
    def default_values(self):
        # Hide buttons                          
        self.ui.small_resume_btn.hide()

        # Show buttons
        self.ui.small_pause_btn.show()
        self.ui.time_label.show()
        self.ui.session_label.show()
        self.image_label.hide()

    def focus_over(self):
        self.close()
        self.main_window.showNormal()
    
    def monk_image(self, width=100, height=120):
        # Create image label
        self.image_label = QLabel()
        pixmap = QPixmap(get_resource_path("logo/monk.png"))
        scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Add image_label to the Designer-created layout
        self.ui.image_layout.addWidget(self.image_label)

        return self.image_label
    
    def delay_starts(self):
        self.ui.small_pause_btn.hide()
        self.ui.small_stop_btn.hide()
        self.ui.session_label.setText("")
        self.ui.time_label.setStyleSheet("font-size: 32px;")

    def delay_ends(self):
        self.ui.small_pause_btn.show()
        self.ui.small_stop_btn.show()
        self.ui.time_label.setStyleSheet("font-size: 48px;")
    



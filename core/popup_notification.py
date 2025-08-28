from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

class PopupNotification(QWidget):
    def __init__(self, message, duration=5000):
        super().__init__()
        self.setWindowFlags(
            Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.message = message

        layout = QVBoxLayout()
        self.label = QLabel(message)
        self.label.setFont(QFont("Segoe UI", 13))
        self.label.setStyleSheet("""
            QLabel {
                background-color: #333;
                color: white;
                padding: 20px 30px;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.adjustSize()

        # Position in bottom left corner
        screen_geometry = self.screen().availableGeometry()
        x = screen_geometry.right() - self.width() - 20
        y = screen_geometry.bottom() - self.height() - 50
        self.move(x, y)

        QTimer.singleShot(duration, self.close)

    def show_notification(self):
        self.show()

    def update_message(self, new_message):
        self.label.setText(new_message)

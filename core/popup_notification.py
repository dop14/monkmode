from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtWidgets import QApplication

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

        is_dark_mode = self.is_dark_mode()
        if is_dark_mode:
            self.label.setStyleSheet("""
            QLabel {
                background-color: #333;
                color: white;
                padding: 20px 30px;
                border-radius: 15px;
            }
        """)
        else:
            self.label.setStyleSheet("""
            QLabel {
                background-color: white;
                color: black;
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
        y = screen_geometry.bottom() - self.height() - 25
        self.move(x, y)

        QTimer.singleShot(duration, self.close)

    def show_notification(self):
        self.show()

    def update_message(self, new_message):
        self.label.setText(new_message)

    def is_dark_mode(app: QApplication) -> bool:
        palette: QPalette = app.palette()
        color: QColor = palette.color(QPalette.Window)
        luminance = 0.2126 * color.redF() + 0.7152 * color.greenF() + 0.0722 * color.blueF()
        return luminance < 0.5  # return true if dark mode, false if light mode

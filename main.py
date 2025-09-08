from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from database.db_manager import initialize_db
from windows.mainwindow import MainWindow
from utils import get_resource_path
import sys

# Application entry point
def main():
    initialize_db()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
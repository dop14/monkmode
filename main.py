from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

# Loading the UI dynamically
def load_ui():
    loader = QUiLoader()
    file = QFile("ui/mainwindow.ui")
    file.open(QFile.ReadOnly)
    window = loader.load(file)
    file.close()
    return window

def main():
    app = QApplication(sys.argv)
    window = load_ui()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

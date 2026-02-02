from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from ui_py.about import Ui_Form
from utils import get_resource_path

class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("about")
        self.setWindowIcon(QIcon(get_resource_path("logo/monkmode.png")))
        
        # Show about text
        self.set_text()

    def set_text(self):
        self.ui.about_text.setText(
            """
        <h2>monkmode</h2>
        <p>Stay focused with monkmode - track your focus sessions and breaks<br> efficiently while creating custom focus periods and subjects.</p>
        <p><b>Version:</b> 1.2.2</p>

        <p><b>Developed by:</b> 
            <a href="https://github.com/dop14">dop14</a>
        </p>

        <p><b>Built with:</b> Python, PySide6, Qt Designer, and SQLite</p>

        <p><b>Credits:</b></p>
        <ul>
            <li>Quotes provided by <a href="https://zenquotes.io/">ZenQuotes API</a></li>
            <li>Logo created with ChatGPT-5</li>
            <li>Testing and ideas by: <a href="https://github.com/zsoci1">zsoci1</a></li>
        </ul>

        <p><b>License:</b> This project is licensed under the 
            <a href="https://opensource.org/licenses/MIT">MIT License</a>.
        </p>

        <p><b>Third-party software:</b> This application uses <b>PySide6 (Qt for Python)</b>,<br> which is licensed under the
            <a href="https://www.gnu.org/licenses/lgpl-3.0.html">GNU LGPL v3</a>.<br>
            Source code is available at the GitHub repository below.
        </p>

        <p><b>Support:</b> For issues, suggestions, or contributions, visit the 
            <a href="https://github.com/dop14/monkmode">GitHub repository</a>.
        </p>

            """
        )

        # Make links clickable
        self.ui.about_text.setOpenExternalLinks(True)
from PySide6.QtWidgets import QDialog
from ui_py.about import Ui_Form
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("about")
        
        self.setWindowIcon(QIcon("logo/monkmode.png"))

        self.link_labels()

    def link_labels(self):
        self.ui.about_text.setText(
            """
        <h2>monkmode</h2>
        <p><b>Version:</b> 1.0</p>
        <p><b>About: </b>monkmode helps you focus by tracking your sessions and breaks efficiently;<br> it also allows you to create custom focus periods and subjects.</p>

        <p><b>Developed by:</b> 
            <a href="https://github.com/dop14">dop14</a>
        </p>

        <p><b>Built with:</b> Python, PySide6, Qt Designer, and SQLite</p>

        <p><b>Credits:</b></p>
        <ul>
            <li>Quotes provided by <a href="https://zenquotes.io/">ZenQuotes API</a></li>
            <li>Logo created with ChatGPT-5</li>
        </ul>

        <p><b>License:</b> This project is licensed under the 
            <a href="https://opensource.org/licenses/MIT">MIT License</a>.
        </p>

        <p><b>Support:</b> For issues, suggestions, or contributions, visit the 
            <a href="https://github.com/dop14/monkmode">GitHub repository</a>.
        </p>

            """
        )

        # Make links clickable
        self.ui.about_text.setOpenExternalLinks(True)


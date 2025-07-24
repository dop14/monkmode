from PySide6.QtGui import QPalette, QColor

class ThemeManager:
    def load_dark_palette():
        palette = QPalette()
        #palette.setColor(QPalette.Window, QColor("#1e1e1e"))
        #palette.setColor(QPalette.Base, QColor("#2c2c2c"))
        #palette.setColor(QPalette.AlternateBase, QColor("#3c3c3c"))
        #palette.setColor(QPalette.Text, QColor("#ffffff"))
        #palette.setColor(QPalette.Button, QColor("#444444"))
        #palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        #palette.setColor(QPalette.BrightText, QColor("#ff0000"))
        palette.setColor(QPalette.Link, QColor("#2a82da"))
        #palette.setColor(QPalette.Highlight, QColor("#2a82da"))
        #palette.setColor(QPalette.HighlightedText, QColor("#000000"))
        return palette

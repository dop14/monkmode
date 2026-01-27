from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings

class ThemeManager:
    def __init__(self):
        self.settings = QSettings("monkmode", "monkmode")

        self.themes = {
            "monkmode_dark": {
                "background": "#1E1E1E",
                "card": "#2D2D2D",
                "accent": "#6C6C6C",
                "accent_text": "#ffffff",
                "text": "#ffffff",
                "text_secondary": "#b0b0b0",
                "progress_bg": "#3F3F3F"
            },
            "monkmode_light": {
                "background": "#f0f0f0",
                "card": "#ffffff",
                "accent": "#A2A2A2",
                "accent_text": "#000000",
                "text": "#000000",
                "text_secondary": "#707070",
                "progress_bg": "#f6f3f3"
            },
            "focus_fire": {
                "background": "#1a1a1a",
                "card": "#262626",
                "accent": "#ff9500",
                "accent_text": "#000000",
                "text": "#ffffff",
                "text_secondary": "#a0a0a0",
                "progress_bg": "#333333"
            },
            "zen_garden": {
                "background": "#1c1e1a",
                "card": "#252822",
                "accent": "#7fb069",
                "accent_text": "#1c1e1a",
                "text": "#e8f0e3",
                "text_secondary": "#8a9484",
                "progress_bg": "#2f342b"
            },
            "deep_focus": {
                "background": "#0f1419",
                "card": "#1a1f26",
                "accent": "#00a8ff",
                "accent_text": "#0f1419",
                "text": "#f5f5f5",
                "text_secondary": "#8a8f98",
                "progress_bg": "#252a33"
            },
            "dawn_ritual": {
                "background": "#1a1816",
                "card": "#252220",
                "accent": "#ff6b6b",
                "accent_text": "#1a1816",
                "text": "#fef4f0",
                "text_secondary": "#b39f96",
                "progress_bg": "#332e2c"
            }
        }
        
        # The default theme
        self.theme_name = self.settings.value("theme", "monkmode_dark")

        # Hex values of the current theme
        self.current_theme = self.themes[self.theme_name]
    
    def get_theme_name(self):
        return self.theme_name
    
    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme_name = theme_name
            self.current_theme = self.themes[theme_name]
            
            # Save to QSettings
            self.settings.setValue("theme", theme_name)
            
            # Apply to app
            app = QApplication.instance()
            app.setStyleSheet(self.get_stylesheet())

            return True
        return False
    
    def apply_initial_theme(self):
        app = QApplication.instance()
        app.setStyleSheet(self.get_stylesheet())

    def get_stylesheet(self):
        return f"""
            QMainWindow {{
                background-color: {self.current_theme['background']};
            }}
            
            QWidget {{
                background-color: {self.current_theme['background']};
                color: {self.current_theme['text']};
            }}
            
            QFrame {{
                background-color: {self.current_theme['card']};
                border-radius: 8px;
            }}

            QFrame:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QComboBox:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QPushButton:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QSpinBox:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QMenuBar:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QProgressBar:disabled {{
                color:{self.current_theme["text_secondary"]};
            }}

            QToolTip {{
                background-color: {self.current_theme['card']};
                color:{self.current_theme["text"]};
            }}
    
            QPushButton {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                border: 1px solid;
                border-color: {self.current_theme['accent']};
                border-radius: 4px;
                padding: 4px 12px;
            }}
            
            QPushButton:hover {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
            }}
            
            QPushButton#start_focus_btn {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['text']};
                font-weight: bold;
                padding: 16px 48px;
                border:1px solid {self.current_theme['accent']};
            }}

            #PopupNotification QLabel {{
                background-color: {self.current_theme['background']};
                color: {self.current_theme['text']};
                padding: 20px 30px;
                border-radius: 15px;
                
            }}

            QSpinBox {{
                background-color: {self.current_theme['background']};
                height:20px;
            }}

            QSpinBox::up-button, QSpinBox::down-button {{
                width: 20px;
            }}

            QCheckBox:checked {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                padding: 2px;
            }}

            QCheckBox:unchecked {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                padding: 2px;
            }}

            #all_history_checkbox {{
                background-color: {self.current_theme['background']};
                color: {self.current_theme['text']};
                padding: 2px;
             }}

            QPushButton#start_focus_btn:hover {{
                color: {self.current_theme['accent_text']};
                border:1px solid {self.current_theme['accent_text']};
            }}
            
            QLabel {{
                background-color: transparent;
                color: {self.current_theme['text']};
            }}
            
            QProgressBar {{
                background-color: {self.current_theme['progress_bg']};
                border: none;
                border-radius: 4px;
                text-align: center;
            }}
            
            QProgressBar::chunk {{
                background-color: {self.current_theme['accent']};
                border-radius: 4px;
            }}
            
            QMenuBar {{
                color: {self.current_theme['text']};
                font-size:13px;
            }}
            
            QMenuBar::item:selected {{
                background-color: {self.current_theme['accent']};
            }}
            
            QMenu {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                border: 2px solid {self.current_theme['background']};
            }}
            
            QMenu::item {{
                padding:5px 5px 5px 5px;
            }}
            
            QMenu::item:selected {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
            }}
            
            QLineEdit, QTextEdit {{
                background-color: {self.current_theme['background']};
                color: {self.current_theme['text']};
                border: 1px solid {self.current_theme['text_secondary']};
                border-radius: 4px;
                padding: 4px;
            }}

            QComboBox {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                border: 1px solid {self.current_theme['accent']};
                border-radius: 4px;
                padding: 2px;
            }}

            QComboBox:hover {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
            }}


            QComboBox QAbstractItemView {{
                outline: 0;
                border: none;
                margin-top: 3px;
            }}

            QComboBox QAbstractItemView::item {{
                padding:0px;
                border-radius: 4px;
                background-color:{self.current_theme['background']};
            }}

            QComboBox QAbstractItemView::item:selected {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
                border: none;
            }}

            QComboBox::drop-down {{
                background: transparent;
            }}

            QScrollBar:vertical {{
                background: {self.current_theme['background']};
                width: 14px;
                margin: 0px;
                border: none;
            }}

            QScrollBar::handle:vertical {{
                background: {self.current_theme['accent']};
                min-height: 20px;
                border: none;
                border-radius: 6px;
            }}

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {{
                background: none;
                border: none;
                height: 0px;
            }}

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {{
                background: {self.current_theme['card']};
                border: none;
            }}  
        """


    
    

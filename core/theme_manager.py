class ThemeManager:
    def __init__(self):

        self.themes = {
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
            },
            "minimal_monk": {
                "background": "#0a0a0a",
                "card": "#1a1a1a",
                "accent": "#ffffff",
                "accent_text": "#0a0a0a",
                "text": "#e0e0e0",
                "text_secondary": "#808080",
                "progress_bg": "#2a2a2a"
            }
        }

        self.current_theme_name = "dawn_ritual"
        self.current_theme = self.themes[self.current_theme_name]

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
            
            QPushButton {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                border: 1px solid;
                border-color: {self.current_theme['accent']};
                border-radius: 4px;
                padding: 8px 16px;
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
                background-color: {self.current_theme['background']};
                color: {self.current_theme['text']};
            }}
            
            QMenuBar::item:selected {{
                background-color: {self.current_theme['card']};
            }}
            
            QMenu {{
                background-color: {self.current_theme['card']};
                color: {self.current_theme['text']};
                border: 1px solid {self.current_theme['accent']};
            }}
            
            QMenu::item:selected {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
            }}
            
            
            QLineEdit, QTextEdit {{
                background-color: {self.current_theme['card']};
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

            QComboBox QAbstractItemView {{
                selection-background-color: {self.current_theme['accent']};
                selection-color: {self.current_theme['accent_text']};
                outline: 0;
            }}

            QComboBox QAbstractItemView::item {{
                padding: 2px 4px;
                border: none;
            }}

            QComboBox QAbstractItemView::item:selected {{
                background-color: {self.current_theme['accent']};
                color: {self.current_theme['accent_text']};
                border: none;
            }}

            QComboBox::drop-down {{
                    background: transparent;
            }}

        """


    
    

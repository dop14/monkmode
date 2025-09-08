import sys
import os
import sqlite3
from pathlib import Path

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_db_path():
    """Get the database path in user's app data directory"""
    if os.name == 'nt':  # Windows
        app_data = os.path.join(os.environ['APPDATA'], 'MonkMode')
    else:  # Linux/Mac
        app_data = os.path.join(Path.home(), '.monkmode')
    
    # Create directory if it doesn't exist
    os.makedirs(app_data, exist_ok=True)
    return os.path.join(app_data, 'monkmode.db')
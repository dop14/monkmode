import sys
import os
from pathlib import Path

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_db_path():
    if os.name == 'nt':  # Windows
        app_data = os.path.join(os.environ['APPDATA'], 'MonkMode')
    else:  # Linux/Mac
        app_data = os.path.join(Path.home(), '.monkmode')
    
    os.makedirs(app_data, exist_ok=True)
    return os.path.join(app_data, 'monkmode.db')
"""
Handles saving and loading game states.
"""
import pickle
from datetime import datetime
import os
from player import Player

SAVE_DIR = 'saves/'

def save_game(player: Player, filename=None):
    os.makedirs(SAVE_DIR, exist_ok=True)
    if filename is None:
        # Generate default filename with current date
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{date_str}_save.pkl"
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, 'wb') as f:
        pickle.dump(player, f)

def list_save_files():
    os.makedirs(SAVE_DIR, exist_ok=True)
    save_files = [f for f in os.listdir(SAVE_DIR) if f.endswith('.pkl')]
    return save_files

def load_game(filename):
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, 'rb') as f:
        return pickle.load(f)
"""
This file contins the Player class which tracks the player's
status, inventory, and attributes.
"""
from locations import *

# TODO
class Player():
    def __init__(self, name="Player"):
        self.name = name
        self.inventory = []
        # set initial location
        self.location = start_location(self)

    def set_name(self, name: str):
        self.name = name
    
    def get_name(self):
        return self.name

    def get_location(self):
        return self.location
    
    def set_location(self, location : Location):
        self.location = location
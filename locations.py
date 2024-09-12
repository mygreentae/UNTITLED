"""
Defines different locations in the game, their descriptions, 
and possible actions.
"""
from error_handler import InvalidActionError

class Location:
    def __init__(self, description):
        self.description = description
        self.actions = dict()

    def add_action(self, action, outcome):
        self.actions[action] = outcome

    def list_actions(self):
        print("Available actions:")
        for index, action in enumerate(self.actions.keys(), start=1):
            print(f"{index}. {action}")
        print()

    def choose_action(self):
        self.list_actions()
        choice = \
            input("What do you want to do? (Enter the number or name of the action) ").strip()

        if choice.isdigit():
            index = int(choice) - 1
            actions_list = list(self.actions.keys())
            if 0 <= index < len(actions_list):
                return actions_list[index]
            else:
                raise InvalidActionError(choice)
        elif choice in self.actions or choice == "save" or choice == "view":
            return choice
        else:
            raise InvalidActionError(choice)

    def process_action(self, action, player):
        if action in self.actions:
            print(self.actions[action])
            return self.actions[action](player)
        else:
            raise InvalidActionError(action)
    
def start_location(player):
    loc = Location("You are at the entrance of a dark forest.")
    loc.add_action("enter", forest_location)
    return loc

def forest_location(player):
    loc = Location("You are in the forest. There is a path ahead.")
    loc.add_action("follow path", path_location)
    loc.add_action("go back", start_location)
    return loc

def path_location(player):
    loc = Location("You follow the path and find an ancient altar.")
    # Add more actions and locations
    return loc

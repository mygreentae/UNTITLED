"""
This is the main entry point of the game. 
It will handle the game loop and initialize the game.
"""
from player import Player
from locations import *
from save_load import save_game, load_game, list_save_files
from error_handler import *
from utils import *
from datetime import datetime

def view_character(player: Player):
    print(player.get_name())

def choose_save_file():
    save_files = list_save_files()
    
    if not save_files:
        print("No save files found.")
        return None

    while True:
        print("Available save files:")
        for index, save_file in enumerate(save_files, start=1):
            print(f"{index}. {save_file}")

        choice = input("Enter the number or name of the save file (or 'exit' to cancel): ").strip()

        if choice.lower() == 'exit':
            print("Exiting load process. Starting a new game.")
            return None

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(save_files):
                return save_files[index]
            else:
                print("Invalid number. Please try again.")
        elif choice in save_files:
            return choice
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome!")
    player = Player()

    try:
        # TODO add other options : load, new, clear saves, etc rather than just a yes or no
        if input("Do you want to load a saved game? (yes/no) ").lower() == "yes":
            save_file = choose_save_file()
            if save_file:
                player = load_game(save_file)
            else:
                print("Starting a new game.")
        else:
            name = input("What is your name? ")
            player.set_name(name)
            print()
        
        current_location = player.get_location()

        while True:
            print(current_location.description)
            print()

            try:
                action = current_location.choose_action()

                if action == "save":
                    default_filename = datetime.now().strftime("%Y-%m-%d") + "_save.pkl"
                    filename = \
                        input(f"Enter a name for your save file (or leave blank for default: '{default_filename}'): ").strip()
                    filename = filename if filename else default_filename
                    save_game(player, filename)
                    print(f"Game saved as '{filename}'. See you next time!")
                    break
                elif action == "view":
                    view_character(player)
                else:
                    print("HERERERERE")
                    current_location = current_location.process_action(action, player)
                    player.set_location(current_location)

            except SaveLoadError as e:
                print(e.message)
            
            except InvalidActionError as e:
                print(e.message)
    except GameError as e:
        print(f"An Error Occured: {e.message}")

if __name__ == "__main__":
    main()

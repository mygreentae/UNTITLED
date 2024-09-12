"""
Designed to handle different types of user errors.
"""

class GameError(Exception):
    """Base class for other exceptions"""
    pass

class InvalidActionError(GameError):
    """Raised when the player inputs an invalid action"""
    def __init__(self, action):
        self.action = action
        self.message = f"Invalid action: {self.action}\n"
        super().__init__(self.message)

class SaveLoadError(GameError):
    """Raised when there is an issue with saving or loading the game"""
    def __init__(self, operation, message="An error occurred during save/load operation\n"):
        self.operation = operation
        self.message = f"{message}: {self.operation}"
        super().__init__(self.message)
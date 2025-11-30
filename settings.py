class Settings:
    """A class to store all the settings for the Wizard Survival Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (30, 30, 40)

        # Wizard settings.
        self.wizard_width = 30
        self.wizard_height = 30
        self.wizard_color = (50, 150, 255)
class Settings:
    """A class to store all the settings for the Wizard Survival Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (30, 30, 40)

        # Wizard settings.
        self.wizard_speed = 3.0
        self.wizard_width = 30
        self.wizard_height = 30
        self.wizard_color = (50, 150, 255)

        # Spell settings
        self.spell_speed = 6.0
        self.spell_width = 6
        self.spell_height = 12
        self.spell_color = (255, 220, 0)
        self.spells_allowed = 5

        # Enemy settings
        self.enemy_speed = 1.5
        self.enemy_size = 28
        self.enemy_color = (200, 60, 60)
        self.max_enemies = 10
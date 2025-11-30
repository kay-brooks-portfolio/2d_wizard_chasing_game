import pygame

class Wizard:
    """A class to manage the player-controlled wizard."""

    def __init__(self, ai_game):
        """Initialize the wizard and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Represent wizard as a simple rectangle and get its rect.
        self.color = self.settings.wizard_color
        self.rect = pygame.Rect(
            0, 0,
            self.settings.wizard_width,
            self.settings.wizard_height
        )

        # Start each new wizard at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the wizard at its current location and as a simple rectangle."""
        pygame.draw.rect(self.screen, self.color, self.rect)
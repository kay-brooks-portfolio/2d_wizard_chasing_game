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

        # Store a float for the wizard's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the wizard at its current location and as a simple rectangle."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Update wizard position based on movement flags."""
        # Horizontal movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.wizard_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.wizard_speed

        # Vertical movement
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.wizard_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.wizard_speed

        # Update rect from float positions
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
import sys
import pygame

from settings import Settings
from wizard import Wizard

class WizardGame:
    """Overall class to manage game assets and resources."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
        self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Wizard Survival Game")

        # Create the wizard.
        self.wizard = Wizard(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.wizard.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event. get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _check_keyup(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keydown(self, event):
        """Respond when keys are pressed."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the hoop.
        self.screen.fill(self.settings.bg_color)
        # Draw the wizard.
        self.wizard.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = WizardGame()
    ai.run_game()
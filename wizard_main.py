import sys
import pygame

class WizardGame:
    """Overall class to manage game assets and resources."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Wizard Survival Game")

        # Set the background color.
        self.bg_color = (30, 30, 40)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events. 
            for event in pygame.event. get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the hoop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = WizardGame()
    ai.run_game()
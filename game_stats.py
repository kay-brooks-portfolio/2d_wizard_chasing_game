import pygame.font

class GameStats:
    """Track the statistics for the game."""

    def __init__(self, ai_game):
        """Initialize the statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.wizard_lives_left = self.settings.wizard_lives
        self.score = 0

class Scoreboard:
    """A class to report the scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # Font settings for scoring information.
        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        self.prep_score()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
                        self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """"Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

    def prep_lives(self):
        """Turn the wizard into a rendered image."""
        lives_str = f"Lives: {self.stats.wizard_lives_left}"
        self.lives_image = self.font.render(lives_str, True, 
                        self.text_color, self.settings.bg_color)
        
        # Display the lives at the top left of the screen.
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = 20
        self.lives_rect.top = 20

    def show_lives(self):
        """"Draw wizard lives to the screen."""
        self.screen.blit(self.lives_image, self.lives_rect)
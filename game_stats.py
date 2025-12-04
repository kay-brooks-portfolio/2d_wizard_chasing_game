import pygame.font

class GameStats:
    """Track the statistics for the game."""

    def __init__(self, ai_game):
        """Initialize the statistics. """
        self.settings = ai_game.settings
        self.high_score = 0
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
        self.prep_high_score()

    def _prep_text(self, text, *, topleft=None, topright=None, midtop=None):
        """Render text and position its rect."""
        image = self.font.render(text, True,
                                self.text_color,
                                self.settings.bg_color)
        rect = image.get_rect()

        # Positioning options for the text.
        if topleft is not None:
            rect.topleft = topleft
        if topright is not None:
            rect.topright = topright
        if midtop is not None:
            rect.midtop = midtop
        return image, rect

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image, self.score_rect = self._prep_text(
            score_str,
            topright=(self.screen_rect.right - 20, 20))
        
    def prep_high_score(self):
        """Turn the high score into an image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(high_score)

        self.high_score_image, self.high_score_rect = self._prep_text(
            high_score_str,
            midtop=(self.screen_rect.centerx, 20))

    def prep_lives(self):
        """Turn the wizard into a rendered image."""
        lives_str = f"Lives: {self.stats.wizard_lives_left}"
        self.lives_image, self.lives_rect = self._prep_text(
            lives_str,
            topleft=(20, 20))

    def show_score(self):
        """"Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
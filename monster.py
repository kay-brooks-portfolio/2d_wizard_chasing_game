import pygame 
from pygame.sprite import Sprite
import random
import math

class Monster(Sprite):
    """A class to represent a single monster."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the the a monster as a simple square and set its rect attribute
        self.rect = pygame.Rect(
            0, 0,
            self.settings.enemy_size,
            self.settings.enemy_size
        )

        # Random monster position along the sides and top of the screen.
        screen_h = self.settings.screen_height
        screen_w = self.settings.screen_width

        edge = random.choice(["top", "left", "right"])

        if edge == "top":
            self.rect.x = random.randint(0, screen_w - self.rect.width)
            self.rect.y = 0
        elif edge == "left":
            self.rect.x = 0
            self.rect.y = random.randint(0, screen_h - self.rect.height)
        else: 
            self.rect.x = screen_w - self.rect.width
            self.rect.y = random.randint(0, screen_h - self.rect.height)

        # Store the monster's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = self.settings.enemy_color
        self.speed = self.settings.enemy_speed

    def draw(self):
        """Draw the monster as a red square."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self, wizard):
        """
        Move the monster toward the wizard by using the Pythagorean theorem.
        """
        dx = wizard.rect.centerx - self.rect.centerx
        dy = wizard.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)
        if distance == 0:
            return

        # Get the direction to the wizard
        dx /= distance
        dy /= distance

        # Move the monster toward the wizard in a smooth way from game settings.
        self.x += dx * self.speed
        self.y += dy * self.speed

        # # Move the monster on the screen from it's float position.
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

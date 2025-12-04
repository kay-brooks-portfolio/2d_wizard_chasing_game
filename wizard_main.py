import sys
import pygame
from time import sleep

from settings import Settings
from wizard import Wizard
from spell import Spell
from monster import Monster
from game_stats import GameStats, Scoreboard

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

        # Start the game in an active state to allow for 'Game Over'.
        self.game_active = True

        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Create the wizard, spells, and enemies objects.
        self.wizard = Wizard(self)
        self.spells = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self._create_enemies()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.wizard.update()
                self._cleanup_offscreen_spells()
                self._update_enemies()
                self._create_enemies()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
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
        elif event.key == pygame.K_UP:
            self.wizard.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = False
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keydown(self, event):
        """Respond when keys are pressed."""
        if event.key == pygame.K_RIGHT:
            self.wizard.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.wizard.moving_left = True
        elif event.key == pygame.K_UP:
            self.wizard.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.wizard.moving_down = True
        elif event.key == pygame.K_SPACE:
                self._fire_spell()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _cleanup_offscreen_spells(self):
        """
        Update spell positions and remove those that have left the screen.
        """
        self.spells.update()

        # Remove spells that move off the screen
        for spell in self.spells.copy():
            if (spell.rect.bottom < 0 or
                spell.rect.top > self.settings.screen_height or
                spell.rect.right < 0 or
                spell.rect.left > self.settings.screen_width):
                self.spells.remove(spell)
        
        # Check if a spell hit a monster and remove spell and monster.
        collisions = pygame.sprite.groupcollide(
            self.spells, self.enemies, True, True
        )
    
    def _create_enemies(self):
        """Create a horde of swarming monsters and make sure it stays at max."""
        while len(self.enemies) < self.settings.max_enemies:
            enemy = Monster(self)
            self.enemies.add(enemy)
        
    def _fire_spell(self):
        """Create a new spell and add it to the spells group if under a limit"""
        if len(self.spells) < self.settings.spells_allowed:
            new_spell = Spell(self)
            self.spells.add(new_spell)

    def _update_enemies(self):
        """Update the enemies to make them move towards the wizard."""
        for enemy in self.enemies:
            enemy.update(self.wizard)

        # If a monster touches the wizard, detect it and print a message.
        if pygame.sprite.spritecollideany(self.wizard, self.enemies):
            self._wizard_hit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the hoop.
        self.screen.fill(self.settings.bg_color)

        # Draw the wizard.
        self.wizard.blitme()
        for spell in self.spells.sprites():
            spell.draw()
        
        # Draw the enemies.
        for enemy in self.enemies.sprites():
            enemy.draw()

        # Draw the score and wizard lives information.
        self.sb.show_score()
        self.sb.show_lives()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _wizard_hit(self):
        """Respond to the wizard being hit by the monsters."""
        if self.stats.wizard_lives_left > 0:
            # Adjust the amount of lives the wizard has. 
            self.stats.wizard_lives_left -= 1

            # Update the lives display on left corner.
            self.sb.prep_lives()

            self.spells.empty()
            self.enemies.empty()
            self._create_enemies()
            sleep(1.0)
        else:
            self.game_active = False

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = WizardGame()
    ai.run_game()
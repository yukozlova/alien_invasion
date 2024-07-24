import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.game_active = False
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)
        self.play_button = Button(self, 'Play')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()
    
    def _create_alien_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        current_y = alien_height
        half_screen_height = self.settings.screen_height / 2

        while current_y <= half_screen_height:
            current_x = alien_width
            while current_x <= self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _check_play_button(self, mouse_pos):
        clicked = self.play_button.rect.collidepoint(mouse_pos)
        if clicked:
            self._start_game()
    
    def _start_game(self):
        if not self.game_active:
            self.game_active = True
            self.stats.reset_stats()
            self.bullets.empty()
            self.aliens.empty()
            self._create_alien_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.settings.initialize_dynamic_settings()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                False, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_speed()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_aliens_bottom(self):
        for alien in self.aliens:
            if (alien.rect.bottom >= self.settings.screen_height):
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()
    
    def _ship_hit(self):
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_alien_fleet()
            self.ship.center_ship()
            sleep(1)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
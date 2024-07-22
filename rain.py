import pygame
import sys
from rain_settings import Settings
from drop import Drop
from random import randint

class Rain:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Rain')
        self.drops = pygame.sprite.Group()

    def _create_a_drop(self, x_position=None):
        new_drop = Drop(self)
        if x_position:
            new_drop.rect.x = x_position
            new_drop.initial_x = x_position
        self.drops.add(new_drop)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _update_drops(self):
        self.drops.update()

        for drop in self.drops.copy():
            if drop.rect.top >= self.settings.screen_height:
                self._create_a_drop(drop.initial_x)
                self.drops.remove(drop)

        if len(self.drops) < self.settings.drop_num:
            self._create_a_drop()

        i = 0
        for drop in self.drops:
            if i % 4 == 0:
                drop.speed += 0.003
            if i % 6 == 0:
                drop.speed += 0.075
            elif i % 10 == 0:
                drop.speed = 1.5
            elif i % 20 == 0:
                drop.speed = 0.05
            i += 1


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_drops()
            self._update_screen()
            self.clock.tick(60)

def print_info(game):
    print(f"screen.rect.width = {rain.screen_rect.width}")
    print(f"screen.rect.height = {rain.screen_rect.height}")
    print(f"settings.screen_width = {rain.settings.screen_width}")
    print(f"settings.screen_height = {rain.settings.screen_height}")

if __name__ == '__main__':
    rain = Rain()
    print_info(rain)
    rain.run_game()
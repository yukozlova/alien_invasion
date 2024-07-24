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
        self._create_drops()

    def _create_drops(self):
        for i in range(self.settings.drop_num):
            new_drop = Drop(self)
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

        for drop in self.drops:
            if drop.rect.top >= self.settings.screen_height:
                drop.reset_drop()

        i = 0
        for drop in self.drops:
            if i % randint(1, 5) == 0:
                drop.speed += 0.03
            if i % randint(1, 10) == 0:
                drop.speed += 0.075
            elif i % randint(10, 20) == 0:
                drop.speed = 1.5
            elif i % randint(20, 30) == 0:
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
    rain.run_game()
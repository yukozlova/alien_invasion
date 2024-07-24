import pygame
import random
from pygame.sprite import Sprite

class Drop(Sprite):
    def __init__(self, rain_game):
        super().__init__()
        self.settings = rain_game.settings
        self.image = pygame.image.load('images/water-drop.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.max_x = self.settings.screen_width - self.width / 2
        self.reset_drop()

    def update(self):
        if self.y > 0.75 * self.settings.screen_height:
            self.y += self.settings.drop_max_speed
        else:
            self.y += self.speed
        self.rect.y = self.y
    
    def reset_drop(self):
        self.rect.y = -self.rect.height
        self.y = float(self.rect.y)
        self.speed = random.random()
        self.initial_x = random.randint(0, self.max_x)
        self.rect.x = self.initial_x
        self.speed = random.random()


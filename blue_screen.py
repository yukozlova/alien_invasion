import pygame
import sys
from cat import Cat

class BlueScreen:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 400))
        self.bg_color = (135,206,250)
        
        pygame.display.set_caption('Blue Screen')
        self.cat = Cat(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.cat.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    bs = BlueScreen()
    bs.run_game()
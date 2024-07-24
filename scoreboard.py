import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.settings = ai_game.settings
        self.font = pygame.font.SysFont(None, 37)
        self.text_color = (47,79,79)
        self.bg_color = self.settings.bg_color
        self.prep_score_imgs()
    
    def _format_score(self, score):
        return f"{score:,}"
    
    def prep_score_imgs(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        score_str = self._format_score(self.stats.score)
        self.score_img = self.font.render(score_str, True, 
                                                 self.text_color,
                                                 self.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = self.settings.sb_top
        self.score_rect.right = self.screen_rect.right - 20
    
    def prep_high_score(self):
        score_str = self._format_score(self.stats.high_score)
        self.high_score_img = self.font.render(score_str, True,
                                               self.text_color,
                                               self.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.top = self.settings.sb_top
        self.high_score_rect.centerx = self.screen_rect.centerx
    
    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_img = self.font.render(level_str, True,
                                          self.text_color,
                                          self.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.settings.sb_top
        self.level_rect.top += self.score_rect.height
    
    def prep_ships(self):
        self.ships = Group()
        for i in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.top = self.settings.sb_top
            ship.rect.left =  i * (ship.rect.width + 5) + 5
            self.ships.add(ship)

    def check_high_score(self):
        if self.stats.high_score < self.stats.score:
            self.stats.high_score = self.stats.score
        self.prep_high_score()
    
    def show_scoreboard(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

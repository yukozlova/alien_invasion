from pathlib import Path

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.score = 0
        self.get_high_score()
        self.reset_stats()
    
    def get_high_score(self):
        path = Path(self.settings.file_name)
        if path:
            try:
                self.high_score = int(path.read_text())
            except Exception:
                self.high_score = 0
        else:
            self.high_score = 0
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
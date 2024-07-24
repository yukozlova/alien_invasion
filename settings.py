class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.file_name = 'scores.txt'

        self.sb_top = 10

        self.ship_limit = 3

        self.bullet_width = 10.0
        self.bullet_height = 20.0
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 7

        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        
        self.alien_points = 10
       
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 3.5
        self.bullet_speed = 2.0
        self.alien_speed = 1

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

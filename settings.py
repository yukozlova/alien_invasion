class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed = 4.5
        self.ship_limit = 3

        self.bullet_speed = 6.0
        self.bullet_width = 100.0
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        self.alien_speed = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
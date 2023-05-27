class Setting:
    #сдесь все файлы игры
    def __init__(self):
        #экран
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #корабль
        self.ship_speed = 2
        self.ship_limit = 3
        #Патрон
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 1

        #пришелец
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        #fleet_direction = 1 - движение вправо
        self.fleet_direction = 1


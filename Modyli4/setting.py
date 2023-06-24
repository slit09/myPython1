class Setting():
    # Класс для хранения всех настроек игры

    def __init__(self):
        # инициализируем статические настройки игры

        # параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # настройки корабля
        self.ship_limit = 3


        # параметры снаряда
        
        self.bullet_width = 5000
        self.bullet_height = 3000
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 1000

        # скорость прищельцев
        
        self.fleet_drop_speed = 2
        # fleet_direction = 1 - движение вправо, = -1 - движение влево
        self.fleet_direction = 1


        # ТЕМП УСКОРЕНИЯ ИГРЫ
        self.speedup_scale = 1.2
        # темп увеличения стоимости пришельца
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # инициализируем настройки игры, котрые изменяются в ходе игры
        self.ship_speed_factor = 2.5
        self.bullets_speed_factor =  5.0
        self.alien_speed_factor = 50.0

        self.ship_speed = self.ship_speed_factor
        self.bullet_speed = self.bullets_speed_factor
        self.alien_speed = self.alien_speed_factor

        # подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        # увеличиваем настройки скорости и стоимости пришельца
        self.ship_speed_factor *= self.speedup_scale
        self.bullets_speed_factor *=  self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        self.ship_speed = self.ship_speed_factor
        self.bullet_speed = self.bullets_speed_factor
        self.alien_speed = self.alien_speed_factor





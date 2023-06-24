import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    # класс для вывода игровой информации 

    def __init__(self,ai_game):
        # инициализируем атрибуты подсчета очков
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # настроим параметры шрифта для вывода счета
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # преобразование текущего счета в графическое изображение
        rounded_score = round(self.stats.score,-1)
        score_str ="{:,}".format(rounded_score)
        
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        # преобразуем рекордный счет в графическое изображдение
        high_score_rect = round(self.stats.high_score,-1)
        rscore_str ="{:,}".format(high_score_rect)
        self.rscore_image = self.font.render(rscore_str,True,self.text_color,self.settings.bg_color)

        # рекорд выравнивается пот центру верхней стороны
        self.high_score_rect = self.rscore_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        # преобразуем уровень в графическое изображение
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        # уровень будем выводить под текущим счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        # вывод счета, рекорда, левела и число оставшихся кораблей на экран 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.rscore_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_ships(self):
        # сообщаем количество оставшихся кораблей !жизней!
        self.ships = Group()
        for ship_number in range(self.stats.ships_lifes):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        # проверим появился ли новый рекорats.score
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score
                self.prep_high_score()       

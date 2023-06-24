import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # Класс для управления кораблем
    def __init__(self,ai_game):
        # инициализировать корабль и задать его начальную позицию
        super().__init__()

        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загрузить изображение корабля и получить прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется у нижней границы экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # флаги перемещения
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        # обновляет позицию коробля с учетом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        self.rect.x = self.x

    def blitme(self):
        # рисуем корабль в текущей позиции
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # размещает корабль в центре нижней стороны
        self.rect.midbottom = self.screen_rect.midbottom
        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)


import sys
from time import sleep
import pygame
from gameStats import GameStats
from scoreboard import Scoreboard
from button import Button
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    # класс для управления рессурсами и поведением игры

    def __init__(self):
        # иницилизируем игру и создаем игровые ресурсы
        pygame.init()
        self.settings = Setting()

        
        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption('Инопланетное вторжение')

        # coздаем экземпляр для хранения игровой статистики
        # и панели результатов
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._creat_flot()

        # создание кнопки Play
        self.play_button = Button(self,"Play")

    def run_game(self):
        # запуск одного цикла игры
        while True:
            self._check_event()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

    def _check_event(self):
        # отслеживание событий клавиатуры и мыши
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                record = open('tect.txt', 'w')
                record.write(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # переместить корабль вправо
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # переместить корабль влево
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    record = open('tect.txt', 'w')
                    record.write(str(self.stats.high_score))
                    sys.exit()
                elif event.key == pygame.K_n:
                    self.start_game()
                elif event.key == pygame.K_p:
                    if self.stats.game_active:
                        self.stats.game_active = False
                    else:
                        self.stats.game_active = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos) 

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # конец перемемещения корабля вправо
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # конец перемещения корабля влево
                    self.ship.moving_left = False

                
 

    def _check_play_button(self,mouse_pos):
        #запускает новую игру при нажатии на кнопку Play
        button_clicket = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicket and not self.stats.game_active:
            #сброс игровых настроек
            self.settings.initialize_dynamic_settings()
            #сбрасываю статистику
            self.stats.reset_stats()
            #запускаем
            self.stats.game_active = True

            #очистить списки пришельцев и снарядом
            self.aliens.empty()
            self.bullets.empty()

            #создаем новый флот и размещае корабль по центру
            self._creat_flot() 
            self.ship.center_ship()

            #указатель мыши скрываем(делаем невидимым)
            pygame.mouse.set_visible(False)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _new_game(self):
            self.stats.reset_stats()
            #запускаем
            self.stats.game_active = True

            #очистить списки пришельцев и снарядом
            self.aliens.empty()
            self.bullets.empty()
            self.stats.score = 0

            #создаем новый флот и размещае корабль по центру
            self._creat_flot()
            self.ship.center_ship()

    def start_game(self):
        #button_clicket = self.play_button.rect.collidepoint()
        self.settings.initialize_dynamic_settings()
        if self.stats.game_active:
            self._new_game()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # вывод информаци о счете
        self.sb.show_score()

        # Кнопка плей будет отображаться тогда, когда игра неи активна
        if not self.stats.game_active: 
            self.play_button.draw_button()

        # отображение последнего прорисованного экрана
        pygame.display.flip()

#################### КОРАБЛЬ ########################
    def _ship_hit(self):
        # обрабатываем столкновение корабля с кораблями пришельцев
        
        if self.stats.ships_lifes > 0:
            # уменьшаем кол-во наших кораблей на еденицу
            self.stats.ships_lifes -= 1
            self.sb.prep_ships()

            # очищаем группы пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            # создадим новый флот пришельцев и вернем наш корабль на начальное положение
            self._creat_flot()
            self.ship.center_ship()

            # пауза
            sleep(0.5)
        else:
            self.stats.game_active = False


################### ИНОПЛАНЕТНЫЙ ФЛОТ #################
    def _creat_flot(self):
        # создание флота пришельцев

        # создание пришельца и вычисление пришельцев в ряду
        # интервал между соседними пришнльцами равен ширине пришельцев
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        availabe_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = availabe_space_x // (2*alien_width)

        # определти количество рядов, которые помещаются на экране
        ship_height = self.ship.rect.height
        availabe_space_y = (self.settings.screen_height -(3*alien_height)-ship_height)
        number_rows = availabe_space_y//(2*alien_height)

        # создание флота инопланетян
        for row_number in range(number_rows): 
            # создание ряда пришельцев
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
    
    def _create_alien(self,alien_number,row_number):
            # создаем пришельца и размещаем его в ряду
            alien = Alien(self)
            alien_width,alien_height = alien.rect.size
            alien.x = alien_width + 2*alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
            self.aliens.add(alien)

    def _update_aliens(self):
        # обновление позиции всех пришельцев
        self._check_fleet_edges()
        self.aliens.update()

        # проверка столкновения вражеского коробля с нашим кораблем (коллизия)
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        # проверяет не добрался ли кто-то из пришельцев до нижнего края экрана
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        # не добрался ли кто-то из пришельцев до дальнего края экрана
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # то же самое, что и столкновение пришельца с кораблем
                self._ship_hit()
                break
    
    def _check_fleet_edges(self):
        # реагирует на достижение пришельцем края
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break
    
    def _check_fleet_direction(self):
        # опускает весь флот и меняет направление бокового движения
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        # обновляет позиции снарядов и уничтожает старые снаряды
        # обновление позиции снарядов
        self.bullets.update()
        # удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        # проверка попадания в пришельца
        # при попадании удаляем снаряд и пришельца 
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # уничтожим все снаряды 
            self.bullets.empty()
            # создание нового флота
            self._creat_flot()
            self.settings.increase_speed()

            # увеличение уровня
            self.stats.level += 1
            self.sb.prep_level()

########################### СНАРЯДЫ ###################
    def _fire_bullet(self):
        # создание нового снаряда и включение его в группу
        if len(self.bullets) < self.settings.bullets_allowed:
            new_ballet = Bullet(self)
            self.bullets.add(new_ballet)

if __name__ == '__main__':
    # создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()

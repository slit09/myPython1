import sys
from time import sleep
import pygame
from buttom import Buttom
from game_stats import GameStats
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Aliens
from wert import Wert

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Setting()

        #self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN )
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width


        pygame.display.set_caption('ИНОПЛАНЕТНОЕ ВТОРЖЕНИЕ')

        self.stats = GameStats(self)
        

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_flote()

        self.play_buttom = Buttom(self,'Играть')
 
    def run_game(self):
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_werts()
            self._update_screen()
            
           

    def _create_flote(self):
        alien = Aliens(self)
        alien_width,alien_height = alien.rect.size
        avaible_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = avaible_space_x // (2*alien_width)
        ship_height = self.ship.rect.height
        avaible_space_y = (self.settings.screen_height -(3*alien_height)-ship_height)
        number_rows = avaible_space_y//(2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_aliens(alien_number,row_number)



    def _create_aliens(self,alien_number,row_number):
            alien = Aliens(self)
            alien_width,alien_height = alien.rect.size
            alien.x = alien_width + 2*alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
            self.aliens.add(alien)



    def _update_aliens(self):
        self._check_flotes_edge()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()



    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

#--------------------------------------------------------------------------
#Game Opehion_______-------_______--------________---------_________-------_________-----------_______----
#---------------------------------------------------------------------------------------------------------
    def _ship_hit(self):
        if self.stats.ships_lifes > 0:
            self.stats.ships_lifes -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_flote()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False


#-----------------------------------------------------------------------------------------------------------
#Flot_____----------________--------_______--------________--------________---------_______-----------______
#------------------------------------------------------------------------------------------------------------
    def _check_flotes_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break



    def _check_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

#
#
#


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)   
        self._check_bullet_alien_collision()



    def _check_bullet_alien_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_flote()



    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True 
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True


                    elif event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullets()
                    
                             
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False  
              
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_ballet = Bullet(self)
            self.bullets.add(new_ballet)


    def _update_screen(self):
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)
            if not self.stats.game_active:
                self.play_buttom.drow_buttom()

            pygame.display.flip()

    
if __name__ == '__main__':
    aw = AlienInvasion()
    aw.run_game()

 
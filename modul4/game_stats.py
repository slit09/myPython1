class GameStats():
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        #иницелизирую статистику в процессе игры
        self.ships_lifes = self.settings.ship_limit
        
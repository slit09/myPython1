class GameStats():
    # отслеживание статистику игры

    def __init__(self,ai_game):
        # получим настройки игры
        self.settings = ai_game.settings
        self.reset_stats()

        # игра будет запускаться в неактивном состоянии
        self.game_active = False

        # рекорд не должен сбрасываться
        with open('tect.txt', 'r') as record:
            sas = record.read()
            if sas != '':
                self.high_score = int(sas)
            else:
                self.high_score = 0

    def reset_stats(self):
        # инициализация статистики, которая изменяется в процессе игры
        self.ships_lifes = self.settings.ship_limit
        self.score = 0
        self.level = 1
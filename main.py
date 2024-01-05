import pygame
from menu import Menu  # assuming you have menu.py file where Menu class is defined
from level import Level  # assuming you have level.py file where Level class is defined


class Game:
    def __init__(self):
        self.state = 'initialized'
        self.screen_width = 1200
        self.screen_height = 800

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def run(self):
        while True:
            if self.state == 'initialized':
                self.state = 'main_menu'

            elif self.state == 'main_menu':
                menu = Menu(self.screen)
                menu_screen = menu.run()  # assuming the run function returns something related to menu
                self.state = 'level_generation'

            elif self.state == 'level_generation':
                level = Level(menu_screen)
                level_screen = level.generate_level()  # assuming this function return something about the level
                self.state = 'quitting'

            elif self.state == 'quitting':
                pygame.quit()

if __name__ == "__main__":
    Game().run()
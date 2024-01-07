import pygame
from menu import Menu  # Import Menu class from menu module
from level import Level  # Import Level class from level module
from character import Character  # Import Character class from character module
from render import Render  # Import Render class from render module

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((1200, 800))


class Game:
    def __init__(self):
        self.state = 'initialized'
        self.menu_screen = None
        self.level = None
        self.character = None
        self.render = None

    def run(self):
        while True:
            if self.state == 'initialized':
                self.state = 'main_menu'
            elif self.state == 'main_menu':
                menu = Menu(screen)
                self.menu_screen = menu.run()
                self.state = 'level_generation'
            elif self.state == 'level_generation':
                self.level = Level(self.menu_screen)
                self.character = Character()  # Instantiate Character class
                self.state = 'rendering'
            elif self.state == 'rendering':
                self.render = Render(self.level.screen, self.level.platforms, self.character)
                self.render.run()
                self.state = 'quitting'  # Change the state to quit the game
            else:
                break  # Quit the game


if __name__ == "__main__":
    Game().run()

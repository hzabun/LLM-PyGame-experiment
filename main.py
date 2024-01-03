import pygame
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        # Set up some constants
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        # Create the screen and a clock for FPS limiting
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        # Initialize our game states
        self.state = "initialized"

        # Create a menu object
        self.menu = Menu(self.screen)

    def run(self):
        while True:  # Loop forever
            if self.state == 'initialized':
                # TODO: initialize game elements here

                # After initialization, go to the main menu
                self.state = "main_menu"

            elif self.state == 'main_menu':
                # Pass control to the menu module
                self.menu.run()
                self.state = 'quitting'  # TODO: implement other states properly

            elif self.state == 'quitting':
                break  # Exit the loop

            else:
                raise ValueError("Invalid game state!")


if __name__ == "__main__":
    Game().run()

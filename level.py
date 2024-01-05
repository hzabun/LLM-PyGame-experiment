import pygame
from pygame import Rect


class Level():
    def __init__(self, screen):
        self.screen = screen

    def draw_platforms(self):

        self.screen.fill((0, 0, 0))

        # Draw medium length platforms
        platform1 = Rect((0, 450), (300, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), platform1)

        platform2 = Rect((900, 450), (300, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), platform2)

        # Draw large platform
        platform3 = Rect((300, 700), (600, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), platform3)

        # Draw small platform
        platform4 = Rect((500, 250), (200, 50))
        pygame.draw.rect(self.screen, (255, 255, 255), platform4)

    def generate_level(self):
        self.draw_platforms()
        pygame.display.flip()

        return self.screen

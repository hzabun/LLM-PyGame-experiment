import pygame


class Level:
    def __init__(self, screen):
        self.screen = screen
        self.platforms = []
        self.load_level()

    def draw_platform(self, platform_dimensions):
        """Draws a platform given the dimensions"""
        pygame.draw.rect(self.screen, (255, 255, 255), platform_dimensions)

    def generate_platforms(self):
        """Generates the platforms"""

        # Left middle side medium
        platform1 = pygame.Rect((0, 450, 300, 50))
        self.draw_platform(platform1)
        self.platforms.append(platform1)

        # Right middle side medium
        platform2 = pygame.Rect(900, 450, 300, 50)
        self.draw_platform(platform2)
        self.platforms.append(platform2)

        # Middle bottom side large
        platform3 = pygame.Rect(300, 700, 600, 50)
        self.draw_platform(platform3)
        self.platforms.append(platform3)

        # Middle upper side small
        platform4 = pygame.Rect(500, 250, 200, 50)
        self.draw_platform(platform4)
        self.platforms.append(platform4)

    def load_level(self):
        """Loads the level"""
        self.screen.fill((0, 0, 0))
        self.generate_platforms()
        pygame.display.flip()



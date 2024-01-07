import pygame
from pygame.sprite import Sprite


class Character(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/images/character.bmp')  # Load character image
        self.rect = self.image.get_rect()  # Get rect of the image
        self.hitpoints = 5  # Initial health
        self.equipments = ['Bow and arrow', 'Shield', 'Health potion']  # List of equipments

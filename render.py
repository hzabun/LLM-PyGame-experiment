import pygame
from pygame.locals import *
import sys

class Render:
    def __init__(self, screen, platforms, character_sprite):
        self.old_screen = screen.copy()
        self.new_screen = screen
        self.character_sprite = character_sprite
        self.clock = pygame.time.Clock()

        # Character attributes
        self.character_rect = character_sprite.rect
        self.character_speed = 5
        self.jump_height = 10
        self.gravity = 1
        self.is_jumping = False
        self.y_velocity = 0

        self.platforms = platforms

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def move_character(self, keys):
        if keys[pygame.K_LEFT] and self.character_rect.left > 0:
            self.character_rect.x -= self.character_speed
        if keys[pygame.K_RIGHT] and self.character_rect.right < self.new_screen.get_width():
            self.character_rect.x += self.character_speed

    def jump(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -self.jump_height

    def apply_gravity(self):
        if self.is_jumping:
            self.y_velocity += self.gravity
            self.character_rect.y += self.y_velocity
            self.is_jumping = False
        else:
            # Check for collision with platforms
            for platform in self.platforms:
                if self.character_rect.colliderect(platform) and self.y_velocity <= 0:
                    self.character_rect.y = platform.top - self.character_rect.height
                    self.y_velocity = 0
                    break
                else:
                    self.character_rect.y += self.gravity

    def run(self):
        while True:
            self.handle_events()

            keys = pygame.key.get_pressed()
            self.move_character(keys)
            self.jump(keys)
            self.apply_gravity()

            self.new_screen.blit(self.old_screen, (0, 0))
            self.new_screen.blit(self.character_sprite.image, (self.character_rect.x, self.character_rect.y))

            pygame.display.flip()

            self.clock.tick(60)



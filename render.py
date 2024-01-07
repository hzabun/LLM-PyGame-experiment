import pygame
from pygame.locals import *

class Render:
    def __init__(self, screen, platforms, character):
        self.screen = screen
        self.character = character
        self.platforms = platforms
        self.running = True

        # Character position and movement
        self.character_x = 100
        self.character_y = 250
        self.character_jump = False
        self.character_left = False
        self.character_right = False

    def run(self):
        while self.running:
            # Detect events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False

                # Movement control
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.character_left = True
                    elif event.key == K_RIGHT:
                        self.character_right = True
                    elif event.key == K_UP:
                        self.character_jump = True
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.character_left = False
                        self.character_right = False

            # Update character position
            if self.character_jump:
                self.character_y -= 10
                self.character_jump = False
            else:
                if self.character_left:
                    self.character_x -= 5
                elif self.character_right:
                    self.character_x += 5

            # Drawing
            self.screen.blit(self.character.image, (self.character_x, self.character_y))
            pygame.display.flip()

        pygame.quit()

    def checkCollision(self):
        for platform in self.platforms:
            if self.character.colliderect(platform):
                self.character.y = platform.y - self.character.height


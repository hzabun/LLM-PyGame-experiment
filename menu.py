import pygame
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 30)
        self.options = ['Start Game', 'Options', 'Quit']
        self.selected_option = 0
        self.background = pygame.image.load('assets/images/background.bmp')

    def draw(self):
        for i in range(len(self.options)):
            if i == self.selected_option:
                color = (255, 255, 0)  # Yellow text for the selected option
            else:
                color = (255, 255, 255)  # White text for unselected options

            text = self.font.render(self.options[i], True, color)
            self.screen.blit(text, (100, 100 + i * 50))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = max(self.selected_option - 1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = min(self.selected_option + 1, len(self.options) - 1)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                            print('Start Game')
                        elif self.selected_option == 1:
                            print('Options')
                        elif self.selected_option == 2:
                            running = False

            # Fill the screen with black to clear away the previous frame
            self.screen.fill((0, 0, 0))
            # Draw the background image at the top left corner of the screen
            self.screen.blit(self.background, (0, 0))

            self.draw()
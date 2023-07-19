# Example file showing a basic pygame "game loop"
import pygame
import time
from utils import Utils
from game_loop import GameLoop


class MainMenu:

    def __init__(self, game_display):
        self.game_display = game_display
        self.utils = Utils()

    def handle_update(self):
        pass

    def play(self):
        game_loop = GameLoop(self.game_display)
        start_time = time.time()
        game_loop.render_environment(start_time)

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    def render(self):
        intro = True
        background_image = pygame.image.load("../resources/homescreen1.jpg").convert()
        screen_width, screen_height = pygame.display.get_surface().get_size()
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        while intro:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                elif event.type == pygame.VIDEORESIZE:
                    # Handle window resizing
                    screen_width, screen_height = event.size
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

            self.game_display.blit(background_image, [0, 0])
            largeText = pygame.font.SysFont("Magneto", 115)

            TextSurf, TextRect = self.utils.text_objects("Farm Off!!", largeText, "black")

            screen_width, screen_height = pygame.display.get_surface().get_size()
            TextRect.center = ((screen_width / 2), (1.2*screen_height / 3))
            self.game_display.blit(TextSurf, TextRect)

            self.utils.button(self.game_display, "Play", screen_width / 2, 2 * screen_height / 3, 100, 50, "#67BF87",
                              (0, 200, 0), self.play)
            self.utils.button(self.game_display, "Exit", screen_width / 2, 4 * screen_height / 5, 100, 50, '#A60000',
                              (200, 0, 0), self.quit_game)

            pygame.display.update()

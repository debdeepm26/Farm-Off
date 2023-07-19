# Example file showing a basic pygame "game loop"
import pygame
from utils import Utils
from environment import Environment


class MainMenu:
    utils = Utils()

    def __init__(self, game_display):
        self.game_display = game_display

    def handle_update(self):
        pass

    def play(self):
        pass

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    def render(self):
        intro = True

        while intro:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            self.game_display.fill("#C2B28F")
            largeText = pygame.font.SysFont("Magneto", 115)

            TextSurf, TextRect = self.utils.text_objects("Farm Off!!", largeText)

            screen_width, screen_height = pygame.display.get_surface().get_size()
            TextRect.center = ((screen_width / 2), (screen_height / 3))
            self.game_display.blit(TextSurf, TextRect)

            self.utils.button(self.game_display, "Play", screen_width / 2, 2 * screen_height / 3, 100, 50, "#67BF87",
                              (0, 200, 0))
            self.utils.button(self.game_display, "Exit", screen_width / 2, 4 * screen_height / 5, 100, 50, '#A60000',
                              (200, 0, 0), self.quit_game)

            pygame.display.update()
# Example file showing a basic pygame "game loop"
import pygame
import time
from utils import Utils
from game_loop import GameLoop


class MainMenu:

    def __init__(self, game_display):
        self.image = None
        self.game_display = game_display
        self.utils = Utils()

    def handle_update(self):
        pass

    def single_player(self):
        start = True

        while start:
            self.game_display.blit(self.image, [0, 0])
            largeText = pygame.font.SysFont("Magneto", 115)

            TextSurf, TextRect = self.utils.text_objects("Start", largeText, "black")

            screen_width, screen_height = pygame.display.get_surface().get_size()
            TextRect.center = ((screen_width / 2), (1.2 * screen_height / 3))
            self.game_display.blit(TextSurf, TextRect)

            pygame.display.update()

            pygame.time.wait(1000)
            start = False

        game_loop = GameLoop(self.game_display)
        start_time = time.time()
        game_loop.render_environment(start_time, 1)

    def dual_player(self):
        start = True

        while start:
            self.game_display.blit(self.image, [0, 0])
            largeText = pygame.font.SysFont("Magneto", 115)

            TextSurf, TextRect = self.utils.text_objects("Start", largeText, "black")

            screen_width, screen_height = pygame.display.get_surface().get_size()
            TextRect.center = ((screen_width / 2), (1.2 * screen_height / 3))
            self.game_display.blit(TextSurf, TextRect)

            pygame.display.update()

            pygame.time.wait(1000)
            start = False

        game_loop = GameLoop(self.game_display)
        start_time = time.time()
        game_loop.render_environment(start_time, 2)

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    def render(self):
        intro = True
        background_image = pygame.image.load("../resources/homescreen1.jpg").convert()
        controls = pygame.image.load("../resources/controls.png").convert()
        screen_width, screen_height = pygame.display.get_surface().get_size()
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        self.image = background_image

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

            self.utils.button(self.game_display, "1-Player", screen_width / 2, 3 * screen_height / 5, 100, 50, "#67BF87",
                              (0, 200, 0), self.single_player)
            self.utils.button(self.game_display, "2-Player", screen_width / 2, 2 * screen_height / 3, 100, 50, '#67BF87',
                              (0, 200, 0), self.dual_player)
            self.utils.button(self.game_display, "Exit", screen_width / 2, 4 * screen_height / 5, 100, 50, '#A60000',
                              (200, 0, 0), self.quit_game)

            controls = pygame.image.load("../resources/controls_2.png").convert()
            controls.set_colorkey((0, 0, 0), pygame.RLEACCEL)
            controls = pygame.transform.scale(controls, (0.20*screen_width, 0.20*screen_height))
            self.game_display.blit(controls, [1.2*screen_width / 3, 4.2*screen_height / 5])

            pygame.display.update()

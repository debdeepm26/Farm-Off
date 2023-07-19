import pygame
import time
from utils import Utils
from environment import Environment


class GameLoop:

    def __init__(self, game_display):
        self.game_display = game_display
        self.environment = Environment('#5A7843', self.game_display)
        self.utils = Utils()

    def render_environment(self, start_time):
        environment_flag = True
        grid_units = 20

        while environment_flag:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            current_time = time.time() - start_time

            if current_time > 60:
                environment_flag = False

            self.game_display.fill("black")

            vertical, horizontal = pygame.display.get_surface().get_size()
            env_width_units, env_hor_units = int(0.9*vertical) // grid_units, int(horizontal) // grid_units
            adp_env_width = env_width_units*grid_units
            adp_env_height = env_hor_units*grid_units

            pygame.draw.rect(self.environment.screen, self.environment.texture,
                             (0, 0, adp_env_width, adp_env_height))

            for x in range(0, adp_env_width, env_width_units):
                pygame.draw.line(self.game_display, (0, 0, 0), (x, 0), (x, adp_env_height))

            for y in range(0, adp_env_height, env_hor_units):
                pygame.draw.line(self.game_display, (0, 0, 0), (0, y), (adp_env_width, y))

            smallText = pygame.font.SysFont("comicsansms", 20)
            textSurf, textRect = self.utils.text_objects(str(int(current_time)) + " Secs", smallText, "#FBF9D9")
            textRect.center = (vertical - 50, 25)
            self.game_display.blit(textSurf, textRect)

            pygame.display.update()

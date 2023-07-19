import pygame
import time
from utils import Utils
from environment import Environment
from player import Player


class GameLoop:

    def __init__(self, game_display):
        self.game_display = game_display
        self.environment = Environment('#5A7843', self.game_display)
        self.utils = Utils()

    def render_environment(self, start_time, player_num = 1):
        environment_flag = True
        grid_units = 20
        players = []
        start = True

        tractor_image = pygame.image.load("../resources/tractor.png").convert()
        clock = pygame.time.Clock()
        while environment_flag:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            current_time = time.time() - start_time

            if current_time > 3600:
                environment_flag = False

            # field render
            self.game_display.fill("black")
            width, height = pygame.display.get_surface().get_size()
            env_width_units, env_height_units = int(0.9*width) // grid_units, int(height) // grid_units
            IMAGE_SIZE = (env_width_units//2, env_height_units//2)
            adp_env_width = env_width_units*grid_units
            adp_env_height = env_height_units*grid_units

            tractor_image = pygame.transform.scale(tractor_image, IMAGE_SIZE)

            pygame.draw.rect(self.environment.screen, self.environment.texture,
                             (0, 0, adp_env_width, adp_env_height))

            # grid render
            for x in range(0, adp_env_width, env_width_units):
                pygame.draw.line(self.game_display, (0, 0, 0), (x, 0), (x, adp_env_height))

            for y in range(0, adp_env_height, env_height_units):
                pygame.draw.line(self.game_display, (0, 0, 0), (0, y), (adp_env_width, y))

            # time render
            smallText = pygame.font.SysFont("comicsansms", 20)
            textSurf, textRect = self.utils.text_objects(str(int(current_time)) + " Secs", smallText, "#FBF9D9")
            textRect.center = (width - 50, 25)
            self.game_display.blit(textSurf, textRect)

            # player render
            # if player_num >= 2:
            #     players.append(Player(adp_env_width - env_width_units//2, adp_env_height - env_height_units//2))
            #     players.append(Player(3*env_width_units//4, 3*env_height_units//4))
            # else:

            if start:
                player = Player(adp_env_width - 3*env_width_units//4, adp_env_height - 3*env_height_units//4, tractor_image)
                start = False

            pressed_keys = pygame.key.get_pressed()

            # for player in players:
            player.update(pressed_keys, env_width_units, env_height_units, adp_env_width, adp_env_height)
            self.game_display.blit(player.image, [player.curr_x, player.curr_y])

            pygame.display.update()
            clock.tick(10)

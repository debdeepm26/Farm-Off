import pygame
import time
import math
from utils import Utils
from environment import Environment
from player import Player
from popup import PopupObject


class GameLoop:

    def __init__(self, game_display):
        self.game_display = game_display
        texture = pygame.image.load("../resources/grass.jpg").convert()
        self.environment = Environment(texture, self.game_display)
        self.utils = Utils()
        self.all_sprites = pygame.sprite.Group()
        self.popup_group = pygame.sprite.Group()
        self.corns = []

    def create_popup(self, width_step, height_step, width, height, IMAGE_SIZE):
        popup = PopupObject(width_step, height_step, width, height, IMAGE_SIZE)
        self.corns.append([popup.rect.x, popup.rect.y])
        self.all_sprites.add(popup)
        self.popup_group.add(popup)
        self.popup_group.remove()

    def show_popup(self, message, game_display, width, height):
        popup_font = pygame.font.Font(None, 100)
        popup_text = popup_font.render(message, True, (255, 255, 255))
        popup_rect = popup_text.get_rect(center=(width // 2, height // 2))
        game_display.blit(popup_text, popup_rect)
        pygame.display.flip()
        pygame.time.delay(5000)

    def render_environment(self, start_time, player_num=1):
        environment_flag = True
        grid_units = 20
        players = []
        start = True

        tractor1_image = pygame.image.load("../resources/tractor_2.1.png").convert()
        tractor1_image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        tractor2_image = pygame.image.load("../resources/tractor_1.1.png").convert()
        tractor2_image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        clock = pygame.time.Clock()
        while environment_flag:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            current_time = time.time() - start_time
            num_popups = 25

            # field render
            self.game_display.fill("black")
            width, height = pygame.display.get_surface().get_size()
            env_width_units, env_height_units = int(0.9 * width) // grid_units, int(height) // grid_units
            IMAGE_SIZE = (env_width_units // 2, env_height_units // 2)
            adp_env_width = env_width_units * grid_units
            adp_env_height = env_height_units * grid_units

            if current_time > 60:
                if player_num == 1:
                    if players[0].score == num_popups:
                        self.show_popup("Green collected; " + str(players[0].score) + "Corns: " + "in 60 seconds", self.game_display, width, height)
                        environment_flag = False
                else:
                    if players[0].score > players[1].score:
                        self.show_popup("Green Player Wins", self.game_display, width, height)
                        environment_flag = False
                    elif players[0].score < players[1].score:
                        self.show_popup("Yellow Player Wins", self.game_display, width, height)
                        environment_flag = False
                    else:
                        self.show_popup("Draw", self.game_display, width, height)
                        environment_flag = False

            tractor1_image = pygame.transform.scale(tractor1_image, IMAGE_SIZE)
            tractor2_image = pygame.transform.scale(tractor2_image, IMAGE_SIZE)

            background_image = pygame.transform.scale(self.environment.texture, (adp_env_width, adp_env_height))
            self.game_display.blit(background_image, (0, 0))

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

            # Total Corn render
            smallText = pygame.font.SysFont("comicsansms", 20)
            textSurf, textRect = self.utils.text_objects("Total Corns: " + str(int(num_popups)), smallText, "#FBF9D9")
            textRect.center = (width - 80, 50)
            self.game_display.blit(textSurf, textRect)

            # Number of pop-ups you want to display

            # player render
            if start:
                if player_num == 2:
                    players.append(Player(1, adp_env_width - 3 * env_width_units // 4,
                                          adp_env_height - 3 * env_height_units // 4, tractor1_image))
                    players.append(Player(2, env_width_units // 4, env_height_units // 4, tractor2_image))
                else:
                    players.append(Player(1, adp_env_width - 3 * env_width_units // 4,
                                          adp_env_height - 3 * env_height_units // 4, tractor1_image))

                for _ in range(num_popups):
                    self.create_popup(env_width_units, env_height_units, adp_env_width, adp_env_height, IMAGE_SIZE)

                start = False

            pressed_keys = pygame.key.get_pressed()

            for index1, player in enumerate(players):
                player.update(pressed_keys, env_width_units, env_height_units, adp_env_width, adp_env_height)
                self.game_display.blit(player.image, [player.curr_x, player.curr_y])

                for index2, corn in enumerate(self.corns):
                    if math.dist([player.curr_x, player.curr_y], corn) <= 1.5:
                        print("Collision")
                        self.corns.pop(index2)
                        sprite_to_kill = self.all_sprites.sprites()[index2]
                        sprite_to_kill.kill()
                        player.score += 1

            # Update and draw all sprites
            self.all_sprites.update()
            self.all_sprites.draw(self.game_display)

            if player_num == 1:
                smallText = pygame.font.SysFont("comicsansms", 20)
                textSurf1, textRect1 = self.utils.text_objects("Green Score: " + str(players[0].score), smallText, "#FBF9D9")
                textRect1.center = (width - 80, 75)
                self.game_display.blit(textSurf1, textRect1)
            elif player_num == 2:
                smallText = pygame.font.SysFont("comicsansms", 20)

                textSurf1, textRect1 = self.utils.text_objects("Green Score: " + str(players[0].score), smallText, "#FBF9D9")
                textRect1.center = (width - 80, 95)
                self.game_display.blit(textSurf1, textRect1)

                textSurf2, textRect2 = self.utils.text_objects("Yellow Score: " + str(players[1].score), smallText, "#FBF9D9")
                textRect2.center = (width - 80, 120)
                self.game_display.blit(textSurf2, textRect2)

            if player_num == 1:
                if players[0].score == num_popups:
                    self.show_popup("Green collected; " + str(players[0].score) + " corns in " + str(int(current_time)) + " seconds", self.game_display, width, height)
                    environment_flag = False
            else:
                if players[0].score + players[1].score == num_popups:
                    if players[0].score > players[1].score:
                        self.show_popup("Green Player Wins", self.game_display, width, height)
                        environment_flag = False
                    elif players[0].score < players[1].score:
                        self.show_popup("Yellow Player Wins", self.game_display, width, height)
                        environment_flag = False
                    else:
                        self.show_popup("Draw", self.game_display, width, height)
                        environment_flag = False

            pygame.display.update()
            clock.tick(10)





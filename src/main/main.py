# Example file showing a basic pygame "game loop"
import os
import pygame
from main_menu import MainMenu
from game_loop import GameLoop


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption('Farm Off')

    info = pygame.display.Info()
    screen_width, screen_height = info.current_w - 200, info.current_h - 150

    game_display = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)

    main_menu = MainMenu(game_display)

    main_menu.render()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

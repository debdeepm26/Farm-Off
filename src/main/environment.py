# Example file showing a basic pygame "game loop"
import pygame


class Environment:

    def __init__(self, texture, vertical, horizontal):
        self.texture = texture
        self.vertical = vertical
        self.horizontal = horizontal

    def render_environment(self):
        screen = pygame.display.set_mode((1280, 720))
        return screen.fill(self.texture)
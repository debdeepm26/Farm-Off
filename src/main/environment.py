# Example file showing a basic pygame "game loop"
import pygame


class Environment:

    def __init__(self, texture, gameDisplay):
        self.texture = texture
        self.screen = gameDisplay

        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.vertical, self.horizontal = self.screen_width - 100, self.screen_height - 200

    def render_environment(self):
        pygame.draw.rect(self.screen, self.texture, (0, 0, self.horizontal, self.vertical))
        # return self.screen.fill(self.texture)

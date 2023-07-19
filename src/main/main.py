# Example file showing a basic pygame "game loop"
import pygame
from environment import Environment


def main():
    # pygame setup
    pygame.init()
    environment = Environment("green", 32, 46)
    # screen = pygame.display.set_mode((1280, 720))
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        environment.render_environment()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

# Example file showing a basic pygame "game loop"
import pygame
from environment import Environment


def main():
    # pygame setup
    pygame.init()
    environment = Environment("purple", 32, 46)
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        environment.render_environment()

        pygame.display.flip()
        #
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()

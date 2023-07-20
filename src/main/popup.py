import pygame
import random


class PopupObject(pygame.sprite.Sprite):
    def __init__(self, width_step, height_step, width, height, IMAGE_SIZE):
        super().__init__()
        # Replace 'your_object_image.png' with the path to your object's image
        self.image = pygame.image.load('../resources/corn-removebg-preview.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()

        x_coord = random.randrange(0, width, width_step) - 3 * width_step // 4
        y_coord = random.randrange(0, height, height_step) - 3 * height_step // 4

        while x_coord <=0:
            x_coord = random.randrange(0, width, width_step) - 3 * width_step // 4

        while y_coord <= 0:
            y_coord = random.randrange(0, height, height_step) - 3 * height_step // 4

        self.rect.x = x_coord
        self.rect.y = y_coord




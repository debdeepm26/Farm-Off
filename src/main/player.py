import pygame


class Player:

    def __init__(self, player_id, start_x, start_y, image):
        self.player_id = player_id
        self.start_x = start_x
        self.start_y = start_y
        self.curr_x = self.start_x
        self.curr_y = self.start_y

        self.image_up = pygame.transform.rotate(image, -90)
        self.image_down = pygame.transform.rotate(image, 90)
        self.image_left = pygame.transform.rotate(image, 0)
        self.image_right = pygame.transform.rotate(image, 180)

        if self.player_id == 1:
            self.image = self.image_left
        else:
            self.image = self.image_right

        self.score = 0

    def update_pos(self, x, y):
        self.curr_x = x
        self.curr_y = y

    def fetch_pos(self):
        return self.curr_x, self.curr_y

    def update(self, pressed_keys, env_width_units, env_height_units, adp_env_width, adp_env_height):
        if self.player_id == 1:
            if pressed_keys[pygame.K_UP]:
                y_tmp = self.curr_y
                y_tmp -= env_height_units
                if 0 < y_tmp < adp_env_height:
                    self.curr_y = y_tmp
                    self.image = self.image_up
            if pressed_keys[pygame.K_DOWN]:
                y_tmp = self.curr_y
                y_tmp += env_height_units
                if 0 < y_tmp < adp_env_height:
                    self.curr_y = y_tmp
                    self.image = self.image_down
            if pressed_keys[pygame.K_LEFT]:
                x_tmp = self.curr_x
                x_tmp -= env_width_units
                if 0 < x_tmp < adp_env_width:
                    self.curr_x = x_tmp
                    self.image = self.image_left
            if pressed_keys[pygame.K_RIGHT]:
                x_tmp = self.curr_x
                x_tmp += env_width_units
                if 0 < x_tmp < adp_env_width:
                    self.curr_x = x_tmp
                    self.image = self.image_right

        elif self.player_id == 2:
            if pressed_keys[pygame.K_w]:
                y_tmp = self.curr_y
                y_tmp -= env_height_units
                if 0 < y_tmp < adp_env_height:
                    self.curr_y = y_tmp
                    self.image = self.image_up
            if pressed_keys[pygame.K_s]:
                y_tmp = self.curr_y
                y_tmp += env_height_units
                if 0 < y_tmp < adp_env_height:
                    self.curr_y = y_tmp
                    self.image = self.image_down
            if pressed_keys[pygame.K_a]:
                x_tmp = self.curr_x
                x_tmp -= env_width_units
                if 0 < x_tmp < adp_env_width:
                    self.curr_x = x_tmp
                    self.image = self.image_left
            if pressed_keys[pygame.K_d]:
                x_tmp = self.curr_x
                x_tmp += env_width_units
                if 0 < x_tmp < adp_env_width:
                    self.curr_x = x_tmp
                    self.image = self.image_right


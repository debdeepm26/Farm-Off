import pygame


class Utils:

    @staticmethod
    def text_objects(text, font):
        textSurface = font.render(text, True, "#FBF9D9")
        return textSurface, textSurface.get_rect()

    def button(self, gameDisplay, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x + w/2 > mouse[0] > x - w/2 and y + h/2 > mouse[1] > y - h/2:
            pygame.draw.rect(gameDisplay, ac, (x-w/2, y-h/2, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x-w/2, y-h/2, w, h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x, y)
        gameDisplay.blit(textSurf, textRect)

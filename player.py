import pygame
from constants import *

class Player():
    def __init__(self, image):
        self.sheet = image
        self.frames = [self.getPlayerSprite(i, 32, 32, 1, (0, 0, 0)) for i in range(4)]
        self.activeFrame = self.frames[0]

    def getPlayerSprite(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            game = False
            pygame.quit()
        if keys[pygame.K_a]:
            self.activeFrame = self.frames[2]
        if keys[pygame.K_d]:
            self.activeFrame = self.frames[3]
        if keys[pygame.K_w]:
            self.activeFrame = self.frames[1]
        if keys[pygame.K_s]:
            self.activeFrame = self.frames[0]
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

game = True
dt = 0 # Delta time
bg = (15, 15, 15)
black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gameClock = pygame.time.Clock()

# Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
masks = pygame.sprite.Group()


import pygame
from constants import *
from player import *

pygame.init()
pygame.display.set_caption("SECT0R")

# Text
titleFont = pygame.font.Font("HackedCRT.ttf", 24)
gameFont = pygame.font.Font("RETROTECH.ttf", 12)
title = titleFont.render("SECT0R", True, "white") # Title
version = gameFont.render("v0.01", True, "white") # Version

# Player
playerSprites = pygame.image.load('Sect0r_Player_32.png').convert_alpha()
player = Player(playerSprites)

def main():
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gameClock.tick(60) / 1000 # Regulate tick rate
        
        screen.fill(bg) # Zero the screen
        pygame.draw.rect(screen, "white", (15, 15, 690, 690), 1) # Render play area
        # Will need other squares to mask out the play area. Render everything outside the play area after this.

        player.update()
        screen.blit(player.activeFrame, (344, 344)) # Position player at center
        
        screen.blit(title, (720, 0)) # Position title on screen
        screen.blit(version, (1245, 710)) # Position version on screen

        pygame.display.flip() # Updates the full display


if __name__ == "__main__":
    main()

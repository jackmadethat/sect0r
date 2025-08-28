import pygame
from constants import *

def main():
    print("Hello from sect0r!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    dt = 0 # Delta time
    gameClock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    titleFont = pygame.font.Font("HackedCRT.ttf", 24)
    gameFont = pygame.font.Font("RETROTECH.ttf", 12)
    title = titleFont.render("SECT0R", True, "white") # Title
    version = gameFont.render("v0.01", True, "white") # Version

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Game loop
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gameClock.tick(60) / 1000 # Regulate tick rate
        
        screen.fill("black") # Zero the screen to black
        pygame.draw.rect(screen, "white", (15, 15, 690, 690), 1) # Render play area
        # Will need other squares to mask out the play area. Render everything outside the play area after this.
        
        screen.blit(title, (720, 0)) # Position title on screen
        screen.blit(version, (1245, 710)) # Position version on screen

        pygame.display.flip()


if __name__ == "__main__":
    main()

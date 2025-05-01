import pygame, sys

def onTrue(screen, bool):
    while bool:
        screen.fill("black")
        pygame.display.update()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
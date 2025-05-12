import pygame, sys, init

def onTrue(screen: any, frames: any, bool : bool):
    
    while bool:

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    screen.fill("black")
    pygame.display.update()
    frames.tick(init.def_setting.get_fps())
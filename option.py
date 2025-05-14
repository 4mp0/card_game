import pygame, sys, init

def onTrue(screen: any, frames: any, bool : bool):
    
    screen_rect = screen.get_rect()

    while bool:

        bg_image = pygame.image.load()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()
                
        screen.fill("black")
        pygame.display.update()
        frames.tick(init.def_setting.get_fps())
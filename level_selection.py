
import pygame, sys, init, controls
import level1 as lvl1

def onTrue(screen: any, frames: any, bool: bool):
    
    screen_rect = screen.get_rect()
    
    bg_img0 = pygame.image.load("./Gameplay/imgs/level-selection/bg/1.png")
    bg_img1 = pygame.image.load("./Gameplay/imgs/level-selection/bg/2.png")
    bg_img2 = pygame.image.load("./Gameplay/imgs/level-selection/bg/3.png")
    bg_img3 = pygame.image.load("./Gameplay/imgs/level-selection/bg/4.png")

    level1, level1_Rect = init.game_properties.getSR(0)
    level1_Rect.x, level1_Rect.y = 0, 100

    level2, level2_Rect = init.game_properties.getSR(1)
    level2_Rect.x, level2_Rect.y = 70, 100

    level3, level3_Rect = init.game_properties.getSR(2)
    level3_Rect.x, level3_Rect.y = 140, 100

    while bool:
        m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if level1_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    if init.save_data["level"] >= 0:
                        lvl1.onTrue(screen, frames, bool)
            if level2_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    if init.save_data["level"] >= 1:
                        lvl1.onTrue(screen, frames, bool)
            if level3_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    if init.save_data["level"] == 2:
                        lvl1.onTrue(screen, frames, bool)

        screen.fill("black")
        screen.blit(pygame.transform.scale(bg_img0, (init.def_setting.get_width(), init.def_setting.get_height())), screen_rect)
        screen.blit(pygame.transform.scale(bg_img1, (init.def_setting.get_width(), init.def_setting.get_height())), screen_rect)
        screen.blit(pygame.transform.scale(bg_img2, (init.def_setting.get_width(), init.def_setting.get_height())), screen_rect)
        screen.blit(pygame.transform.scale(bg_img3, (init.def_setting.get_width(), init.def_setting.get_height())), screen_rect)
        screen.blit(pygame.transform.scale(level1, (50, 50)), (level1_Rect.x, level1_Rect.y))
        screen.blit(pygame.transform.scale(level2, (50, 50)), (level2_Rect.x, level2_Rect.y))
        screen.blit(pygame.transform.scale(level3, (50, 50)), (level3_Rect.x, level3_Rect.y))
        pygame.display.update()
        frames.tick(init.def_setting.get_fps())

import pygame, sys, init, controls
import json as js
import level1 as lvl1
import level2 as lvl2
import level3 as lvl3

def onTrue(screen: any, frames: any, bool: bool):
    
    screen_rect = screen.get_rect()

    bg_img0 = pygame.image.load("./Gameplay/imgs/bg/level-selection/bg/1.png")
    bg_img1 = pygame.image.load("./Gameplay/imgs/bg/level-selection/bg/2.png")
    bg_img2 = pygame.image.load("./Gameplay/imgs/bg/level-selection/bg/3.png")
    bg_img3 = pygame.image.load("./Gameplay/imgs/bg/level-selection/bg/4.png")

    level1, level1_Rect = init.level_buttons.getSR(0)
    level1_Rect.x, level1_Rect.y = 150, 150

    level2, level2_Rect = init.level_buttons.getSR(1)
    level2_Rect.x, level2_Rect.y = 250, 150

    level3, level3_Rect = init.level_buttons.getSR(2)
    level3_Rect.x, level3_Rect.y = 350, 150

    level2_u = pygame.image.load("./assets/imgs/lvl-selection/2_2.png").convert_alpha()
    level2_u_Rect = level2_u.get_rect()
    level2_u_Rect.x, level2_u_Rect.y = 250, 150

    level3_u = pygame.image.load("./assets/imgs/lvl-selection/3_3.png").convert_alpha()
    level3_u_Rect = level3_u.get_rect()
    level3_u_Rect.x, level3_u_Rect.y = 350, 150

    back_button, back_button_Rect = init.level_buttons.getSR(3)
    back_button_Rect.x, back_button_Rect.y = 0, 0

    visible1, visible2 = True, True

    while bool:
        m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()
        
        with open("./SaveData/data.json", "r") as f:
            save_data = js.load(f)

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()

            if level1_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    if save_data["level"] == 0 or save_data["level"] >= 0:
                        lvl1.onTrue(screen, frames, bool)
            if level2_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    if save_data["level"] == 1 or save_data["level"] >= 1:
                        lvl2.onTrue(screen, frames, bool)
            if level3_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    if save_data["level"] >= 2:
                        lvl3.onTrue(screen, frames, bool)
            if back_button_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    bool = False

        if init.click_sfx:
            onclick_sfx = pygame.mixer.Sound("./assets/sfx/click.mp3")
            channel_sfx = onclick_sfx.play()
            channel_sfx.set_volume(1)
            init.click_sfx = False

        screen.fill("black")
        screen.blit(pygame.transform.scale(bg_img0, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_img1, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_img2, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_img3, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        
        screen.blit(back_button, (back_button_Rect.x, back_button_Rect.y))
        screen.blit(level1, (level1_Rect.x, level1_Rect.y))

        if save_data["level"] != 1:
            screen.blit(level2_u, (level2_u_Rect.x, level2_Rect.y))
        if save_data["level"] != 2:
            screen.blit(level3_u, (level3_u_Rect.x, level3_Rect.y))  

        if save_data["level"] == 1:
            visible1 = not True
        if save_data["level"] == 2:
            visible2 = not True

        if not visible1:
            screen.blit(level2, (level2_Rect.x, level2_Rect.y))
        if not visible2:
            screen.blit(level3, (level3_Rect.x, level3_Rect.y))  

        pygame.display.update()
        frames.tick(init.settings_data["fps"])
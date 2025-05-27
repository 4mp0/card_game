import pygame, sys, init
import json as js
def onTrue(screen: any, frames: any, bool : bool):
    
    bg_layer0 = pygame.image.load("./Option/bg/0.png")
    bg_layer1 = pygame.image.load("./Option/bg/1.png")
    bg_layer2 = pygame.image.load("./Option/bg/2.png")
    bg_layer3 = pygame.image.load("./Option/bg/3.png")

    screen_rect = screen.get_rect()

    back_button, back_button_Rect = init.level_buttons.getSR(3)
    back_button_Rect.x, back_button_Rect.y = 0, 0

    bgm_arrow_up = pygame.image.load("./option/imgs/up.png").convert_alpha()
    bgm_arrow_upRect = bgm_arrow_up.get_rect()
    bgm_arrow_upRect.x, bgm_arrow_upRect.y = 159, 50

    bgm_arrow_down = pygame.image.load("./option/imgs/down.png").convert_alpha()
    bgm_arrow_downRect = bgm_arrow_down.get_rect()
    bgm_arrow_downRect.x, bgm_arrow_downRect.y = 200, 50

    sfx_arrow_up = pygame.image.load("./option/imgs/up.png").convert_alpha()
    sfx_arrow_upRect = sfx_arrow_up.get_rect()
    sfx_arrow_upRect.x, sfx_arrow_upRect.y = 159, 100

    sfx_arrow_down = pygame.image.load("./option/imgs/down.png").convert_alpha()
    sfx_arrow_downRect = sfx_arrow_down.get_rect()
    sfx_arrow_downRect.x, sfx_arrow_downRect.y = 200, 100

    with open("./Option/settings.json", "r") as f:
        settings_data = js.load(f)

    bgm_vol = settings_data["bgm_vol"]
    sfx_vol = settings_data["sfx_vol"]

    txtBGM = pygame.image.load("./option/imgs/0.png").convert_alpha()
    txtBGM_rect = txtBGM.get_rect()
    txtBGM_rect.x, txtBGM_rect.y = 0, 0

    txtSFX = pygame.image.load("./option/imgs/1.png").convert_alpha()
    txtSFX_rect = txtSFX.get_rect()
    txtSFX_rect.x, txtSFX_rect.y = 0, 50
    
    while bool:
        with open("./Option/settings.json", "r") as f:
            settings_data = js.load(f)
        m_x, m_y = init.controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()
            if bgm_arrow_upRect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    bgm_vol += 0.01
            if bgm_arrow_downRect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    bgm_vol -= 0.01
            if sfx_arrow_upRect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    sfx_vol += 0.01
            if sfx_arrow_downRect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    sfx_vol -= 0.01
            if back_button_Rect.collidepoint(m_x, m_y):
                if evs.type == pygame.MOUSEBUTTONDOWN:
                    init.click_sfx = True
                    user_data = init.save_setting.SaveSetting(600, 400, 60, False, bgm_vol, sfx_vol)
                    user_data.save()
                    bool = False

        if init.click_sfx:
            onclick_sfx = pygame.mixer.Sound("./assets/sfx/click.mp3")
            channel_sfx = onclick_sfx.play()
            channel_sfx.set_volume(settings_data["sfx_vol"])
            init.click_sfx = False

        screen.fill("black")
        screen.blit(pygame.transform.scale(bg_layer0, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer1, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer2, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer3, (init.settings_data["width"], init.settings_data["height"])), screen_rect)

        screen.blit(pygame.transform.scale(txtBGM, (150, 150)), (txtBGM_rect.x, txtBGM_rect.y))
        screen.blit(pygame.transform.scale(txtSFX, (150, 150)), (txtSFX_rect.x, txtSFX_rect.y))
        screen.blit(bgm_arrow_up, (bgm_arrow_upRect.x, bgm_arrow_upRect.y))
        screen.blit(bgm_arrow_down, (bgm_arrow_downRect.x, bgm_arrow_downRect.y))

        screen.blit(sfx_arrow_up, (sfx_arrow_upRect.x, sfx_arrow_upRect.y))
        screen.blit(sfx_arrow_down, (sfx_arrow_downRect.x, sfx_arrow_downRect.y))

        screen.blit(back_button, (back_button_Rect.x, back_button_Rect.y))

        pygame.display.update()
        frames.tick(init.settings_data["fps"])
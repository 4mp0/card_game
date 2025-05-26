import pygame, sys, init

def onTrue(screen: any, frames: any, bool : bool):
    
    bg_layer0 = pygame.image.load("./Option/bg/0.png")
    bg_layer1 = pygame.image.load("./Option/bg/1.png")
    bg_layer2 = pygame.image.load("./Option/bg/2.png")
    bg_layer3 = pygame.image.load("./Option/bg/3.png")

    screen_rect = screen.get_rect()

    back_button, back_button_Rect = init.level_buttons.getSR(0)
    back_button_Rect.x, back_button_Rect.y = 0, 0

    while bool:

        m_x, m_y = init.controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()
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
        screen.blit(pygame.transform.scale(bg_layer0, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer1, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer2, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer3, (init.settings_data["width"], init.settings_data["height"])), screen_rect)

        screen.blit(back_button, (back_button_Rect.x, back_button_Rect.y))

        pygame.display.update()
        frames.tick(init.settings_data["fps"])
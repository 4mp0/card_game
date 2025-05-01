
import pygame
import controls
import sys
import init

def onTrue(screen, frames, bool):

    screenRect = screen.get_rect()
    bg_img = init.fight_sceneBG
    
    pygame.mixer_music.stop()

    randCard1 = init.game_properties.getRand() # Random card #
    randCard1, randCard1Rect = init.game_properties.getSR(randCard1) # Select as Card 1 #
    randCard1Rect.x, randCard1Rect.y = 0, 100

    randCard2 = init.game_properties.getRand() # Random card #
    randCard2, randCard2Rect = init.game_properties.getSR(randCard2) # Select as Card 2 #
    randCard2Rect.x, randCard2Rect.y = 0, 160
    
    randCard3 = init.game_properties.getRand() # Random card #
    randCard3, randCard3Rect = init.game_properties.getSR(randCard3) # Select as Card 2 #
    randCard3Rect.x, randCard3Rect.y = 0, 220

    char_anim = pygame.sprite.Group()
    player = init.char.Char(50, 230)
    char_anim.add(player)

    while bool:
        m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # 1st Layer #
        screen.blit(pygame.transform.scale(bg_img, (init.def_setting.get_width(), init.def_setting.get_height())), screenRect)
        # 2nd Layer #
        screen.blit(randCard1, (randCard1Rect.x, randCard1Rect.y))
        screen.blit(randCard2,(randCard2Rect.x, randCard2Rect.y))
        screen.blit(randCard3, (randCard3Rect.x, randCard3Rect.y))
        # 3rd Layer #
        char_anim.draw(screen)
        char_anim.update(0.15)
        # Refresh Display #
        pygame.display.update()
        frames.tick(init.def_setting.get_fps())
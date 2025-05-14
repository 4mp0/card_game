
import pygame, init, controls
import sys

def onTrue(screen: any, frames: any, bool: bool):

    screen_rect = screen.get_rect()
    bg_img = init.fight_sceneBG
    
    p_hp = init.player_Health
    npc_hp = init.npc_Health

    npcHP_visible1, npcHP_visible2, npcHP_visible3 = True, True, True
    pHP_visible1, pHP_visible2, pHP_visible3 = True, True, True

    card1_visible, card2_visible, card3_visible = True, True, True

    pygame.mixer_music.stop()
    pygame.mixer_music.unload()

    player_heart1, player_heart1Rect = init.player_hp.getSR(0)
    player_heart1Rect.x, player_heart1Rect.y = 0, 0

    player_heart2, player_heart2Rect = init.player_hp.getSR(1)
    player_heart2Rect.x, player_heart2Rect.y = 20, 0

    player_heart3, player_heart3Rect = init.player_hp.getSR(2)
    player_heart3Rect.x, player_heart3Rect.y = 40, 0

    npc_heart1, npc_heart1Rect = init.npc_hp.getSR(0)
    npc_heart1Rect.x, npc_heart1Rect.y = 550, 0

    npc_heart2, npc_heart2Rect = init.npc_hp.getSR(1)
    npc_heart2Rect.x, npc_heart2Rect.y = 530, 0

    npc_heart3, npc_heart3Rect = init.npc_hp.getSR(2)
    npc_heart3Rect.x, npc_heart3Rect.y = 510, 0

    player_rand_Card1 = init.game_properties.getRand() # Random card #
    player_randCard1, player_randCard1Rect = init.game_properties.getSR(player_rand_Card1) # Select as Card 1 #
    player_randCard1Rect.x, player_randCard1Rect.y = 0, 100

    player_rand_Card2 = init.game_properties.getRand() # Random card #   
    player_randCard2, player_randCard2Rect = init.game_properties.getSR(player_rand_Card2) # Select as Card 2 #
    player_randCard2Rect.x, player_randCard2Rect.y = 0, 160
    
    player_rand_Card3 = init.game_properties.getRand() # Random card #
    player_randCard3, player_randCard3Rect = init.game_properties.getSR(player_rand_Card3) # Select as Card 2 #
    player_randCard3Rect.x, player_randCard3Rect.y = 0, 220

    npc_rand_Card1 = init.game_properties.getRand() # Random card #
    npc_randCard1, player_randCard1Rect = init.game_properties.getSR(npc_rand_Card1) # Select as Card 1 #
    player_randCard1Rect.x, player_randCard1Rect.y = 0, 100

    npc_rand_Card2 = init.game_properties.getRand() # Random card #
    npc_randCard2, npc_randCard2Rect = init.game_properties.getSR(npc_rand_Card2) # Select as Card 2 #
    npc_randCard2Rect.x, npc_randCard2Rect.y = 0, 160
    
    npc_rand_Card3 = init.game_properties.getRand() # Random card #
    npc_randCard3, npc_randCard3Rect = init.game_properties.getSR(npc_rand_Card3) # Select as Card 2 #
    npc_randCard3Rect.x, npc_randCard3Rect.y = 0, 220

    char_anim = pygame.sprite.Group()
    player = init.char.Char(50, 230)
    char_anim.add(player)

    npc_anim = pygame.sprite.Group()
    bot1 = init.npc.NPC(400, 230)
    npc_anim.add(bot1)

    while bool:
        m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        if npc_hp == 0 or npc_hp < 0:
            # Win
            user_data = init.save_Data.SaveData("user", 1)
            user_data.save()
            for evs in pygame.event.get():
                if evs.type == pygame.MOUSEBUTTONDOWN:                 
                    if evs.type ==pygame.MOUSEBUTTONDOWN: 
                        bool = False

        if p_hp == 0 or p_hp < 0:
            # Game Over
            user_data = init.save_Data.SaveData("user", 0)
            user_data.save()
            for evs in pygame.event.get():
                if screen_rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:         
                        bool = False

        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()
                
            if card1_visible:
                if player_randCard1Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        print(player_rand_Card1)
                        card1_visible = False
                        if player_rand_Card1 == 0 and npc_rand_Card1 == 0:
                            npc_hp = 3
                            p_hp = 3
                        if player_rand_Card1 == 0 and npc_rand_Card1 >= 1:
                            npc_hp -= 2
                            player.attack()
                            bot1.attack()
                        if player_rand_Card1 >= 1 and npc_rand_Card1 >= 1:
                            p_hp -= 1
                            npc_hp -= 1
                            player.attack()
                            bot1.attack()
                        if player_rand_Card1 >= 1 and npc_rand_Card1 == 0:
                            p_hp -= 2
                            player.attack()
                            bot1.attack()
                            
            if card2_visible:
                if player_randCard2Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        card2_visible = False
                        if player_rand_Card2 == 0 and npc_rand_Card2 == 0:
                            npc_hp = 3
                            p_hp = 3
                        if player_rand_Card2 == 0 and npc_rand_Card2 >= 1:
                            npc_hp -= 2
                            player.attack()
                            bot1.attack()
                        if player_rand_Card2 >= 1 and npc_rand_Card2 >= 1:
                            p_hp -= 1
                            npc_hp -= 1
                            player.attack()
                            bot1.attack()
                        if player_rand_Card2 >= 1 and npc_rand_Card2 == 0:
                            p_hp -= 2
                            player.attack()
                            bot1.attack()
            
            if card3_visible:
                if player_randCard3Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        card3_visible = False
                        if player_rand_Card3 == 0 and npc_rand_Card3 == 0:
                            npc_hp = 3
                            p_hp = 3
                        if player_rand_Card3 == 0 and npc_rand_Card3 >= 1:
                            npc_hp -= 2
                            player.attack()
                            bot1.attack()
                        if player_rand_Card3 >= 1 and npc_rand_Card3 >= 1:
                            p_hp -= 1
                            npc_hp -= 1
                            player.attack()
                            bot1.attack()
                        if player_rand_Card3 >= 1 and npc_rand_Card3 == 0:
                            p_hp -= 2
                            player.attack()
                            bot1.attack()    
          
        if not card1_visible and not card2_visible and not card3_visible:
            player_rand_Card1 = init.game_properties.getRand() # Random card #
            player_randCard1, player_randCard1Rect = init.game_properties.getSR(player_rand_Card1) # Select as Card 1 #
            player_randCard1Rect.x, player_randCard1Rect.y = 0, 100
            card1_visible = True

            player_rand_Card2 = init.game_properties.getRand() # Random card #   
            player_randCard2, player_randCard2Rect = init.game_properties.getSR(player_rand_Card2) # Select as Card 2 #
            player_randCard2Rect.x, player_randCard2Rect.y = 0, 160
            card2_visible = True

            player_rand_Card3 = init.game_properties.getRand() # Random card #
            player_randCard3, player_randCard3Rect = init.game_properties.getSR(player_rand_Card3) # Select as Card 2 #
            player_randCard3Rect.x, player_randCard3Rect.y = 0, 220
            card3_visible = True

        # 1st Layer #
        screen.fill("black")
        screen.blit(pygame.transform.scale(bg_img, (init.def_setting.get_width(), init.def_setting.get_height())), screen_rect)
        
        # 2nd Layer #
        if npc_hp == 3:
            npcHP_visible1 = True
            npcHP_visible2 = True
            npcHP_visible3 = True
        if p_hp == 3:
            pHP_visible1 = True
            pHP_visible2 = True
            pHP_visible3 = True
        if p_hp == 2:
            pHP_visible1 = False
        if p_hp == 1:
            pHP_visible1 = False
            pHP_visible2 = False
        if p_hp < 0:
            pHP_visible3 = False
        
        if pHP_visible1:
            screen.blit(pygame.transform.scale(player_heart1, (50, 50)), (player_heart1Rect.x, player_heart1Rect.y))
        if pHP_visible2:
            screen.blit(pygame.transform.scale(player_heart2, (50, 50)), (player_heart2Rect.x, player_heart2Rect.y))
        if pHP_visible3:
            screen.blit(pygame.transform.scale(player_heart3, (50, 50)), (player_heart3Rect.x, player_heart3Rect.y))

        if npc_hp == 2:
            npcHP_visible1 = False
        if npc_hp == 1:
            npcHP_visible1 = False
            npcHP_visible2 = False
        if npc_hp < 0:
            npcHP_visible3 = False

        if npcHP_visible1:
            screen.blit(pygame.transform.scale(npc_heart1, (50, 50)), (npc_heart1Rect.x, npc_heart1Rect.y))
        if npcHP_visible2:
            screen.blit(pygame.transform.scale(npc_heart2, (50, 50)), (npc_heart2Rect.x, npc_heart2Rect.y))
        if npcHP_visible3:
            screen.blit(pygame.transform.scale(npc_heart3, (50, 50)), (npc_heart3Rect.x, npc_heart3Rect.y))
        
        # 3rd Layer #
        if card1_visible:
            screen.blit(player_randCard1, (player_randCard1Rect.x, player_randCard1Rect.y))
        if card2_visible:
            screen.blit(player_randCard2,(player_randCard2Rect.x, player_randCard2Rect.y))
        if card3_visible:
            screen.blit(player_randCard3, (player_randCard3Rect.x, player_randCard3Rect.y))
        
        # 4th Layer #
        char_anim.draw(screen)
        char_anim.update(0.15)
        npc_anim.draw(screen)
        npc_anim.update(0.15)
        # Refresh Display #
        pygame.display.update()
        frames.tick(init.def_setting.get_fps())
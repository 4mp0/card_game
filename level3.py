
import pygame, init, controls
import sys

book_thrw = False
p_1, p_2, n_1, n_2 = True, True, True, True
p_1_1, p_2_1, n_1_1, n_2_1 = True, True, True, True

def onTrue(screen: any, frames: any, bool: bool):

    screen_rect = screen.get_rect()
    
    bg_layer0 = pygame.image.load("./Gameplay/imgs/bg/lvl1/1.png").convert_alpha()
    bg_layer1 = pygame.image.load("./Gameplay/imgs/bg/lvl1/2.png").convert_alpha()
    bg_layer2 = pygame.image.load("./Gameplay/imgs/bg/lvl1/3.png").convert_alpha()
    bg_layer3 = pygame.image.load("./Gameplay/imgs/bg/lvl1/4.png").convert_alpha()
    
    bgmMenu_channel = init.bgmMenu_channel
    bgmMenu_channel.pause()

    global book_thrw

    bgm_lvl1 = pygame.mixer.Sound("./assets/bgm/lvl/3.mp3")
    channel = bgm_lvl1.play()
    channel.set_volume(0.2)

    p_hp = init.player_Health
    npc_hp = init.npc_Health

    npcHP_visible1, npcHP_visible2, npcHP_visible3 = True, True, True
    pHP_visible1, pHP_visible2, pHP_visible3 = True, True, True

    card1_visible, card2_visible, card3_visible = True, True, True

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

    book_anim = pygame.sprite.Group()
    book = init.book_anim.Book(120, 285)
    book_anim.add(book)

    char_anim = pygame.sprite.Group()
    player = init.char.Char(50, 230)
    char_anim.add(player)

    npc_anim = pygame.sprite.Group()
    bot = init.npc.NPC(400, 230)
    npc_anim.add(bot)

    p_indi0 = pygame.image.load("./Gameplay/imgs/damage-indi/+2.png").convert_alpha()
    p_indiRect0 = p_indi0.get_rect()
    p_indiRect0.x, p_indiRect0.y = 95, 230

    p_indi1 = pygame.image.load("./Gameplay/imgs/damage-indi/+1.png").convert_alpha()
    p_indiRect1 = p_indi1.get_rect()
    p_indiRect1.x, p_indiRect1.y = 95, 230

    n_indi0 = pygame.image.load("./Gameplay/imgs/damage-indi/-2.png").convert_alpha()
    n_indiRect0 = n_indi0.get_rect()
    n_indiRect0.x, n_indiRect0.y = 95, 230

    n_indi1 = pygame.image.load("./Gameplay/imgs/damage-indi/-1.png").convert_alpha()
    n_indiRect1 = n_indi1.get_rect()
    n_indiRect1.x, n_indiRect1.y = 95, 230
    global p_1, p_2, n_1, n_2
    global p_1_1, p_2_1, n_1_1, n_2_1 

    i = 0
    j = 0

    win = pygame.image.load("./Gameplay/imgs/output/1.png").convert()
    lose = pygame.image.load("./Gameplay/imgs/output/0.png").convert()
    win_bool, lose_bool = True, True
    
    while bool:
        m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()

        if init.click_sfx:
            onclick_sfx = pygame.mixer.Sound("./assets/sfx/click.mp3")
            channel_sfx = onclick_sfx.play()
            channel_sfx.set_volume(1)
            init.click_sfx = False

        if npc_hp == 0 or npc_hp < 0:
            # Win
            win_bool = not True
            user_data = init.save_Data.SaveData("user", 3)
            user_data.save()
            for evs in pygame.event.get():
                if evs.type == pygame.MOUSEBUTTONDOWN:                 
                    if evs.type ==pygame.MOUSEBUTTONDOWN: 
                        p_1, p_2, n_1, n_2 = True, True, True, True
                        p_1_1, p_2_1, n_1_1, n_2_1 = True, True, True, True 
                        book_thrw = False                       
                        channel.stop()  
                        bgmMenu_channel.unpause()
                        bool = False

        if p_hp == 0 or p_hp < 0:
            # Game Over
            lose_bool = not True
            user_data = init.save_Data.SaveData("user", 0)
            user_data.save()
            for evs in pygame.event.get():
                if screen_rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN: 
                        p_1, p_2, n_1, n_2 = True, True, True, True
                        p_1_1, p_2_1, n_1_1, n_2_1 = True, True, True, True
                        book_throw = False
                        channel.stop()  
                        bgmMenu_channel.unpause()
                        bool = False

        if card1_visible:
            if "one" in init.txt :
                card1_visible = False
                if player_rand_Card1 == 0 and npc_rand_Card1 == 0:
                    player.guard()
                    bot.guard()
                if player_rand_Card1 == 1 and npc_rand_Card1 == 1:
                    bot.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 1
                    npc_hp -= 1
                    n_1 = not True
                    n_1_1 = not True
                if player_rand_Card1 == 1 and npc_rand_Card1 == 0:
                    bot.guard()
                    bot.attack()
                    player.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 2
                    n_2 = not True
                if player_rand_Card1 == 0 and npc_rand_Card1 == 1:
                    bot.attack()
                    player.guard()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    n_2_1 = not True
                if player_rand_Card1 == 2 and npc_rand_Card1 == 0:
                    bot.guard()
                    p_hp += 1
                    p_1 = not True
                if player_rand_Card1 == 0 and npc_rand_Card1 == 2:
                    player.guard()
                    npc_hp += 1
                if player_rand_Card1 == 2 and npc_rand_Card1 == 2:
                    p_hp += 2
                    npc_hp += 2
                    p_2 = not True
                    p_2_1 = not True
                if player_rand_Card1 == 1 and npc_rand_Card1 == 2:
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    npc_hp += 1
                    p_1_1 = not True
                    n_2_1 = not True
                if player_rand_Card1 == 2 and npc_rand_Card1 == 1:
                    bot.attack()
                    p_hp -= 2
                    p_hp += 1
                    p_1 = not True
                    n_2 = not True
        if card2_visible:
            if "two" in init.txt or "to" in init.txt:
                card2_visible = False
                if player_rand_Card2 == 0 and npc_rand_Card2 == 0:
                    player.guard()
                    bot.guard()
                if player_rand_Card2 == 1 and npc_rand_Card2 == 1:
                    bot.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 1
                    npc_hp -= 1
                    n_1 = not True
                    n_1_1 = not True
                if player_rand_Card2 == 1 and npc_rand_Card2 == 0:
                    bot.guard()
                    bot.attack()
                    player.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 2
                    n_2 = not True
                if player_rand_Card2 == 0 and npc_rand_Card2 == 1:
                    bot.attack()
                    player.guard()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    n_2_1 = not True
                if player_rand_Card2 == 2 and npc_rand_Card2 == 0:
                    bot.guard()
                    p_hp += 1
                    p_1 = not True
                if player_rand_Card2 == 0 and npc_rand_Card2 == 2:
                    player.guard()
                    npc_hp += 1
                if player_rand_Card2 == 2 and npc_rand_Card2 == 2:
                    p_hp += 2
                    npc_hp += 2
                    p_2 = not True
                    p_2_1 = not True
                if player_rand_Card2 == 1 and npc_rand_Card2 == 2:
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    npc_hp += 1
                    p_1_1 = not True
                    n_2_1 = not True
                if player_rand_Card2 == 2 and npc_rand_Card2 == 1:
                    bot.attack()
                    p_hp -= 2
                    p_hp += 1
                    p_1 = not True
                    n_2 = not True

        if card3_visible:
            if "three" in init.txt:
                card3_visible = False
                if player_rand_Card3 == 0 and npc_rand_Card3 == 0:
                    player.guard()
                    bot.guard()
                if player_rand_Card3 == 1 and npc_rand_Card3 == 1:
                    bot.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 1
                    npc_hp -= 1
                    n_1 = not True
                    n_1_1 = not True
                if player_rand_Card3 == 1 and npc_rand_Card3 == 0:
                    bot.guard()
                    bot.attack()
                    player.attack()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    p_hp -= 2
                    n_2 = not True
                if player_rand_Card3 == 0 and npc_rand_Card3 == 1:
                    bot.attack()
                    player.guard()
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    n_2_1 = not True
                if player_rand_Card3 == 2 and npc_rand_Card3 == 0:
                    bot.guard()
                    p_hp += 1
                    p_1 = not True
                if player_rand_Card3 == 0 and npc_rand_Card3 == 2:
                    player.guard()
                    npc_hp += 1
                if player_rand_Card3 == 2 and npc_rand_Card3 == 2:
                    p_hp += 2
                    npc_hp += 2
                    p_2 = not True
                    p_2_1 = not True
                if player_rand_Card3 == 1 and npc_rand_Card3 == 2:
                    player.attack()
                    book_thrw = True
                    book.book_bool()
                    npc_hp -= 2
                    npc_hp += 1
                    p_1_1 = not True
                    n_2_1 = not True
                if player_rand_Card3 == 2 and npc_rand_Card3 == 1:
                    bot.attack()
                    p_hp -= 2
                    p_hp += 1
                    p_1 = not True
                    n_2 = not True
                
        for evs in pygame.event.get():
            if evs.type == pygame.QUIT:
                init.stream.stop_stream()
                init.stream.close()
                pygame.quit()
                sys.exit()
                
            if card1_visible:
                if player_randCard1Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        card1_visible = False
                        if player_rand_Card1 == 0 and npc_rand_Card1 == 0:
                            player.guard()
                            bot.guard()
                        if player_rand_Card1 == 1 and npc_rand_Card1 == 1:
                            bot.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            n_1 = not True
                            n_1_1 = not True
                        if player_rand_Card1 == 1 and npc_rand_Card1 == 0:
                            bot.guard()
                            bot.attack()
                            player.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            p_hp -= 2
                            n_2 = not True
                        if player_rand_Card1 == 0 and npc_rand_Card1 == 1:
                            bot.attack()
                            player.guard()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            n_2_1 = not True
                        if player_rand_Card1 == 2 and npc_rand_Card1 == 0:
                            bot.guard()
                            p_hp += 1
                            p_1 = not True
                        if player_rand_Card1 == 0 and npc_rand_Card1 == 2:
                            player.guard()
                            npc_hp += 1
                        if player_rand_Card1 == 2 and npc_rand_Card1 == 2:
                            p_hp += 2
                            npc_hp += 2
                            p_2 = not True
                            p_2_1 = not True
                        if player_rand_Card1 == 1 and npc_rand_Card1 == 2:
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            npc_hp += 1
                            p_1_1 = not True
                            n_2_1 = not True
                        if player_rand_Card1 == 2 and npc_rand_Card1 == 1:
                            bot.attack()
                            p_hp -= 2
                            p_hp += 1
                            p_1 = not True
                            n_2 = not True

            if card2_visible:
                if player_randCard2Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        card2_visible = False
                        if player_rand_Card2 == 0 and npc_rand_Card2 == 0:
                            player.guard()
                            bot.guard()
                        if player_rand_Card2 == 1 and npc_rand_Card2 == 1:
                            bot.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            p_hp -= 1
                            npc_hp -= 1
                            n_1 = not True
                            n_1_1 = not True
                        if player_rand_Card2 == 1 and npc_rand_Card2 == 0:
                            bot.guard()
                            bot.attack()
                            player.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            p_hp -= 2
                            n_2 = not True
                        if player_rand_Card2 == 0 and npc_rand_Card2 == 1:
                            bot.attack()
                            player.guard()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            n_2_1 = not True
                        if player_rand_Card2 == 2 and npc_rand_Card2 == 0:
                            bot.guard()
                            p_hp += 1
                            p_1 = not True
                        if player_rand_Card2 == 0 and npc_rand_Card2 == 2:
                            player.guard()
                            npc_hp += 1
                        if player_rand_Card2 == 2 and npc_rand_Card2 == 2:
                            p_hp += 2
                            npc_hp += 2
                            p_2 = not True
                            p_2_1 = not True
                        if player_rand_Card2 == 1 and npc_rand_Card2 == 2:
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            npc_hp += 1
                            p_1_1 = not True
                            n_2_1 = not True
                        if player_rand_Card2 == 2 and npc_rand_Card2 == 1:
                            bot.attack()
                            p_hp -= 2
                            p_hp += 1
                            p_1 = not True
                            n_2 = not True
            
            if card3_visible:
                if player_randCard3Rect.collidepoint(m_x, m_y):
                    if evs.type == pygame.MOUSEBUTTONDOWN:
                        card3_visible = False
                        if player_rand_Card3 == 0 and npc_rand_Card3 == 0:
                            player.guard()
                            bot.guard()
                        if player_rand_Card3 == 1 and npc_rand_Card3 == 1:
                            bot.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            p_hp -= 1
                            npc_hp -= 1
                            n_1 = not True
                            n_1_1 = not True
                        if player_rand_Card3 == 1 and npc_rand_Card3 == 0:
                            bot.guard()
                            bot.attack()
                            player.attack()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            p_hp -= 2
                            n_2 = not True
                        if player_rand_Card3 == 0 and npc_rand_Card3 == 1:
                            bot.attack()
                            player.guard()
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            n_2_1 = not True
                        if player_rand_Card3 == 2 and npc_rand_Card3 == 0:
                            bot.guard()
                            p_hp += 1
                            p_1 = not True
                        if player_rand_Card3 == 0 and npc_rand_Card3 == 2:
                            player.guard()
                            npc_hp += 1
                        if player_rand_Card3 == 2 and npc_rand_Card3 == 2:
                            p_hp += 2
                            npc_hp += 2
                            p_2 = not True
                            p_2_1 = not True
                        if player_rand_Card3 == 1 and npc_rand_Card3 == 2:
                            player.attack()
                            book_thrw = True
                            book.book_bool()
                            npc_hp -= 2
                            npc_hp += 1
                            p_1_1 = not True
                            n_2_1 = not True
                        if player_rand_Card3 == 2 and npc_rand_Card3 == 1:
                            bot.attack()
                            p_hp -= 2
                            p_hp += 1
                            p_1 = not True
                            n_2 = not True

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
        
        if p_hp > 3:
            p_hp = 3
        if npc_hp > 3:
            npc_hp = 3

        # 1st Layer #
        screen.fill("black")
        screen.blit(pygame.transform.scale(bg_layer0, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer1, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer2, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        screen.blit(pygame.transform.scale(bg_layer3, (init.settings_data["width"], init.settings_data["height"])), screen_rect)
        
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
            pHP_visible2 = True
        if p_hp == 1:
            pHP_visible1 = False
            pHP_visible2 = False
        if p_hp < 0:
            pHP_visible1 = False
            pHP_visible2 = False
            pHP_visible3 = False

        if npc_hp == 2:
            npcHP_visible1 = False
            npcHP_visible2 = True
        if npc_hp == 1:
            npcHP_visible1 = False
            npcHP_visible2 = False
        if npc_hp < 0:
            npcHP_visible1 = False
            npcHP_visible2 = False
            npcHP_visible3 = False

        if pHP_visible1:
            screen.blit(pygame.transform.scale(player_heart1, (50, 50)), (player_heart1Rect.x, player_heart1Rect.y))
        if pHP_visible2:
            screen.blit(pygame.transform.scale(player_heart2, (50, 50)), (player_heart2Rect.x, player_heart2Rect.y))
        if pHP_visible3:
            screen.blit(pygame.transform.scale(player_heart3, (50, 50)), (player_heart3Rect.x, player_heart3Rect.y))

        if npcHP_visible1:
            screen.blit(pygame.transform.scale(npc_heart1, (50, 50)), (npc_heart1Rect.x, npc_heart1Rect.y))
        if npcHP_visible2:
            screen.blit(pygame.transform.scale(npc_heart2, (50, 50)), (npc_heart2Rect.x, npc_heart2Rect.y))
        if npcHP_visible3:
            screen.blit(pygame.transform.scale(npc_heart3, (50, 50)), (npc_heart3Rect.x, npc_heart3Rect.y))
        
        if not p_1:
            screen.blit(p_indi1, (p_indiRect1.x, p_indiRect1.y))
            i+=1
            if i == 230:
                i = 0
                p_1 = True
        if not p_2:
            screen.blit(p_indi0, (p_indiRect0.x, p_indiRect0.y))
            i+=1
            if i == 230:
                i = 0
                p_2 = True
        if not n_1:
            screen.blit(n_indi1, (n_indiRect1.x, n_indiRect1.y))
            i+=1
            if i == 230:
                i = 0
                n_1 = True
        if not n_2:
            screen.blit(n_indi0, (n_indiRect0.x, n_indiRect0.y))
            i+=1
            if i == 230:
                i = 0
                n_2 = True


        if not p_1_1:
            screen.blit(p_indi1, (435, 230))
            j+=1
            if j == 230:
                j = 0
                p_1_1 = True
        if not p_2_1:
            screen.blit(p_indi0, (435, 230))
            j+=1
            if j == 230:
                j = 0
                p_2_1 = True
        if not n_1_1:
            screen.blit(n_indi1, (435, 230))
            j+=1
            if i == 230:
                j = 0
                n_1_1 = True
        if not n_2_1:
            screen.blit(n_indi0, (435, 230))
            j+=1
            if j == 230:
                j = 0
                n_2_1 = True

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

        if book_thrw and not player.attack_animBool:
            book_anim.draw(screen)
            book_anim.update(0.15)
        
        if not win_bool:
            screen.blit(pygame.transform.scale(win, (init.settings_data["width"], init.settings_data["height"])), screen_rect)

        if not lose_bool:
            screen.blit(pygame.transform.scale(lose, (init.settings_data["width"], init.settings_data["height"])), screen_rect)

        # Refresh Display #
        pygame.display.update()
        frames.tick(init.settings_data["fps"])
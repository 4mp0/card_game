                if player_rand_Card3 == 0 and npc_rand_Card3 == 0:
                    player.guard()
                    bot.guard()
                    npc_hp = 3
                    p_hp = 3
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
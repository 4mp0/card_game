
import pygame
import setting, controls, buttons, char, npc, stages
import saveData

# Setting #
def_setting = setting.Setting(
    600, # width
    400, #heigt
    60, # Frames per second
    False # Fullscreen
)

# Background Music #



# Menu #

menu_buttons = buttons.Buttons([
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
])

# stage / selection #

# Fight scene: Health, Character, Npcs #

player_Health = 3
npc_Health = 3

player_hp = buttons.Buttons([
    pygame.image.load("./Gameplay/imgs/hearts/player/0.png"),
    pygame.image.load("./Gameplay/imgs/hearts/player/1.png"),
    pygame.image.load("./Gameplay/imgs/hearts/player/2.png")
])

npc_hp = buttons.Buttons([
    pygame.image.load("./Gameplay/imgs/hearts/npc/0.png"),
    pygame.image.load("./Gameplay/imgs/hearts/npc/1.png"),
    pygame.image.load("./Gameplay/imgs/hearts/npc/2.png")
])

fight_sceneBG = pygame.image.load("./Gameplay/imgs/bg/bg1.png")

game_properties = buttons.Buttons([
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
])

"""main_char_hearts = buttons.Buttons([
    pygame.image.load("./Gameplay/imgs/hearts/player/0.jpg"),
    pygame.image.load("./Gameplay/imgs/hearts/player/1.jpg"),
    pygame.image.load("./Gameplay/imgs/hearts/player/2.jpg")
])"""

# Main character in fight scene

# Save Data
"""save = saveData.SaveData("amp", 0)
save.save()"""

"""main_char = char.Char([
    pygame.image.load("./Gameplay/imgs/char/main/0.png"),
    pygame.image.load("./Gameplay/imgs/char/main/1.png"),
    pygame.image.load("./Gameplay/imgs/char/main/2.png"),
    pygame.image.load("./Gameplay/imgs/char/main/3.png"),
    pygame.image.load("./Gameplay/imgs/char/main/4.png"),
    pygame.image.load("./Gameplay/imgs/char/main/5.png"),
    pygame.image.load("./Gameplay/imgs/char/main/6.png"),
    pygame.image.load("./Gameplay/imgs/char/main/7.png"),
    pygame.image.load("./Gameplay/imgs/char/main/8.png")
])"""


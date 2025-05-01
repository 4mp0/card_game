
import pygame
import setting, controls, buttons, char
import random as rand

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


# Fight scene #

fight_sceneBG = pygame.image.load("./Gameplay/imgs/bg/bg1.png")

game_properties = buttons.Buttons([
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
])

# Main character in fight scene

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


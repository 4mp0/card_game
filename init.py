
import pygame, setting, controls, buttons, char, npc, stages, save_Data
import threading, pyaudio
from vosk import Model, KaldiRecognizer
import json as js

# Setting #
def_setting = setting.Setting(
    600, # width
    400, #heigt
    60, # Frames per second
    False # Fullscreen
)

txt = any

model = Model(r"./vosk-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
pause_sr = threading.Event()
pause_sr.set()

def speech_Recognition():
    while True:
        pause_sr.wait()
        data = stream.read(1024)
        if recognizer.AcceptWaveform(data):
            text = recognizer.FinalResult()
            print("Listening")
            txt = text[14:-3]

sr_Thread = threading.Thread(target=speech_Recognition)
sr_Thread.start()

# Background Music #



# Menu #

menu_buttons = buttons.Buttons([
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
    pygame.image.load("./card.png"),
])

# Level Selection

level_buttons = buttons.Buttons([
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

with open("./SaveData/data.json", "r") as f:
    save_data = js.load(f)

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


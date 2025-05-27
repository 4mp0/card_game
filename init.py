
import pygame, controls, buttons, char, npc, save_Data, book_anim, save_setting
import threading, pyaudio
import vosk
import json as js


# BGM
bgmMenu_channel = any


# Sound Effects

click_sfx = False

model = vosk.Model(r"./vosk-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream()
pause_sr = threading.Event()
pause_sr.set()

txt = ""

def speech_Recognition():
    global txt
    while True:
        pause_sr.wait()
        data = stream.read(1024)
        if recognizer.AcceptWaveform(data):
            text = recognizer.FinalResult()
            txt = text[14:-3]
            print(txt)

sr_Thread = threading.Thread(target=speech_Recognition)
sr_Thread.start()

# Menu #

menu_buttons = buttons.Buttons([
    pygame.image.load("./Menu/imgs/buttons/play.png"),
    pygame.image.load("./Menu/imgs/buttons/option.png"),
    pygame.image.load("./Menu/imgs/buttons/quit.png"),
])

option_buttons = buttons.Buttons([
    pygame.image.load("./Menu/imgs/buttons/back.png")
])

# Option Buttons

# Level Selection

level_buttons = buttons.Buttons([
    pygame.image.load("./assets/imgs/lvl-selection/1.png"),
    pygame.image.load("./assets/imgs/lvl-selection/2.png"),
    pygame.image.load("./assets/imgs/lvl-selection/3.png"),
    pygame.image.load("./Menu/imgs/buttons/back.png"),
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
    pygame.image.load("./Gameplay/imgs/cards/0.png"),
    pygame.image.load("./Gameplay/imgs/cards/1.png"),
    pygame.image.load("./Gameplay/imgs/cards/2.png"),
])

# Main character in fight scene

# Load Saved Data

with open("./SaveData/data.json", "r") as f:
    save_data = js.load(f)

# Load Saved Settings
with open("./Option/settings.json", "r") as f:
    settings_data = js.load(f)


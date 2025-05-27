
import pygame, sys
import cv2
import init
import level_selection, option

# Controls and Setting #

controls = init.controls

pygame.init()

pygame.display.set_caption("Card Game")

screen = pygame.display.set_mode((init.settings_data["width"], init.settings_data["height"]))
screenRect = screen.get_rect()

vcap = cv2.VideoCapture('video.mp4')
success, img = vcap.read()
shape = img.shape[1::-1]
frames = pygame.time.Clock()

bgm_menu = pygame.mixer.Sound("./assets/bgm/menu/Hopes and Dreams.mp3")
init.bgmMenu_channel = bgm_menu.play()
init.bgmMenu_channel.set_volume(0.3)

# Menu BG #
BG_img = pygame.image.load("./Menu/imgs/bg/bg.jpg").convert()
# Menu #
play_buttonSurf, play_buttonRect = init.menu_buttons.getSR(0)
play_buttonRect.x, play_buttonRect.y =  265, 150
# option #
option_buttonSurf, option_buttonRect = init.menu_buttons.getSR(1)
option_buttonRect.x, option_buttonRect.y = 265, 220
# quit #
quit_buttonSurf, quit_buttonRect = init.menu_buttons.getSR(2)
quit_buttonRect.x, quit_buttonRect.y = 265, 289

skip_vid = False

i = 0

while True:
    # Events #
    m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()
    success, img = vcap.read()
    for evs in pygame.event.get():
        # Menu Interaction #
        if screenRect.collidepoint(m_x, m_y):
            if evs.type == pygame.MOUSEBUTTONDOWN:
                skip_vid = True
        if play_buttonRect.collidepoint(m_x, m_y):
            if evs.type == pygame.MOUSEBUTTONDOWN: # play #
                init.click_sfx = True
                level_selection.onTrue(screen, frames, True)
        if option_buttonRect.collidepoint(m_x, m_y):
            if evs.type == pygame.MOUSEBUTTONDOWN: # option #
                init.click_sfx = True
                option.onTrue(screen, frames, True)
        if quit_buttonRect.collidepoint(m_x, m_y):
            if evs.type == pygame.MOUSEBUTTONDOWN: # quit #
                init.click_sfx = True
                init.stream.stop_stream()
                init.stream.close()
                sys.exit()
        # QUIT #
        if evs.type == pygame.QUIT:
            init.stream.stop_stream()
            init.stream.close()
            pygame.quit()
            sys.exit()

    # 1st Layer #
    screen.fill("black")
    # 2nd Layer #
    if i != 1590:
        print(i)
        screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))   
        i += 1 
    # 3rd Layer #
    if skip_vid or not success:
        i = 1590
        screen.blit(pygame.transform.scale(BG_img, (init.settings_data["width"], init.settings_data["height"])), screenRect)
        screen.blit(play_buttonSurf, (play_buttonRect.x, play_buttonRect.y))
        screen.blit(option_buttonSurf, (option_buttonRect.x, option_buttonRect.y))
        screen.blit(quit_buttonSurf, (quit_buttonRect.x, quit_buttonRect.y))

    # Refresh Display #
    pygame.display.update()
    frames.tick(init.settings_data["fps"])

import pygame
import sys
import init
import level_selection
import option

### Code is received via init ###

# Controls and Setting #
def_setting = init.def_setting
controls = init.controls

pygame.init()

pygame.display.set_caption("Card Game")
screen = pygame.display.set_mode((def_setting.get_width(), def_setting.get_height()), def_setting.get_fullscreen())
screenRect = screen.get_rect()
frames = pygame.time.Clock()

pygame.mixer_music.load("./BGM/menu/sound1.mp3")
pygame.mixer_music.play(999)

# Menu BG #
BG_img = pygame.image.load("./Menu/imgs/bg.jpg").convert()
# Menu #
play_buttonSurf, play_buttonRect = init.menu_buttons.getSR(0)
play_buttonRect.x, play_buttonRect.y =  265, 150
# option #
option_buttonSurf, option_buttonRect = init.menu_buttons.getSR(1)
option_buttonRect.x, option_buttonRect.y = 265, 220
# quit #
quit_buttonSurf, quit_buttonRect = init.menu_buttons.getSR(2)
quit_buttonRect.x, quit_buttonRect.y = 265, 289

while True:

    #1st Layer #
    screen.fill("black")
    # 2nd Layer #
    screen.blit(pygame.transform.scale(BG_img, (def_setting.get_width(), def_setting.get_height())), screenRect)
    # 3rd Layer #
    screen.blit(play_buttonSurf, (play_buttonRect.x, play_buttonRect.y))
    screen.blit(option_buttonSurf, (option_buttonRect.x, option_buttonRect.y))
    screen.blit(quit_buttonSurf, (quit_buttonRect.x, quit_buttonRect.y))

    # Events #
    m_x, m_y = controls.Controls(pygame.mouse.get_pos()).get_m_XY()

    for evs in pygame.event.get():
        # Menu Interaction #
        if play_buttonRect.collidepoint(m_x, m_y): # Play #
            if evs.type == pygame.MOUSEBUTTONDOWN:
                level_selection.onTrue(screen, frames, True)
        if option_buttonRect.collidepoint(m_x, m_y): # Option #
            if evs.type == pygame.MOUSEBUTTONDOWN:
                option.onTrue(screen, frames, True)
        if quit_buttonRect.collidepoint(m_x, m_y): # Quit #
            if evs.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()
        # QUIT #
        if evs.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Refresh Display #
    pygame.display.update()
    frames.tick(def_setting.get_fps())
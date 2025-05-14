
import pygame

class Char(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int ):
        super().__init__()
        self.animation = []
        self.current_iter = 0
        self.attack_animation = []
        self.attack_current_iter = 0
        self.attack_animBool = False

        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/0.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/1.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/2.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/3.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/4.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/5.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/6.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/7.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/char/0/8.png"))
        self.image = self.animation[self.current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/9.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/10.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/11.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/12.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/13.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/14.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/15.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/char/0/16.png"))
        self.image = self.attack_animation[self.attack_current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

    def attack(self):
        self.attack_animBool = True

    def update(self, speed):

        if not self.attack_animBool:
            self.current_iter += speed
            if int(self.current_iter) >= len(self.animation):
                self.current_iter = 0
            self.image = self.animation[int(self.current_iter)]

        if self.attack_animBool:
            self.attack_current_iter += speed
            if int(self.attack_current_iter) >= len(self.attack_animation):
                self.attack_current_iter = 0
                if self.attack_current_iter == 0:
                    self.attack_animBool = False
            self.image = self.attack_animation[int(self.attack_current_iter)]

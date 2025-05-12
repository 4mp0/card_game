
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

""" 
        self.attack_anim = False
        self.merge_sprite = []
        self.pos_x, self.pos_y = pos_x, pos_y
        
        self.sprites = []
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/0.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/1.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/2.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/3.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/4.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/5.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/6.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/7.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/char/0/8.png"))

        self.attack_sprite = []
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/9.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/10.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/11.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/12.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/13.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/14.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/15.png"))
        self.attack_sprite.append(pygame.image.load("./Gameplay/imgs/char/0/16.png"))

        self.merge_sprite = self.sprites

        self.current_sprite = 0
        self.image = self.merge_sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

    def attack(self):
        self.attack_anim = True
        
    def update(self, speed):

        if self.attack_anim == True:
            self.current_sprite += speed
            print(self.current_sprite)
            self.merge_sprite = self.attack_sprite.copy()
            if int(self.current_sprite) >= len(self.merge_sprite):
                self.current_sprite = 0
                self.attack_anim = False
            self.image = self.merge_sprite[int(self.current_sprite)]


       if self.attack_anim == True:
            self.current_attack_sprite += speed
            if int(self.current_attack_sprite) >= len(self.attack_sprite):
                self.current_attack_sprite = 0
                self.attack_anim = False
            self.attack_image = self.attack_sprite[int(self.current_attack_sprite)]
        elif self.attack_anim == False:
            self.current_attack_sprite += speed      
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_anim = False
            self.image = self.sprites[int(self.current_sprite)]"""

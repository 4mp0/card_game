
import pygame, level1, level2, level3

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int ):
        super().__init__()
        
        self.pos_x, self.pos_y = pos_x, pos_y

        self.animation = []
        self.current_iter = 0

        self.walk_animation = []
        self.walk_current_iter = 0
        self.walk_animBool = False

        self.attack_animation = []
        self.attack_current_iter = 0
        self.attack_animBool = False

        self.guard_animation = []
        self.guard_current_iter = 0
        self.guard_animBool = False

        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/0.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/1.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/2.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/3.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/4.png"))
        self.animation.append(pygame.image.load("./Gameplay/imgs/npc/0/5.png"))
        self.image = self.animation[self.current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x, self.pos_y

        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/26.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/25.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/24.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/23.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/22.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/21.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/20.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/19.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/18.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/17.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/16.png"))
        self.walk_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/15.png"))
        self.image = self.animation[self.walk_current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/6.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/7.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/8.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/9.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/10.png"))
        self.attack_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/11.png"))        
        self.image = self.attack_animation[self.attack_current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

        self.guard_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/12.png"))
        self.guard_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/13.png"))
        self.guard_animation.append(pygame.image.load("./Gameplay/imgs/npc/0/14.png"))
        self.image = self.guard_animation[self.guard_current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

    def guard(self):
        self.guard_animBool = True

    def attack(self):
        self.attack_animBool = True

    def update(self, speed):

        if not self.attack_animBool and not self.guard_animBool:
            self.current_iter += speed
            if int(self.current_iter) >= len(self.animation):
                self.current_iter = 0
            self.image = self.animation[int(self.current_iter)]

        if self.attack_animBool and not level1.book_thrw and not level2.book_thrw and not level3.book_thrw:
            self.rect.x -= 2
            self.walk_current_iter += speed
            if int(self.walk_current_iter) >= len(self.walk_animation):
                self.walk_current_iter = 0
            self.image = self.walk_animation[int(self.walk_current_iter)]

            if self.rect.x <= 160:
                self.attack_current_iter += speed
                if int(self.attack_current_iter) >= len(self.attack_animation):
                    self.attack_current_iter = 0
                    if self.attack_current_iter == 0:
                        self.rect.x = self.pos_x
                        self.attack_animBool = False
                self.image = self.attack_animation[int(self.attack_current_iter)]


        if self.guard_animBool:
            self.guard_current_iter += speed
            if int(self.guard_current_iter) >= len(self.guard_animation):
                self.guard_current_iter = 0
                if self.guard_current_iter == 0:
                    self.guard_animBool = False
            self.image = self.guard_animation[int(self.guard_current_iter)]


"""
        if self.attack_animBool:
            self.attack_current_iter += speed
            if int(self.attack_current_iter) >= len(self.attack_animation):
                self.attack_current_iter = 0
                if self.attack_current_iter == 0:
                    self.attack_animBool = False
            self.image = self.attack_animation[int(self.attack_current_iter)]
"""
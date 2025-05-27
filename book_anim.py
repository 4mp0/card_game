
import pygame, level1, level2, level3

class Book(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int ):
        super().__init__()
        
        self.book_animation = []
        self.current_iter = 0
        self.bool = False
        self.pos_x, self.pos_y = pos_x, pos_y
        
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/21.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/22.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/23.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/24.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/25.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/26.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/27.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/28.png"))
        self.book_animation.append(pygame.image.load("./Gameplay/imgs/char/0/29.png"))
        self.image = self.book_animation[self.current_iter]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos_x, self.pos_y

    def book_bool(self):
        self.bool = True

    def update(self, speed):
        if self.bool == True:
            self.current_iter += speed
            self.rect.x += speed+5
            
            if int(self.current_iter) >= len(self.book_animation):
                self.current_iter = 0
            self.image = self.book_animation[int(self.current_iter)]
            
            if int(self.rect.x) >= 430:
                self.rect.x = self.pos_x
                self.bool = False
                level1.book_thrw = False
                level2.book_thrw = False
                level3.book_thrw = False
            self.rect.x = int(self.rect.x)

            if self.rect.x == 0:
                self.rect.x = 120                

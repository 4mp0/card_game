
import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int ):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/0.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/1.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/2.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/3.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/4.png"))
        self.sprites.append(pygame.image.load("./Gameplay/imgs/npc/0/5.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_x, pos_y

    def update(self, speed):
        self.current_sprite += speed
        if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
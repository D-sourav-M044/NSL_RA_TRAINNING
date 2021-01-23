import pygame,sys
import random
height =800
width =800

bg = pygame.image.load('images/missile.png')

class Missile(pygame.sprite.Sprite):
    def __init__(self,ind_x,ind_y):
        super().__init__()
        self.image = pygame.transform.scale(bg,(80,60))
        self.rect = self.image.get_rect()
        self.rect.x = ind_x
        self.rect.y = ind_y
        
    def update(self):
        self.rect.x += 0
        self.rect.y += 1
        if self.rect.top > height +10 or self.rect.left < -25 or self.rect.right >width +20 :
            self.kill()
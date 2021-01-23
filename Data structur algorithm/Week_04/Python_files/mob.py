import pygame,sys
import random
height =800
width =800
bg = pygame.image.load('images/brick.png')

class MOB(pygame.sprite.Sprite):
    def __init__(self,ind_x):
        super().__init__()
        #self.image = pygame.Surface((30,40))
        self.image = pygame.transform.scale(bg,(40,25))
        #self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        #self.rect.x = random.randrange(60)
        self.rect.x = ind_x
        self.rect.y = random.randrange(-120,-100)
        
    def update(self):
        self.rect.x += 0
        self.rect.y += 1
        if self.rect.top > height +10 or self.rect.left < -25 or self.rect.right >width +20 :
            #self.rect.x = random.randrange(width - self.rect.width)
            #self.rect.y = random.randrange(-100,-40)
            #self.speedy = random.randrange(1,8)
            self.kill()
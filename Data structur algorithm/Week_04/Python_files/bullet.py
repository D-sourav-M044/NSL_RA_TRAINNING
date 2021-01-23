import pygame,sys


bg = pygame.image.load('images/bullet.png')


class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.transform.scale(bg,(20,25))
        self.rect = self.image.get_rect(center =(pos_x,pos_y))
    def update(self):
        self.rect.y -=5
        screen_width,screen_height = 500,500
        if self.rect.x >= screen_width + 200:
            self.kill()
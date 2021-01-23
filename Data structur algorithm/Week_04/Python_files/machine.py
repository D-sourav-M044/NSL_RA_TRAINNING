import pygame,sys
from bullet import Bullet


bg = pygame.image.load('images/rocket.png')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(bg,(85,110))
        self.rect = self.image.get_rect(center = (500,300))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

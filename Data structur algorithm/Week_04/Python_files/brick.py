import pygame
BLACK = (0,0,0)


bg = pygame.image.load('images/brick.png')

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, Color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(bg,(80,50))
        #self.image.fill(color)
        #self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image,BLACK, [-100, 0, width, height])
        

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
#Import the pygame library and initialise the game engine
import  random
import pygame
from pygame import sprite
from pygame import mixer
#Let's import the Paddle Class & the Ball Class
#from paddle import Paddle

from brick import Brick
from bullet import Bullet
from machine import Player
from mob import MOB
from missile import Missile

pygame.init()

bg = pygame.image.load('images/back.jpg')
mixer.music.load('sounds/back_music.mp3')


#Initializing_Some_Colors
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

score = 0
lives = 3

# Open a new window
size = (800, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
pygame.mouse.set_visible(False)

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()



#creating machine
machine = Player()



all_bricks = pygame.sprite.Group()
all_ghost = pygame.sprite.Group()
all_bullet = pygame.sprite.Group()
all_mob = pygame.sprite.Group()


for i in range(10):
    brick = Brick(DARKBLUE,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(RED,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(YELLOW,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(DARKBLUE,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(RED,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 220
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(10):
    brick = Brick(YELLOW,60, 30)
    brick.rect.x = 50 + i * 70
    brick.rect.y = 260
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(machine)
all_sprites_list.update()


# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
              
        if event.type == pygame.MOUSEBUTTONDOWN:
           shot = machine.create_bullet()
           all_sprites_list.add(shot)
           all_bullet.add(shot)
           all_sprites_list.update()
           all_bricks.update()
           all_bullet.update()
        brick_hits = pygame.sprite.spritecollide(machine,all_bricks,False)
        if brick_hits:
            hit_sound = mixer.Sound('sounds/hit.mp3')
            hit_sound.play()
            font = pygame.font.Font(None, 84)
            text = font.render("Game Over !!!!!!", 1, WHITE)
            text1= font.render("Better Luck Next Time ('_')",1,WHITE)
            screen.blit(text, (200, 100))
            screen.blit(text1,(60,150))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False
        hits = pygame.sprite.groupcollide(all_bricks,all_bullet,True,True)
        
        if score!=0 and (score % 20 == 0):
            ghost = Missile(random.randrange(60,900),random.randrange(10,50))
            all_ghost.add(ghost)
            all_sprites_list.add(ghost)

            ghost_bullet = pygame.sprite.groupcollide(all_bullet,all_ghost,True,True)

            all_ghost.update()
            all_sprites_list.update()

            if ghost_bullet :
                score += 2

        if hits:
            bullet_hit = mixer.Sound('sounds/brick.mp3')
            bullet_hit.play()
            brick.kill()
            score +=1 
            print(sprite.Rect.x)
            for i in range(3):
                mob = MOB(pygame.mouse.get_pos()[0])
                all_mob.add(mob)
                all_sprites_list.add(mob)

        all_sprites_list.update()
        all_mob.update()    
        mob_machine = pygame.sprite.spritecollide(machine,all_mob,False)
        mob_bullet = pygame.sprite.groupcollide(all_bullet,all_mob,True,True)
        if mob_machine:
            hit_sound = mixer.Sound('sounds/hit.mp3')
            hit_sound.play()
            font = pygame.font.Font(None, 74)
            text = font.render("Game Over !!!!!!", 1, WHITE)
            text1= font.render("Better Luck Next Time ('_')",1,WHITE)
            screen.blit(text, (200, 100))
            screen.blit(text1, (60, 150))
            pygame.display.flip()
            pygame.time.wait(2000)
            carryOn = False
            
        if mob_bullet:
            bullet_hit = mixer.Sound('sounds/brick.mp3')
            bullet_hit.play()
            score += 1


        all_sprites_list.update()
        all_bricks.update()
        all_bullet.update()    
       
   
    
    
    # --- Game logic should go here
    all_sprites_list.update()
        
    if len(all_bricks) == 0:
        #Display Level Complete Message for 3 seconds
        font = pygame.font.Font(None, 74)
        text = font.render("   Congrates !!!", 1, WHITE)
        text1 = font.render("LEVEL COMPLETE", 1, WHITE)
        screen.blit(text, (200, 100))
        screen.blit(text1, (200, 150))
        pygame.display.flip()
        pygame.time.wait(3000)

        #Stop the Game
        carryOn = False

    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(LIGHTBLUE)
    screen.blit(bg,(-600,-100))
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Brick Breaker" , 1, DARKBLUE)
    screen.blit(text, (280, 10))
    text = font.render("Break all  the bricks" , 1, RED)
    screen.blit(text, (550, 10))

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(70)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()

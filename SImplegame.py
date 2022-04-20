import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RIGHT, K_LEFT, K_SPACE

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
person_display = False 

screen = pygame.display.set_mode(SIZE)

#COLOUR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (207, 16, 32)
GRAY = (157, 161, 158)
PURPLE = (48, 25, 52)
ORANGE = (255, 119, 0)

#triangle
triangle_x = 100
triangle_y = 300

#Alien
alien_x = 630
alien_y = random.randrange(200,400)


#Laser variables
laser_speed = 3
laser_x = random.randrange(75, 100)
laser_y = 0
laser1_x = random.randrange(255, 275)
laser1_y = 0 
laser2_x = random.randrange(155, 190)
laser2_y = 380
laser3_x = random.randrange(500, 520)
laser3_y = 425
laser4_x = random.randrange(475, 495)
laser4_y = 0


# Score Counter 
score = 0 
score_count = 0
scene_title_font = pygame.font.SysFont('Arial', 30)



#Menu Screen

current_screen = 0

clock = pygame.time.Clock()

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT:
                current_screen = 1
            elif event.key == K_LEFT:
                current_screen = 0
                score = 0
            elif event.key == K_SPACE:
                triangle_y += 50
            elif event.type == MOUSEBUTTONDOWN:
                print(event.pos)    
            elif event.type == K_SPACE:
                triangle_y += 10
        elif event.type == QUIT:
            running = False
    
    
    alien_x -= 5
    if alien_x <= 0:
        alien_x = 800
        
        

  


    
            
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    # screen.fill((255, 255, 255))  # always the first drawing command

    if current_screen == 0:
        # Scene 1 (Menu screen)
        screen.fill(GRAY)  # always the first drawing command
        scene_title = scene_title_font.render('WELCOME TO SPACE DODGE!', True, (BLACK))
        screen.blit(scene_title, (0, 0))
        some_title = scene_title_font.render('Instructions:', True,(WHITE))
        screen.blit(some_title, (5, 79))
        some_title = scene_title_font.render('Press space to jump', True,(BLACK))
        screen.blit(some_title, (5, 155))
        some_title = scene_title_font.render('Do not hit the lasers or the space junk', True,(BLACK))
        screen.blit(some_title, (5, 115))
        some_title = scene_title_font.render('Press the right arrow key to begin', True, (BLACK))
        screen.blit(some_title, (5,241))
        some_title = scene_title_font.render('Press the left arrow key to restart', True, (BLACK))
        screen.blit(some_title, (5,341))


    elif current_screen == 1:
        
        #Scene 2 (Game Screen)
        screen.fill(PURPLE)
    
                # triangle
        spaceship = pygame.draw.polygon(screen, (BLACK),[(triangle_x + 70, triangle_y + 60),(triangle_x + 70, triangle_y + 40),(triangle_x + 90, triangle_y + 50)])
        spaceship = pygame.draw.rect(screen, (GRAY),[triangle_x + 30 , triangle_y + 41, 40, 20])
        spaceship = pygame.draw.rect(screen, (ORANGE),[triangle_x + 30 , triangle_y + 41, 10, 20])
        spaceship = pygame.draw.polygon(screen, (GRAY),[(triangle_x + 30, triangle_y + 30),(triangle_x + 70, triangle_y + 40),(triangle_x + 70, triangle_y + 50)])
        spaceship = pygame.draw.polygon(screen, (GRAY),[(triangle_x + 30, triangle_y + 70),(triangle_x + 70, triangle_y + 50),(triangle_x + 70, triangle_y + 60)])
        triangle_y -= 3

#Draw Alien

        aliens = pygame.draw.circle(screen, ("GRAY"), (alien_x, alien_y), 25)

        
#Draw Laser
        laser = pygame.draw.rect(screen, RED,[laser_x, laser_y, 40, 150])
        laser1 = pygame.draw.rect(screen, RED,[laser1_x, laser1_y, 40, 200])
        laser2 = pygame.draw.rect(screen, RED,[laser2_x, laser2_y, 40, 125])
        laser3 = pygame.draw.rect(screen, RED,[laser3_x, laser3_y, 40, 190])
        laser4 = pygame.draw.rect(screen, RED,[laser4_x, laser4_y, 40, 190])

# Laser movement
        if laser_x <= 0:
            laser_x = 700
        elif laser1_x <= 0:
            laser1_x = 700
        elif laser2_x <= 0:
            laser2_x = 700
        elif laser3_x <= 0:
            laser3_x = 700
        elif laser4_x <= 0:
            laser4_x = 700

#Laser Speed
        laser_x -= laser_speed
        laser1_x -= laser_speed
        laser2_x -= laser_speed
        laser3_x -= laser_speed
        laser4_x -= laser_speed

# Spaceship Collide 
        if spaceship.colliderect(laser):
            current_screen = 2 
        elif spaceship.colliderect(laser1) : 
            current_screen = 2 
        elif spaceship.colliderect(laser2): 
            current_screen = 2 
        elif spaceship.colliderect(laser3):
            current_screen = 2 
        elif spaceship.colliderect(laser4): 
            current_screen = 2

# Space Junk Collide 
        if spaceship.colliderect(aliens):
            current_screen = 2 
        
# Score Adder 
        main_score = scene_title_font.render(f"Score : {score}", True , BLACK)
        score_count = 1
        score += score_count 
        screen.blit(main_score , (20,40))
        
    
        if triangle_y >= 480 or triangle_y <= 0: 
            current_screen = 2
        
    elif current_screen == 2 :
        # End Screen
        screen.fill(WHITE)
        end_title = scene_title_font.render("RETURN TO THE SPACE STATION", True , (BLACK))
        score_screen = scene_title_font.render(f"Your Score Was:{score}",True ,(BLACK))
        triangle_y = 300
        screen.blit(end_title , (40,180))
        screen.blit(score_screen , (200,240))
        
#Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit() 



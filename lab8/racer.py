import pygame 
from pygame.locals import *
import random, time

#Colors
WIDTH = 400
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
score = 0                       #Amount of eaten coins


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

#Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()                #Frequency of updates
pygame.display.set_caption("Racer")        #Name of the Game
road = pygame.image.load('road.jpg')       #Uploading the background


class Player(pygame.sprite.Sprite): #Player
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car1.jpg')        #Uploading the player image
        self.surf = pygame.Surface((40, 60))              #Size of the car
        self.rect = self.surf.get_rect(center=(200, 500)) #Position of the car
        self.speed = 5                                    #Amount of steps

    def move(self):
     
        pressed_keys = pygame.key.get_pressed()           #Moving the car
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
   
    def draw(self):
        
        self.surf.blit(pygame.transform.scale(self.image, (40, 60)), (0, 0))    #Creating the surface, putting the image of the full screen
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pygame.sprite.Sprite): #Enemy cars
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car2.jpg')
        self.surf = pygame.Surface((40, 60))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(2, 4)

    def move(self):                        #Moving the car by Y-axis
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pygame.transform.scale(self.image, (40, 60)), (0, 0))    #Blit the image 
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def killing(self):                    #Checking for desappearance of cars on the screen
        if self.rect.top > HEIGHT:
            self.kill()


class Coin(pygame.sprite.Sprite):   #Coin 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.jpg')   #Loading the image
        self.surf = pygame.Surface((20, 20))         
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))  #Randomly taken pos of coins
        self.speed = random.randint(1, 5)                  #Randomly raken speed
        
    def move(self):                                        #Moving the coin by Y-axis
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pygame.transform.scale(self.image, (20, 20)), (0, 0))   #Blit the image
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def killing(self):                                                       #Disappeare the coin if they are out of the screen
        if self.rect.top > HEIGHT:
            self.kill()


P1 = Player()
enemies = pygame.sprite.Group([Enemy() for _ in range(3)])                  #Amount of randomly appeared cars (Making the group)
coins = pygame.sprite.Group([Coin() for _ in range(5)])                     #Amount of randomlu appeared coins

running = True                   #Running the loop

#Main Loop
while running:
    clock.tick(FPS)                                         #Initial movement of cars
    for event in pygame.event.get():                        #Checking for ending the game
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)                                      #Fill the screen in white color
    screen.blit(pygame.transform.scale(road, (WIDTH, HEIGHT)), (0, 0 % HEIGHT))  #Blit the image by the screen size
    

    P1.draw()                                     #Show the car on the screen (drawing the rect)
    P1.move()                                     #Moving the car
    for enemy in enemies:                         #Looping through the class, initialize the functions
        enemy.draw()
        enemy.move()
        enemy.killing()

    for coin in coins:                           #Looping for the class, initialize the functions
        coin.draw()
        coin.move()
        coin.killing()

    if enemies.__len__() < 3:                    #Adding new cars (checking the size of the group)
        enemies.add(Enemy())

    if coins.__len__() < 5:                       #Adding coins
        coins.add(Coin())

    if pygame.sprite.spritecollide(P1, enemies, False):        #Checking if they matched or not
        if pygame.sprite.spritecollideany(P1, enemies):        #Checking P1 and enemy matched
          screen.fill(RED)                                  
          screen.blit(game_over, (30,250))                     #Set 'Game Over' Label
          pygame.display.update()                              #Updating the changes
          for entity in pygame.sprite.Group():                 #Ending the game
                entity.kill()
          time.sleep(1)           
          running = False
        
    scores = font_small.render(str(score), True, BLACK)        #Setting the font for the score
    screen.blit(scores, (380,10))                              #Setting the core on the screen
    if pygame.sprite.spritecollide(P1, coins, True):           #Adding the scores, if car catches the coin
        score += 1

    pygame.display.update()                                    #Updating the changes
pygame.quit()                                                  #Exit


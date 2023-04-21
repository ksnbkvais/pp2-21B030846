import random
import pygame, time

pygame.init()               #Starting of pygame

#Color
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OLIVE = (128, 128, 0)
BROWN = (150, 75, 0)

screen = pygame.display.set_mode((800, 600))                #Size of the screen
background = pygame.transform.smoothscale(pygame.image.load('2.jpg'), (800, 600))  #Set the background by the screen size
pygame.display.set_caption('SNAKE')

font = pygame.font.SysFont('Arial', 66, bold=True)
game_over = font.render("Game Over!", True, RED)
font1 = pygame.font.SysFont('Verdana', 14)
levele = font1.render("LEVEL = ", True, BLACK)
scoree = font1.render("SCORE = ", True, BLACK)

a=[]

class Snake:
    global level, score             
    def __init__(self, x, y):
        self.size = 1             #Initial size of Snake (head)
        self.elements = [[x, y]]  # [[x0, y0], [x1, y1], [x2, y2] ...] (i) -> (i - 1)    position 
        self.radius = 10         #Snake size
        self.dx = 5              # Starting direction (right direction)
        self.dy = 0
        self.is_add = False      #Condition for eating
        self.speed = 30          #Amount of steps
        if len(a) >= 30:         #Condition for speed increasing
            self.speed +=3

    def draw(self):
        for element in self.elements:       #Creating head of Snake
            pygame.draw.circle(screen, BLACK, element, self.radius)

    def add_to_snake(self):      #Updating Snake size
        self.size += 1          
        self.elements.append([0, 0])  
        self.is_add = False
        if score % 5 == 0:        #Speed insreasing
            self.speed += 10

    def move(self):      
        if self.is_add:                  #If True
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):    #Movement of tale of the snake
            self.elements[i][0] = self.elements[i - 1][0]    #from the end they change their pos
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx           #Direction setup (repeating) Head
        self.elements[0][1] += self.dy

        if self.elements[0][0] > 795 or self.elements[0][0] < 5:   #Game Over Condition (if the snake is out of screen)
                                                                   #By X-axis
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))                     
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            pygame.exit()

        if self.elements[0][1] > 595 or self.elements[0][1] < 5:  #By Y-axis
            
            screen.fill(BLACK)
            screen.blit(game_over, (220, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            pygame.exit()

    def eat(self, foodx, foody):                       #Condition of position equality (snake and food)
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 20 and foody <= y <= foody + 20:
            return True
        return False

class Food:
    def __init__(self):                        #Initialization of Food
        self.x = random.randint(0, 700)        #By X-axis
        self.y = random.randint(0, 500)        #By Y-axis

    def gen(self):                             #Random Appearance of Food
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        
    def draw(self):                            #Creating Food
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 15, 15))
    
 
score = 0               #Counter for amount of food
level = 0               #Counter for level changing

def show_level(x, y):
    global level
    s = font1.render(f'{level}', True, BLACK)         #Creating a Label
    screen.blit(s, (x, y))
    
def show_score(x, y):
    global score
    s = font1.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

snake1 = Snake(100, 100)                #Initial position and assigning of class to a variable
food = Food()

running = True                          #Condtion for running a Main Loop
FPS = 30                                #Frames Per Seconds
s = 5                                   #Amount of steps

clock = pygame.time.Clock()             #Amount of FPS per 1 second

#Main Loop
while running:
    clock.tick(snake1.speed)           #Initial movement of snake (like speed)
    show_score(795, 20)                #Showing the score on the screen at (x,y) position
    for event in pygame.event.get():   #Condition for ending the Loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_ESCAPE:  #If press ESC - end the loop
                running = False

            if event.key == pygame.K_RIGHT and snake1.dx != -s:  #If K_RIGHT and snake doesn't move to the left
                snake1.dx = s                                    #Snake moves to the right
                snake1.dy = 0                                    #No vertical moving 
            if event.key == pygame.K_LEFT and snake1.dx != s:    #Changing of direction using arrows
                snake1.dx = -s
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != s:
                snake1.dx = 0
                snake1.dy = -s
            if event.key == pygame.K_DOWN and snake1.dy != -s:
                snake1.dx = 0
                snake1.dy = s
    
    
    if snake1.eat(food.x, food.y):                               #If the function is called                  
        snake1.is_add = True                                     #Snake eats food
        score += 1                                               #Adding the score
        food.gen()                                               #Generation of food again at another pos
    
        #Changing of level
        if score % 4 == 0:       #If we passed 4 levels     
            level += 1
            a.append(1)          #Speed increasing

    
    snake1.move()                               #Calling the movement
    screen.fill(BLACK)                          
    screen.blit(background, (0, 0))             #Setting background
    snake1.draw()                               #Blitting of snake
    food.draw()                                 #Blitting of food
    

    screen.blit(levele, (700, 0))               #Label for Level
    screen.blit(scoree, (700, 20))              #Label for Score
    show_score(775, 20) 
    show_level(770, 0)
    pygame.display.update()                     #Updating of screen with changings

pygame.quit()                                   #Exit 
import pygame

pygame.init()                                           #starting pygame
screen = pygame.display.set_mode((800, 600))            #creating a screen
screen.fill((255, 255, 255))


def line(screen, start, end, d, color):                 #class of line
    x1 = start[0]                                       #starting point on x
    y1 = start[1]                                       #starting point on y
    x2 = end[0]                                         #ending point on x
    y2 = end[1]                                         #ending point on y

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B                            #formula of equation of line
            pygame.draw.circle(screen, color, (x, y), d)
    else:   
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), d)
        

def rectangle(screen, start, end, d, color):
    x1 = start[0]                                       #starting point on x
    y1 = start[1]                                       #starting point on y
    x2 = end[0]                                         #ending point on x
    y2 = end[1]                                         #ending point on y

    width = abs(x1-x2)                                         #width of rectangle
    height = abs(y1-y2)                                        #height of rectangle

    if x1 <= x2:                                                                #condition that starting point is to the left of the end point
        if y1 < y2:                                                             #condition that starting point is to the left of the end point
            pygame.draw.rect(screen, color, (x1, y1, width, height), d)         #creating rectangle with starting positions x1 and y1
        else:
            pygame.draw.rect(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, width, height), d)
        else:
            pygame.draw.rect(screen, color, (x2, y2, width, height), d)



def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x1, y1, width, height), d)
        else:
            pygame.draw.ellipse(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x2, y1, width, height), d)
        else:
            pygame.draw.ellipse(screen, color, (x2, y2, width, height), d)


last_pos = (0, 0)                                   #a variable that will take the last coordinates of the shapes
w = 2                                               #the width of the shapes
draw_line = False
erase = False
ed = 50                                             #the scale of the erasure
color = (0, 0, 0)                                   #default color black
d = {
    'line' : True,                                  #default figure line
    'rect': False,
    'circle': False,
    'erase': False
}

running = True                                                          #variable for loop operation
while running:                                                          #starting loop
    pos = pygame.mouse.get_pos()                                        #starting position of the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                   #when the screen is closed, the cycle stops
            running = False
        if event.type == pygame.KEYDOWN:                                #reaction to button presses
            if event.key == pygame.K_l:                                 #press l - draw the line
                d['line'] = True                                        #by defautl - is line 
                for k, v in d.items():                                  #looping through the dict
                    if k != 'line':                                     #if not line - another is False
                        d[k] = False
            if event.key == pygame.K_r:                                 #press r - draw rectangle 
                d['rect'] = True
                for k, v in d.items():
                    if k != 'rect':
                        d[k] = False
            if event.key == pygame.K_c:                                 #press c - draw circle
                d['circle'] = True
                for k, v in d.items():
                    if k != 'circle':
                        d[k] = False
            if event.key == pygame.K_e:                                 #press e - eraser
                d['erase'] = True
                for k, v in d.items():
                    if k != 'erase':
                        d[k] = False
            if event.key == pygame.K_z:                                 #press z - set green color
                color = (0, 255, 0)
            if event.key == pygame.K_k:                                 #press k - set red color
                color = (255, 0, 0)
            if event.key == pygame.K_g:                                 #press g - set blue color
                color = (0, 0, 255)

        if d['line'] == 1:                                              #if line = true
            if event.type == pygame.MOUSEBUTTONDOWN:                    #if we press the mouse (click)
                last_pos = pos
                pygame.draw.circle(screen, color, pos, w)               #get the mouse pos 
                draw_line = True                                        
            if event.type == pygame.MOUSEBUTTONUP:                      #if we unpress the mouse - stop line
                draw_line = False
            if event.type == pygame.MOUSEMOTION:                        #movement of the mouse 
                if draw_line:
                    line(screen, last_pos, pos, w, color)               #draw line by the mouse pos 
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:                    #if we press the mouse (click)
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:                      #if we unpress the mouse - draw rectangle
                rectangle(screen, last_pos, pos, w, color)
        elif d['circle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:                    #if we press the mouse (click)
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:                      #if we unpress the mouse- draw circle
                circle(screen, last_pos, pos, w, color)
        elif d['erase'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:                    #if we press the mouse (click)
                (x, y) = pos                                      
                pygame.draw.rect(screen, (255, 255, 255), (x, y, ed, ed))   
                erase = True
            if event.type == pygame.MOUSEMOTION:                        # movement of mouse- erase
                if erase:
                    pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:                      #if we unpress the mouse- stop erase
                erase = False
    pygame.display.update()
pygame.quit()
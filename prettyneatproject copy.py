from turtle import Screen
import pygame
import math
d = 0
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (100, 100, 100)
BROWN = (120, 75, 20)
RED = (255, 0, 0)
DARKBROWN = (99, 58, 16)
DARKBROWN2 = (70, 35, 10)
DARKBROWN3 = (50, 22, 5)
DARKBROWN4 = (32, 10, 3)
DARKBROWN5 = (15, 5, 0)
PURPLE = (70, 0, 255)
# I LEFT OFF ON THE VIDEO TITLED: "Basic PyGame Animation" AT THE 12:29 Timestamp.

pygame.init()


screen_size = 600

surface = pygame.display.set_mode((screen_size, screen_size))

step = 0
stepminute = 0+1
stephour = 0
if stepminute: d = d+1
if d >= 60: d = 1
angle_per_step = .05
line_len = screen_size * .8
cx = cy = screen_size//2
ca = cb = screen_size//2
cm = cn = screen_size//2

while True:
    
    if pygame.event.peek(pygame.QUIT):
        break

    surface.fill((0, 0, 0))

    angle = step * angle_per_step
    x = line_len / 2.0 * math.sin(angle)
    y = line_len / 2.0 * math.cos(angle)

    angle = stepminute * angle_per_step
    a = line_len / 2.0 * math.sin(angle)
    b = line_len / 2.0 * math.cos(angle)

    angle = stephour * angle_per_step
    m = line_len / 2.0 * math.sin(angle)
    n = line_len / 2.0 * math.cos(angle)

    pygame.draw.circle(surface, DARKBROWN5, [300, 300], 320)

    pygame.draw.circle(surface, DARKBROWN4, [300, 300], 310)

    pygame.draw.circle(surface, DARKBROWN3, [300, 300], 300)

    pygame.draw.circle(surface, DARKBROWN2, [300, 300], 290)

    pygame.draw.circle(surface, DARKBROWN, [300, 300], 280)

    pygame.draw.circle(surface, BROWN, [300, 300], 270)

    pygame.draw.circle(surface, DARKBROWN, [300, 300], 260)

    pygame.draw.circle(surface, WHITE, [300, 300], 250)

    pygame.draw.rect(surface, BLACK, [290, 70, 20, 60])

    pygame.draw.rect(surface, BLACK, [290, 470, 20, 60])

    pygame.draw.rect(surface, BLACK, [470, 290, 60, 20])

    pygame.draw.rect(surface, BLACK, [70, 290, 60, 20])
    
    pygame.draw.circle(surface, BLACK, [200, 120], 7)

    pygame.draw.circle(surface, BLACK, [120, 200], 7)

    pygame.draw.circle(surface, BLACK, [400, 120], 7)

    pygame.draw.circle(surface, BLACK, [120, 400], 7)

    pygame.draw.circle(surface, BLACK, [480, 400], 7)

    pygame.draw.circle(surface, BLACK, [400, 480], 7)

    pygame.draw.circle(surface, BLACK, [480, 200], 7)

    pygame.draw.circle(surface, BLACK, [200, 480], 7)

    font = pygame.font.SysFont('Cursive', 50, True, False)

    text = font.render("AUSTIN",True,BLACK)
 
    surface.blit(text, [232, 200])

    text = font.render("CLOCKWORK",True,BLACK)
 
    surface.blit(text, [186, 370])

    text = font.render("9",True,BLACK)
 
    surface.blit(text, [135, 284])

    text = font.render("3",True,BLACK)
 
    surface.blit(text, [444, 284])

    text = font.render("12",True,BLACK)
 
    surface.blit(text, [278, 132])

    text = font.render("6",True,BLACK)
 
    surface.blit(text, [289, 435])

    pygame.draw.line(surface, (255, 100, 0), (300, 300), ((cx+x), (cx-y)), 8)
    #pygame.draw.line(surface, (255, 255, 0), ((cx+x), (cy+y)), ((cx-x), (cx-y)), 8)

    pygame.draw.line(surface, RED, (300, 300), ((ca+a), (ca-b)), 10)

    pygame.draw.line(surface, PURPLE, (300, 300), ((cm+m), (cm-n)), 14)

    pygame.draw.circle(surface, BLACK, [300, 300], 45)

    pygame.draw.circle(surface, DARKGRAY, [300, 300], 37)

    pygame.draw.circle(surface, BLACK, [300, 300], 30)

    pygame.display.update()

    pygame.time.Clock().tick(1)

    step += 2.094
    stepminute += 0.03491666667
    stephour += 0.002909722223

pygame.quit()
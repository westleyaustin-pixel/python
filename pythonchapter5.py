
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (50, 200, 255)
LIGHTBROWN = (181, 101, 29)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (255, 255, 197)
BROWN = (150, 75, 0)
DARKGREEN = (0, 100, 0)
DARKRED = (139, 0 , 0)
GRAY = (100, 100, 100)
PI = 3.14159265359
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("house on the prairie")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHTBLUE)
 #birds
    for x_offset in range(0, 600, 100):
        pygame.draw.arc(screen, BLACK, [300,+x_offset, 40, 20], 0, PI, 2)
        pygame.draw.arc(screen, BLACK, [340,+x_offset, 40, 20], 0, PI, 2)

    # --- Drawing code should go here
    pygame.draw.rect(screen, RED, [55, 200, 150, 150])
    pygame.draw.rect(screen, GREEN, [0, 350, 800, 150])
    pygame.draw.rect(screen, BLACK, [75, 250, 60, 100], 4)
    pygame.draw.rect(screen, LIGHTBLUE, [145, 250, 50, 50])
    pygame.draw.polygon(screen, LIGHTBROWN, [[55, 200], [205, 200], [125, 130]])
    pygame.draw.circle(screen, YELLOW, [550, 100], 70)
    pygame.draw.circle(screen, LIGHTYELLOW, [550, 100], 50)
    pygame.draw.rect(screen, BROWN, [400, 320, 20, 50])
    pygame.draw.polygon(screen, DARKGREEN, [[410, 250], [360, 320], [460, 320]])
    pygame.draw.polygon(screen, DARKGREEN, [[360, 280], [410, 180], [460, 280]])
    pygame.draw.circle(screen, WHITE, [370, 150], 20)
    pygame.draw.circle(screen, WHITE, [360, 160], 20)
    pygame.draw.circle(screen, WHITE, [340, 140], 20)
    pygame.draw.circle(screen, WHITE, [330, 160], 20)
    pygame.draw.circle(screen, WHITE, [200, 100], 20)
    pygame.draw.circle(screen, WHITE, [190, 110], 20)
    pygame.draw.circle(screen, WHITE, [170, 100], 20)
    pygame.draw.circle(screen, WHITE, [160, 120], 20)
    pygame.draw.rect(screen, DARKRED, [500, 340, 50, 50])
    pygame.draw.rect(screen, BLACK, [510, 350, 30, 30])
    pygame.draw.rect(screen, DARKRED, [515, 355, 20, 20])
    pygame.draw.rect(screen, DARKRED, [500, 380, 100, 35])
    pygame.draw.circle(screen, BLACK, [510, 420], 30)
    pygame.draw.circle(screen, BLACK, [580, 420], 30)
    pygame.draw.circle(screen, GRAY, [580, 420], 20)
    pygame.draw.circle(screen, GRAY, [510, 420], 20)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
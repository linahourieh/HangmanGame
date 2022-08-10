'''
ELLAK - May 2017
Stick Figure

'''
 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
ORANGE   = ( 232, 163,  24)
BLUE     = (   0,   0, 255)
    
# Setup
pygame.init()
  
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("ELLAK - May 2017 - Stick Figure")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
##        elif event.type == pygame.KEYDOWN:
##            print("User pressed a key.")
##        elif event.type == pygame.KEYUP:
##            print("User let go of a key.")
##        elif event.type == pygame.MOUSEBUTTONDOWN:
##            print("User pressed a mouse button")
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # Get mouse position
##    pos = pygame.mouse.get_pos()
##    x = pos[0]
##    y = pos[1]
##    print(x,y)

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT    

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
	
	# Create the Stick Figure
    
	# Head
    pygame.draw.circle(screen, BLACK, [100, 100], 15)
    
    # Body
    pygame.draw.line(screen, ORANGE, [100, 115], [100, 180], 5)

 
    # Legs
    pygame.draw.line(screen, BLUE, [100, 180], [80, 250], 5)
    pygame.draw.line(screen, BLUE, [100, 180], [120, 250], 5)
 
    # Arms
    pygame.draw.line(screen, RED, [100, 125], [50, 140], 5)
    pygame.draw.line(screen, RED, [100, 125], [150, 140], 5)
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
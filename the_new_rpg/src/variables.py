import pygame

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
modes = pygame.display.list_modes()
mode = modes[0]
height = mode[1]#displayinfo.current_h - 200
width = height #for not it is a square window
hh = height/2
screen = pygame.Surface([height, width])
wide_screen = pygame.display.set_mode(mode, pygame.FULLSCREEN)
scaleoffset = 1
font = pygame.font.Font(None, 30)

playerspeed = height/800 * 3
healthanimationspeed = 2000#time in milliseconds for the health bar animation to go

#encountering enemies
encounter_check_rate = 100 #rate of check in milliseconds
encounter_chance = 0.0025#chance per check

#state can be world, battle, or conversation
state = "world"

#keybindings
enterkeys = [pygame.K_SPACE, pygame.K_RETURN, pygame.K_KP_ENTER]

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
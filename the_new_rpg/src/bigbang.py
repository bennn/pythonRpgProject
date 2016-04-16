#!/usr/bin/python
import pygame, variables, maps

from Player import Player
from Battle import Battle
import conversations, classvar

pygame.display.set_caption("theNewRpg")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
#pygame.mouse.set_visible(0)

maps.new_scale_offset()

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing- this is like keyPressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_ESCAPE:
                done = True
            if variables.state == "conversation":
                conversations.currentconversation.keypress(event.key)
            elif variables.state == "world":
                classvar.player.keypress(event.key)
                maps.on_key(event.key)
            elif variables.state == "battle":
                classvar.battle.onkey(event.key)


        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            classvar.player.keyrelease(event.key)

    # --- Game Logic
    if variables.state == "world":
        classvar.player.move()
        maps.checkexit()
        maps.current_map.checkenemy()
    elif variables.state == "battle":
        classvar.battle.ontick()

    # --- Drawing Code
    variables.screen.fill(variables.WHITE)
    maps.current_map.draw(classvar.player.xpos, classvar.player.ypos)
    if variables.state == "conversation":
        conversations.currentconversation.draw()
        classvar.player.draw()
    elif variables.state == "world":
        classvar.player.draw()
    elif variables.state == "battle":
        classvar.battle.draw()

    #put the screen on the widescreen
    pygame.draw.rect(variables.wide_screen, variables.BLACK, [0,0, variables.mode[0], variables.mode[1]])
    variables.wide_screen.blit(variables.screen, [int(variables.mode[0]/2-variables.width/2), 0])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit, this is after the main loop has finished
pygame.quit()

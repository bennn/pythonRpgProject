#!/usr/bin/python
import pygame, variables, maps

from Player import Player
from Battle import Battle
import conversations, enemies, classvar

pygame.display.set_caption("theNewRpg")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
#pygame.mouse.set_visible(0)
battle = Battle(enemies.sheep)

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


        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            classvar.player.keyrelease(event.key)

    # --- Game Logic
    classvar.player.move()
    maps.checkexit()

    # --- Drawing Code
    variables.screen.fill(variables.WHITE)
    maps.current_map.draw(classvar.player.xpos, classvar.player.ypos)
    if variables.state == "conversation":
        conversations.currentconversation.draw()
        classvar.player.draw()
    elif variables.state == "world":
        classvar.player.draw()
    else:
        battle.draw()


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit, this is after the main loop has finished
pygame.quit()

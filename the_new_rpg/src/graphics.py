#!/usr/bin/python

import pygame, os, variables

#sscale means smart scale, Oliver works on this
def sscale(img, factor):
    w = img.get_width()
    h = img.get_height()
    endsize = variables.height*factor
    if w > h:
        smaller = h
    else:
        smaller = w
    return pygame.transform.scale(img, [int((w/smaller)*endsize), int((h/smaller)*endsize)])

#Oliver's example- make sure to put .convert() at the end to make it run faster (as a png)
testmapimage = pygame.image.load(os.path.join('pics', 'testmap.jpg')).convert()
testmapimage = sscale(testmapimage, 3)

test_rock = pygame.image.load(os.path.join('pics', 'pokemon_grass.png')).convert()
test_rock = sscale(test_rock, 0.08)
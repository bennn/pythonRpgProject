#!/usr/bin/python
import pygame, variables, graphics
from Map import Map
from Rock import Rock

block = graphics.front_honey.get_width()
testmap1 = Map(graphics.testmapimage, [Rock(graphics.bed, 2*block, 2*block, True),
                                       Rock(graphics.bed, 3*block, 2*block, True),
                                       Rock(graphics.front_honey, 6*block, 2*block, False)])

testmap1.startpoint = [block * 10, block*10]
testmap1.endarea = [block * 50, block * 50, block * 55, block*55]

#Rock(graphics.(whatever picture), x value, y value, Collision Detection)
house1 = Map(graphics.houseInside, [Rock(graphics.welcomeMat, 2.25*block, 5.3*block, False),
                                   Rock(graphics.bed, 0*block, 0*block, False),
                                   Rock(graphics.warddrobe2, 2*block, 0*block, False),
                                   Rock(graphics.tpanda, 4*block, 5*block, True)])
#blank.endpoint (top left x, top left y, bottom right x, bottom right y)
house1.startpoint = [0,0]
house1.endpoint = [block*2,block*4,block*2.5,block*5.5]


houserock = Rock(graphics.house, 0, 0, True)
houserock.h = houserock.h * 3/5

outside1 = Map(graphics.scrub1, [houserock,
                                Rock(graphics.welcomeMat, 0.4*block,3*block, False),
                                Rock(graphics.tree1, 5*block, 3*block, True),
                                Rock(graphics.tree1, 2.1*block, 3*block, True),
                                Rock(graphics.tree3, 2.2*block, 3*block, True),
                                Rock(graphics.tree3, 2.5*block, 3.2*block, True)])

outside1.startpoint = [block *0.85, block*2.9]
outside1.endpoint = [block*50,block*50,block*55,block*55]

current_map = testmap1

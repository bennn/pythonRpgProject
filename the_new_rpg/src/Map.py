#!/usr/bin/python
#Oliver Flatt works on Classes
import variables, pygame, classvar
from random import random
from Battle import Battle

def draw_map(b, t):
    i = b
    for x in range(0, len(t)):
        r = t[x]
        i.blit(r.base, [r.x, r.y])
    return i

class Map():
    startpoint = [10, 10] #xy coordinates of spawn point
    exitareas = []#list of exit
    enemies = []
    lvrange = [1]
    last_encounter_check = 0

    def __init__(self, base, terrain):
        #base is a png
        self.base = base
        #terrain is a list of Rock
        self.terrain= terrain
        self.finalimage = draw_map(base, terrain)

    #x and y are the player's x and y pos
    def draw(self, x, y):
        w = self.finalimage.get_width()
        h = self.finalimage.get_height()
        if x < variables.hh: #if it is in the left side of the map
            drawx = 0 #do not scroll the map at all
        elif x > (w - variables.hh): #if it is on the right side of the map
            drawx = w - variables.height #set it to the maximum scroll
        else:
            drawx = x - variables.hh #otherwise, scroll it by pos (accounting for the initial non-scolling area
        if y < variables.hh: #same but for y pos
            drawy = 0
        elif y > (h - variables.hh):
            drawy = h - variables.height
        else:
            drawy = y - variables.hh

        variables.screen.blit(self.finalimage, [-drawx, -drawy])

        #draw button above exits
        e = self.checkexit()
        pw = classvar.player.normal_width/2
        if not e == False:
            pygame.draw.ellipse(variables.screen,
                                variables.WHITE,
                                [e.area[0] + e.area[2]/2 - pw/2, e.area[1] - pw/2, pw, pw])

    def scale_by_offset(self):
        self.finalimage = pygame.transform.scale(self.finalimage, [int(self.finalimage.get_width()*variables.scaleoffset),
                                                 int(self.finalimage.get_height()*variables.scaleoffset)])

    def checkexit(self):
        currentexit = False
        for x in range(0, len(self.exitareas)):
            e = self.exitareas[x]
            p = classvar.player
            if (p.xpos+p.normal_width) >= e.area[0] and p.xpos<=(e.area[0] + e.area[2]) \
                and (p.ypos + p.normal_height)>=e.area[1] and p.ypos<=(e.area[1] + e.area[3]):
                currentexit = e
                x = len(self.exitareas)
        return currentexit

    def checkenemy(self):
        #goes through the list of enemies, adding up all the encounter chances up until that list number
        def collect_encounter_chances(list_placement):
            chance = 0
            for x in range(0, list_placement+1):
                chance+=self.enemies[x].rarity
            return chance

        #if it is time to check, the player is moving, and we do encounter an enemy
        if (pygame.time.get_ticks() - self.last_encounter_check) >= variables.encounter_check_rate and \
                        classvar.player.ismoving() and random()<variables.encounter_chance:
            currentenemy = False
            random_factor = random()
            for x in range(0, len(self.enemies)):
                e = self.enemies[x]
                #if the random factor is below all of the chances previously to now added up
                if random_factor<collect_encounter_chances(x):
                    currentenemy = e
                    break
            if currentenemy == False:
                currentenemy = self.enemies[len(self.enemies)-1]
            variables.state = "battle"
            classvar.battle = Battle(currentenemy)
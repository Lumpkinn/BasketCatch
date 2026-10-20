import pygame as pg
import os
#TODO: Collision detection!!!! 
class player():
    def __init__(self, screen):
        #Make sure that this is sprite height - window height
        self.position = [0,600]
        #change this either dynamically, of have it set at a static value that feels good to you.
        self.speed = 250
        #sprite size dependant
        self.size = [50,50]
        #create the visual display
        pg.draw.circle(screen, "red", self.position, 40)
        
    def moveL(self, delta):
        self.position[0] -= (self.speed * delta)

    def moveR(self, delta):
        self.position[0] += (self.speed * delta)

    #Theres prolly a pre-bulit function for this you know
    def redraw(self, screen):
        pg.draw.circle(screen, "red", self.position, 40)
        

    def CheckCollision():
        pass
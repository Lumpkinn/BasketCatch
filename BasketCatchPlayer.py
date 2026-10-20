import pygame as pg
import os

class player():
    def __init__(self, screen):
        #change this to be at the bottom of the users screen
        self.position = [0,0]
        #change this either dynamically, of have it set at a static value that feels good to you.
        self.speed = 10
        #sprite size dependant
        self.size = [50,50]
        #create the visual display
        pg.draw.circle(screen, "red", self.position, 40)
        
    
    def moveL(self, delta):
        self.position[0] += self.speed * delta

    def moveR(self, delta):
        self.position[0] += self.speed * delta

    def redraw(self, screen):
        pg.draw.circle(screen, "red", self.position, 40)
        pass

    def CheckCollision():
        pass
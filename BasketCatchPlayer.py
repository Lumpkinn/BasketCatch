import pygame as pg
import os

class player():
    def __init__(self):
        #change this to be at the bottom of the users screen
        self.position = [0,0]
        #change this either dynamically, of have it set at a static value that feels good to you.
        self.speed = 10
        #sprite size dependant
        self.size = [50,50]
    
    def moveL(self):
        self.position[0] += self.speed

    def moveR(self):
        self.position[0] += self.speed
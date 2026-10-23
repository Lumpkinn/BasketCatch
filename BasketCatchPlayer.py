import pygame as pg
import os
#TODO: Collision detection!!!! Look at rect documentation to make this easier, colliderect will make all of the collision stuff a cakewalk (Current issue = Sprite not updating position.)
class player():
    def __init__(self, screen):
        #Make sure that this is sprite height - window height
        self.position = [20,1200]
        #change this either dynamically, of have it set at a static value that feels good to you.
        self.speed = 250
        #sprite size dependant
        self.size = [50,50]
        #creates a circle obj based off of these parameters.
        self.playerCollisionRect = pg.Rect(100, self.position[0], self.size[0], self.size[1])

        #create the visual display
        self.playerIcon = pg.draw.rect(screen,"red",self.size(1), )
        
    def moveL(self, delta):
        print("Moving L", self.position[0], self.position[1])
        self.position[0] -= (self.speed * delta)


    def moveR(self, delta):
        print("Moving r", self.position[0], self.position[1])
        self.position[0] += (self.speed * delta)


    #Theres prolly a pre-bulit function for this you know
    def redraw(self, screen):
        pg.draw.rect(screen, "red", self.playerCollisionRect)
        
    #returns the position of the players collision.
    def CheckCollision(self):
        return self.playerCollisionRect
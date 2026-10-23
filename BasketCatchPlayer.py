import pygame as pg
import os
#TODO: Collision detection!!!! Look at rect documentation to make this easier, colliderect will make all of the collision stuff a cakewalk (Current issue = Sprite not updating position.)

class player():
    def __init__(self, screen):
        #sprite
        self.image = pg.image.load("Assets/Resources/Basket.jpg").convert()

        #Position of the object (x,y)
        self.position = [20,100]

        #change this either dynamically, of have it set at a static value that feels good to you.
        self.speed = 250

        #sprite size dependant
        self.size = [50,50]

        #creates a circle obj based off of these parameters.
        self.playerCollisionRect = pg.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pg.draw.rect(screen, "red", (self.position[0], self.position[1], self.size[0], self.size[1]), self.size[0])
        
    def moveL(self, delta):
        self.position[0] -= (self.speed * delta)


    def moveR(self, delta):
        self.position[0] += (self.speed * delta)


    #Theres prolly a pre-bulit function for this you know
    def redraw(self, screen):
        pg.draw.rect(screen, "red", (self.position[0], self.position[1], self.size[0], self.size[1]), self.size[0])
        
    #returns the position of the players collision.
    def Get_Xpos(self):
        return self.position[0]

import pygame as pg
import os

#TODO: make sure that the sprite resources for the veggies are stored in an array for good ones, and one for bad ones. change the array used depending on if its good or not

#put the path to all the sprites here. Maybe combine the two arrays into a dict?
goodVeggieSprites = []

evilVeggieSprites = []

#use this to randomize the position of the apples

x=1

class Obj():

     def __init__(self, screen):
          #Initial values, feel free to tweak as needed.
          self.position =[x,0]
          self.speed = 20
          self.size = [30,30]
          #this variable is checking if the veggie adds to your score, or if it ends the game.
          self.goodness = True
          #Placeholder for the fruit
          pg.draw.circle(screen, "green", self.position, 20)


     #handles the falling speed. Again, feel free to tweak as needed.
     def fall(self):
          while self.position[1] != 0:
               self.position[1] -= 10

     def redraw(self, screen):
        pg.draw.circle(screen, "red", self.position, 40)

     def evil(self):
          self.goodness = False
          #make sure to also change the sprite!
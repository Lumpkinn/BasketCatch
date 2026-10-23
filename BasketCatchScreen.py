import pygame as pg
import os
import BasketCatchUI as BCI

#TODO: ADD BUTTONS TO TITLE (button code is marked out, consider making it its own class. you might need it l8r)

#TODO: make score indicator (shouldn't be that hard)

class menuScreen():

     def __init__(self, screen, screenHeight, screenWidth):
          self.text = ""
          self.title = ""
          self.size = [480,480]
          screen.fill("purple")
          #button code
          buttonfont = pg.font.SysFont('courier',35)
          buttonText = buttonfont.render('Start', True, (100,100,100))
          #draw the button
          pg.draw.rect(screen, (2,200,50), [screenWidth/2, screenHeight/2, 140, 40])
          #this line is for the text. Make sure that the stuff is aligned properly.
          screen.blit(buttonText, (screenWidth/2+50, screenHeight/2))

     #this should also pass the arguments to it as well.. 
     def AddElement(self, type, text, font, color, xpos, ypos):
          Elements = BCI.GUIElement()
          if type.toUpper() == "BUTTON":
               Elements.createButton(text, font, color, (255,255,255) , xpos, ypos)
          elif type.toUpper() == "LABEL":
               #Double check if method signature works.... i did it kinda halfhazardly
               Elements.createLabel(text, font, color, (255,255,255) , xpos, ypos)

     #recursive call that'll change the screen
     def ChangeScreen():
          pass
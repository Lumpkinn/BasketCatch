import pygame as pg
import os

#make sure to add the buttons

class menuScreen():
     def __init__(self):
          self.text = ""
          self.title = ""
          self.size = [480,480]

     #setter method
     def setText(self, CustomTitle ,CustomMessage):
          self.title = CustomTitle
          self.text = CustomMessage
          
     #add exit button and start button (The most you really have to change between the two things is just the text.)
     def GameStart():
          pass

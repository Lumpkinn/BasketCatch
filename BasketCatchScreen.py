import pygame as pg
import os


#make sure to add the buttons
titleFont = pg.font.Font("Assets/Resources/Pusab-MnqP.otf", 23)



class menuScreen():
     def __init__(self, screen):
          self.text = ""
          self.title = ""
          self.size = [480,480]
          screen.fill("purple")
          self.isStart = False

                             
          
     #setter method
     def setText(self,screen, CustomTitle, CustomMessage):
          self.title = CustomTitle
          self.text = CustomMessage
          Titletext = titleFont.render(CustomMessage, True, "black")
          textbox = Titletext.get_rect()
          screen.blit(Titletext, textbox)
     #add exit button and start button (The most you really have to change between the two things is just the text.)
     def GameStart():
          pass

import pygame as pg
import os

#TODO: ADD BUTTONS TO TITLE (button code is marked out, consider making it its own class. you might need it l8r)

#TODO: Fix path issues, and make sure that the text shows up properly!!! ( look here and at setText() method.)

#TODO: make score indicator (shouldn't be that hard)


#make sure to add the buttons
#titleFont = pg.font.Font(fontpath, 23)


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

                             
          
     #setter method
     def setText(self,screen, CustomTitle, CustomMessage):
          self.title = CustomTitle
          self.text = CustomMessage
#          Titletext = titleFont.render(CustomMessage, True, "black")
 #         textbox = Titletext.get_rect()
  #        screen.blit(Titletext, textbox)
     #add exit button and start button (The most you really have to change between the two things is just the text.)
     def GameStart():
          pass
#class for the buttons (if I need, i can make a settings menu as well)
class selectionButton():
     def __init__(self,x,y,width,height, onclick, singleuse, buttontext):
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.onclick = onclick
          self.singleuse = singleuse
          self.buttontext = buttontext
          
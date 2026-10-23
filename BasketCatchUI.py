import pygame as pg

class GUIElement:
     #TODO: MAKE ALL OF THIS GO TO THE BUTTON CODE
     def __init__(self,x,y,width,height, onclick, singleuse, buttontext):
          self.x = x
          self.y = y
          self.width = width
          self.height = height
          self.onclick = onclick
          self.singleuse = singleuse
          self.buttontext = buttontext
          

     #!!!!!BE AWARE OF HOW PYGAME USES IT'S COORDINATE PLANE, ITS NOT NORMAL!!!!!!
     #button method (buttons size is set, add more parameters if needed)
     def createButton(self, ButtonText, font, color, TxtColor, Xpos, Ypos):
          #make sure to change text color as well
          buttonfont = pg.font.SysFont(font,35)
          buttonText = buttonfont.render(ButtonText, True, TxtColor)
          #draw the button
          pg.draw.rect(self.screen, color, [self.screenWidth/2, self.screenHeight/2, 140, 40])
          #this line is for the text. Make sure that the stuff is aligned properly.
          self.screen.blit(buttonText, (Xpos, Ypos))

     #creates a label for the screen (Size is static, maybe fix in future?)
     def createLabel(self, text, font, color, bgColor, Xpos, Ypos):
          LabelFont = pg.font.Font(font,35)
          Labeltext = LabelFont.render(Labeltext, True, color)
          #drawing label
          #box around label
          pg.draw.rect(self.screen, bgColor, [self.screenWidth/2, self.screenHeight/2, 140, 40])
          #label itself
          self.screen.blit(Labeltext, [Xpos, Ypos, 140, 40])
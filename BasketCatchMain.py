import pygame as pg
import os, random
import BasketCatchPlayer as BCP, BasketCatchVeggie as BCV, BasketCatchScreen as BCS
#make use of this l8r, after the sprites are done. If you need some clarification, chimp pygame project should clarify some stuff. here the line: assetsDirectory = os.path.split()
# I should lowk make a vn for my next project....

#screen things
screen = pg.display.set_mode((1280,720))
screenHeight = screen.get_height()
screenwidth = screen.get_width()

#UI element placement
UICoord = {"Buttons" : [1,2], "Label":[1,2]}
delta = 0
#TODO: collision doesn't exactly work. you also just need to be able to block the player from moving in its specific lane, and nowhere else (you should probably work on having its position printed)
class GameWindow:
     def __init__(self):
          pg.init()
          #prolly just setting the dimensions of the window.
          pg.display.set_caption("BasketCatch")
          clock = pg.time.Clock()
          running = True
          player = BCP.player(screen)
          canMoveL = True
          canMoveR = True
          BorderRect = [pg.Rect(0,0,10,1280), pg.Rect(720,0,10,1280)]
          
          while running:
               isStart = False
               mouse = pg.mouse.get_pos()
               for event in pg.event.get():
                    
                    if event.type == pg.QUIT:
                         running = False
                    
                    #checks where mouse is, and if its over button when clicked, prints stuff
                    #if event.type == pg.MOUSEBUTTONDOWN:
                         #Does this work??
                    #     if UICoord["Buttons"][0] + 50 <= mouse[0]<= ["Buttons"][0] - 50 and UICoord["Buttons"][1]+50 <= mouse[1]<= UICoord["Buttons"][1]-50: 
                    #          pass

               pg.display.flip()
               
               #title screen code
          #    title = BCS.menuScreen(screen, screenwidth, screenHeight)
          #    title.AddElement("LABEL", "BasketCatch", 'Calibri', (100,100,100), 450, 600)

               #ALL OF THE GAME CODE BELOW
               #if isStart == True:
               screen.fill((255,255,255))
               if True:

                    
                    PlayerKey = pg.key.get_pressed()
                    if (PlayerKey[pg.K_a] or PlayerKey[pg.K_LEFT]) and player.Get_Xpos() > 10:
                         player.moveL(delta)
                    if (PlayerKey[pg.K_d] or PlayerKey[pg.K_RIGHT]) and player.Get_Xpos() < 1200:
                         player.moveR(delta)



                    player.redraw(screen)
                    delta = clock.tick(30) / 1000
               pg.display.flip()
               
               #redraw stuff

               


Game = GameWindow()

pg.quit()
import pygame as pg
import os, random
import BasketCatchPlayer as bcp, BasketCatchVeggie as bcv, BasketCatchScreen as bcs

#make use of this l8r, after the sprites are done. If you need some clarification, chimp pygame project should clarify some stuff. here the line: assetsDirectory = os.path.split()


#issue with button detection

#screen things
screen = pg.display.set_mode((1280,720))
#size of screen
screenHeight = screen.get_height()
screenwidth = screen.get_width()

class GameWindow:
     
     delta = 0

     def __init__(self):
          pg.init()
          #prolly just setting the dimensions of the window.
          pg.display.set_caption("BasketCatch")
          clock = pg.time.Clock()
          running = True
          player = bcp.player(screen)
          while running:
               isStart = False
               #apple spawn stuff, you prolly wanna make this better
               spawnchance = random.randint(1,10)
               mouse = pg.mouse.get_pos()
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         running = False
                    if event.type == pg.MOUSEBUTTONDOWN:
                         print(screenwidth/2, screenwidth/2+140,screenHeight/2 ,screenHeight/2+40, mouse[0], mouse[1])
                         if screenwidth/2 <= mouse[0] <= screenwidth/2+140 and screenHeight/2 <= mouse[1] <=screenHeight/2+40:
                              #starts the game.
                              print("hehehehe 4")
                              
                              isStart = True
               pg.display.flip()
               
               #title screen code
               title = bcs.menuScreen(screen, screenwidth, screenHeight)
               title.setText(screen, "BasketCatch", "Basket Catch")
               for i in range (0, spawnchance):
                    obj = bcv.Obj(screen)
                    if spawnchance % 2 == 0:
                         obj.evil()
                    else:
                         pass
                    obj.fall()
                    obj.redraw(screen)
               #ALL OF THE GAME CODE BELOW
               if isStart == True:
                    if True:
                         PlayerKey = pg.key.get_pressed()
                         if PlayerKey[pg.K_a] or PlayerKey[pg.K_LEFT]:
                              player.moveL(delta)
                         if PlayerKey[pg.K_d] or PlayerKey[pg.K_RIGHT]:
                              player.moveR(delta)
                         player.redraw(screen)
                         delta = clock.tick(30) / 1000


Game = GameWindow()

pg.quit()
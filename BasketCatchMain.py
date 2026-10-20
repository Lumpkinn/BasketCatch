import pygame as pg
import os
import BasketCatchPlayer as bcp, BasketCatchVeggie as bcv, BasketCatchScreen as bcs

#use delta for everything movement related
#make use of this l8r, after the sprites are done.
#If you need some clarification, chimp pygame project should clarify some stuff
#assetsDirectory = os.path.split()

screen = pg.display.set_mode((1280,720))


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
          
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         running = False
               pg.display.flip()
               
               #title screen code
               title = bcs.menuScreen(screen)
               title.setText(screen, "BasketCatch", "Basket Catch")
               
               #ALL OF THE GAME CODE BELOW
               #if title.isStart == True:
               if True:
                    PlayerKey = pg.key.get_pressed()
                    if PlayerKey[pg.K_a]:
                         player.moveL(delta)
                    if PlayerKey[pg.K_d]:
                         player.moveR(delta)
                    player.redraw(screen)
                    delta = clock.tick(30) / 1000


Game = GameWindow()

pg.quit()
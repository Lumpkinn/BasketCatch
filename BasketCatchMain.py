import pygame as pg
import os
import BasketCatchPlayer as bcp, BasketCatchVeggie as bcv, BasketCatchScreen as bcs

#use delta for everything movement related

#make use of this l8r, after the sprites are done.
#If you need some clarification, chimp pygame project should clarify some stuff
#assetsDirectory = os.path.split()

class mainWindow:
     delta = 0
     def __init__(self):
          pg.init()
          #prolly just setting the dimensions of the window.
          pg.display.set_caption("BasketCatch")
          global screen
          screen = pg.display.set_mode((1280,720))
          clock = pg.time.Clock()
          global playerLocation
          playerLocation = pg.Vector2(screen.get_width()/2, screen.get_height()/2)
          global veggieLocation
          veggieLocation = pg.Vector2(screen.get_width()/2, screen.get_height()/2)
          running = True
          
          while running:
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         running = False
               screen.fill("white")
               pg.draw.circle(screen, "red", playerLocation, 40)
               #methods for everything else go here
               player = bcp.player()

               PlayerKey = pg.key.get_pressed()
               if PlayerKey[pg.K_a]:
                    player.moveL(delta)

               if PlayerKey[pg.K_d]:
                    player.moveR(delta)

               delta = clock.tick(30) / 1000
          pg.display.flip()

               

     def loadImg():
          imageName = os.path.join()
          pass


Game = mainWindow()

pg.quit()
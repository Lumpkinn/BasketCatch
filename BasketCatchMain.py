import pygame as pg
import os
#all things considered, i should prolly make a little function that lets me make some simple gui elements before i do anything

#use delta for everything movement related

#make use of this l8r, after the sprites are done.
#If you need some clarification, chimp pygame project should clarify some stuff
#assetsDirectory = os.path.split()

running = True

#put the path to all the sprites here. Maybe put this in a dict?
veggieSprites = []

def loadImg():
     imageName = os.path.join()
     pass

class mainWindow:
     delta = 0
     def __init__():
          pg.init()
          #prolly just setting the dimensions of the window.
          screen = pg.display.set_mode((1280,720))
          clock = pg.time.Clock()
          global playerLocation
          playerLocation = pg.Vector2(screen.get_width()/2, screen.get_height()/2)
          global veggieLocation
          veggieLocation = pg.Vector2(screen.get_width()/2, screen.get_height()/2)
          while running:
               for event in pg.event.get():
                    if event.type == pg.QUIT:
                         running = False
               screen.fill("white")

               #methods for everything else go here

               pg.display.flip()

               delta = clock.tick(30) / 1000
     pg.quit()

#class for the players and veggies               
class physObj():
     def Player():
          #??: Do I need to code in collision manuallly?? idrk tbh, ill look into it l8r
          #handles movement (Specifically side to side)
          PlayerKey = pg.key.get_pressed()
          if PlayerKey[pg.k_a]:
               playerLocation.x -= 300
          if PlayerKey[pg.k_d]:
               playerLocation.x += 300

          def Veggies():
               #TODO: Handle veggie spawning
               
               #makes veggies move down
               veggieLocation.y += 100
               

import pygame as pg# type: ignore

#use delta for everything, fall into bad habits



class mainWindow:
     def __init__():
          pg.init()
          #prolly just setting the dimensions of the window.
          screen = pg.display.set_mode((1280,720))
          clock = pg.time.Clock()
          running = True

          while running:
               for event in pg.event.get():
                    if event.type ==pg.QUIT:
                         running = False
               screen.fill("white")

               #methods for everything else go here

               pg.display.flip()

               clock.tick(30)

     def Player():
          PlayerKey = pg.key.get_pressed()
          if PlayerKey[pg.K_w]:
               pass
          if PlayerKey[pg.K_s]:
               pass
          if PlayerKey[pg.k_w]:
               pass
          if PlayerKey[pg.k_w]:
               pass

     def Veggies():
          pass

     #Should I make a class for the menus? 
     pg.quit()
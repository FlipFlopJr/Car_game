import pygame as pg



pg.init()

WIDTH = 500
HEIGHT = 300


screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Car Game')

background = pg.transform.scale(pg.image.load('background.png'),(WIDTH,HEIGHT))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(background, (0,0))


    pg.display.update()
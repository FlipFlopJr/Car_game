import pygame as pg
from pygame.sprite import AbstractGroup



pg.init()

WIDTH = 500
HEIGHT = 300


screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Car Game')

background = pg.transform.scale(pg.image.load('background.png'),(WIDTH,HEIGHT))

class Car(pg.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(filename), (size-20, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))

car = Car(200,250,60,'car2.png')  



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(car.image, car.rect)


    pg.display.update()
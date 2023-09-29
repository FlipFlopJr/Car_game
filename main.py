import pygame as pg
from pygame.sprite import AbstractGroup



pg.init()

WIDTH = 500
HEIGHT = 300
SPEED = 0

clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Car Game')

background = pg.transform.scale(pg.image.load('background.png'),(WIDTH,HEIGHT))


class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))

class Car(pg.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        Sprite.__init__(self,x,y,size,filename)
        self.image = pg.transform.scale(pg.image.load(filename), (size-20, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = SPEED

car = Car(200,250,60,'car2.png')  



running = True
while running:
    if car.rect.left <= 70:
        car.rect.left = 70
    if car.rect.right >= 430:
        car.rect.right = 430

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                car.speed = -4
            elif event.key == pg.K_RIGHT:
                car.speed = 4
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_RIGHT, pg.K_LEFT]:
                car.speed = 0
    
    car.rect.x += car.speed

    screen.blit(background, (0,0))
    screen.blit(car.image, car.rect)


    pg.display.update()
    clock.tick(60)
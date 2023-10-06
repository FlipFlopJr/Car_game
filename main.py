import pygame as pg
from pygame.sprite import AbstractGroup
import random



pg.init()

WIDTH = 500
HEIGHT = 300
SPEED = 0
SCORE = 5 
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Car Game')

background = pg.transform.scale(pg.image.load('background.jpg'),(WIDTH,HEIGHT))


def font():
    font = pg.font.SysFont(None,32)
    text = font.render(f'{SCORE}',True,(0,0,0))
    text_rect = text.get_rect(center = (45,150))
    heart = Sprite(45,110,30,'heart.png')
    screen.blit(text,text_rect)
    screen.blit(heart.image, heart.rect)
class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))

class Car(Sprite):
    def __init__(self, x, y, size, filename):
        Sprite.__init__(self,x,y,size,filename)
        
        self.image = pg.transform.scale(pg.image.load(filename), (size-20, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = SPEED

class Obstacle(Sprite):
    def __init__(self,x,y,weight,height,filename,speed):
        Sprite.__init__(self,x,y,weight,filename)
        x = random.randrange(75, 425)
        self.image = pg.transform.scale(pg.image.load(filename), (weight,height))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(75, 425)
            self.rect.bottom = 0
        self.rect.y+=self.speed
    def score(self):
        global SCORE
        if self.rect.top > HEIGHT:
            SCORE -= 1
        # self.rect.y+=self.speed 
class Line(Sprite):
    def __init__(self,x,y,size,filename,speed):
        Sprite.__init__(self,x,y,size,filename)
        self.image = pg.image.load(filename)
        # self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
    
    def update(self):
        if self.rect.top > 375:
            self.rect.bottom = 0
        self.rect.y+=self.speed

car = Car(200,250,60,'car2.png')  
fuel = Obstacle(100,0,30,30,'fuel.png',4)

obs1 = Obstacle(200,0,50,35,'obs1.png',3)
obs1.image = pg.transform.rotate(obs1.image,90)

lines = pg.sprite.Group()
lines.add(Line(172,25,1,'line.png',2),Line(172,125,1,'line.png',2),Line(172,225,1,'line.png',2),Line(172,325,1,'line.png',2),
          Line(328,25,1,'line.png',2),Line(328,125,1,'line.png',2),Line(328,225,1,'line.png',2), Line(328,325,1,'line.png',2) )

running = True
while SCORE>0:
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
    if pg.sprite.collide_rect(car,fuel):
        SCORE+=1
        fuel.rect.bottom = -20
        fuel.rect.x = random.randrange(75, 425)
    if pg.sprite.collide_rect(car,obs1):
        SCORE = -10
        
    
    car.rect.x += car.speed

    obs1.update()
    fuel.update()
    fuel.score()
    lines.update()

    screen.blit(background, (0,0))

    lines.draw(screen)

    screen.blit(car.image, car.rect)

    screen.blit(obs1.image, obs1.rect)
    screen.blit(fuel.image, fuel.rect)
    font()

    pg.display.update()
    clock.tick(60)
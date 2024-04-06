from pygame import *
from random import randint
#from time import *


finish=False
game=True

win_height=700
win_wight=500
window=display.set_mode((win_height,win_wight))
display.set_caption('Шутер')
galaxy=transform.scale(image.load('galaxy.jpg'),(win_height,win_wight))

clock=time.Clock()
FPS=60


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        # self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT]and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[K_RIGHT]and self.rect.x<win_height-80:
            self.rect.x+=self.speed
 

while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    display.update()
    clock.tick(FPS)

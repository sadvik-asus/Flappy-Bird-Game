import pygame as pg
from random import randint

# creating a class named pipe

class Pipe:
    def __init__(self,scale_factor,move_speed):
        # loading the pipe images 
        self.img_up=pg.transform.scale_by(pg.image.load("Assets/pipeup.png").convert_alpha(),scale_factor)
        self.img_down=pg.transform.scale_by(pg.image.load("Assets/pipedown.png").convert_alpha(),scale_factor)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.pipe_distance=150
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=600
        self.move_speed=move_speed

        # displaying the pipe
    
    def drawPipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)
    
        # upadating the pipe 

    def update(self,dt):
        self.rect_up.x-=int(self.move_speed*dt)
        self.rect_down.x-=int(self.move_speed*dt)

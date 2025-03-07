import pygame as pg

# creating a class named bird

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        # scale factor for size
        super(Bird,self).__init__()
        # loading the bird images
        self.img_list=[pg.transform.scale_by(pg.image.load("Assets/birdup.png").convert_alpha(),scale_factor),
                        pg.transform.scale_by(pg.image.load("Assets/birddown.png").convert_alpha(),scale_factor)]
        # giving a flap sound 
        self.flapSound = pg.mixer.Sound("Assets/sfx/flap.wav")
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=False

    # upadating everything after a flap 

    def update(self,dt):
        if self.update_on:
            self.playAnimation()
            self.applyGravity(dt)

            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

    
    def applyGravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity
    
    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt
    
    def playAnimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0: self.image_index=1
            else: self.image_index=0
            self.anim_counter=0
            
        
        self.anim_counter+=1
        
    # resetting the position after the game is over

    def resetPosition(self):
        self.rect.center=(100,100)
        self.y_velocity = 0
        self.anim_counter = 0

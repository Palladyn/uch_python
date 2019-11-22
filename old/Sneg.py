import pygame
import random
import sys
import time

max_x=1024
max_y=768
max_s=100
size=64

class Snow():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=random.randint(1,3)
        self.img_n=random.randint(1,3)
        self.img_f="i"+str(self.img_n)+".jpg"
        self.img=pygame.image.load(self.img_f).convert()
        self.img=pygame.transform.scale(self.img,(size,size))


    def m_s(self):
        self.y=self.y+self.speed
        if self.y>max_y:
            self.y=(0-size)

        i=random.randint(1,3)
        if i==1:      #right
            self.x=self.x+1
            if self.x>max_x:
                self.x=(0-size)
        elif i==2:   #left
            self.x=self.x-1
            if self.x<(0-size):
                self.x=max_x

    def draw(self):
        screan.blit(self.img, (self.x, self.y))


def int_snow(m_s,snwf):
    for i in range(0,m_s):
        xx=random.randint(0,max_x)
        yy=random.randint(0,max_y)
        snwf.append(Snow(xx,yy))

def ext():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()




#-------------------------------------------MAIN-----------------------------------

pygame.init()
screan=pygame.display.set_mode((max_x,max_y),pygame.FULLSCREEN)
bg_color=(0 ,0 ,0)
snw=[]

int_snow(max_s,snw)

while True:
    screan.fill(bg_color)
    ext()
    for i in snw:
       i.m_s()
       i.draw()
    time.sleep(0.020)
    pygame.display.flip()




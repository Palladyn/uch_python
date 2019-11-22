import pygame

max_x=1024
max_y=768
pygame.init()
s=pygame.display.set_mode((max_x,max_y),pygame.FULLSCREEN)
pygame.display.set_caption("My First Game")

img=pygame.image.load("intel1.jpg").convert()
img=pygame.transform.scale(img,(100,100))


b_c=(0,0,0)

x_s=100
y_s=100
go=False
ml=False
mr=False
mu=False
md=False

while go == False:

    for ev in pygame.event.get():
         if ev.type == pygame.KEYDOWN:
             if ev.key==pygame.K_ESCAPE :
                 go=True
             if ev.key==pygame.K_LEFT:
                 ml=True
             if ev.key == pygame.K_RIGHT:
                 mr=True
             if ev.key == pygame.K_UP:
                 mu=True
             if ev.key == pygame.K_DOWN:
                 md = True
         if ev.type==pygame.KEYUP:
             if ev.key == pygame.K_LEFT:
                 ml = False
             if ev.key == pygame.K_RIGHT:
                 mr = False
             if ev.key == pygame.K_UP:
                 mu = False
             if ev.key == pygame.K_DOWN:
                 md = False
         if ev.type == pygame.MOUSEBUTTONDOWN:
            x_s, y_s = ev.pos
            
    if ml==True:
        x_s-=1
        if x_s<0:
            x_s=0
    if mr==True:
         x_s+=1
         if x_s>max_x-100:
            x_s=max_x-100
    if mu==True:
         y_s-=1
         if y_s<0:
            y_s=0
    if md == True:
        y_s += 1
        if y_s > max_y-100:
                y_s = max_y-100



    s.fill(b_c)
    s.blit(img,(x_s,y_s))
    pygame.display.flip()
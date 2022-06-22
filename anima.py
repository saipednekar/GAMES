from cmath import rect
from codecs import charmap_build
from distutils.fancy_getopt import FancyGetopt
from tkinter import constants
import pygame
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()


import random
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("SAH-SID-RUN!")

pygame.display.update()
font_score=pygame.font.Font("fonts/font.TTF",50)
background= pygame.image.load('im/b.jpg')
background= pygame.transform.scale(background, (800,600))

backi_width=800
b_v=0
b_x=0


volume=2
mixer.music.load("music/Arcade.mp3")
mixer.music.set_volume(volume)
mixer.music.play(-1)





def menu(b_v, b_x ,backi_width):
    menu=False
    character1=False
    character2=True
    i=0

  
    a1= pygame.image.load('im/1.png')
    a2= pygame.image.load('im/2.png')
    a3= pygame.image.load('im/3.png')
    a4= pygame.image.load('im/4.png')
    a5= pygame.image.load('im/5.png')
    a6= pygame.image.load('im/6.png')
    a7= pygame.image.load('im/7.png')
    a8= pygame.image.load('im/8.png')
    a9= pygame.image.load('im/9.png')
    a10= pygame.image.load('im/10.png')
    a11= pygame.image.load('im/11.png')
    a12= pygame.image.load('im/12.png')
    a13= pygame.image.load('im/13.png')
    a14= pygame.image.load('im/14.png')

    b2= pygame.image.load('im/b.png')
    b1= pygame.image.load('im/a.png')
    b3= pygame.image.load('im/c.png')
    b4= pygame.image.load('im/d.png')
    b5= pygame.image.load('im/e.png')
    b6= pygame.image.load('im/f.png')
    b7= pygame.image.load('im/g.png')
    b8= pygame.image.load('im/h.png')
    b9= pygame.image.load('im/i.png')
    b10= pygame.image.load('im/j.png')
    b11= pygame.image.load('im/k.png')
    b12= pygame.image.load('im/l.png')
    b13= pygame.image.load('im/m.png')
    b14= pygame.image.load('im/n.png')

    
    c=0,0,100

    while not menu:
        screen.fill((255, 255, 255))
        screen.blit(background,(0,0))
        mt=font_score.render("PRESS Space to Enter the Game",True,(255,60,60))
        screen.blit(mt,(70,100))
        mt2=font_score.render("chosse characters using arowkeys",True,(255,60,60))
        screen.blit(mt2,(1,200))
        

        li1=[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,a12, a13, a14]

        li2=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]


        a1= pygame.transform.scale(a1, (110,111))
        a2= pygame.transform.scale(a2, (110,111))
        a3= pygame.transform.scale(a3, (110,111))
        a4= pygame.transform.scale(a4, (110,111))
        a5= pygame.transform.scale(a5, (110,111))
        a6= pygame.transform.scale(a6, (110,111))
        a7= pygame.transform.scale(a7, (110,111))
        a8= pygame.transform.scale(a8, (110,111))
        a9= pygame.transform.scale(a9, (110,111))
        a10= pygame.transform.scale(a10, (110,111))
        a11= pygame.transform.scale(a11, (110,111))
        a12= pygame.transform.scale(a12, (110,111))
        a13= pygame.transform.scale(a13, (110,111))
        a14= pygame.transform.scale(a14, (110,111))


        b1= pygame.transform.scale(b1, (110,111))
        b2= pygame.transform.scale(b2, (110,111))
        b3= pygame.transform.scale(b3, (110,111))
        b4= pygame.transform.scale(b4, (110,111))
        b5= pygame.transform.scale(b5, (110,111))
        b6= pygame.transform.scale(b6, (110,111))
        b7= pygame.transform.scale(b7, (110,111))
        b8= pygame.transform.scale(b8, (110,111))
        b9= pygame.transform.scale(b9, (110,111))
        b10= pygame.transform.scale(b10, (110,111))
        b11= pygame.transform.scale(b11, (110,111))
        b12= pygame.transform.scale(b12, (110,111))
        b13= pygame.transform.scale(b13, (110,111))
        b14= pygame.transform.scale(b14, (110,111))

        if i < len(li1):
                    
            screen.blit(li1[i], (200,300))
            
            i+=1
                # print(i)
            
        elif i ==len(li1):

            screen.blit(li1[1], (200,300))
                

            i=0 
        

        if i < len(li2):
                    
            screen.blit(li2[i], (600,300))
            
            i+=1
                # print(i)
            
        elif i ==len(li2):

            screen.blit(li2[1], (600,300))
                

            i=0 
        




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character1=True
                    character2=False
                    pygame.draw.rect(screen, c, [200, 300, 30, 30])


                if event.key == pygame.K_RIGHT:
                    character2=True
                    character1=False
                    pygame.draw.rect(screen, c, [520, 300, 30, 30])


                if event.key == pygame.K_SPACE:
                    gameloop(b_v,b_x,backi_width,character1,character2)  
                    
        
                
        if character1:
                pygame.draw.rect(screen, c, [180, 300, 30, 30])
        if character2:
                pygame.draw.rect(screen, c, [580, 300, 30, 30])

        pygame.display.update() 
        clock.tick(60)


def gameover(s,score,rect_color,b_v,b_x,backi_width,gameo,character1,character2):
    menu=False
    gameo.play()
    while not menu:
        screen.fill((255, 255, 255))
        screen.blit(background,(0,0))
        mt=font_score.render(f"GAME OVER! YourScore{score}",True,(rect_color))
        mt2=font_score.render("HiGHSCORE "+str(s),True,(rect_color))

        screen.blit(mt,(100,240))
        screen.blit(mt2,(200,100))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop(b_v,b_x,backi_width,character1,character2)  
                    

                

        pygame.display.update() 

    pygame.quit()

def gameloop(b_v,b_x,backi_width,character1,character2):
    
    with open('hi.txt') as f:
        s = f.read()

    if character1:
        a1= pygame.image.load('im/1.png')
        a2= pygame.image.load('im/2.png')
        a3= pygame.image.load('im/3.png')
        a4= pygame.image.load('im/4.png')
        a5= pygame.image.load('im/5.png')
        a6= pygame.image.load('im/6.png')
        a7= pygame.image.load('im/7.png')
        a8= pygame.image.load('im/8.png')
        a9= pygame.image.load('im/9.png')
        a10= pygame.image.load('im/10.png')
        a11= pygame.image.load('im/11.png')
        a12= pygame.image.load('im/12.png')
        a13= pygame.image.load('im/13.png')
        a14= pygame.image.load('im/14.png')
    elif character2:
        a1= pygame.image.load('im/a.png')
        a2= pygame.image.load('im/b.png')
        a3= pygame.image.load('im/c.png')
        a4= pygame.image.load('im/d.png')
        a5= pygame.image.load('im/e.png')
        a6= pygame.image.load('im/f.png')
        a7= pygame.image.load('im/g.png')
        a8= pygame.image.load('im/h.png')
        a9= pygame.image.load('im/i.png')
        a10= pygame.image.load('im/j.png')
        a11= pygame.image.load('im/k.png')
        a12= pygame.image.load('im/l.png')
        a13= pygame.image.load('im/m.png')
        a14= pygame.image.load('im/n.png')

    collision=False

    i=0

    velo=0

    space =True

    x=200
    y=400
    # a1= pygame.image.load('i/sidp.png')
    running=True

    rx=750
    
    ry=377
    
    rx2=500
    rx3=200

    rsizex=50
    rsizey=100
    color1=random.randint(0,255)
    color2=random.randint(0,255)
    color3=random.randint(0,255)

    rect_color=color1,color2,color3

    rectv=5
    
    
    score=0

    cn=0
    
    def draw_rect(s,c,x,y,sx,sy):
        # global collision
        # collision=True
        pygame.draw.rect(s, c, [x, y, sx, sy])
        

    def sco(sc):
        scorefon=font_score.render("Score  " +str(sc) +""+" highscore "+str(s),True,(255,10,10))
        screen.blit(scorefon,(10,10))

    reward = pygame.mixer.Sound('music/reward.wav')
    gameo = pygame.mixer.Sound('music/gameover.wav')
    scoo = pygame.mixer.Sound('music/score.wav')

    pygame.mixer.music.set_volume(volume-0.3)
   
    while  running:
            # # print(rx3)
            # if int(rx3) == 300:
            #     print(rx3)
            space =True
            # print(velo) 
            screen.fill((255, 255, 255))
            screen.blit(background,(b_v,0))
            screen.blit(background,(backi_width+b_v,0))
            b_v-=1
            
            if (backi_width+b_v)<0:
                backi_width=800
                b_v=0
                # print("t")
                        



            sco(score)

            draw_rect(screen, rect_color,rx,ry,rsizex,rsizey)

            draw_rect(screen, rect_color,rx2,ry,rsizex,rsizey)
            draw_rect(screen, rect_color,rx3,ry,rsizex,rsizey)



            

            rx-=rectv

            rx2-=rectv

            rx3-=rectv
        
            if rx3<=-700:
                v=random.randint(1500,1600)
                # print(v)
                rx=v

                rx2=rx-350
                rx3=rx2-350

            l=[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,a12, a13, a14]

            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velo+=5 
                        if event.key == pygame.K_LEFT:
                            velo+=-5
                        if event.key == pygame.K_SPACE: 
                        
                                reward.play()

                                screen.blit(l[i<=len(l)], (x,y ))
                                y+=-200
                                space=False  
                                

                    if event.type == pygame.KEYUP: 
                            if event.key == pygame.K_RIGHT:
                                velo = 0  
                            
                            if event.key == pygame.K_LEFT:
                                velo = 0
                        
                            if event.key == pygame.K_SPACE:
                            
                                screen.blit(l[i<=len(l)], (x,400))
                                y=383
                                space=False   
                                if x >= rx3 and x<rx2-200 and y==383:
                                        score+=10
                                elif  x>= rx2 and  x<rx-50 and y==383:
                                        score+=10

                                elif x >= rx+10 and y==383:
                                        score+=10



            a1= pygame.transform.scale(a1, (110,111))
            a2= pygame.transform.scale(a2, (110,111))
            a3= pygame.transform.scale(a3, (110,111))
            a4= pygame.transform.scale(a4, (110,111))
            a5= pygame.transform.scale(a5, (110,111))
            a6= pygame.transform.scale(a6, (110,111))
            a7= pygame.transform.scale(a7, (110,111))
            a8= pygame.transform.scale(a8, (110,111))
            a9= pygame.transform.scale(a9, (110,111))
            a10= pygame.transform.scale(a10, (110,111))
            a11= pygame.transform.scale(a11, (110,111))
            a12= pygame.transform.scale(a12, (110,111))
            a13= pygame.transform.scale(a13, (110,111))
            a14= pygame.transform.scale(a14, (110,111))


        

            if space:    
                if i < len(l):
                    
                    screen.blit(l[i], (x,y))
                    x+=velo
                    # print("x",velo)
                    i+=1
                    # print(i)
                
                elif i ==len(l):

                        screen.blit(l[1], (x,y))
                        x+=velo

                        i=0 
            

            if rx3-30 <= 198 and rx3-30 >= 189 and y==383:
                print(f"c{cn}")
                cn+=1
                collision=True
            elif  rx2-30 <= 198 and rx2-30 >= 189   and y==383:
                print(f"c{cn}")
                cn+=1
                collision=True

            elif  rx-30 <= 198 and rx-30 >= 189 and y==383 :
                print(f"c{cn}")
                cn+=1   
                collision=True
            # print(rectv)    
            if score >=30 and score<=100:
                rectv =6
            elif score >100 and score <=250:

                rectv = 7   
            elif score >250 and score <=500:

                rectv = 8
            elif score >590 and score <=1100:
         
                rectv = 10
            elif score >1100 and score <=2500:

                rectv = 12
            elif score >2500 :

                rectv = 13
            
            if score ==30 or score ==100 or score ==250 or score ==500 or score ==900 or score==1800 or score==2400:
                scoo.play()

            if collision:
                if score > int(s):
                    with open("hi.txt","w") as f:
                        f.write(str(score))
                # restart= True
                b_x=0
                gameover(s,score,rect_color,b_v,b_x,backi_width,gameo,character1,character2)

            # # pygame.draw.rect(screen, (111,223,113), [0, 467, 900, 900])
            pygame.display.update()
            clock.tick(60)
menu(b_v,b_x,backi_width)
gameover()
pygame.quit()

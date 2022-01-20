# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:29:59 2022

@author: EYA
"""
from operator import truediv
from random  import randint
from window import window
import pygame
import sys
fen=window()
background=pygame.image.load(r'C:\Users\EYA\Documents\Ing\FIA1\ParadigmeDeProgrammation\TP\MyPyGame-main\MyPyGame\py Game\images\Sans titre.png')
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)

while True:
    fen.screen.fill((0,0,0))
    fen.screen.blit(background,(0,0))
    for event  in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode    
    pygame.display.update()
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(fen.screen,pygame.Color('black') ,input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
        
    # render at position stated in arguments
    fen.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
        
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()

def count(ch,x):
    if(ch==x):
        return (4,0)
    else:
        nt=0
        nv=0
        for i in x:
            if (i in ch) :
                pos=ch.index(i)
                if(pos==x.index(i)):
                    nt+=1
                else:
                    nv+=1
        return(nt,nv)

""" cs=randint(1000, 9999)
x=str(input("i'm thinking of 4 digit number guess it"))
ch=str(cs)
essai=1
while(essai<6):
        if(count(ch,x)==(4,0)):
           print("you won!") 
           break
        else:
           l=count(ch,x)
           print('{}T,{}V'.format(l[0], l[1]))
           x=str(input("try again "))
           essai+=1 """

        



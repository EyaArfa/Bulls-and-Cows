import pygame
from button import button
pygame.init() #initialize the pygame library

screen=pygame.display.set_mode([500,500])
running=True
button1=button('ouss',(100,100),30,'white','',screen)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    button1.show()
    pygame.display.flip()
pygame.quit()



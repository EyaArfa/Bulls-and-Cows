import pygame
from button import button
from window import window
pygame.init() #initialize the pygame library
fen=window()
running=True
button1=button('ouss',(100,100),30,'green','',fen.screen)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        button1.click(event)
    button1.show()
    pygame.display.flip()
pygame.quit()



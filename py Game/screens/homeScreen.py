import pygame
from button import button
pygame.init() #initialize the pygame library

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('vache&taureau')
Icon = pygame.image.load('C:/Users/medou/Desktop/py Game/images/icon.png')
pygame.display.set_icon(Icon)

running=True
button1=button('ouss',(100,100),30,'green','',screen)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        button1.click(event)
    button1.show()
    pygame.display.flip()
pygame.quit()



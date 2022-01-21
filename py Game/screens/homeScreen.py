import pygame
from button import button
from window import window
pygame.init() #initialize the pygame library

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)

fen=window()
background=pygame.image.load(r'F:\oussema\study\ingenierie\1er\pyGame\MyPyGame\py Game\images\Sans titre.png')
running=True
bt=pygame.image.load(r'F:\oussema\study\ingenierie\1er\pyGame\MyPyGame\py Game\images\button.png')
bt=pygame.transform.scale(bt, (400, 150))
button1=button('play',(220,220),30,bt,'green','',fen.screen)
button2=button('highest scores',(220,260),30,bt,'green','',fen.screen)
button3=button('exit',(220,300),30,bt,'green','',fen.screen)
while running:
    fen.screen.fill((0,0,0))
    fen.screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        button1.click(event)
        button2.click(event)
        button3.clickExit(event)
    button1.show()
    button2.show()
    button3.show()
    button1.changeColor(pygame.mouse.get_pos())
    button2.changeColor(pygame.mouse.get_pos())
    button3.changeColor(pygame.mouse.get_pos())
    pygame.display.update()
    pygame.display.flip()
pygame.quit()



import pygame
from button import Button
from window import window
pygame.init() #initialize the pygame library

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 50)

fen=window()
background=pygame.image.load(r'py Game\images\bulls-and-cows-android.jpg')
running=True
button_surface = pygame.image.load(r'py Game\images\button.png')
button_surface = pygame.transform.scale(button_surface, (100, 50))
button1 = Button(button_surface, 20, 20, "Button",screen,main_font)
while running:
    fen.screen.fill((0,0,0))
    fen.screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # button1.click(event)
    # button1.show()
    # button1.changeColor(pygame.mouse.get_pos())
    pygame.display.update()
    pygame.display.flip()
pygame.quit()



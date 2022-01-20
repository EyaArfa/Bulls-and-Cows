import pygame
pygame.init()
class window:
    def __init__(self) :
        self.screen=pygame.display.set_mode((500,500))
        pygame.display.set_caption('vache&taureau')
        Icon = pygame.image.load(r'C:\Users\EYA\Documents\Ing\FIA1\ParadigmeDeProgrammation\TP\MyPyGame-main\MyPyGame\py Game\images\icon.png')
        pygame.display.set_icon(Icon)
    
        

    
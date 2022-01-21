import pygame
pygame.init()

class button:
    def __init__(self, text, pos, font, image,bg="black", feedback="",screen=pygame.display.set_mode((500, 600))):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        self.image=image
        self.rect=self.image.get_rect(center=(self.x,self.y))
        if feedback == "":
            self.feedback = text
        else:
            self.feedback = feedback
        self.change_text(text, bg)
        self.screen=screen
        
        

    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
    def clickExit(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    pygame.quit()

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.change_text(self.feedback,'yellow')
        else:
            self.change_text(self.feedback,'green')
	        
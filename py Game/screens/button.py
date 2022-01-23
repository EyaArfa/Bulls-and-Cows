from turtle import home
import pygame
from game import play
from tkinter import *
from tkinter import ttk
from about import about
from highScore import high
import var
from levels import *
pygame.init()
music=True

class button:
    def __init__(self, pos, font, image,screen=pygame.display.set_mode((500, 600))):
        self.x, self.y = pos
        self.image=image
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.screen=screen
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
    

        
        

    # def change_text(self, text, bg="black"):
    #     self.text = self.font.render(text, 1, pygame.Color("White"))
    #     self.size = self.text.get_size()
    #     self.surface = pygame.Surface(self.size)
    #     self.surface.blit(self.text, (0, 0))
    #     self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def music(self, event,bol,width,height):
        global music
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if(bol):
                        pygame.mixer.music.pause()
                        music=False
                        var.bol=False
                        b=pygame.draw.line(self.screen,'white',(width-100,height-(height//5)-90),(width+60,height-(height//5)+20),10)
                    else:
                        pygame.mixer.music.unpause()
                        var.bol=True
                        b=pygame.draw.line(self.screen,'green',(width-100,height-(height//5)-90),(width+60,height-(height//5)+20),10)

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    levels(music)
    def clickHigh(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    high()
    def clickExit(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    pygame.quit()
    def about(self,event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    about()



    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.change_text(self.feedback,'yellow')
        else:
            self.change_text(self.feedback,'green')
    
        
	        
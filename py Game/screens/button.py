from turtle import Screen
import pygame
pygame.init()

class Button():
	def __init__(self, image, x_pos, y_pos, text_input,screen,main_font):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.screen = screen
		self.main_font = main_font
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        

	def update(self):
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.main_font.render(self.text_input, True, "green")
		else:
			self.text = self.main_font.render(self.text_input, True, "white")

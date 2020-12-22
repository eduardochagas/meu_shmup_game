import pygame
import random
from constantes import *


class Power(pygame.sprite.Sprite):

	def __init__(self, rectCenter):
		pygame.sprite.Sprite.__init__(self)
		self.type = random.choice(['blood', 'gun']) # escolhe aleatóriamente um nome
		self.image = powers[self.type] # atribui o nome em self.type como a chave do dicionário: powers
		self.rect = self.image.get_rect()
		self.rect.center = rectCenter


	def update(self):

		self.rect.centerx -= 5



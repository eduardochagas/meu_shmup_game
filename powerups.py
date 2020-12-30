import pygame
import random
from constants import *


class Powerups(pygame.sprite.Sprite):

	def __init__(self, rectCenter):
		pygame.sprite.Sprite.__init__(self)
		self.type = random.choice(['blood', 'gun']) # escolhe aleatóriamente um nome
		self.image = powers[self.type] # atribui o nome em self.type como a chave do dicionário: powers
		self.rect = self.image.get_rect()
		self.rect.center = rectCenter


	def update(self):

		self.rect.centerx -= 4


	def update(self):

		self.rect.centerx -= 4




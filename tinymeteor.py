import pygame
from constants import *
import random
import math

class Tinymeteor(pygame.sprite.Sprite):

	def __init__(self, rectCenter, x1, y1, x2, y2):
		pygame.sprite.Sprite.__init__(self)
		self.image = random.choice(array_tiny_meteors)
		self.rect = self.image.get_rect()
		self.vec = pygame.math.Vector2(random.randrange(x1, y1), random.randrange(x2, y2))		# self.rect.x = self.vec[0]
		# self.rect.y = self.vec[1]
		self.rect.center = rectCenter
		# self.angle = random.randrange(-10, -5)

	


	def update(self):

		# self.vec = 
		self.rect.x += self.vec[0]
		self.rect.y -= self.vec[1]

		if self.rect.top < HEIGHT_PANEL_PLAYER or self.rect.bottom > (HEIGHT_PANEL_PLAYER+HEIGHT):
			self.kill()



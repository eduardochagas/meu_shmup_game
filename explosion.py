import pygame
from constants import *


class Explosion(pygame.sprite.Sprite):

	def __init__(self, rectCenter, sizeExplosion):
		pygame.sprite.Sprite.__init__(self)
		self.frame = 0
		self.sizeExplosion = sizeExplosion
		self.image = explosions[self.sizeExplosion][self.frame]
		self.rect = self.image.get_rect()
		self.rect.center = rectCenter
		self.last_update = pygame.time.get_ticks()
		sound_explosion_tiny.play()


	def update(self):		

		####################################################
		# Faz o controle da troca de imagens de explosão
		# de forma suave...
		now = pygame.time.get_ticks()
		if now - self.last_update > 60:
			self.last_update = now
			self.frame += 1
			self.image = explosions[self.sizeExplosion][self.frame]
			if self.frame == len(explosions[self.sizeExplosion])-1:
				self.kill()






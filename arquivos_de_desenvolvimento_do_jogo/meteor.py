import pygame
from constants import *
import random


class Meteor(pygame.sprite.Sprite):

	def __init__(self, arrayMeteor, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image_orig = random.choice(arrayMeteor) # escolhe aleatóriamente uma imagem no array
		self.image = self.image_orig.copy()
		self.rect = self.image.get_rect()
		self.vec = pygame.math.Vector2(x, y)
		self.rect.x = self.vec[0]
		self.rect.y = self.vec[1]
		self.radius = int(self.rect.width / 4) 
		self.velocity = random.randrange(2, 4)
		self.last_update = pygame.time.get_ticks()
		#############################################
		# as duas variáveis que usamos para configurar
		# a velocidade de rotação dos meteóros 
		#
		self.rot = 0
		self.rot_speed = random.randrange(-8, 8)



	def update(self):

		self.rect.x -= self.velocity

		now = pygame.time.get_ticks()
		if now - self.last_update > 50:
			self.last_update = now
			########################################################
			# primeiro, quardamos o centro da imagem de: self.image
			# em uma variável (nesse caso, a variável: old_center)....
			old_center = self.rect.center
			##############################################
			# essas linha abaixo é a formula usada 
			# para fazer os meteóros  rotacionarem
			#
			self.rot = (self.rot + self.rot_speed) % 360
			###############################################
			# rotacionamos a imagem original...
			#
			img_rotate = pygame.transform.rotate(self.image_orig, self.rot)
			###########################################
			# aqui, atribuimos a imagem rotacionada em: self.image dessa classe,
			#
			self.image = img_rotate
			#######################################
			#
			# criamos uma área retângular para a imagem rotacionada com o método get_rect()
			self.rect = self.image.get_rect()
			# e definimos o antigo centro de self.image (que é o valor de: old_center), e 
			# atribuimos ao centro da imagem rotacionada ( que é a imagem em: self.image.orig )
			#
			self.rect.center = old_center

			if self.rect.x < -300:
				self.kill()

			##################################################################
			# usado para gerar o pixel perfect, mas como a imagem é pequena,
			#  mal dá pra ver a colisão perfeita
			#
			self.mask = pygame.mask.from_surface(self.image)






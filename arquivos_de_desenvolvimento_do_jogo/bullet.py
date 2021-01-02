import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):

	def __init__(self, imgBullet, width, height, RectMid, velocity, LeftOrRight='right'):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((width, height))
		# self.image.fill(YELLOW)
		self.image = imgBullet
		self.rect = self.image.get_rect()
		self.LeftOrRight = LeftOrRight

		#####################################################
		# se o parametro LeftOrRight receber o valor: 'right',
		# o lado esquerdo da bala recebe o centro do lado direito 
		# do character (que pode ser o player ou o inimigo)
		if self.LeftOrRight == 'right':
			self.rect.midleft = RectMid

		#####################################################
		# se o parametro LeftOrRight receber o valor: 'left',
		# o lado esquerdo da bala recebe o centro do lado esquerdo 
		# do character (que pode ser o player ou o inimigo)
		if self.LeftOrRight == 'left':
			self.rect.midright = RectMid

		#######################################
		# define a velocidade da bala do player
		# e do inimigo
		#
		self.velocity = 10 


	def update(self):

		if self.LeftOrRight == 'right':
			self.rect.x += self.velocity
			#########################################################################
			# se a bala percorrer UMA DISTÂNCIA MAIOR que a largura da tela (WIDTH),
			# a bala é removida da tela
			#
			if self.rect.left > WIDTH:
				self.kill()


		if self.LeftOrRight == 'left':
			self.rect.x -= self.velocity
			
			########################################################
			# se a bala percorrer UMA DISTÂNCIA MENOR que 0,
			# a bala é removida da tela
			#
			if self.rect.left < 0:
				self.kill()



		##################################################################
		# usado para gerar o pixel perfect, mas como a imagem é pequena,
		#  mal dá pra ver a colisão perfeita
		#
		self.mask = pygame.mask.from_surface(self.image)

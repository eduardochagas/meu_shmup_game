import pygame
from constants import *
from bullet import Bullet

class EnemyShip(pygame.sprite.Sprite):

	def __init__(self, imgBullet, img, width, height, posX, posY, velocity, group_All_Sprites, group_Bullet):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((width, height))
		# self.image.fill(BLUE)
		self.image = img
		self.rect = self.image.get_rect()
		self.vec = pygame.math.Vector2(posX,posY)
		self.rect.x = self.vec.x
		self.rect.y = self.vec.y
		self.velocity = velocity
		self.group_all_sprites = group_All_Sprites
		self.group_bullet = group_Bullet
		self.last_update = pygame.time.get_ticks()
		self.imgBullet = imgBullet



	def update(self):


		self.rect.x -= self.velocity

		now = pygame.time.get_ticks()
		if now - self.last_update > 1050:
			self.last_update = now
			self.shoot()

		if self.rect.right < -300:
			self.kill()


		##################################################################
		# usado para gerar o pixel perfect, mas como a imagem é pequena,
		#  mal dá pra ver a colisão perfeita
		#
		self.mask = pygame.mask.from_surface(self.image)

	def shoot(self):


		bullet = Bullet(self.imgBullet, 10, 5, self.rect.midleft, 10, 'left')
		self.group_all_sprites.add(bullet)
		self.group_bullet.add(bullet)



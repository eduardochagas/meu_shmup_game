import pygame
from constantes import *
from bullet import Bullet
from ship import Ship

class EnemyShip(Ship):

	def __init__(self, width, height, posX, posY, velocity, group_All_Sprites, group_Bullet):
		Ship.__init__(self, width, height, posX, posY, velocity, group_All_Sprites, group_Bullet)



	def update(self):

		self.rect.x -= self.velocity

		now = pygame.time.get_ticks()
		if now - self.last_update > 1050:
			self.last_update = now 
			self.shoot()

		if self.rect.right < -500:
			self.kill()


	def shoot(self):

		bullet = Bullet(10, 5, self.rect.midleft, 10, 'left')
		self.group_all_sprites.add(bullet)
		self.group_bullet.add(bullet)



import pygame
from constantes import *
from ship import Ship
from bullet import Bullet

class PlayerShip(Ship):

	def __init__(self, width, height, posX, posY, velocity, group_All_Sprites, group_Bullet):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((width, height))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.vec = pygame.math.Vector2(posX,posY)
		self.rect.x = self.vec.x
		self.rect.y = self.vec.y
		self.velocity = velocity
		self.group_all_sprites = group_All_Sprites
		self.group_bullet = group_Bullet
		self.last_update = pygame.time.get_ticks()
		self.score = 0


	def update(self):

		# são os controles de movimento do player
		self.control()

		# verifica as colisões das laterais da tela com o player
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > HEIGHT:
			self.rect.bottom = HEIGHT
		

	def control(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			self.rect.y -= self.velocity

		if keys[pygame.K_s]:
			self.rect.y += self.velocity

		if keys[pygame.K_a]:
			self.rect.x -= self.velocity

		if keys[pygame.K_d]:
			self.rect.x += self.velocity

		if keys[pygame.K_SPACE]:
			now = pygame.time.get_ticks()
			if now - self.last_update > 150:
				self.last_update = now 
				self.shoot()


	def shoot(self):
		bullet = Bullet(10, 5, self.rect.midright, 10, 'right')
		self.group_all_sprites.add(bullet)
		self.group_bullet.add(bullet)



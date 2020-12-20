import pygame
from constantes import *
from bullet import Bullet



class PlayerShip(pygame.sprite.Sprite):

	def __init__(self, imgBullet, width, height, posX, posY, velocity, group_All_Sprites, group_Bullet):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((width, height))
		# self.image.fill(BLUE)
		self.image = img_player1
		self.rect = self.image.get_rect()
		self.vec = pygame.math.Vector2(posX,posY)
		self.rect.x = self.vec.x
		self.rect.y = self.vec.y
		self.velocity = velocity
		self.group_all_sprites = group_All_Sprites
		self.group_bullet = group_Bullet
		self.last_update = pygame.time.get_ticks()
		self.score = 0
		self.blood = 100
		self.lives = 4
		self.imgBullet = imgBullet
		self.hidden = False
		self.hidde_timer = 0
		self.__distance_hidden_axis_x = 10000 



	def update(self):

		if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
			self.hidden = False
			self.rect.x = self.vec.x
			self.rect.y = self.vec.y 

		# são os controles de movimento do player
		self.control()

		# verifica as colisões das laterais da tela com o player
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < HEIGHT_PANEL_PLAYER:
			self.rect.top = HEIGHT_PANEL_PLAYER
		if self.rect.bottom > HEIGHT_SCREEN:
			self.rect.bottom = HEIGHT_SCREEN


		##################################################################
		# usado para gerar o pixel perfect, mas como a imagem é pequena,
		#  mal dá pra ver a colisão perfeita
		#
		self.mask = pygame.mask.from_surface(self.image)


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
			if now - self.last_update > 400:
				self.last_update = now 
				self.shoot()


	def shoot(self):
		bullet = Bullet(self.imgBullet, 10, 5, self.rect.midright, 10, 'right')
		self.group_all_sprites.add(bullet)
		self.group_bullet.add(bullet)


	def hide(self):
		self.hidden = True
		self.hide_timer = pygame.time.get_ticks()
		self.rect.center = (self.__distance_hidden_axis_x, HEIGHT)

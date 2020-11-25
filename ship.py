import pygame
from constantes import *
from bullet import Bullet

class Ship(pygame.sprite.Sprite):

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
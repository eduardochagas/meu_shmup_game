import pygame
import random
from constantes import *
from playership import PlayerShip
from enemyship import EnemyShip
from meteor import Meteor
from tinymeteor import Tinymeteor




class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT_SCREEN))
		pygame.display.set_caption(TITULO_DO_JOGO)
		self.clock = pygame.time.Clock()
		self.score = 0

		self.all_sprites = pygame.sprite.Group()
		self.bullet_player1 = pygame.sprite.Group()

		self.player1 = PlayerShip(imgBullet=img_laser_player1, width=30, height=40, posX=20, posY=int(HEIGHT)/2, velocity=5, group_All_Sprites=self.all_sprites, group_Bullet=self.bullet_player1)
		self.all_sprites.add(self.player1)

		#####################################################################
		# cria os grupos dos primeiros inimigos
		# cria o grupo que armazena as balas dos inimigos do primeiro grupo
		#
		self.group_enemy1 = pygame.sprite.Group()
		self.bullet_enemy1 = pygame.sprite.Group() 
		#
		# cria a primeira onda inimiga 1
		self.createEnemies(imgBullet=dict_lasers['lasers_blue'][0] ,img=dict_enemies['blue'][0], listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy1, groupEnemy=self.group_enemy1)

		#self.meteor = Meteor(WIDTH, HEIGHT/2)
		#self.all_sprites.add(self.meteor)

		# self.wave_meteor = False
		self.wave1_meteor = pygame.sprite.Group()


		


		# controla as ondas de ataque
		self.num_waves = 1
		self.running = True
		self.loop()

	
	def loop(self):

		while self.running:

			########################################
			# limpa a tela do jogo a cada frame
			self.screen.fill(BLACK)
			#########################################################################
			# desenha o fundo do painel do player que fica na parte superior da tela
			self.createPanelPlayer(self.screen)
			##################################################################
			# desenha o nome do jogador na tela do jogo junto com o sangue do jogador
			self.textNamePlayer(self.screen, 10, 10, 'Player1', 20, YELLOW, self.player1.blood)

			self.showNumWave(self.screen, WIDTH/2, 30, 'Wave: '+str(self.num_waves), 20, YELLOW)

			# fecha a tela do jogo
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			#################################################################################
			# desenha todas as sprites na tela do jogo
			self.all_sprites.draw(self.screen)

			#################################################################################
			# chama todos os métodos update() de cada objeto do grupo self.all_sprites
			self.all_sprites.update()


			if self.num_waves == 1:
				#################################################################################
				# chaca a colisão do player1 com OS INIMIGOS da primeira onda inimiga do jogo
				# OBS: se qualquer um dos inimigos acertar o player, e o parâmetro boleano  
				# for igual a True, o inimigo que colidiu com o player é removido da tela
				# OBS2: o valor que a variável hit recebe é o objeto inimigo (no caso desse jogo,
				# o objeto inimigo é o meteoro)
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.group_enemy1, False)
				if hit_enemy:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy1, True)
				if hit_enemy:
					self.player1.blood -= random.randrange(5, 10)
					if self.player1.blood <= 0:
						self.player1.blood = 0
						print('jogo perdido !!!!')

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy1, True, True)
				if hit_enemy:
					self.player1.score += 1

				#################################################################################
				# se não houver mais inimigos no grupo da primeira onda inimiga...
				if len(self.group_enemy1) == 0:
					self.num_waves = 2 # muda para a segunda onda inimiga
					self.group_enemy2 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy2 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################
					# cria os meteoros na tela do jogo
					self.createMeteors(3, self.wave1_meteor, self.all_sprites)
					####################################################
					# cria a segunda onda inimiga: wave2
					self.createEnemies(imgBullet=dict_lasers['lasers_blue'][1],img=dict_enemies['red'][0], listWave=wave2, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy2, groupEnemy=self.group_enemy2)
					####################################################
					# cria os meteoros na tela do jogo
					self.createMeteors(5, self.wave1_meteor, self.all_sprites)

			#################################################################################
			# se a onda inimiga for a segunda onda...			
			if self.num_waves == 2:

				#################################################################################
				# chaca a colisão do player1 com OS METEOROS da segunda onda inimiga do jogo
				hit = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True)
				for hit_enemy in hit:
					# print(hit_enemy.radius)
					self.player1.blood -= hit_enemy.radius 

				#################################################################3
				# colisão das balas do player1 com os meteoros...
				hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
				for hit_meteor in hit:
					########################################################
					# cria os meteoros minusculos a partir do momento que 
					# atiramos no meteoro grande.
					# os valores: (5, 7, -5, 5) e (5, 7, 5, 6) são referentes a 
					# posição em que os meteóros minúsculos percorrerão na tela 
					# quando atingimos o meteoro grande...
					tinymeteor1 = Tinymeteor(hit_meteor.rect.center, 5, 7, -5, 5)
					tinymeteor2 = Tinymeteor(hit_meteor.rect.center, 5, 7, 5, 6)
					################################################################
					# adicinamos os meteoros pequenos no grupo self.all_sprites
					#
					self.all_sprites.add(tinymeteor1)
					self.all_sprites.add(tinymeteor2)
					


				#################################################################################
				# chaca a colisão do player1 com OS INIMIGOS da primeira onda inimiga do jogo
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.group_enemy2, False)
				if hit_enemy:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy2, True)
				if hit_enemy:
					self.player1.blood -= random.randrange(5, 10)
					if self.player1.blood <= 0:
						self.player1.blood = 0
						print('jogo perdido !!!!')

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy2, True, True)
				if hit_enemy:
					self.player1.score += 1


				if len(self.group_enemy2) == 0:
					self.num_waves = 3
					self.group_enemy3 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy3 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					# cria a terceira onda inimiga: wave3
					self.createEnemies(imgBullet=dict_lasers['lasers_blue'][4], img=dict_enemies['blue'][3], listWave=wave3, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy3, groupEnemy=self.group_enemy3)


			if self.num_waves == 3:

				#################################################################################
				# chaca a colisão do player1 com OS METEOROS da segunda onda inimiga do jogo
				hit = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True)
				for hit_enemy in hit:
					# print(hit_enemy.radius)
					self.player1.blood -= hit_enemy.radius 

				#################################################################3
				# colisão das balas do player1 com os meteoros...
				hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
				for hit_meteor in hit:
					########################################################
					# cria os meteoros minusculos a partir do momento que 
					# atiramos no meteoro grande.
					# os valores: (5, 7, -5, 5) e (5, 7, 5, 6) são referentes a 
					# posição em que os meteóros minúsculos percorrerão na tela 
					# quando atingimos o meteoro grande...
					tinymeteor1 = Tinymeteor(hit_meteor.rect.center, 5, 7, -5, 5)
					tinymeteor2 = Tinymeteor(hit_meteor.rect.center, 5, 7, 5, 6)
					################################################################
					# adicinamos os meteoros pequenos no grupo self.all_sprites
					#
					self.all_sprites.add(tinymeteor1)
					self.all_sprites.add(tinymeteor2)



				#################################################################################
				# chaca a colisão do player1 com OS INIMIGOS da primeira onda inimiga do jogo
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.group_enemy3, False)
				if hit_enemy:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy3, True)
				if hit_enemy:
					self.player1.blood -= random.randrange(5, 10)
					if self.player1.blood <= 0:
						self.player1.blood = 0
						print('jogo perdido !!!!')

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy3, True, True)
				if hit_enemy:
					self.player1.score += 1

				##################################3
				# implementando aqui.......
				#
				if len(self.group_enemy3) == 0:
					self.num_waves = 4
					self.group_enemy4 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy4 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					# cria a terceira onda inimiga: wave3
					self.createEnemies(imgBullet=dict_lasers['lasers_blue'][0], img=dict_enemies['red'][1], listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)


			if self.num_waves == 4:

				#################################################################################
				# chaca a colisão do player1 com OS INIMIGOS da primeira onda inimiga do jogo
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.group_enemy4, False)
				if hit_enemy:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy4, True)
				if hit_enemy:
					self.player1.blood -= random.randrange(5, 10)
					if self.player1.blood <= 0:
						self.player1.blood = 0
						print('jogo perdido !!!!')

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy4, True, True)
				if hit_enemy:
					self.player1.score += 1




			#################################################################################
			# define os frames do jogo
			self.clock.tick(FPS)

			#################################################################################
			# atualiza a tela do jogo
			pygame.display.update()


	def createEnemies(self, imgBullet, img, listWave, groupAll_sprites, groupBullet, groupEnemy):

		for lista in listWave:
			for item in range(len(lista)):
				print(item)
				e = EnemyShip(imgBullet, img, lista[0], lista[1], lista[2], lista[3], lista[4], groupAll_sprites, groupBullet)
				groupEnemy.add(e) # adiciona o inimigo ao grupo de inimigo correspondente
				groupAll_sprites.add(e) # adiciona o inimigo ao grupo que contêm todos os objetos do jogo


	def createPanelPlayer(self, screen):
		surf = pygame.Surface((WIDTH, HEIGHT_PANEL_PLAYER))
		surf.fill(GREY_DARK)
		screen.blit(surf, (0, 0))


	#############################################################
	# cria o nome do jogador na tela do jogo
	def textNamePlayer(self, screen, posX, posY, text, sizeText, color, bloodPlayer):
		font_default = pygame.font.get_default_font()
		font = pygame.font.Font(font_default, sizeText)
		font_render = font.render(text, False, color)
		rect = font_render.get_rect()
		screen.blit(font_render, (posX, posY))

		##########################################
		# ao desenhamos o sangue do jogador
		self.DrawBloodPlayer(screen, posX, rect.height+15, bloodPlayer)


	#############################################################
	# cria o sangue do jogador na tela do jogo...
	def DrawBloodPlayer(self, screen, posX, posY, percentBlood):
		WIDTH_BLOOD_BAR = 100
		HEIGHT_BLOOD_BAR = 10
		fill = (WIDTH_BLOOD_BAR * percentBlood) / 100
		pygame.draw.rect(screen, GREEN, pygame.Rect(posX, posY, fill, HEIGHT_BLOOD_BAR))
		pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(posX, posY, WIDTH_BLOOD_BAR, HEIGHT_BLOOD_BAR), 2)

		GAP_BETWEEN_BLOOD_AND_SCORE = 5

		self.DrawScore(self.screen, posX, posY+HEIGHT_BLOOD_BAR+GAP_BETWEEN_BLOOD_AND_SCORE, 'score:'+str(self.player1.score), 20, BLUE_TURKEY)


	def DrawScore(self, screen, posX, posY, text, sizeText, color):
		font_default = pygame.font.get_default_font()
		font = pygame.font.Font(font_default, sizeText)
		font_render = font.render(text, False, color)
		rect = font_render.get_rect()
		screen.blit(font_render, (posX, posY))

		# ##############################################
		# # temporário.....
		array_img = []

		for i in range(self.player1.lives): # pelo valor de self.player1.lives....
			# array_img.append(pygame.Surface((30, 30))) # adiciona as representaçoes das imagens da vida do player1
			array_img.append(img_life_player_mini)

		self.DrawImageLifes(screen, posX, posY+25, array_img) # desenha essas representações da imagem de vida do player1 na tela

	#############################################################
	# método temporário...
	def DrawImageLifes(self, screen, posX, posY, listImages):
		i = 0
		gap_between_images = 10
		for img in listImages:
			# img.fill(RED)
			img_rect = img.get_rect()
			##########################################
			# na primeira passada do loop for, i vale 0, então
			# 40 * 0 dá zero, já a variável posX vale 10, por isso 
			# img_rect.x vale 10 na primeira passada do loop for
			# img_rect.x = posX + 10 * i # essa linha é como tá no video do Kids_can_Code...
			img_rect.x = posX + ((gap_between_images + img_rect.width) * i) # essa linha define as imagens com o espaço entre elas.
			screen.blit(img, (img_rect.x, posY))
			i += 1
		i = 0

		if self.player1.blood <= 0:
			self.player1.lives -= 1
			self.player1.blood = 100

	def createMeteors(self, num, groupMeteor, all_sprites):

		for i in range(num):
			m = Meteor(array_meteors, random.randrange(WIDTH, WIDTH+800), random.randrange(HEIGHT_PANEL_PLAYER, HEIGHT))
			groupMeteor.add(m)
			all_sprites.add(m)

	def showNumWave(self, screen, posX, posY, text, sizeText, color):
		font_default = pygame.font.get_default_font()
		font = pygame.font.Font(font_default, sizeText)
		font_render = font.render(text, False, color)
		rect = font_render.get_rect()
		screen.blit(font_render, (posX, posY))
			











# inicia o jogo
if __name__ == '__main__':
	Game()
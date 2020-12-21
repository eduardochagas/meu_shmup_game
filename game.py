import pygame
import random
from constantes import *
from playership import PlayerShip
from enemyship import EnemyShip
from meteor import Meteor
from tinymeteor import Tinymeteor
from explosion import Explosion
from powerupshoot import PowerupShoot




class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT_SCREEN))
		pygame.display.set_caption(TITULO_DO_JOGO)
		self.clock = pygame.time.Clock()
		self.score = 0

		self.all_sprites = pygame.sprite.Group()
		self.bullet_player1 = pygame.sprite.Group()

		self.player1 = PlayerShip(imgBullet=img_laser_player1, width=30, height=40, posX=20, posY=int(HEIGHT_SCREEN)/2, velocity=5, group_All_Sprites=self.all_sprites, group_Bullet=self.bullet_player1)
		self.all_sprites.add(self.player1)

		####################################
		# 
		#
		self.powerupsPlayer1 = pygame.sprite.Group()

		#####################################################################
		# cria os grupos dos primeiros inimigos
		# cria o grupo que armazena as balas dos inimigos do primeiro grupo
		#
		self.group_enemy1 = pygame.sprite.Group()
		self.bullet_enemy1 = pygame.sprite.Group() 
		#
		# cria a primeira onda inimiga 1
		self.createEnemies(imgBullet=dict_lasers['lasers_blue'][0] ,img=dict_enemies['blue'][0], listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy1, groupEnemy=self.group_enemy1)


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
			##################################################################
			# exibe o número de onda inimiga que está atacando no momento 
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
				# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				# 
				hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy1, True, pygame.sprite.collide_mask)
				########################################################################
				# para cada uma das balas do array hit_bullet_enemy...
				#
				for bullet in hit_bullet_enemy:
					self.player1.blood -= random.randrange(2, 4)
					################################################################################
					# define uma explosão do tipo pequena quando a bala colide com a nave do player
					#
					expl = Explosion(bullet.rect.center, 'tiny')
					self.all_sprites.add(expl)
					############################################
					# se o sangue do player acabar...
					#
					if self.player1.blood <= 0:
						self.player1.blood = 0
						###################################################
						# atribui a imagem do player na classe de explosão
						expl = Explosion(self.player1.rect.center, 'normal') 
						self.all_sprites.add(expl) # adiciona a classe explosão em self.all_sprites
						self.player1.hide() # esconde a imagem do player, da tela do pygame

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				#
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy1, True, True)
				####################################
				# se a colisão for verdadeira...
				#
				for enemy in hit_enemy:
					self.player1.score += 1
					################################################
					# explode a nave inimiga
					#
					expl = Explosion(enemy.rect.center, 'normal')
					self.all_sprites.add(expl)

				#################################################################################
				# se não houver mais inimigos no grupo da primeira onda inimiga...
				#
				if len(self.group_enemy1) == 0:
					self.num_waves = 2 # muda para a segunda onda inimiga
					self.group_enemy2 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy2 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################
					# cria os meteoros na tela do jogo
					self.createMeteors(7, self.wave1_meteor, self.all_sprites)
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
				#   OBS: o método spritecollide RETORNA UMA LISTA DE OBJETOS (nesse caso, SÃO 
				#   OS METEÓROS)
				#
				hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True, pygame.sprite.collide_mask)
				########################################################################
				# para cada meteoro da lista...
				#
				for hit_meteor in hit_meteors:
					################################################
					# tira o sangue do player baseado no raio do meteoro
					#
					self.player1.blood -= hit_meteor.radius
					################################################################
					# define a explosão pequena na colisão do player com o meteoro
					# e adiciona ao grupo: self.all_sprites
					#
					expl = Explosion(hit_meteor.rect.center, 'tiny')
					self.all_sprites.add(expl)
					################################################################
					# se o sangue da nave do player for igual ou menor que zero....
					#
					if self.player1.blood <= 0:
						self.player1.blood = 0
						###################################################
						# atribui a imagem do player na classe de explosão,
						# ou seja, as imagens de explosão vao espawnar onde 
						# a POSIÇÂO DA IMAGEM DO PLAYER ESTAVA NA TELA.
						#
						#  OBS: as imagens da explosão NÃO FICAM ATRELADAS A
						#  IMAGEM DO PLAYER, ela fica atrelada Á POSIÇÃO
						#  EM QUE A IMAGEM DO PLAYER ESTAVA NA TELA DO JOGO,
						#  É POR ISSO QUE QUANDO OCORRE A EXPLOSÃO, CONSEGUIMOS
						#  MOVER A IMAGEM DO PLAYER PARA UM OUTRO LUGAR FORA DA 
						#  TELA QUANDO USAMOS O MÈTODO: self.player1.hide()
						expl = Explosion(self.player1.rect.center, 'normal') 
						self.all_sprites.add(expl) # adiciona a classe explosão em: self.all_sprites
						self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
						

				#################################################################3
				# colisão das balas do player1 com os meteoros...
				#
				hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
				for hit_meteor in hit:
					# p = PowerShoot(hit_meteor.rect.center)
					# self.all_sprites.add(p)
					################################################################
					# define a explosão pequena na colisão do player com o meteoro
					# e adiciona ao grupo: self.all_sprites
					#
					expl = Explosion(hit_meteor.rect.center, 'tiny')
					self.all_sprites.add(expl)
					########################################################
					# cria os meteoros minusculos a partir do momento que 
					# atiramos no meteoro grande.
					# os valores: (5, 7, -5, 5) e (5, 7, 5, 6) são referentes a 
					# posição em que os meteóros minúsculos percorrerão na tela 
					# quando atingimos o meteoro grande...
					#
					tinymeteor1 = Tinymeteor(hit_meteor.rect.center, 5, 7, -5, 5)
					tinymeteor2 = Tinymeteor(hit_meteor.rect.center, 5, 7, 5, 6)
					################################################################
					# adicinamos os meteoros pequenos no grupo self.all_sprites
					#
					self.all_sprites.add(tinymeteor1)
					self.all_sprites.add(tinymeteor2)

					#####################################################################
					# se o valor aleatório de random.random() for maior do que 0.8 (ou seja,
					# tem 20 por cento de chance dos poderes aparecerem
					#					
					if random.random() > 0.7:
						power = PowerupShoot(hit_meteor.rect.center)
						self.powerupsPlayer1.add(power)
						self.all_sprites.add(power)


				########################################################
				# faz a colisão do player com as imagens dos powerups
				#
				hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
				
				for power in hit_powers:
					if power.type == 'blood': # se o tipo do powerup tiver esse nome...
						if self.player1.blood < 100: # se o sangue do player for menor que 100...
							self.player1.blood += random.randrange(10, 15)
					if power.type == 'gun': # se o tipo do powerup tiver esse nome...
						self.player1.double_shoot_player()


				#################################################################################
				# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				#
				hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy2, True)
				######################################################################
				# para cada bala inimiga acertada na nave do player...				#
				#
				for enemy in hit_bullet_enemy:
					self.player1.blood -= random.randrange(2, 4)
					#############################################################################
					# define uma explosão pequena na colisão da bala inimiga com a nave do player
					#
					expl = Explosion(enemy.rect.center, 'tiny')
					self.all_sprites.add(expl) # adiciona a classe explosão em self.all_sprites
					################################################################
					# se o sangue da nave do player for igual ou menor que zero....
					#
					if self.player1.blood <= 0:
						self.player1.blood = 0
						###################################################
						# atribui a imagem do player na classe de explosão,
						# ou seja, as imagens de explosão vao espawnar onde 
						# a POSIÇÂO DA IMAGEM DO PLAYER ESTAVA.
						#
						#  OBS: as imagens da explosão NÃO FICAM ATRELADAS A
						#  IMAGEM DO PLAYER, ela fica atrelada Á ÚLTIMA POSIÇÃO
						#  EM QUE A IMAGEM DO PLAYER ESTAVA NA TELA DO JOGO,
						#  É POR ISSO QUE QUANDO OCORRE A EXPLOSÃO, CONSEGUIMOS
						#  MOVER A IMAGEM DO PLAYER PARA UM OUTRO LUGAR FORA DA 
						#  TELA QUANDO USAMOS O MÈTODO: self.player1.hide()
						expl = Explosion(self.player1.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a classe explosão em self.all_sprites 
						self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
						

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy2, True, True)
				for enemy in hit_enemy:
					self.player1.score += 1
					################################################
					# explode a nave inimiga
					#
					expl = Explosion(enemy.rect.center, 'normal')
					self.all_sprites.add(expl)

				#################################################################################
				# se não houver mais inimigos no grupo da segunda onda inimiga...
				#
				if len(self.group_enemy2) == 0 and len(self.wave1_meteor) == 0:
					self.num_waves = 3 # troca para a nova onda inimiga
					self.player1.shoot_player = 1 # RETORNA PARA O TIRO INDIVIDUAL da nave do player
					self.group_enemy3 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy3 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################################
					# cria a terceira onda inimiga: wave3
					#
					self.createEnemies(imgBullet=dict_lasers['lasers_blue'][4], img=dict_enemies['blue'][3], listWave=wave3, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy3, groupEnemy=self.group_enemy3)


			if self.num_waves == 3:

				#################################################################################
				# checa a colisão do player1 com OS METEOROS QUE RESTOU DA SEGUNDA ONDA INIMIGA No jogo
				#
				hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True, pygame.sprite.collide_mask)
				####################################################
				# checa a colisão com cada meteoro da lista...
				#
				for hit_enemy in hit_meteors:
					########################################################
					# tira o sangue do player baseado no raio do meteoro
					#
					self.player1.blood -= hit_enemy.radius
					#####################################################
					# se o sangue do player for menor ou igual a zero...
					#
					if self.player1.blood <= 0:
						self.player1.blood = 0
						###################################################
						# atribui a imagem do player na classe de explosão,
						# ou seja, as imagens de explosão vao espawnar onde 
						# a POSIÇÂO DA IMAGEM DO PLAYER ESTAVA.
						#
						#  OBS: as imagens da explosão NÃO FICAM ATRELADAS A
						#  IMAGEM DO PLAYER, ela fica atrelada Á ÚLTIMA POSIÇÃO
						#  EM QUE A IMAGEM DO PLAYER ESTAVA NA TELA DO JOGO,
						#  É POR ISSO QUE QUANDO OCORRE A EXPLOSÃO, CONSEGUIMOS
						#  MOVER A IMAGEM DO PLAYER PARA UM OUTRO LUGAR FORA DA 
						#  TELA QUANDO USAMOS O MÈTODO: self.player1.hide()
						expl = Explosion(self.player1.rect.center) 
						self.all_sprites.add(expl) # adiciona a classe explosão em self.all_sprites
						self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
						

				#################################################################3
				# colisão das balas do player1 com os meteoros...
				hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
				for hit_meteor in hit:
					################################################################
					# define a explosão pequena na colisão do player com o meteoro
					# e adiciona ao grupo: self.all_sprites
					#
					expl = Explosion(hit_meteor.rect.center, 'tiny')
					self.all_sprites.add(expl)
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



				########################################################
				# faz a colisão do player com as imagens dos powerups
				#
				hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
				
				for power in hit_powers:
					if power.type == 'blood': # se o tipo do powerup tiver esse nome...
						if self.player1.blood < 100: # se o sangue do player for menor que 100...
							self.player1.blood += random.randrange(10, 15)
					if power.type == 'gun': # se o tipo do powerup tiver esse nome...
						self.player1.double_shoot_player()



				#################################################################################
				# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				#
				hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy3, True)
				#######################################################################################
				# checa a colisão da nave do player com cada bala inimiga no array: hit_bullet_enemy
				#
				for bullet in hit_bullet_enemy:						
					self.player1.blood -= random.randrange(5, 10)
					#####################################################
					# se o sangue do player for menor ou igual a zero...
					#
					if self.player1.blood <= 0:
						self.player1.blood = 0
						###################################################
						# atribui a imagem do player na classe de explosão,
						# ou seja, as imagens de explosão vao espawnar onde 
						# a POSIÇÂO DA IMAGEM DO PLAYER ESTAVA.
						#
						#  OBS: as imagens da explosão NÃO FICAM ATRELADAS A
						#  IMAGEM DO PLAYER, ela fica atrelada Á ÚLTIMA POSIÇÃO
						#  EM QUE A IMAGEM DO PLAYER ESTAVA NA TELA DO JOGO,
						#  É POR ISSO QUE QUANDO OCORRE A EXPLOSÃO, CONSEGUIMOS
						#  MOVER A IMAGEM DO PLAYER PARA UM OUTRO LUGAR FORA DA 
						#  TELA QUANDO USAMOS O MÈTODO: self.player1.hide()
						expl = Explosion(self.player1.rect.center, 'normal') 
						self.all_sprites.add(expl) # adiciona a classe explosão em self.all_sprites
						self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
						

				################################################################
				# checa a colisão das balas do player com as balas dos inimigos
				#
				hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy3, True, True)
				for enemy in hit_enemy:
					self.player1.score += 1
					################################################
					# explode a nave inimiga
					#
					expl = Explosion(enemy.rect.center, 'normal')
					self.all_sprites.add(expl)

				#################################################################################
				# se não houver mais inimigos no grupo da terceira onda inimiga...
				#
				if len(self.group_enemy3) == 0:
					self.num_waves = 4
					# self.group_enemy4 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					# self.bullet_enemy4 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					# # cria a terceira onda inimiga: wave3
					# self.createEnemies(imgBullet=dict_lasers['lasers_blue'][0], img=dict_enemies['red'][1], listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)







			#################################################################################
			# define os frames do jogo
			self.clock.tick(FPS)

			#################################################################################
			# atualiza a tela do jogo
			pygame.display.update()



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


	def showNumWave(self, screen, posX, posY, text, sizeText, color):
		font_default = pygame.font.get_default_font()
		font = pygame.font.Font(font_default, sizeText)
		font_render = font.render(text, False, color)
		rect = font_render.get_rect()
		screen.blit(font_render, (posX, posY))

			
	def createEnemies(self, imgBullet, img, listWave, groupAll_sprites, groupBullet, groupEnemy):

		for lista in listWave:
			for item in range(len(lista)):
				#print(item)
				e = EnemyShip(imgBullet, img, lista[0], lista[1], lista[2], lista[3], lista[4], groupAll_sprites, groupBullet)
				groupEnemy.add(e) # adiciona o inimigo ao grupo de inimigo correspondente
				groupAll_sprites.add(e) # adiciona o inimigo ao grupo que contêm todos os objetos do jogo


	def createMeteors(self, num, groupMeteor, all_sprites):

		for i in range(num):
			m = Meteor(array_meteors, random.randrange(WIDTH, WIDTH+800), random.randrange(HEIGHT_PANEL_PLAYER, HEIGHT))
			groupMeteor.add(m)
			all_sprites.add(m)

# inicia o jogo
if __name__ == '__main__':
	Game()
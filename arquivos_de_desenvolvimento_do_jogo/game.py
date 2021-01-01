import pygame
import random
from constants import *
from playership import PlayerShip
from enemyship import EnemyShip
from meteor import Meteor
from tinymeteor import Tinymeteor
from explosion import Explosion
from powerups import Powerups




class Game:

	def __init__(self):
		############################################
		# inicia os módulos do pygame
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT_SCREEN))
		pygame.display.set_caption(TITULO_DO_JOGO)
		self.clock = pygame.time.Clock()
		self.score = 0

		# #####################################################
		# variável de controle do loop principal do jogo		
		self.running = True
		
		###############################################
		# variavel de controle da tela inicial do jogo
		self.game_over = True
		
		##############################################
		# variavel de controle da tela inicial do jogo
		self.paused = False

		#######################################
		# executa o loop do jogo
		self.loop()


	
	def loop(self):

		#############################
		# loop principal do jogo
		while self.running:

			########################################
			# game over sempre inicia como True
			# 
			if self.game_over:


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
				##############################################
				# cria a primeira onda inimiga 1
				self.createEnemies(imgBullet=dict_lasers['lasers_green'][4] ,img=dict_enemies['blue'][0], listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy1, groupEnemy=self.group_enemy1)
				###########################################################
				# grupo que armazena a primeira onda de meteoros do jogo
				self.wave1_meteor = pygame.sprite.Group()
				###########################################################
				# grupo que armazena a primeira onda de meteoros do jogo
				self.wave2_meteor = pygame.sprite.Group()
				########################################################
				# variáveis que controlam as ondas de ataque inimigas
				#
				self.show_enemies_new_wave = False
				self.num_waves = 1
				###############################################
				# variável de controle do loop da tela inicial	
				self.initial_screen = True

				#####################################################
				# variável de controle do loop principal do jogo
				#		
				#self.running = True
				##############################################
				# variavel de controle da tela inicial do jogo
				#self.game_over = True

				##############################################
				# variavel de controle da tela inicial do jogo
				self.paused = False






				# enquanto tela inicial for True...
				while self.initial_screen:

					############################################################
					# tbm definimos o controle de FPS na tela inicial 
					# do jogo. Isso AJUDA A CONTROLAR A TAXA DE ATUALIZAÇÕES
					# DA TELA INICIAL DO nosso JOGO
				    self.clock.tick(FPS)
				    ###########################################
				    # insere o texto na tela inicial do jogo
				    #
				    self.drawText(self.screen, int(WIDTH/2), int(HEIGHT/2), 'Shmup Game', 60, YELLOW)
				    self.drawText(self.screen, int(WIDTH/2), int(HEIGHT/2+200), 'Press SPACEBAR to Play', 30, YELLOW)
				    
				    ################################################################
				    # insere as imagens das naves na tela inicial do jogo
				    #   OBS: NÃO MEXA NOS VALORES das funções: self.drawImagesScreenPrincipal()
				    #
				    self.drawImagesScreenPrincipal(img_initial_screen, int(WIDTH/4)+100, int(HEIGHT/2)+47)
				    self.drawImagesScreenPrincipal(img_laser_player_initial_screen, int(WIDTH/4)+185, int(HEIGHT/2)+60)	    
				    self.drawImagesScreenPrincipal(img_ship_enemy_initial_screen, int(WIDTH/4)+300, int(HEIGHT/2)+17)
				    self.drawImagesScreenPrincipal(img_ship_enemy_initial_screen, int(WIDTH/4)+350, int(HEIGHT/2)+50)  
				    self.drawImagesScreenPrincipal(img_ship_enemy_initial_screen, int(WIDTH/4)+300, int(HEIGHT/2)+85)


				    ############################################
				    # loop de verificação das teclas do teclado
				    for event in pygame.event.get():
				    	###################################################
				    	# se depois de soltarmos uma tecla pressionada...
				    	if event.type == pygame.KEYUP:
				    		#################################################
				    		# se a tecla pressionada for a barra de espaçõ...
				    		if event.key == pygame.K_SPACE:
				    			###########################################################
				    			# definimos a variável de controle do loop da tela inicial
				    			# para false, saindo do loop da tela inicial
					    		self.initial_screen = False 
					    		#################################################
					    		# definimos a propriedade que entra para o loop
					    		# da tela inicial para: False
					    		self.game_over = False
					    		###################################################
					    		# limpamos as informações da tela inicial do jogo
					    		# para o pygame poder inserir todos os elementos do
					    		# jogo na tela.
					    		pygame.display.flip()

				    	if event.type == pygame.QUIT:
				    		pygame.quit()
				    		exit()
				    
				    #################################################################
		    		# usamos aqui o metodo de atualização da tela pq 
		    		# EXATAMENTE NO MOMENTO EM QUE O PYGAME ABRE A TELA dele, 
		    		# A TELA É ABERTA SEM NENHUMA INFORMAÇÃO, somente QUANDO
		    		# É FEITA A PRIMEIRA ATUALIZAÇÃO DA TELA é que o pygame
		    		# INSERE AS INFORMAÇÕES DE TEXTO definidas nos métodos abaixo, NA TELA:
		    		#
		    		#	self.drawText(self.screen, int(WIDTH/2), int(HEIGHT/2), 'Shmup Game', 40, YELLOW)
				    #	self.drawText(self.screen, int(WIDTH/2), int(HEIGHT/2+100), 'Press SPACEBAR to Play', 40, YELLOW)
				    #
				    # e como essas INFORMAÇÕES DE TEXTO estão DENTRO DE UM LOOP com a TAXA DE FRAMES
				    # JÁ DEFINIDAS (nesse caso, definimos com a mesma taxa de frame do jogo, 
				    # ou seja: 60 fps), ou seja, a cada 60 frames por segundo, a 
				    # tela inicial do jogo é atualizada
				    #
				    #  OBS: o sistema de atualização de telas do pygame é parecido com
				    #  o sistema de camadas (as layers) do photoshop, ou seja, antes de
				    #  qualquer atualização de tela, o pygame exibe uma tela inicial (em branco,  
				    #  sem conteúdo). Quando definimos um conteúdo para ser exibido na tela, e
				    #  inserimos esse(s) conteúdo(s) na tela, temos que usar um método de 
				    #  atualização de tela, como por exemplo:
				    #
				    #    pygame.display.flip()  ou  pygame.display.update()
				    #
				    #  para que esse(s) conteúdo(s) sejam exibidos na tela. Como TANTO OS CONTEÚDOS 
				    #  INSERIDOS NA TELA, quanto O MÉTODO DE ATUALIZAÇÃO DE TELA estão DENTRO 
				    #  DE UM LOOP, essas INFORMAÇÕES NA TELA vao ficar SENDO ATUALIZADAS a 
				    #  cada 60 FRAMES POR SEGUNDO. Essa é a FORMA CORRETA de se FAZER 
				    #  UMA TELA INICIAL BÀSICA para um jogo. 
				    #
				    #  Quando definimos O COMPORTAMENTO DE APERTARMOS 
				    #  UMA TECLA para INSERIRMOS UM NOVO CONTEÚDO NA TELA, temos tbm que INSERIR UM
				    #  METODO DE ATUALIZAÇÃO DE TELA para que TODAS AS INFORMAÇÕES que queremos 
				    #  inserir na tela possam ser inseridas na tela. Se a tela já possui 
				    #  conteúdo sendo exibido, e vc quer limpar esses conteúdos atuais da tela para
				    #  inserir um novo conteudo, é necessário usar os métodos abaixo:
				    #
				    #    # limpa os conteúdos da tela
				    #    self.screen.fill(BLACK)  
				    #
				    #    # atualiza a tela para poder exibir um novo conteúdo
				    #    pygame.display.flip()   
				    #
				    #    # exibe um novo conteúdo na tela
				    #    self.drawText(self.screen, int(WIDTH/2), int(HEIGHT/2), 'um texto qualquer', 60, YELLOW) 
				    #
				    #  OU SEJA, LIMPA A TELA para que AS PROXIMAS INFORMAÇÕES CONFIGURADAS PARA SEREM 
				    #  INSERIDAS NA TELA POSSAM DE FATO SER INSERIDAS NA TELA. isso é o que fizemos 
				    #  dentro do bloco da linha: 
				    #
				    #    if event.key == pygame.K_SPACE:
				    #		...
				    #
				    #  OBS2: a linha acima fica dentro do loop for que verifica se as teclas do teclado
				    #  foram pressionadas ou não.  


				    pygame.display.flip()

			if self.game_over == False:



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
				self.drawText(self.screen, WIDTH/2, 100, 'Wave: '+str(self.num_waves), 25, YELLOW)


				#################################################################################
				# desenha todas as sprites na tela do jogo
				self.all_sprites.draw(self.screen)

				
				self.pausedGame()
				#################################################################################
				# chama todos os métodos update() de cada objeto do grupo self.all_sprites
				self.all_sprites.update()

				###########################################################
				# *********************************************************
				# metodo que possui a mecanica que PAUSA e DESPAUSA o jogo
				# *********************************************************

				#############################
				# primeira onda inimiga
				if self.num_waves == 1:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
					# 
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy1, True, pygame.sprite.collide_mask)
					
	
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							################################3
							# 
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							######################################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy1, True, True)
					####################################
					# para cada inimigo em self.group_enemy1...
					#
					for enemy in hit_enemy:
						self.player1.score += 1 # aumenta 1 ponto para o player1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl)
						##############################################
						# ativa o barulho de explosão da nave inimiga
						# sound_explosion_enemies.play()
						#########################################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)


					#################################################################################
					# se não houver mais inimigos no grupo da primeira onda inimiga...
					#
					if len(self.group_enemy1) == 0:
						
						########################################################
						# variável de controle para a criação das ondas inimigas
						self.show_enemies_new_wave = True
						########################################################
						# muda para a segunda onda inimiga 
						self.num_waves = 2 

				############################################################
				# se a variável de controle: self.show_enemies_new_wave, for 
				# verdadeira e self.num_waves tiver o valor: 2....
				if self.show_enemies_new_wave == True and self.num_waves == 2:

					############################################################
					# cria todos os objetos referente a segunda onda inimiga
					#
					self.group_enemy2 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy2 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################
					# cria os meteoros na tela do jogo
					self.createMeteors(7, self.wave1_meteor, self.all_sprites)
					####################################################
					# cria a segunda onda inimiga: wave2
					self.createEnemies(imgBullet=dict_lasers['lasers_green'][8],img=dict_enemies['black'][1], listWave=wave2, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy2, groupEnemy=self.group_enemy2)
					####################################################
					# cria os meteoros na tela do jogo
					self.createMeteors(5, self.wave1_meteor, self.all_sprites)
					####################################################
					# temos que configurar a variável de controle para False
					# quando criamos todos os inimigos na tela do pygame
					self.show_enemies_new_wave = False


				################################################################################
				# se a onda inimiga for a segunda onda...	
				#		
				if self.num_waves == 2:

					#**********************************************************************************************
					# Essa parte do código verifica colisões das balas dos inimigos ainda da primeira onda inimiga 
					#################################################################################
					# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
					# 
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy1, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						###############################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							################################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame

					#************************************************************************************

					#####################################################################################
					# Daqui é onde começa a verificação de colisão da SEGUNDA ONDA INIMIGA...
					#################################################################################
					# chaca a colisão do player1 com OS METEOROS da segunda onda inimiga do jogo
					#   OBS: o método spritecollide RETORNA UMA LISTA DE OBJETOS (nesse caso, SÃO 
					#   OS METEÓROS)
					#
					hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True, pygame.sprite.collide_mask)
					
					########################################################################
					# para cada meteoro do grupo: self.wave1_meteor...
					#   OBS: o valor retornado do metodo spritecollide é uma lista de
					#   objetos (classes) de meteoro.

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
						# sound_explosion_meteor.play()
						#####################################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							#########################################
							#
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em: self.all_sprites
							# sound_explosion_player1.play()
							###################################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
							


					########################################################
					# faz a colisão do player com as imagens dos powerups
					#
					hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
					
					for power in hit_powers:
						if power.type == 'blood': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(7).play(sound_item_blood)
							#####################################
							#
							if self.player1.blood < 100: # se o sangue do player for menor que 100...
								self.player1.blood += random.randrange(10, 15)

						if power.type == 'gun': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(6).play(sound_item_shoot)
							################################################
							#
							if self.num_waves:
								self.player1.double_shoot_player()


					#################################################################3
					# colisão das balas do player1 com os meteoros...
					#
					hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
					

					for hit_meteor in hit:


						################################################################
						# define a explosão pequena na colisão do player com o meteoro
						# e adiciona ao grupo: self.all_sprites
						#
						expl = Explosion(hit_meteor.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_meteor.play()
						########################################
						#
						pygame.mixer.Channel(4).play(sound_explosion_meteor)
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
						# se o valor aleatório de random.random() for maior do que 0.7 (ou seja,
						# tem 30 por cento de chance dos poderes aparecerem
						#					
						if random.random() > 0.7:
							power = Powerups(hit_meteor.rect.center)
							self.powerupsPlayer1.add(power)
							self.all_sprites.add(power)



							


					#################################################################################
					# checa a colisão do player1 com AS BALAS da SEGUNDA onda inimiga do jogo 
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
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							######################################
							#
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True

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
							death_explosion = Explosion(self.player1.rect.center, 'normal')
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites 
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
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
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy2) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 3 # troca para a nova onda inimiga (a terceira onda inimiga)


				############################################################
				# se a variável de controle: self.show_enemies_new_wave, for 
				# verdadeira e: self.num_waves, tiver o valor: 3....
				if self.show_enemies_new_wave == True and self.num_waves == 3:

					self.group_enemy3 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy3 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################################
					# cria a terceira onda inimiga: wave3
					#
					self.createEnemies(imgBullet=dict_lasers['lasers_green'][8], img=dict_enemies['red'][2], listWave=wave3, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy3, groupEnemy=self.group_enemy3)
					####################################################
					# temos que configurar a variável de controle para False
					# quando criamos todos os inimigos na tela do pygame
					self.show_enemies_new_wave = False


				if self.num_waves == 3:

					#**********************************************************************************************
					# Essa parte do código verifica colisões das balas dos inimigos ainda da SEGUNDA ONDA INIMIGA 
					#################################################################################
					# checa a colisão do player1 com AS BALAS da SEGUNDA ONDA INIMIGA do jogo 
					# 
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy2, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


					################################################################
					# checa a colisão do player1 com OS METEOROS da onda anterior (da SEGUNDA ONDA INIMIGA) do jogo 
					hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave1_meteor, True, pygame.sprite.collide_mask)
					
					########################################################################
					# para cada meteoro do grupo: self.wave1_meteor...
					#   OBS: o valor retornado do metodo spritecollide é uma lista de
					#   objetos (classes) de meteoro.

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
						# sound_explosion_meteor.play()
						#####################################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							#########################################
							#
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em: self.all_sprites
							# sound_explosion_player1.play()
							###################################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.



					########################################################
					# faz a colisão do player com as imagens dos powerups
					#
					hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
					
					for power in hit_powers:
						if power.type == 'blood': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(7).play(sound_item_blood)
							if self.player1.blood < 100: # se o sangue do player for menor que 100...
								self.player1.blood += random.randrange(10, 15)

						if power.type == 'gun': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(6).play(sound_item_shoot)
							if self.num_waves:
								self.player1.double_shoot_player()



					#################################################################################################
					# checa a colisão das balas do player1 com OS METEOROS QUE RESTOU DA SEGUNDA ONDA INIMIGA No jogo
					##################################################################
					# colisão das balas do player1 com os meteoros...
					hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave1_meteor, True, True)
					for hit_meteor in hit:
						################################################################
						# define a explosão pequena na colisão do player com o meteoro
						# e adiciona ao grupo: self.all_sprites
						#
						expl = Explosion(hit_meteor.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_meteor.play()
						##################################
						#
						pygame.mixer.Channel(4).play(sound_explosion_meteor)
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

						#####################################################################
						# se o valor aleatório de random.random() for maior do que 0.7 (ou seja,
						# tem 30 por cento de chance dos poderes aparecerem
						#					
						if random.random() > 0.7:
							power = Powerups(hit_meteor.rect.center)
							self.powerupsPlayer1.add(power)
							self.all_sprites.add(power)



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da TERCEIRA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy3, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)


					#################################################################################
					# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy3, True)
					#######################################################################################
					# checa a colisão da nave do player com cada bala inimiga no array: hit_bullet_enemy
					#
					for bullet in hit_bullet_enemy:						
						self.player1.blood -= random.randrange(5, 10)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						#####################################################
						# se o sangue do player for menor ou igual a zero...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)

							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
							

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy3) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 4 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 3....
					if self.show_enemies_new_wave == True and self.num_waves == 4:

						self.group_enemy4 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy4 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_blue'][6],img=dict_enemies['green'][3], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				if self.num_waves == 4:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da TERCEIRA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy3, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da QUARTA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy4, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy4, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy4) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 5 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 5:

						self.group_enemy5 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy5 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_green'][12],img=dict_enemies['black'][4], listWave=wave5, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy5, groupEnemy=self.group_enemy5)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				if self.num_waves == 5:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da TERCEIRA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy4, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da QUARTA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy5, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy5, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


			############################
			# ljlçjljlkjçlkj

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy5) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 6 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 6:

						self.group_enemy6 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy6 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_green'][8],img=dict_enemies['black'][1], listWave=wave6, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy6, groupEnemy=self.group_enemy6)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				if self.num_waves == 6:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da TERCEIRA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy5, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da SEXTA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy6, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy6, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


			############################
			# ljlçjljlkjçlkj

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy6) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 7 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 7:

						self.group_enemy7 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy7 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_blue'][6],img=dict_enemies['green'][2], listWave=wave7, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy7, groupEnemy=self.group_enemy7)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				if self.num_waves == 7:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da SEXTA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy6, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da SETIMA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy7, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy7, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


			############################
			# ljlçjljlkjçlkj

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy7) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 8 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 8:

						############################################################
						# cria todos os objetos referente a segunda onda inimiga
						#
						self.group_enemy8 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy8 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################
						# cria os meteoros na tela do jogo
						self.createMeteors(7, self.wave2_meteor, self.all_sprites)
						####################################################
						# cria a segunda onda inimiga: wave2
						self.createEnemies(imgBullet=dict_lasers['lasers_blue'][4],img=dict_enemies['red'][3], listWave=wave8, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy8, groupEnemy=self.group_enemy8)
						####################################################
						# cria os meteoros na tela do jogo
						self.createMeteors(5, self.wave2_meteor, self.all_sprites)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				if self.num_waves == 8:


					#**********************************************************************************************
					# Essa parte do código verifica colisões das balas dos inimigos ainda da SETIMA ONDA INIMIGA 
					#################################################################################
					# checa a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
					# 
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy7, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame

					#************************************************************************************


					#####################################################################################
					# Daqui é onde começa a verificação de colisão da OITAVA ONDA INIMIGA...
					#################################################################################
					# chaca a colisão do player1 com OS METEOROS da segunda onda inimiga do jogo
					#   OBS: o método spritecollide RETORNA UMA LISTA DE OBJETOS (nesse caso, SÃO 
					#   OS METEÓROS)
					#
					hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave2_meteor, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada meteoro do grupo: self.wave1_meteor...
					#   OBS: o valor retornado do metodo spritecollide é uma lista de
					#   objetos (classes) de meteoro.

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
						# sound_explosion_meteor.play()
						#####################################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em: self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
							


					########################################################
					# faz a colisão do player com as imagens dos powerups
					#
					hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
					
					for power in hit_powers:
						if power.type == 'blood': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(7).play(sound_item_blood)
							if self.player1.blood < 100: # se o sangue do player for menor que 100...
								self.player1.blood += random.randrange(10, 15)

						if power.type == 'gun': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(6).play(sound_item_shoot)
							if self.num_waves:
								self.player1.double_shoot_player()




					#################################################################3
					# colisão das balas do player1 com os meteoros...
					#
					hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave2_meteor, True, True)
					for hit_meteor in hit:
						# p = PowerShoot(hit_meteor.rect.center)
						# self.all_sprites.add(p)
						################################################################
						# define a explosão pequena na colisão do player com o meteoro
						# e adiciona ao grupo: self.all_sprites
						#
						expl = Explosion(hit_meteor.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_meteor.play()
						##################################
						#
						pygame.mixer.Channel(4).play(sound_explosion_meteor)
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
						# se o valor aleatório de random.random() for maior do que 0.7 (ou seja,
						# tem 30 por cento de chance dos poderes aparecerem
						#					
						if random.random() > 0.7:
							power = PowerupShoot(hit_meteor.rect.center)
							self.powerupsPlayer1.add(power)
							self.all_sprites.add(power)





					#################################################################################
					# checa a colisão do player1 com AS BALAS da OITAVA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy8, True)
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
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal')
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites 
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
							

					################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy8, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl)
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy8) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 9 # troca para a nova onda inimiga (a terceira onda inimiga)


				############################################################
				# se a variável de controle: self.show_enemies_new_wave, for 
				# verdadeira e: self.num_waves, tiver o valor: 3....
				if self.show_enemies_new_wave == True and self.num_waves == 9:

					self.group_enemy9 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy9 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					####################################################################
					# cria a terceira onda inimiga: wave3
					#
					self.createEnemies(imgBullet=dict_lasers['lasers_green'][4], img=dict_enemies['blue'][4], listWave=wave9, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy9, groupEnemy=self.group_enemy9)
					####################################################
					# temos que configurar a variável de controle para False
					# quando criamos todos os inimigos na tela do pygame
					self.show_enemies_new_wave = False


				if self.num_waves == 9:

					#**********************************************************************************************
					# Essa parte do código verifica colisões dos meteoros ainda da onda inimiga anterior (da ONDA OITO)...
					###############################################################################################
					#
					hit_meteors = pygame.sprite.spritecollide(self.player1, self.wave2_meteor, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada meteoro do grupo: self.wave1_meteor...
					#   OBS: o valor retornado do metodo spritecollide é uma lista de
					#   objetos (classes) de meteoro.

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
						# sound_explosion_meteor.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						################################################################
						# se o sangue da nave do player for igual ou menor que zero....
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
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
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em: self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem da nave do nosso player quando acaba o sangue de cada vida do player.
							

					#################################################################################
					#
					# faz a colisão do player com as imagens dos powerups
					#
					hit_powers = pygame.sprite.spritecollide(self.player1, self.powerupsPlayer1, True)
					
					for power in hit_powers:
						if power.type == 'blood': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(7).play(sound_item_blood)
							if self.player1.blood < 100: # se o sangue do player for menor que 100...
								self.player1.blood += random.randrange(10, 15)

						if power.type == 'gun': # se o tipo do powerup tiver esse nome...
							##################################
							#
							pygame.mixer.Channel(6).play(sound_item_shoot)
							if self.num_waves:
								self.player1.double_shoot_player()



					#################################################################3
					# colisão das balas do player1 com os meteoros...
					#
					hit = pygame.sprite.groupcollide(self.bullet_player1, self.wave2_meteor, True, True)
					for hit_meteor in hit:
						# p = PowerShoot(hit_meteor.rect.center)
						# self.all_sprites.add(p)
						################################################################
						# define a explosão pequena na colisão do player com o meteoro
						# e adiciona ao grupo: self.all_sprites
						#
						expl = Explosion(hit_meteor.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_meteor.play()
						##################################
						#
						pygame.mixer.Channel(4).play(sound_explosion_meteor)
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
						# se o valor aleatório de random.random() for maior do que 0.7 (ou seja,
						# tem 30 por cento de chance dos poderes aparecerem
						#					
						if random.random() > 0.6:
							power = PowerupShoot(hit_meteor.rect.center)
							self.powerupsPlayer1.add(power)
							self.all_sprites.add(power)
					


					#################################################################################
					# checa a colisão do player1 com AS BALAS da onda inimiga anteriror (da ONDA INIMIGA 8)
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy8, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da NONA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy9, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy9, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							#######################################
							# volta para o tiro de bala única
							self.player1.turn_shoot_to_one = True
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


			############################
			# ljlçjljlkjçlkj

					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy9) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 10 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 10:

						self.group_enemy10 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy10 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_green'][10],img=dict_enemies['black'][1], listWave=wave6, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy10, groupEnemy=self.group_enemy10)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				##########################
				# hlkjhlkhkjhlk

				if self.num_waves == 10:

					#################################################################################
					# checa a colisão do player1 com AS BALAS da NONA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy9, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da DECIMA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy10, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy10, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy10) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 11 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 11:

						self.group_enemy11 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy11 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_blue'][6],img=dict_enemies['blue'][3], listWave=wave11, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy11, groupEnemy=self.group_enemy11)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False


				##########################
				# hlkjhlkhkjhlk

				if self.num_waves == 11:

					#################################################################################
					# checa a colisão do player1 com AS BALAS ainda da DECIMA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy10, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da DECIMA PRIMEIRA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy11, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy11, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy11) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 12 # troca para a nova onda inimiga (a terceira onda inimiga)


					############################################################
					# se a variável de controle: self.show_enemies_new_wave, for 
					# verdadeira e: self.num_waves, tiver o valor: 5....
					if self.show_enemies_new_wave == True and self.num_waves == 12:

						self.group_enemy12 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
						self.bullet_enemy12 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
						####################################################################
						# cria a quarta onda inimiga: wave4
						#
						#self.createEnemies(imgBullet=dict_lasers['lasers_green'][3], img=dict_enemies['black'][1], listWave=wave4, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy4, groupEnemy=self.group_enemy4)
						self.createEnemies(imgBullet=dict_lasers['lasers_green'][8],img=dict_enemies['red'][4], listWave=wave12, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy12, groupEnemy=self.group_enemy12)
						####################################################
						# temos que configurar a variável de controle para False
						# quando criamos todos os inimigos na tela do pygame
						self.show_enemies_new_wave = False

						##########################
				# hlkjhlkhkjhlk

				if self.num_waves == 12:

					#################################################################################
					# checa a colisão do player1 com AS BALAS ainda da DECIMA ONDA INIMIGA do jogo 
					#
					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy11, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame



					#####################################################################################
					# Daqui é onde começa a verificação de colisão da DECIMA SEGUNDA ONDA INIMIGA...
					###########################################################################
					# checa a colisão das balas do player com as balas dos inimigos
					#
					hit_enemy = pygame.sprite.groupcollide(self.bullet_player1, self.group_enemy12, True, True)
					for enemy in hit_enemy:
						self.player1.score += 1
						################################################
						# explode a nave inimiga
						#
						expl = Explosion(enemy.rect.center, 'normal')
						self.all_sprites.add(expl) # adiciona a explosão em: self.all_sprites
						# sound_explosion_enemies.play()
						##################################
						#
						pygame.mixer.Channel(3).play(sound_explosion_enemies)



					hit_bullet_enemy = pygame.sprite.spritecollide(self.player1, self.bullet_enemy12, True, pygame.sprite.collide_mask)
					########################################################################
					# para cada uma das balas do array hit_bullet_enemy...
					#
					for bullet in hit_bullet_enemy:
						################################################################
						# tira entre dois e quatro pontos da barra de sangue do player
						self.player1.blood -= random.randrange(2, 4)
						################################################################################
						# define uma explosão do tipo pequena quando a bala colide com a nave do player
						#
						expl = Explosion(bullet.rect.center, 'tiny')
						self.all_sprites.add(expl)
						# sound_explosion_tiny.play()
						##################################
						#
						pygame.mixer.Channel(5).play(sound_explosion_tiny)
						############################################
						# se o sangue do player acabar...
						#
						if self.player1.blood <= 0:
							self.player1.blood = 0
							###################################################
							# atribui a imagem do player na classe de explosão
							death_explosion = Explosion(self.player1.rect.center, 'normal') 
							self.all_sprites.add(death_explosion) # adiciona a classe explosão em self.all_sprites
							# sound_explosion_player1.play()
							##################################
							#
							pygame.mixer.Channel(1).play(sound_explosion_player1)
							self.player1.hide() # esconde a imagem do player, da tela do pygame


					#################################################################################
					# se não houver mais inimigos no grupo da segunda onda inimiga...
					#
					if len(self.group_enemy12) == 0:
						########################################
						# variável de controle para chamar 
						# a próxima onda inimiga...
						self.show_enemies_new_wave = True
						self.num_waves = 12 # troca para a nova onda inimiga (a terceira onda inimiga)

						################################################################################################################################
						# se em qualquer uma das ondas AND as vidas do player for 0 AND as imagens da esplosão do player acabarem de ser executadas...
						if self.num_waves == 12:
							#################################
							# limpa a tela do jogo
							self.screen.fill(BLACK)
							
							#######################################
							# removemos a imagem do player da tela
							self.player1.kill()

							##########################################
							# variável de controle do loop de exibição 
							# do score feito pelo player1
							end_game = True
							#################################
							# se end_game for verdadeiro....
							while end_game:
								
								###############################
								# define os frames do loop
								self.clock.tick(FPS)
								############################################################
								# atualiza a tela para inserir novas informações na tela
								pygame.display.flip()

								
								self.drawText(self.screen, WIDTH/2, HEIGHT/2, 'Your score: '+str(self.player1.score), 40, YELLOW)

								##################################################
								# abre o arquivo score.txt em modo gravação (w)
								arquivo = open('score.txt', 'w')
								############################################################
								# grava no arquivo score.txt o valor zero 
								arquivo.write(str('0'))
								#############################################################
								# fecha o arquivo score.txt depois de grava a pontuação nele
								arquivo.close()


								for event in pygame.event.get():
									if event.type == pygame.QUIT:
										pygame.quit()
										exit()
									if event.type == pygame.KEYUP:
										if event.key == pygame.K_p:
											self.screen.fill(BLACK)
											end_game = False
											self.game_over = True
											self.initial_screen = True
											pygame.display.flip()








				################################################################################################################################
				# se em qualquer uma das ondas AND as vidas do player for 0 AND as imagens da esplosão do player acabarem de ser executadas...
				if (self.num_waves == 1 or self.num_waves == 2 or self.num_waves == 3 or 
					self.num_waves == 4 or self.num_waves == 5 or self.num_waves == 6 or 
					self.num_waves == 7 or self.num_waves == 8 or self.num_waves == 9 or 
					self.num_waves == 10 or self.num_waves == 11 or self.num_waves == 12) and self.player1.lives == 0 and not death_explosion.alive():
					#######################################
					# removemos a imagem do player da tela
					self.player1.kill()
					####################################
					# abrimos o arquivo: score.txt
					arquivo = open('score.txt', 'r')
					#########################################################################
					# assim que lemos o arquivo, ja temos que converter o dado para inteiro,
					# para podermos usar esse dado em uma estrutura condicional. Se vc tentar
					# fazer de um jeito diferente, não vai funcionar.
					data = int(arquivo.readline())
					#################################
					# temos que fechar o arquivo.
					arquivo.close()

					##########################################
					# variável de controle do loop de exibição 
					# do score feito pelo player1
					end_game = True
					#################################
					# se end_game for verdadeiro....
					while end_game:
						
						###############################
						# define os frames do loop
						self.clock.tick(FPS)
						############################################################
						# atualiza a tela para inserir novas informações na tela
						pygame.display.flip()

						###########################################################################################
						# se o dado for igual a zero OR self.player1.score for menor ou igual ao valor de data... 
						if self.player1.score == 0 and data == 0:
							##############################################
							# insere na tela a pontuação feita
							self.drawText(self.screen, WIDTH/2, HEIGHT/2, 'score: '+str(self.player1.score), 30, YELLOW)

						########################################################################################
						# quando a pontuação do player for 1 AND o dado no arquivo score.txt for igual a zero...
						elif self.player1.score == 1 and data == 0:							
							##############################################
							# insere na tela a pontuação feita
							self.drawText(self.screen, WIDTH/2, HEIGHT/2, 'newRecordScore: '+str(self.player1.score), 40, YELLOW)
							##################################################
							# abre o arquivo score.txt em modo gravação (w)
							arquivo = open('score.txt', 'w')
							############################################################
							# grava no arquivo score.txt o valor da pontuação 
							arquivo.write(str(self.player1.score))
							#############################################################
							# fecha o arquivo score.txt depois de grava a pontuação nele
							arquivo.close()


						##############################################################################
						# se a pontuação do player1 for MENOR OU IGUAL ao dado do arquivo score.txt...
						elif self.player1.score <= data:
							##############################################
							# insere na tela a pontuação feita
							self.drawText(self.screen, WIDTH/2, HEIGHT/2, 'sscore: '+str(self.player1.score), 40, YELLOW)

						##############################################################################
						# se a pontuação do player1 for MAIOR que o dado do arquivo score.txt...
						elif self.player1.score > data:
							##############################################
							# insere na tela a pontuação feita
							self.drawText(self.screen, WIDTH/2, HEIGHT/2, 'New Record Score: '+str(self.player1.score), 40, YELLOW)
							##################################################
							# abre o arquivo score.txt em modo gravação (w)
							arquivo = open('score.txt', 'w')
							############################################################
							# grava no arquivo score.txt o valor da pontuação 
							arquivo.write(str(self.player1.score))
							#############################################################
							# fecha o arquivo score.txt depois de grava a pontuação nele
							arquivo.close()


						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
								exit()
							if event.type == pygame.KEYUP:
								if event.key == pygame.K_p:
									self.screen.fill(BLACK)
									end_game = False
									self.game_over = True
									self.initial_screen = True
									pygame.display.flip()



				#################################################################################
				# define os frames do jogo
				self.clock.tick(FPS)

				#################################################################################
				# atualiza a tela do jogo
				pygame.display.update()


	def pausedGame(self):

		#######################################
		# fecha a tela do jogo
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					####################################################################
					# ******************************************************************
					# É nesse trecho de código que funciona a MECANICA DE PAUSAR O JOGO
					# ******************************************************************
					#
					# a variável de controle de pausa do jogo recebe como valor: True
					#PAUSED_GAME = True
					################################################
					# enquanto self.pause for verdadeiro...
					self.paused = True
					PAUSED_GAME = True
					# print('PAUSED_GAME: ',PAUSED_GAME)
					while self.paused:
						########################################
						# desenha na tela o texto: Pause
						self.drawText(self.screen, WIDTH/2, HEIGHT/2+50, 'Paused' , 50, YELLOW)
						################################################################
						# verifica os eventos de tecla do teclado e da janela do pygame
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
								exit()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_p:
									self.paused = False
									PAUSED_GAME = False
						pygame.display.flip()
					


	######################################################
	# desenha as imagens da tela inicial do jogo...
	def drawImagesScreenPrincipal(self, img, centerx, centery):

		rect = img.get_rect()
		rect.centerx = centerx 
		rect.centery = centery 

		self.screen.blit(img, (rect.centerx, rect.centery))

	#############################################################
	# cria o painel do player1 na parte superior da tela do jogo
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

	###############################################################
	# desenha o score do player1 na barra superior da tela do jogo...
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
	# desenha as imagens das vidas do player
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

	##############################################################
	# desenha o nome do player1 na barra superior da tela do jogo
	def drawText(self, screen, posX, posY, text, sizeText, color):
		font_default = pygame.font.get_default_font()
		font = pygame.font.Font(font_default, sizeText)
		font_size = font.size(text)
		font_render = font.render(text, False, color)
		rect = font_render.get_rect()
		############################################################
		# poe o valor de posX no centro da área retangular do texto
		rect.centerx = posX		
		############################################################
		# poe o valor de posY no centro da área retangular do texto
		rect.centery = posY		
		############################################################
		# pega a largura do texto, divide por dois: (font_size[0]/2), 
		# E SUBTRAI A METADA DA LARGURA DO TEXTO COM O centerx da 
		# área retângular do texto
		centerText_X = rect.centerx-(font_size[0]/2)
		############################################################
		# pega o valor armazenado em centery e subtrai com o tamanho
		# da altura do texto
		centerText_Y = rect.centery-font_size[1]
		################################################
		# insere na tela o texto renderizado
		screen.blit(font_render, (centerText_X,  centerText_Y))

	#################################################
	# cria as naves inimigas do jogo
	def createEnemies(self, imgBullet, img, listWave, groupAll_sprites, groupBullet, groupEnemy):

		for lista in listWave:
			for item in range(len(lista)):
				#print(item)
				e = EnemyShip(imgBullet, img, lista[0], lista[1], lista[2], lista[3], lista[4], groupAll_sprites, groupBullet)
				groupEnemy.add(e) # adiciona o inimigo ao grupo de inimigo correspondente
				groupAll_sprites.add(e) # adiciona o inimigo ao grupo que contêm todos os objetos do jogo


	###########################################
	# cria os meteoros do jogo
	def createMeteors(self, num, groupMeteor, all_sprites):

		for i in range(num):
			m = Meteor(array_meteors, random.randrange(WIDTH, WIDTH+800), random.randrange(HEIGHT_PANEL_PLAYER, HEIGHT))
			groupMeteor.add(m)
			all_sprites.add(m)


# inicia o jogo
if __name__ == '__main__':
	Game()
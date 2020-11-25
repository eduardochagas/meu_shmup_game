import pygame
from constantes import *
from playership import PlayerShip
from enemyship import EnemyShip




class Game:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITULO_DO_JOGO)
		self.clock = pygame.time.Clock()

		self.all_sprites = pygame.sprite.Group()
		self.bullet = pygame.sprite.Group()

		self.player1 = PlayerShip(width=30, height=40, posX=20, posY=int(HEIGHT)/2, velocity=5, group_All_Sprites=self.all_sprites, group_Bullet=self.bullet)
		self.all_sprites.add(self.player1)

		#####################################################################
		# cria os grupos dos primeiros inimigos
		# cria o grupo que armazena as balas dos inimigos do primeiro grupo
		#
		self.group_enemy1 = pygame.sprite.Group()
		self.bullet_enemy1 = pygame.sprite.Group() 
		#
		# cria a primeira onda inimiga 1
		self.createEnemies(listWave=wave1, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy1, groupEnemy=self.group_enemy1)



		# controla as ondas de ataque
		self.num_waves = 1
		self.running = True
		self.loop()

	
	def loop(self):

		while self.running:

			# limpa a tela do jogo a cada frame
			self.screen.fill(BLACK)
		
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
				hit = pygame.sprite.spritecollide(self.player1, self.group_enemy1, False)
				if hit:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit = pygame.sprite.spritecollide(self.player1, self.bullet_enemy1, True)
				if hit:
					pass

				#################################################################################
				# se não houver mais inimigos no grupo da primeira onda inimiga...
				if len(self.group_enemy1) == 0:
					self.num_waves = 2 # muda para a segunda onda inimiga
					self.group_enemy2 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy2 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					# cria a segunda onda inimiga: wave2
					self.createEnemies(listWave=wave2, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy2, groupEnemy=self.group_enemy2)


			#################################################################################
			# se a onda inimiga for a segunda onda...			
			if self.num_waves == 2:
				
				#################################################################################
				# chaca a colisão do player1 com OS INIMIGOS da primeira onda inimiga do jogo
				hit = pygame.sprite.spritecollide(self.player1, self.group_enemy2, False)
				if hit:
					pass

				#################################################################################
				# chaca a colisão do player1 com AS BALAS da primeira onda inimiga do jogo 
				hit = pygame.sprite.spritecollide(self.player1, self.bullet_enemy2, True)
				if hit:
					pass


				if len(self.group_enemy2) == 0:
					self.num_waves = 3
					self.group_enemy3 = pygame.sprite.Group() # cria o grupo da segunda onda inimiga..
					self.bullet_enemy3 = pygame.sprite.Group() # cria o grupo das balas da segunda onda inimiga
					# cria a segunda onda inimiga: wave2
					self.createEnemies(listWave=wave3, groupAll_sprites=self.all_sprites, groupBullet=self.bullet_enemy3, groupEnemy=self.group_enemy3)


			#################################################################################
			# define os frames do jogo
			self.clock.tick(FPS)

			#################################################################################
			# atualiza a tela do jogo
			pygame.display.update()


	def createEnemies(self, listWave, groupAll_sprites, groupBullet, groupEnemy):

		for lista in listWave:
			for item in range(len(lista)):
				print(item)
				e = EnemyShip(lista[0], lista[1], lista[2], lista[3], lista[4], groupAll_sprites, groupBullet)
				groupEnemy.add(e) # adiciona o inimigo ao grupo de inimigo correspondente
				groupAll_sprites.add(e) # adiciona o inimigo ao grupo que contêm todos os objetos do jogo






# inicia o jogo
if __name__ == '__main__':
	Game()
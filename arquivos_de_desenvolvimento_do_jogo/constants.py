import pygame
import os
import random


######################################################
# definindo o caminho até a pasta das imagens do jogo
#
path_img = os.path.join(os.path.dirname(__file__), 'img')
# path_img = os.path.join(os.path.dirname('/home/eduardo/meu_shmup_game/'), 'img')

img_ship = pygame.image.load(os.path.join(path_img, 'playerShip1_orange.png'))
img_initial_screen = pygame.transform.scale(img_ship, (30, 30))

img_laser_player = pygame.image.load(os.path.join(path_img, 'laserRed7.png'))
img_laser_player_initial_screen_rotate = pygame.transform.rotate(img_laser_player, 90)
img_laser_player_initial_screen = pygame.transform.scale(img_laser_player_initial_screen_rotate, (32, 8))

img_ship_enemy = pygame.image.load(os.path.join(path_img, 'enemyBlack3.png'))
img_ship_enemy_initial_screen = pygame.transform.scale(img_ship_enemy, (30, 30))

img_laser_enemy = pygame.image.load(os.path.join(path_img, 'laserBlue2.png'))
img_laser_enemy_initial_screen_rotate = pygame.transform.rotate(img_laser_enemy, 90)
img_laser_enemy_initial_screen = pygame.transform.scale(img_laser_enemy_initial_screen_rotate, (32, 8))

##############################################
# definindo o caminho até a imagem do player1
#
img_player1_orig = os.path.join(path_img, 'playerShip1_orange.png')
load_img_player1 = pygame.image.load(img_player1_orig) # carrega a imagem do player1 no pygame
img_player1 = pygame.transform.scale(load_img_player1, (40, 40)) # redimensiona o tamanho da imagem do player1

img_laser = os.path.join(path_img, 'laserRed7.png')
load_laser = pygame.image.load(img_laser)
img_laser_rotate = pygame.transform.rotate(load_laser, -90)
img_laser_player1 = pygame.transform.scale(img_laser_rotate, (37, 12))

img_life_player1 = pygame.image.load(img_player1_orig)
img_life_player1_scaled = pygame.transform.scale(img_life_player1, (30, 30))
img_life_player_mini = pygame.transform.rotate(img_life_player1_scaled, 90)

##############################################
# carregando as imagens do raio e do escudo
# (são as imagens dos poderes do player)
#
powers = {}

path_img_bolt = os.path.join(path_img, 'bolt_gold.png')
img_bolt = pygame.image.load(path_img_bolt)

path_img_blood = os.path.join(path_img, 'shield_gold.png')
img_blood = pygame.image.load(path_img_blood)

powers['gun'] = img_bolt
powers['blood'] = img_blood 



############################################################
# dicionário para armazenar os arrays que contem as imagens 
# dos lasers...
#
dict_lasers = {}

lasers_blue = []
lasers_green = []

for i in range(1, 16):

	img_laser = pygame.image.load(os.path.join(path_img, 'laserBlue'+str(i)+'.png'))
	img_rotate = pygame.transform.rotate(img_laser, 90)
	img_scaled = pygame.transform.scale(img_rotate, (37, 12))
	lasers_blue.append(img_scaled)

	img_laser = pygame.image.load(os.path.join(path_img, 'laserGreen'+str(i)+'.png'))
	img_rotate = pygame.transform.rotate(img_laser, 90)
	img_scaled = pygame.transform.scale(img_rotate, (37, 12))
	lasers_green.append(img_rotate)



dict_lasers['lasers_blue'] = lasers_blue
dict_lasers['lasers_green'] = lasers_green



############################################################
# dicionário para armazenar os arrays que contem as imagens 
# dos inimigos...
#
dict_enemies = {}

#################################################
# arrays que armazenam as imagens dos inimigos
#   OBS: esses arrays são armazenados no dicionário dict_enemies = {} 
#
enemies_black = []
enemies_blue = []
enemies_green = []
enemies_red = []

#################################################################
# faz o loop para armazenar as imagens dos inimigos 
# nos arrays: enemies_black = [], enemies_blue = [], enemies_green = [], enemies_red = []
#
for i in range(1,6):
	img_enemy = pygame.image.load(os.path.join(path_img, 'enemyBlack'+str(i)+'.png'))
	img_enemy_scaled = pygame.transform.scale(img_enemy, (40, 40))
	enemies_black.append(img_enemy_scaled)

	img_enemy = pygame.image.load(os.path.join(path_img, 'enemyBlue'+str(i)+'.png'))
	img_enemy_scaled = pygame.transform.scale(img_enemy, (40, 40))
	enemies_blue.append(img_enemy_scaled)

	img_enemy = pygame.image.load(os.path.join(path_img, 'enemyGreen'+str(i)+'.png'))
	img_enemy_scaled = pygame.transform.scale(img_enemy, (40, 40))
	enemies_green.append(img_enemy_scaled)	

	img_enemy = pygame.image.load(os.path.join(path_img, 'enemyRed'+str(i)+'.png'))
	img_enemy_scaled = pygame.transform.scale(img_enemy, (40, 40))
	enemies_red.append(img_enemy_scaled)

#################################################################
# adiciona os arrays com as imagens do inimigos 
# nas chaves: black, blue, green e red, do dicionário dict_enemies. 
#
dict_enemies['black'] = enemies_black
dict_enemies['blue'] = enemies_blue
dict_enemies['green'] = enemies_green
dict_enemies['red'] = enemies_red


#################################################################
# armazena os meteoros grandes... 
array_meteors = []
##################################
# armazena os meteoros minúsculos
array_tiny_meteors = []


for i in range(1,4):

	img_meteor = pygame.image.load(os.path.join(path_img, 'meteorBrown_big'+str(i)+'.png'))
	img_meteor_scaled = pygame.transform.scale(img_meteor, (80, 80))
	array_meteors.append(img_meteor_scaled) 


	img_meteor = pygame.image.load(os.path.join(path_img, 'meteorBrown_med'+str(i)+'.png'))
	img_meteor_scaled = pygame.transform.scale(img_meteor, (70, 70))
	array_meteors.append(img_meteor_scaled)


	img_meteor = pygame.image.load(os.path.join(path_img, 'meteorBrown_small'+str(i)+'.png'))
	img_meteor_scaled = pygame.transform.scale(img_meteor, (60, 60))
	array_meteors.append(img_meteor_scaled)

	############################################################
	# insere os meteoros minusculos ao array: array_tiny_meteors
	img_meteor = pygame.image.load(os.path.join(path_img, 'meteorBrown_tiny'+str(i)+'.png'))
	img_meteor_scaled = pygame.transform.scale(img_meteor, (20, 20))
	array_tiny_meteors.append(img_meteor_scaled)


###########################################
# imagens da esplosão
#

explosions = {}

explosions_normal = []
explosions_tiny = []

for i in range(0, 9):

	img_explosion = pygame.image.load(os.path.join(path_img, 'regularExplosion0'+str(i)+'.png'))
	img_explosion_scaled_normal = pygame.transform.scale(img_explosion, (40, 40))
	explosions_normal.append(img_explosion_scaled_normal)

	img_explosion_scaled_tiny = pygame.transform.scale(img_explosion, (20, 20))
	explosions_tiny.append(img_explosion_scaled_tiny)

explosions['normal'] = explosions_normal
explosions['tiny'] = explosions_tiny



######################################################
# definindo o caminho até a pasta de sons e musica do jogo
#
path_sound = os.path.join(os.path.dirname(__file__), 'sound')
# path_sound = os.path.join(os.path.dirname('/home/eduardo/meu_shmup_game/'), 'sound')


################################################
# inicia o módulo de sons e musica do pygame
pygame.mixer.init() 

###############################################################################
# define a quantidade de canais do nosso mixer (será USADO PAR OS SONS do jogo)
#
#  OBS: para vc entender melhor, quando utilizamos 
#  o método: pygame.mixer.set_num_channels(numero), internamente o pygame CRIA 
#  UM MIXER (igual a um mixer de produção musical), com vários canais, onde cada
#  canal podemos inserir um tipo do som diferente. A quantidade de canais padrão
#  de um mixer é: 8
#
#  OBS2: lembre-se que, som é diferente de música. Som SÃO OS BARULHOS que acontecem
#  DURANTE O JOGO, como por exemplo: um som de explosão, um som de tiro, um som executado  
#  quando pegamos um powerup, etc... 
#  
#  MÚSICA, por exemplo, é a musica que toca durante o jogo.
# 
#  como mostra a linha abaixo, criamos um mixer com somente 8 canais (é a quantidade padrão)...
#
pygame.mixer.set_num_channels(8)
#####################################
# define os canais que queremos reservar no mixer do pygame para inserir
# os sons do jogo...
#
#  OBS: os NÚMERO ARMAZENADO NOS PARÊNTESES do método: pygame.mixer.set_reserved(num),
#  representam A NÚMERAÇÃO DE UM CANAL do mixer criado com o método: pygame.mixer.set_num_channels(num)
#
#  minha_dúvida: sinseramente eu não sei como funcionaria o código se reservassemos aguns canais do mixer e 
#  para usar e outros não. Na dúvida, eu crio os canais que eu preciso, reservo todos eles, e utilizo
#  cada um deles para cada um dos sons que eu preciso, exatamente como fizemos nesse código.
#
pygame.mixer.set_reserved(0)
pygame.mixer.set_reserved(1)
pygame.mixer.set_reserved(2)
pygame.mixer.set_reserved(3)
pygame.mixer.set_reserved(4)
pygame.mixer.set_reserved(5)
pygame.mixer.set_reserved(6)
pygame.mixer.set_reserved(7)
#
# depois que reservamos os canais, temos que INSERIR O NÚMERO do canal reservado, 
# DENTRO DOS PARÊNTESES da classe: pygame.mixer.Channel(), e em seguida, CHAMAR 
# O MÉTODO play() e INSERIR O SOM que queremos atribuir, DENTRO 
# DOS PARÊNTESES do metodo play(), assim: 
#
#  pygame.mixer.Channel(0).play(sound_shoot)
#
# OBS: lembrando que, o nome do arquivo de som do nosso jogo tem que ser INSERIDO 
# DENTRO DOS PARÊNTESES de uma classe: pygame.mixer.Sound(), para aí sim poder ser
# inserido dentro dos parênteses do método play() da classe: pygame.mixer.Channel()
#



####################################################
# define o caminho do sistema até a pasta: sound
sound = os.path.join(os.path.dirname(__file__),'sound')
# sound = os.path.join(os.path.dirname('/home/eduardo/meu_shmup_game/'),'sound')

##############################################
# som do tiro do nosso player1
sound_shoot_player1 = os.path.join(sound, 'pew.wav')
sound_shoot = pygame.mixer.Sound(sound_shoot_player1)

##############################################
# som da explosão do nosso player1
sound_expl_player1 = os.path.join(sound, 'expl_player.wav')
sound_explosion_player1 = pygame.mixer.Sound(sound_expl_player1)


##################################################################################
# Sons de tiro dos inimigos...
##############################################
# som do tiro do(s) nosso(s) inimigos...
sound_shoot_enemies = os.path.join(sound, 'pew2.wav')
sound_shoot_enemy = pygame.mixer.Sound(sound_shoot_enemies)
sound_shoot_enemy.set_volume(0.1) # configura a altura do volume do som...

####################################
# som da explosão dos inimigos
sound_expl_enemies = os.path.join(sound, 'expl6.wav')
sound_explosion_enemies = pygame.mixer.Sound(sound_expl_enemies)


###########################################
# som do item de tiro que sai do meteoro
sound_expl_meteor = os.path.join(sound, 'expl3.wav')
sound_explosion_meteor = pygame.mixer.Sound(sound_expl_meteor)
# sound_item_shoot.set_volume(0.1)

##############################################
# som do tiro do(s) nosso(s) inimigos...
sound_expl_tiny = os.path.join(sound, 'expl_tiny.wav')
sound_explosion_tiny = pygame.mixer.Sound(sound_expl_tiny)



###########################################
# som do item de tiro que sai do meteoro
sound_item_1 = os.path.join(sound, 'pow4.wav')
sound_item_shoot = pygame.mixer.Sound(sound_item_1)
################################################################
# som do item de sangue (figura do escudo) que sai do meteoro...
sound_item_2 = os.path.join(sound, 'pow5.wav')
sound_item_blood = pygame.mixer.Sound(sound_item_2)
# sound_item_blood.set_volume(0.1)

# sound_game = os.path.join(sound,'tgfcoder-FrozenJam-SeamlessLoop.ogg')
# sound_game_principal = pygame.mixer.music.load(sound_game)
 


#CONSTANTES

# Cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (154, 172, 168)
GREY_DARK = (66, 64, 64)
WHITE = (216, 227, 240)
BLUE_TURKEY = (54, 255, 208)


#LARGURA E ALTURA DA TELA
WIDTH = 900
HEIGHT = 500
TITULO_DO_JOGO = "Shmup Game"
FPS = 50

# PAUSED_GAME = False

# ALTURA TAMANHO PAINEL DO PLAYER
HEIGHT_PANEL_PLAYER = 120
HEIGHT_SCREEN = HEIGHT_PANEL_PLAYER + HEIGHT

# tempo em que o poder do powerup do tiro duplo ficará ativo
TIME_POWERUP = 3000

#ONDA DE ATAQUE INIMIGA
WIDTH_ENEMIES = 20
HEIGTH_ENEMIES = 30
VELOCITY_ENEMIES = 2

################################################################################
# será a primeira onda inimiga
wave1 = [ 
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+60), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+340), VELOCITY_ENEMIES]
		]

################################################################################
# será a segunda onda inimiga
wave2 = [
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_SCREEN*30)/100, VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*45)/100, VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_SCREEN*60)/100, VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*80)/100, VELOCITY_ENEMIES],
		]

# wave1 = [[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*45)/100, VELOCITY_ENEMIES]]

################################################################################
# será a terceira onda inimiga
wave3 = [
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+115), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+175), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+275), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+325), VELOCITY_ENEMIES],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+405), VELOCITY_ENEMIES]
		]


wave4 = [
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+120), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+300), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+390), VELOCITY_ENEMIES],
		  
		  
		]

wave5 =[
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+120), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+300), VELOCITY_ENEMIES],
		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+390), VELOCITY_ENEMIES],

	]

wave6 = [
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+120), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+190), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+270), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+330), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+410), VELOCITY_ENEMIES],
 		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+410), VELOCITY_ENEMIES],

      ]

wave7 = [
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+220), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+180), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+260), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+410), VELOCITY_ENEMIES],

		]

wave8 = [
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+30), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+220), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+180), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+220), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+260), VELOCITY_ENEMIES],
  		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+400), VELOCITY_ENEMIES],

		]

wave9 = [
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+40), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+130), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+220), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+310), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+400), VELOCITY_ENEMIES],

]

wave10 = [
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+40), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+130), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+220), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_PANEL_PLAYER+310), VELOCITY_ENEMIES],
   		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+400), VELOCITY_ENEMIES],

]

wave11 = [
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+40), VELOCITY_ENEMIES],
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+110), VELOCITY_ENEMIES],
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+550, (HEIGHT_PANEL_PLAYER+210), VELOCITY_ENEMIES],
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+310), VELOCITY_ENEMIES],
    		  [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+400), VELOCITY_ENEMIES],

		]

wave12 = [

   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+50), VELOCITY_ENEMIES],
   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+120), VELOCITY_ENEMIES],
   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+650, (HEIGHT_PANEL_PLAYER+190), VELOCITY_ENEMIES],
   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_PANEL_PLAYER+360), VELOCITY_ENEMIES],
   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+650, (HEIGHT_PANEL_PLAYER+270), VELOCITY_ENEMIES],
   		    [WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT_PANEL_PLAYER+400), VELOCITY_ENEMIES],
]


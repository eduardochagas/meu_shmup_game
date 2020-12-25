import pygame
import os

######################################################
# definindo o caminho até a pasta das imagens do jogo
#
path_img = os.path.join(os.path.dirname(__file__), 'img')

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
lasers_red = []

for i in range(1, 16):

	img_laser = pygame.image.load(os.path.join(path_img, 'laserBlue'+str(i)+'.png'))
	img_rotate = pygame.transform.rotate(img_laser, 90)
	img_scaled = pygame.transform.scale(img_rotate, (37, 12))
	lasers_blue.append(img_scaled)

	img_laser = pygame.image.load(os.path.join(path_img, 'laserRed'+str(i)+'.png'))
	img_rotate = pygame.transform.rotate(img_laser, 90)
	lasers_red.append(img_rotate)



dict_lasers['lasers_blue'] = lasers_blue
dict_lasers['lasers_red'] = lasers_red



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
for i in range(1,5):
	img_enemy = pygame.image.load(os.path.join(path_img, 'enemyBlack'+str(i)+'.png'))
	img_enemy_scaled = pygame.transform.scale(img_enemy, (40, 40))
	enemies_red.append(img_enemy_scaled)

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
# wave2 = [
# 			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_SCREEN*30)/100, VELOCITY_ENEMIES],
# 			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*45)/100, VELOCITY_ENEMIES],
# 			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT_SCREEN*60)/100, VELOCITY_ENEMIES],
# 			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*80)/100, VELOCITY_ENEMIES],
# 		]

wave2 = [[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT_SCREEN*45)/100, VELOCITY_ENEMIES]]

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





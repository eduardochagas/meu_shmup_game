

#CONSTANTES

# Cores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


#LARGURA E ALTURA DA TELA
WIDTH = 800
HEIGHT = 500
TITULO_DO_JOGO = "Shmup Game"
FPS = 50

#ONDA DE ATAQUE INIMIGA
WIDTH_ENEMIES = 20
HEIGTH_ENEMIES = 30

################################################################################
# será a primeira onda inimiga
wave1 = [ 
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*30)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT*45)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*60)/100, 3]
		]

################################################################################
# será a segunda onda inimiga
wave2 = [
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*30)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+450, (HEIGHT*45)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*60)/100, 3]
		]

################################################################################
# será a terceira onda inimiga
wave3 = [
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT*10)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT*25)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*40)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+350, (HEIGHT*55)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT*70)/100, 3],
			[WIDTH_ENEMIES, HEIGTH_ENEMIES, WIDTH+250, (HEIGHT*85)/100, 3]
		]





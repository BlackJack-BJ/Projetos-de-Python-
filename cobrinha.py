import pygame
from pygame.locals import *

comp = 100
larg = 100

pygame.init() #incia o pygame
janela = pygame.display.set_mode((comp, larg)) #cria a janela

while True:
	janela.fill((68, 189, 50)) #define as cores (usa codigos numericos)
	
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			quit()
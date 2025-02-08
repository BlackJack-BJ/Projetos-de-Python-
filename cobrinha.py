import pygame #só para não deixar vazio
from pygame.locals import * #biblioteca com todos os eventos

#CONSTANTES:
COMP = 600 #x
LARG = 600 #y
POS_INICIAL_X = COMP / 2 #para começar...
POS_INICIAL_Y = LARG / 2 #...no meio
BLOCK = 10 #numero de pixels

pygame.init() #incia o pygame
janela = pygame.display.set_mode((COMP, LARG)) #cria a janela

#Variáveis relacionadas à cobra:
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)] #posiçoes iniciais da cobra
cobra_surface = pygame.Surface((BLOCK, BLOCK)) #cria a superficie da cobra
cobra_surface.fill((53, 59, 72)) #para colorir a cobra
direcao = K_LEFT #só para declarar a variável


while True:
	pygame.time.Clock().tick(10) #taxa de atualizacao do frame (da tela) | com numeros mais altos, fica mais rapido
	janela.fill((68, 189, 50)) #define as cores (usa codigos numericos)
	
	for evento in pygame.event.get(): #loop para receber os eventos que acontecem no jogo
		if evento.type == QUIT: #caso o clique seja no "x" vermelho:
			pygame.quit() #sai
			quit()
		
		elif evento.type == KEYDOWN: #caso seja uma chave clicada
			if evento.key in [K_RIGHT, K_LEFT, K_UP, K_DOWN]:
				direcao = evento.key
			
	
	for pos in cobra_pos:
		janela.blit(cobra_surface, pos) #para desenhar algo na tela
	'''
{
	O plano cartesiano aqui funciona assim:
	{
		P(0,0) - canto superior esquerdo, então:
		{
			•para direita: aumenta o X
			•para a esquerda: diminui o X
			•para cima: aumenta o Y
			•para baixo: diminui o Y
		}
	}
}
	'''
	#tentei match-case, não funciona :(
	if direcao == K_RIGHT:
		cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] #Movimenta para a direita # sao 2 elementos por causa da funcao da linha 27
	elif direcao == K_LEFT:
		cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] #Movimenta para a esquerda
	elif direcao == K_UP:
		cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK #Movimenta para a cima
	elif direcao == K_DOWN:
		cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK #Movimenta para a baixo
		
	pygame.display.update() #para atualizar a tela
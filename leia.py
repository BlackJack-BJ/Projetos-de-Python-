def leiaInt(txt):
	while True:
		try:
			n = int(input(txt))
			return n
		except ValueError:
			print('\033[1;31mERRO! Digite um número Inteiro Válido.\033[m')
			
		
def leiaFloat(txt):
	while True:
		try :
			n = float(input(txt))
			return n 
		except ValueError:
			print('\033[1;31mERRO! Digite um número Real Válido.\033[m')
			

def cores():
	vm = '\033[1;31m' #Vermelho
	vd = '\033[1;32m' #Verde
	am = '\033[1;33m' #Amarelo
	az = '\033[1;34m' #Azul
	rx = '\033[1;35m' #Roxo
	ci = '\033[1;36m' #Ciano
	cz = '\033[1;37m' #Cinzento
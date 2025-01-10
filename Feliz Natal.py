from random import randint
from time import sleep


def arv():
	arvore =('                               *\n'
'                             * * *\n' 
'                            * * * *\n'
'                           * * * * *\n'
'                             _| |_')
	print(arvore)

arv()

f1 = '\033[1;31mFeliz Natal\033[m'
f2 = '\033[1;32mFeliz Natal\033[m'
f3 = '\033[1;33mFeliz Natal\033[m'
f4 = '\033[1;34mFeliz Natal\033[m'

lista = [f1, f2, f3, f4]

print()
while True:
	escolha = randint(0,3)
	print(f"   {lista[escolha]:^67}")
	sleep(0.5)	

		
'''Uma versão que estou analisando...
from random import randint
from time import sleep


def arv():
    arvore = ('                               *\n'
              '                             * * *\n'
              '                            * * * *\n'
              '                           * * * * *\n'
              '                             _| |_')
    print(arvore)


f1 = '\033[1;31mFeliz Natal\033[m'
f2 = '\033[1;32mFeliz Natal\033[m'
f3 = '\033[1;33mFeliz Natal\033[m'
f4 = '\033[1;34mFeliz Natal\033[m'

lista = [f1, f2, f3, f4]

while True:
    print("\033[H\033[J", end="")  # Limpa a tela
    arv()  # Reexibe a árvore
    escolha = randint(0, 3)
    print(f"   {lista[escolha]:^67}")  # Exibe a mensagem
    sleep(0.5)
'''
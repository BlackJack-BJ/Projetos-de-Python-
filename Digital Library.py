print(f"{'Digital Library':-^67}")
contador = -1
dict = {}
lib = []


def menu():
	print('''Menu:
1 - Remover Item
2 - Editar Item
3 - Listar Biblioteca
4 - Filtro de busca
5 - Adicionar outro artigo''')


def remo():
	remover = int(input('Número do artigo que deseja remover: '))
	if 0 <= remover < len(lib):
		del lib[remover]
		print('Item removido com sucesso!')
	else:
		print('Erro. Item não encontrado')
			

def edit():
	editar = int(input('Número do artigo que deseja editar: '))
	print(f"\nNovos dados do livro/revista nº {editar}")
	for chave in dict.keys():
		dict[chave] = input("Novo {lista[editar][chave]}: ")
			

def dados():
	dict.clear()
	print('\nDados do livro/revista')
	dict['titulo'] = input('\n \nTítulo: ').strip().title()
				
	dict['autor'] = input('\nAutor: ').strip().capitalize()
		
	dict['ano'] = int(input('\nAno de publicação: '))
				
	dict['genero'] = input('\nGênero: ').strip().capitalize()
				
	dict['status'] = input('\nStatus de leitura [ Lido (S) / Não lido (N) ]: ').strip().upper()
	
	
	while dict['status'] not in 'SN':
		dict['status'] = input('Erro. Digite [S/N]: ').strip().upper()[0]
	print(f"\nArtigo nº {contador} registado com sucesso")


def listar():
	print()
	for artigo in lib:
#		print(f"{artigo}")
#		for artigo in dict.keys():
#			print(f"{artigo}: ", end='')
#		for artigo in dict.values():
#			print(artigo)
		print()


def buscar():
	gen = input('Que gênero quer buscar?: ')
	for artigo in lib:
		for key, value in dict.items():
			if key == 'genero' and value == 'gen':
				print(f"{key}: {value}")
				
				
while True:
	continuar = ''
	while continuar != 'n':
		contador += 1
		dados()
		
		#Continuar ?
		continuar = input('\nQuer registar outro artigo? [S/N]: ').strip().lower()[0]
		
		while continuar not in 'sn':
			continiar = input('Erro. Digite [S/N]: ').strip().lower()[0]
		print('\n' + '-'*67 + '\n')
		lib.append(dict.copy())
	menu()
	while True:
		opcao = int(input('\nOpção: '))
		if opcao == 1:
			remo()
		elif opcao == 2:
			edit()
		elif opcao == 3:
			listar()
		elif opcao == 4:
			buscar()
		elif opcao == 5:
			dados()
		else:
			print('Número inválido. Tente novamente.')
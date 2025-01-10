'''exp = input('Expressão: ')
sol = eval(exp)
print(f"{exp} = {sol}")''' #Modo batota

from leia import *

f = '\033[m' #Fim
vm = '\033[1;31m' #Vermelho
vd = '\033[1;32m' #Verde
am = '\033[1;33m' #Amarelo
az = '\033[1;34m' #Azul
rx = '\033[1;35m' #Roxo
ci = '\033[1;36m' #Ciano
cz = '\033[1;37m' #Cinzento


def soma(a, b):
	return a + b


def subt(a, b):
	return a - b


def mult(a, b):
	return a * b

		
def divi(a ,b):	
	try:
		resul = a / b
	except:
		print("Impossível dividir, o divisor é igual a 0")
	else:
		return resul


def linha1():
	print('\n' + '-'*67 + '\n')

		
def linha2():
	print('\n' + '='*67 + '\n')

		
def menu():
	print(f'''
{am}1{f} - {az}Adição {f}
{am}2{f} - {az}Subtração {f}
{am}3{f} - {az}Multiplicação {f}
{am}4{f} - {az}Divisão {f}
{am}5{f} - {az}Sair{f}''')
	linha1()


while True:
	n1 = leiaInt('Digite o 1º número: ')
	n2 = leiaInt('Digite o 2º número: ')
	
	menu()
	opc = leiaInt('Sua opção: ')
	match opc:
		case 1:
			print(f"\n{n1} + {n2} = {soma(n1, n2)}")
		case 2:
			print(f"\n{n1} - {n2} = {subt(n1, n2)}")
		case 3:
			print(f"\n{n1} x {n2} = {mult(n1, n2)}")
		case 4:
			print(f"\n{n1} / {n2} = {divi(n1, n2)}")
		case 5:
			break
		case _:
			print(f"{vm}Opção Inválida, tente novamente!{f}")
			opc = leiaInt('\nSua opção: ')
	linha2()
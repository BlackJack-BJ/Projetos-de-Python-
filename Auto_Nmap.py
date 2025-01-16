from os import system as sys
from InquirerPy import inquirer

ip_base = '192.168.18'
opcao = inquirer.select(
    message = 'Sua opção:',
    choices = ['IP Privado', 'IP Público', 'Testar manualmente']
).execute()

match opcao:
    case 'IP Privado':
        inicio = int(input('Digite o início: '))
        fim = int(input('Digite o fim: '))

        for c in range (inicio, fim + 1):
            sys(f'nmap {ip_base}.{c}')

    case 'IP Público':
        ip = input('Digite o IP: ')
        sys(f'nmap {ip}')
    
    case _:
        inicio = int(input('Digite o início: '))
        fim = int(input('Digite o fim: '))
        
        print('nmap', end = ' ')
        for c in range (inicio, fim + 1):
           print(f'{ip_base}.{c}', end = ' ')
sys('')

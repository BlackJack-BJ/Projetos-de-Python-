from InquirerPy import inquirer
#Expansão ds Domínio: VOID!
def criptografar():
    lista_criptografar = []
    try:
        texto = input('Digite o texto a criptografar: ')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar nada :(')

    for carater in texto:
        txt = ord(carater)
        lista_criptografar.append(txt)
    print(f'"{texto}" criptografado: \033[1;31m', end = '')

    for pos, item in enumerate(lista_criptografar):
        if pos < len(lista_criptografar) - 1:
            print(item, end = ' ')
        else:
            print(item)
    print('\033[m')
        

def descriptografar():
    lista_descriptografar = []
    try:
        texto = input('Digite o texto a descriptografar: ')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar nada :(')
    '''
#    texto.replace('-', ' ')
#    texto.split()
    '''
    for conjunto in texto.split():
        lista_descriptografar.append(conjunto)
    
    print(f'"{texto}" descriptografado: \033[1;32m', end = '')

    for numero in lista_descriptografar:
        numero_convertido = int(numero)
        print(chr(numero_convertido), end = '')
    print('\033[m\n')


while True:
    try:
        opcao = inquirer.select(
            message = 'Sua opção:',
            choices = ['🔐 Criptografar', '🔓 Descriptografar', '🚪 Sair']
        ).execute()

    except KeyboardInterrupt:
        print('O usuário preferiu não selecionar nada :(\n')
        continue

    if opcao == '🔐 Criptografar':
        criptografar()
    elif opcao == '🔓 Descriptografar':
        descriptografar()
    else:
        print()
        print('---------------------'.center(55))
        print('||Tenha um bom dia!||'.center(55))
        print('---------------------'.center(55))
        break

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
    print(f'"{texto}" criptografado: ', end = '')

    for pos, item in enumerate(lista_criptografar):
        if pos < len(lista_criptografar) - 1:
            print(item, end = '-')
        else:
            print(item)
        

def descriptografar():
    lista_descriptografar = []
    try:
        texto = input('Digite o texto a descriptografar: ')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar nada :('     )
    
    texto.replace('-', ' ')
    texto.split()
    
    print(f'"{texto}" descriptografado: ', end = '')

    for string in lista_descriptografar:
        chr(int(string))
        print(chr, end = '')

while True:
    opcao = inquirer.select(
        message = 'Sua opção:',                     
        choices = ['🔐 Criptografar', '🔓 Descriptografar', '🚪 Sair']
    ).execute()

    if opcao == '🔐 Criptografar':
        criptografar()
    elif opcao == '🔓 Descriptografar':
        descriptografar()
    else:
        print('\n'+'||Tenha um bom dia!||'.center(55))
        break
    print('\n')

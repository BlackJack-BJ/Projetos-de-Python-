from InquirerPy import inquirer

def menu():
    global opcao
    opcao = inquirer.select(
        message = 'Sua opção:',
        choices = ['Registar livro', 'Registar pessoa', 'Pegar livro emprestado', 'Devolver livro emprestado', 'Sair'], 
    ).execute()


def registar_livro():
    livro = input('Digite o título do livro: ')
    with open ('Livros.txt', 'a') as arquivo:
        arquivo.write(f"• {livro}\n")


def registar_pessoa():
    pessoa = input('Digite o nome da pessoa: ')
    with open ('Pessoas.txt', 'a') as arquivo:
        arquivo.write(f"{pessoa}\n")


def pegar_livro_emprestado():
    nome_livro = input('Degite o nome do livro: ')
    with open ('Livros.txt', 'r') as arquivo:
        for linha in arquivo:
            for char in linha:
                if char == '•':
                    print('Este livro não está disponível para empréstimo')
                else:
                    if nome_livro in linha:
                        print(f"\033[32;1mVocê pegou o livro {nome_livro} emprestado\033[m")
                    else:
                        print(f"\033[1;31mLivro {nome_livro} não encontrado :(\033[m")


def devolver_livro_emprestado():
    nome_livro = input('Digite o nome do livro: ')
    with open ('Livros.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        for linha in conteudo:
            if nome_livro in linha:
                for char in linha:
                    if char == '*':
                        print('Livro devolvido!')
                        conteudo = '•'
                        with open ('Livros.txt', 'w') as arquivo:
                            arquivo.write(conteudo)
                    else:
                        print('Este livro não foi emprestado')
            else:
                print(f"\033[1;31mLivro {nome_livro} não encontrado :(\033[m")


    nome_livro = input('Digite o nome do livro: ')
while True:
    try:
        menu()
    except KeyboardInterrupt:
        print('Aqui só se sai Da forma certa')

    match opcao:
        case 'Registar livro':
            registar_livro()
        
        case 'Registar pessoa':
            registar_pessoa()

        case 'Pegar livro emprestado':
            pegar_livro_emprestado()

        case 'Devolver livro emprestado':
            devolver_livro_emprestado()

        case _:
            break


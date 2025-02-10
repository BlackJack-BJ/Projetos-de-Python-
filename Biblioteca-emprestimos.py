from InquirerPy import inquirer

def menu() -> str:
    try:
        opcao = inquirer.select(
            message = 'Sua opção:',
            choices = ['Registar livro', 'Registar pessoa', 'Pegar livro emprestado', 'Devolver livro emprestado', 'Sair'], 
        ).execute()

    except KeyboardInterrupt:
        print ('Aqui só se sai da forma certa')
    return opcao


def registar_livro() -> None:
    livro: str = input('Digite o título do livro: ').capitalize()
    with open ('Livros.txt', 'a') as arquivo:
        arquivo.write(f"0 {livro}\n")


def registar_pessoa() -> None:
    pessoa: str = input ('Digite o nome da pessoa: ')
    with open ('Pessoas.txt', 'a') as arquivo:
        arquivo.write(f"{pessoa}\n")


def pegar_livro_emprestado() -> None:
    nome_livro: str = input ('Digite o nome do livro: ')
    with open ('Livros.txt', "a+") as arquivo:
        conteudo: list = arquivo.readlines()

        for pos, linha in enumerate (conteudo):
            if nome_livro.lower() in linha.lower():
                linha_var: str = linha
                #0 - False: Não emprestado
                #1 - True: Emprestado
                if linha_var[0] == 1:
                    print ('Este livro não está disponível para empréstimo')

                else:
                    linha_var.replace('1', '0')
                    conteudo[pos] = linha_var
                    print (f"\033[32;1mVocê pegou o livro {nome_livro} emprestado\033[m")
                    for item in conteudo:
                        arquivo.write(item)
            else:
                print (f"\033[1;31mLivro \"{nome_livro}\" não encontrado :(\033[m")


def devolver_livro_emprestado() -> None:
    nome_livro: str = input ('Digite o nome do livro: ')
    with open ('Livros.txt', "a+") as arquivo:
        conteudo: list = arquivo.readlines()

        for pos, linha in enumerate (conteudo):
            if nome_livro.lower() in linha.lower():
                linha_var: str = linha
                #0 - False: Não emprestado                                                  #1 - True: Emprestado
                if linha_var[0] == 0:
                    linha_var.replace('0', '1')
                    conteudo.replace(linha, linha_var)
                    print ('Livro devolvido!')
                    arquivo.write(conteudo)

                else:
                    print ('Este livro não foi emprestado')
            else:
                print (f"\033[1;31mLivro \"{nome_livro}\" não encontrado :(\033[m")


#    nome_livro = input('Digite o nome do livro: ')
while True:
    opcao = menu()
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



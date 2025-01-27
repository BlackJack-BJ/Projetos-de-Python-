import socket

try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#except socket.error:
#    print('Erro na criação do socket')

except Exception as error:
    print(f"Erro: \033[1;31m{error}\033[m")
    exit()

IP = '' #Local 127.0.0.1
porta = 9999

tcp_socket.bind((IP, porta)) #começa a escutar
tcp_socket.listen(1) #nº de vezes que vai escutar

while True:
    conexao, endereco = tcp_socket.accept()
    print(f"Conexão de {endereco[0]}:{endereco[1]}")
    print('\n')
    conexao.close()

tcp_socket.close() #fecha o servidor

import os
from cryptography.fernet import Fernet

arquivos = []
caminho = '/data/data/com.termux/files/home/Python_No_Termux/ransomware/chave.key'

key = Fernet.generate_key()
with open (caminho, 'rb') as chave:
    secret_key = chave.read()

#Colocando os arquivos na lista
for arquivo in os.listdir():
    if arquivo == 'encrypt.py' or arquivo == 'chave.key' or arquivo == 'decrypt.py':
        continue #que lindo :P

    if os.path.isfile(arquivo):
        arquivos.append(arquivo)

for arquivo in arquivos:
    with open (arquivo, 'rb') as file:
        conteudo = file.read()
    conteudo_desencriptado = Fernet(secret_key).decrypt(conteudo)
    with open (arquivo, 'wb') as file:
        file.write(conteudo_desencriptado)

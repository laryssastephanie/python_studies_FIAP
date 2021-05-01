from socket import *
servidor = "127.0.0.1"
porta = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)  # parametros: DNS/IP e protocolo TCP
obj_socket.bind((servidor, porta))
obj_socket.listen(2)  # definindo número máximo de clientes
print("Aguardando Cliente.....")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", str(msg_recebida)[2:-1])
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')  # todos os dados transmitidos via socket devem estar no formato byte. Não envia nem recebe dados strings, por exemplo.
        con.send(msg_enviada)
        break
    con.close()

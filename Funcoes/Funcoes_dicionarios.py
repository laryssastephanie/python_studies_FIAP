def perguntar():
    return input("O que deseja realizar?\n" +
            "<I> - Para inserir um usuário\n" +
            "<P> - Para pesquisar um usuário\n" +
            "<E> - Para excluir um usuário\n" +
            "<L> - Para listar um usuário: ").upper()
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)
def pesquisar(dicionario, chave):
    lista = dicionario.get(chave.upper())
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir (dicionario, chave):
    if dicionario.get(chave.upper()) != None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto........")
        print("Login: ", chave)
        print("Dados: ", valor)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
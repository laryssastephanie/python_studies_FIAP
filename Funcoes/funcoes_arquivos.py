def chamarMenu():
    escolha = int(input("Digite: \n" +
                        "<1> para registrar ativo\n" +
                        "<2> para persistir em arquivo\n" +
                        "<3> para exibir ativos armazenados: "))
    return escolha

def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + " ")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas
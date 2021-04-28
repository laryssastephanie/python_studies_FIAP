from Funcoes.funcoes_arquivos import *
inventario = {}
opcao = chamarMenu()
while 0 < opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        print(exibir())
        resultado = exibir()
        for linha in resultado:
            lista = linha.split(";")
            print("Data...........: ", lista[1])
            print("Descrição......: ", lista[2])
            print("Departamento...: ", lista[3])
    opcao = chamarMenu()

# Código acima está bem mais limpo do que o descrito abaixo, devido ao uso das funções.
# inventario = {}
# opcao = int(input("Digite: "
#                   "<1> para registrar ativo"
#                   "<2> para persistir em arquivo"
#                   "<3> para exibir ativos armazenados: "))
# while 0 < opcao < 4:
#     if opcao == 1:
#         resp = "S"
#         while resp == "S":
#             inventario[input("Digite o número patrimonual: ")] = [
#                 input("Digite a data da última atualização: "),
#                 input("Digite a descrição: "),
#                 input("Digite o departamento: ")]
#             resp = (input("Digite <S> para continuar: ").upper())
#     elif opcao == 2:
#         with open("inventario.csv", "a") as inv:
#             for chave, valor in inventario.items():
#                 inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "")
#                 print("Persistido com sucesso!")
#     elif opcao == 3:
#             with open("inventario.csv", "r") as inv:
#                 print(inv.readlines())
#     opcao = int(input("Digite:"
#                       "<1> para registrar ativo"
#                       "<2> para persistir em arquivo"
#                       "<3> para exibir ativos armazenados: "))


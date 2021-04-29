# Código extenso, sem módulos.
# Ver arquivo Manipular_JSON_com_funcoes

import json
import os
if os.path.exists("inventario_json.json"):
    with open("inventario_json.json", "r") as arq_json:
        inventario = json.load(arq_json)
else:
    inventario = {}
opcao = int(input("Digite: \n"
                  "<1> para registrar ativo\n"
                  "<2> para exibir ativos armazenados: "))
while 0 < opcao < 3:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")
            ]
            resp = input("Digite <S> para continuar.").upper()
        with open("inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json)
        print("JSON gerado!!!")
    elif opcao == 2:
        for chave, dado in inventario.items():
            print("Data...........: ", dado[0])
            print("Descrição......: ", dado[1])
            print("Departamento...: ", dado[2])
    opcao = int(input("Digite: \n"
                      "<1> para registrar ativo\n"
                      "<2> para exibir ativos armazenados:"))

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamentos: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento....: ", (indice+1))
    print("Nome...........:", equipamentos[indice])
    print("Valor..........:", valores[indice])
    print("Serial.........:", seriais[indice])
    print("Departamento...:", departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamento)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])

serial = int(input("Digite o serial do equipamento que será excluído: "))
for indice in range(0, len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break #quando encontrar o item desejado, irá executar e sair do laço

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
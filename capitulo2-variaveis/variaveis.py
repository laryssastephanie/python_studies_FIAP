# nome = "Humberto Delgado"
# empresa = 'FIAP'
# qtde_funcionarios = 500 #int
# mediaMensalidade = 856.50 #float
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionarios: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A media da mensalidade é de: " + str(mediaMensalidade))
print("==========Verifique os tipos de dados abaixo:==========")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))



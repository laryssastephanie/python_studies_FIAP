nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper() #função upper para converter as letras para caixa alta
if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para a sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM": #dois sinais de 'igual' é para comparação. Um sinal é para atribuição.
    print("O paciente será direcionado para a sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para a sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para a sala BRANCA - SEM prioridade")
else: #só será executado se for digitado algo diferente de sim ou não
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

#Utilizamos menos variáveis do que na Decisão Simples
#Variáveis ocupam espaço em memória, então utilizamos menos espaço
#Não seria uma boa prática utilizar dois if's, um para cada condição. O mais correto é o 'else'.
#Não substituir uma decisão composta por duas ou mais simples. NUNCA.


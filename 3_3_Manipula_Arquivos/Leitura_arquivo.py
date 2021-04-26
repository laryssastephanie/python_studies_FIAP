with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines() # read() - retorna string por padrão / readlines() - retorna lista
print("Tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo: ", conteudo)

with open("teste.txt", "w") as arquivo: # with abre o arquivo, executa e fecha, sem precisar dar o close()
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open ("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")

# o W cria um novo arquivo e se utilizado duas vezes, ele sobrescreve o anterior.
# para poder adicionar novas linhas, sem sobrescrever, utiliza-se o A

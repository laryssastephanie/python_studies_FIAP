from Capitulo3_Funcoes.identificacao_de_funcoes import *

minhaLista = []
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))  # chamada dentro do print, pois possui return
exibirInventario(minhaLista)

print("Resumindo")
resumirvalores(minhaLista)

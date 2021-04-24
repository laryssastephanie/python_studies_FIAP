usuarios = {}
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))
print(tupla)

for chave in range (0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome"), input("Digite o nível")]

print(tupla)
for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])
import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "LARY" and senha == "102030":
    print("Usuário Logado")
else:
    print("Login Negado")

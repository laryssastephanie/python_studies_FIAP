usuarios = {}
usuarios = {
    "Chaves": ["Chaves Silva", "17/06/2017", "Recep_01"],
    "Quico": ["Enrico Flore", "03/06/2017", "Raiox_02"]
    }

print(usuarios)

usuarios["Florinda"] = ["Dona Florinda", "24/12/2017", "Riox_01"]

print(usuarios)

print("##########========##########")
print("Dados: ", usuarios.get("Chaves"))

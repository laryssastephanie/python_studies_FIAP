from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco = input("Digite um endereço com número e cidade\n"
                 "Exemplo: Avenida Paulista, 100 São Paulo: ")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Região............: ", resultado[2])
    print("Cidade............: ", resultado[3])
print("Conoce mi ciudad")

name_city = input("¿Cuál es mi ciudad favorita, Caracas, Marcay o Sao Paulo? ")

def favorite_city(name_city):
    if (name_city == "Maracay"):
        print("Casi cerca")
    if (name_city == "Caracas"):
        print("En esta yo naci")
    if (name_city == "Sâo Paulo"):
        print("Exacto")
    else:
        print("Intenta de nuevo")

favorite_city(name_city)

# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Creamos la lista de personajes
personajes = [
    {"Nombre": "Boromir", "Clase": "Guerrero", "Raza": "Hombre de Gondor"},
    {"Nombre": "Sauron", "Clase": "Señor Oscuro", "Raza": "Maia"},
    {"Nombre": "Galadriel", "Clase": "Dama de Lothlórien", "Raza": "Elfa Noldor"},
    {"Nombre": "Elrond", "Clase": "Señor de Rivendel", "Raza": "Medio elfo"},
    {"Nombre": "Saruman", "Clase": "Mago", "Raza": "Istar"}

]

# -----------------------------------------------------------
# Mostrar los personajes de forma ordenada
# -----------------------------------------------------------
print("Lista de personajes del Señor de los Anillos:\n")
for personaje in personajes:
    print(f"Nombre: {personaje['Nombre']}")
    print(f"Clase: {personaje['Clase']}")
    print(f"Raza: {personaje['Raza']}")
    print("-" * 30)  # separador visual
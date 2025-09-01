# Recorremos el Diccionario seleccionArgentina 
seleccionArgentina = {
10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 millones", "Posicion": "Extremo derecho"},
11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 millones", "Posicion": "Extremo"},
21: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 millones", "Posicion": "Media punta"},
19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 millones", "Posicion": "Defensa central"},
1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 millones", "Posicion": "Portero"},
}

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')

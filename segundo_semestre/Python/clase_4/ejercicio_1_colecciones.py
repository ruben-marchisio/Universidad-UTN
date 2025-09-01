# -----------------------------------------------------------
# Ejercicio 1: Eliminar duplicados de una lista
# escriba un programa donde tenga una lista y que a continuacion 
# elimine los elementos repetidos y por ultimo muestre la lista

# Creamos una lista con elementos repetidos
lista = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]
print("Lista original:", lista)

# -----------------------------------------------------------
#  Convertir la lista en un conjunto (set)
#  Los conjuntos eliminan automáticamente los duplicados.

sin_duplicados = list(set(lista))
print("Lista sin duplicados (usando set):", sin_duplicados)

# -----------------------------------------------------------
#  Otra forma: recorrer la lista y agregar manualmente
#  solo los elementos que no estén repetidos.
#  (Esta forma mantiene el orden original).

lista_sin_duplicados = []
for elemento in lista:
    if elemento not in lista_sin_duplicados:  # si no está, lo agrego
        lista_sin_duplicados.append(elemento)

print("Lista sin duplicados (manteniendo orden):", lista_sin_duplicados)

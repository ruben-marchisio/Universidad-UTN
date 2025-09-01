# -----------------------------------------------------------
# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas


# Creamos dos listas 
lista1 = ["manzana", "pera", "uva", "banana", "kiwi"]
lista2 = ["pera", "melon", "kiwi", "sandia", "banana"]

print("Lista 1:", lista1)
print("Lista 2:", lista2)

# -----------------------------------------------------------
# 2. Convertimos las listas a conjuntos para eliminar duplicados

set1 = set(lista1)
set2 = set(lista2)

# Lista de palabras que aparecen en las listas (unión)
union_listas = list(set1 | set2)
print("\n1. Palabras que aparecen en las listas:", union_listas)

# Palabras que aparecen en la primera lista, pero no en la segunda (diferencia)
solo_lista1 = list(set1 - set2)
print("2. Palabras solo en la primera lista:", solo_lista1)

# Palabras que aparecen en la segunda lista, pero no en la primera (diferencia)
solo_lista2 = list(set2 - set1)
print("3. Palabras solo en la segunda lista:", solo_lista2)

# Palabras que aparecen en ambas listas (intersección)
en_ambas = list(set1 & set2)
print("4. Palabras en ambas listas:", en_ambas)
# 2.3 Repaso y más conceptos de Listas

# En Python, las LISTAS son estructuras que almacenan elementos.
# En otros lenguajes se conocen como "arreglos" o "vectores".
# Permiten distintos tipos de datos dentro de la misma lista.
# Son MUTABLES: se pueden modificar (agregar, eliminar, cambiar).
# -----------------------------------------------------------

# Crear una lista inicial

nombres = ['ana', 'juan', 'pedro', 'maria']
print("Lista inicial:", nombres)  

# -----------------------------------------------------------
# AGREGAR ELEMENTOS
# Con append() podemos agregar un elemento al FINAL de la lista.

nombres.append('luis')      # Agregar cadena
nombres.append(100)         # Agregar número entero
nombres.append(True)        # Agregar booleano
nombres.append(10.5)        # Agregar número decimal
nombres.append([1, 2, 3])   # Incluso otra lista dentro de la lista
print("Lista con nuevos elementos:", nombres)

# -----------------------------------------------------------
# CONCATENAR LISTAS
# Se pueden unir listas usando el operador + o el método extend().

lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2     # Usando +
print("Concatenación con '+':", lista3)

# Forma alternativa: usando extend() (agrega los elementos de otra lista)

lista3.extend([7, 8, 9])
print("Lista después de usar extend():", lista3)

# -----------------------------------------------------------
# BÚSQUEDA EN LISTAS
# index() -> devuelve la posición del primer elemento encontrado

print("Posición del número 5 en lista3:", lista3.index(5))

# Si el elemento no existe, da error:
# print(lista3.index(0))  # ValueError

# count() -> cuenta cuántas veces aparece un elemento
print("Cantidad de veces que aparece el 1:", lista3.count(1))

# -----------------------------------------------------------
# INVERSIÓN Y REPETICIÓN DE LISTAS
# reverse() -> invierte el orden de la lista

lista3.reverse()
print("Lista invertida:", lista3)

# Multiplicar listas (*) -> repite los elementos varias veces

lista4 = lista1 * 3
print("Lista repetida 3 veces:", lista4)

# -----------------------------------------------------------
# ORDENAMIENTO DE LISTAS
# sort() -> ordena la lista de menor a mayor

lista3.sort()
print("Lista ordenada de menor a mayor:", lista3)

# sort(reverse=True) -> ordena la lista de mayor a menor

lista3.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista3)
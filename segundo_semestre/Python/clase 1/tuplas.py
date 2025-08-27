# Tupla = datos que no deben cambiar (inmutable).

# DEFINIMOS UNA TUPLA
cocina = ('cuchara', 'cuchillo', 'tenedor')
print("TODO", cocina)  # Imprime la tupla completa

print(len(cocina))  # Imprime la cantidad de elementos en la tupla

#acceder a un elemento
print(cocina[0])  # Imprime el primer elemento de la tupla
print(cocina[1])  # Imprime el segundo elemento de la tupla

# Acceder a un elemento desde el final
print(cocina[-1])  # Imprime el último elemento de la tupla

# Acceder a un rango de elementos
print(cocina[0:2])  # Imprime los elementos desde el índice


# una tupla necesita aunque sea de un elemento una coma
verdura = ('tomate',)  # Tupla con un solo elemento
# de lo contrario, se consideraría una cadena de texto

# recorrer una tupla
for utensilio in cocina:
    print(utensilio, end= ', ')  # Imprime cada elemento de la tupla
    # Usamos end = para eliminar los saltos de línea


# convertir una tupla en una lista para modificarla
cocina_lista = list(cocina)  # Convierte la tupla en una lista
cocina_lista.append('plato')  # Agrega un nuevo elemento a la lista
print(cocina_lista)  # Imprime la lista modificada
# convertir una lista en una tupla
cocina_lista = tuple(cocina)  # Convierte la lista
print(cocina)  # Imprime la tupla convertida

# eliminar una tupla
del cocina  # Elimina la tupla 'cocina'
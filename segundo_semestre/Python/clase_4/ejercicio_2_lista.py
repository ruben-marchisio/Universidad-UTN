# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

# 1. Crear la lista con números del 1 al 10
lista = list(range(1, 11))
print("Lista original:", lista)

# 2. Pedir al usuario un número para multiplicar
factor = int(input("Ingrese un número para multiplicar la lista: "))

# 3. Recorrer la lista y multiplicar cada elemento
for i in range(len(lista)):
    lista[i] = lista[i] * factor

# 4. Mostrar la lista modificada
print("Lista modificada:", lista)
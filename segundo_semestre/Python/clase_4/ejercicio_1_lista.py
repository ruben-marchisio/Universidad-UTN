# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostra
# la lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma:
# 1-2-3-4-5-...-50

# 1. Crear la lista con range()
lista = list(range(1, 51))  # genera números del 1 al 50

# 2. Mostrar la lista usando un bucle for
for numero in lista:
    print(numero, end="-")  # 'end' evita salto de línea y pone un guion
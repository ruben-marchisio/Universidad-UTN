"""""
Ejercicio 3: 
Intercambiar el valor de dos variables.
Por ejemplo: 
a = 10        a = 5
b = 5              b = 10
"""

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print(f"Antes de intercambiar: a = {a}, b = {b}")
# Intercambiamos los valores de a y b
a, b = b, a
print(f"Después de intercambiar: a = {a}, b = {b}")
# Otra forma de intercambiar los valores de a y b
# temp = a
# a = b
# b = temp
# print(f"Después de intercambiar: a = {a}, b = {b}")
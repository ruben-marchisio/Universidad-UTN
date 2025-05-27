"""""
Ejercicio 2:
Determinar la solución lógica de la siguiente operación.

((3 + 5 x 8 ) < 3 and ((- 6/3 x 4 ) + 2 < 2)) or ( a > b)

"""

# Pide valores al usuario
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Evalúa la expresión lógica
resultado = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)

# Muestra el resultado
print(f"El resultado de la expresión es: {resultado}")


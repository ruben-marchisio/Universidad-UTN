# 6.9.1 Ejercicio Funciones 01

# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

# 1. Definir la función
def sumar(*args):
    """
    Esta función recibe múltiples números como argumentos
    y devuelve la suma de todos ellos.
    Parámetro:
        *args -> tupla de valores numéricos
    Retorna:
        suma total de los valores
    """
    return sum(args)  # usamos la función integrada sum()

# 2. Probar la función con diferentes cantidades de números
print("Suma de 1, 2, 3:", sumar(1, 2, 3))
print("Suma de 10, 20, 30, 40:", sumar(10, 20, 30, 40))
print("Suma de 5.5, 4.5:", sumar(5.5, 4.5))
# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos.

# 1. Definir la función
def multiplicar(*args):
    """
    Esta función recibe múltiples números como argumentos
    y devuelve el resultado de multiplicarlos a todos.
    Parámetro:
        *args -> tupla con valores numéricos
    Retorna:
        producto total de los valores
    """
    resultado = 1  # inicializamos en 1 (identidad de la multiplicación)
    for numero in args:
        resultado *= numero  # multiplicamos uno por uno
    return resultado

# 2. Probar la función con diferentes conjuntos de valores
print("Multiplicación de 2, 3, 4:", multiplicar(2, 3, 4))
print("Multiplicación de 5, 10:", multiplicar(5, 10))
print("Multiplicación de 1.5, 2, 4:", multiplicar(1.5, 2, 4))
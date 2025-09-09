# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
#
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
#
# Si se ingresan números negativos no imprime nada

# 1. Definir la función recursiva
def imprimir_descendente(n):
    """
    Función recursiva que imprime números desde n hasta 1.
    Parámetro:
        n -> número entero positivo
    """
    if n > 0:  # caso base: si n es mayor que 0
        print(n)
        imprimir_descendente(n - 1)  # llamada recursiva con n-1

# 2. Probar la función con ejemplos
print("Ejemplo con n = 5:")
imprimir_descendente(5)

print("\nEjemplo con n = 3:")
imprimir_descendente(3)

print("\nEjemplo con número negativo (-2):")
imprimir_descendente(-2)  # no imprime nada
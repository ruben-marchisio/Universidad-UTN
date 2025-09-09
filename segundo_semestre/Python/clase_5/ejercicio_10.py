# Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

# 1. Pedir cadena al usuario
cadena = input("Ingrese una cadena de texto: ")

# 2. Crear lista vacía donde guardaremos los caracteres únicos
caracteres_unicos = []

# 3. Recorrer cada carácter de la cadena
for caracter in cadena:
    # Si el carácter aún no está en la lista, lo agregamos
    if caracter not in caracteres_unicos:
        caracteres_unicos.append(caracter)

# 4. Mostrar la lista final
print("Lista de caracteres sin repetir:", caracteres_unicos)
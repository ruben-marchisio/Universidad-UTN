# 7.4 Funciones recursivas con factorial (hacer la tarea)

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1) # llamada recursivo
    

resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")

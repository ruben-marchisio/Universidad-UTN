#ciclo while (mientras se cumpla una condicion se ejecuta el bloque de codigo o durante)

contador = 0
while contador < 10:
    print("ejecutamos el ciclo while", contador)
    contador += 1  # Incrementamos el contador para evitar un bucle infinito
else:
    print("El ciclo while ha terminado")
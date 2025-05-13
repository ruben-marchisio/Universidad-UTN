num = int(input("Ingrese un número entre 1 y 3: "))
numeTexto = ""
if num == 1:
    numeTexto = "numero uno"
elif num == 2:
    numeTexto = "numero dos"
elif num == 3:
    numeTexto = "numero tres"
else:
    numeTexto = "numero fuera de rango"
    

print(f"El número ingresado es: {num} - {numeTexto}")
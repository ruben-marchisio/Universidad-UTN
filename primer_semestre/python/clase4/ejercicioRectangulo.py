#Ejercicio Rectángulo
#En el siguiente ejercicio se solicita calcular el área y el perímetro de un rectángulo. Para ello debemos de crear las siguientes variables:
#alto (int)
#ancho (int)
#El usuario debe de proporcionar los valores de alto y ancho, después se debe de imprimir el resultado en el siguiente formato:

alto = int(input("Ingrese el alto del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))

area = alto * ancho
perimetro = 2 * (alto + ancho)

print(f"El área del rectangulo es: {area}")
print(f"El perímetro del rectangulo es: {perimetro}")

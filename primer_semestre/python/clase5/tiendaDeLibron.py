"""""
Ejercicio: Tienda de libros
1 Mostrar: Ingrese los siguientes datos del libro
2 Digite el nombre del libro
3 Digite el ID del libro
4 Digite el precio del libro
5 Indicar si el envío es gratuito (True/False)
6 Mostrar:
	Nombre:
	ID: 
	Precio:
	Envío Gratuito?:
"""
nombre = input("Ingrese el nombre del libro: ")
id = int(input("Ingrese el ID del libro: "))
precio = float(input("Ingrese el precio del libro: "))
envioGratuito = input("¿El envío es gratuito? (True/False): ")

if envioGratuito == "true":
    envioGratuito = True
elif envioGratuito == "false":
    envioGratuito = False
else:
    envioGratuito = "Error: valor no válido debe escribirse True o False"
print(f'''
      Nombre: {nombre}
      ID: {id}
      Precio: {precio}
      Envío Gratuito?: {envioGratuito}
      ''')
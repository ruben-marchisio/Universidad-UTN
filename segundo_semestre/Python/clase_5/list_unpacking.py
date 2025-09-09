# 6.3 List Unpacking: Desempaquetado de listas

def show (name, lastName):
    print(name+" "+lastName)

person = ["John", "Doe"]
show(person[0], person[1]) # pasamos uno por uno los datos de la lista a la función

show(*person) # el asterisco desempaqueta la lista y pasa los datos a la función

persona2 = ("Jane", "Doe")
show(*persona2) # también funciona con tuplas

persona3 = {"lastName": "lucero", "name" : "natalia"}# también funciona con diccionarios
show(**persona3)
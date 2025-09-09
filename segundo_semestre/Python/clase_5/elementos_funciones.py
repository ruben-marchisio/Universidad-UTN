# 7.3 Lista de elementos con funciones (convertir)


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ["juan", "pedro", "maria", "ana"]
desplegarNombres(nombres2)
desplegarNombres("carlos") 

# desplegarNombres(123)  # esto da error porque no es iterable

desplegarNombres((10, 20, 30))  # funciona con tuplas
desplegarNombres([1, 2, 3, 4])  # funciona con listas)  

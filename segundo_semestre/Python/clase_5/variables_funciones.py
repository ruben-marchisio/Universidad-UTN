# 6.8 Funciones: Valores por Default en Argumentos

# variables en funciones

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres("juan", "pedro", "maria", "ana")
listarNombres("carlos", "luis")

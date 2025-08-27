# un diccionario esta compuesto por dos elementos 
# una llave y un valor 
# dict (key,value)

diccionario = {
    'IDE' : 'integrated development environment',
    'POO' : 'programacion oriantada a objetos',
    'SABD' : 'sistema de administracion de base de datos'
}

print(diccionario)

#para ver la cantidad de elementos 
print(len(diccionario))

# acceder con la llave dato: tiene que ser igual la sintaxis si no da error 

print(diccionario ['IDE'])

# otra forma de recuperar un elemento 

print(diccionario.get('POO'))

# modificar un elemento dato un diccionario pouede modificar el valor

diccionario['IDE'] = 'entorno de desarrollo integrado'
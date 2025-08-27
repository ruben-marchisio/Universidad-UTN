# colas con listas 
# estructura FIFO (first input, first output) 

cola = ['ruben', 'caelos', 'marcos']
print(cola)

# agregar elementos a la cola por el final
cola.append('luis')
print(cola)
cola.append('ana')
print(cola)

# sacar elementos de la cola
elemento_borrado = cola.pop(0)
print("Elemento sacado:", elemento_borrado)
print(cola)


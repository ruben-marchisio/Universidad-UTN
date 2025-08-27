# palabra reservada: continue
# La palabra reservada continue se utiliza para saltar a la siguiente iteración del ciclo sin ejecutar el resto del código en esa iteración.
# Por ejemplo, si queremos imprimir todas las letras de una palabra excepto la letra 'a', podemos usar continue:

for i in range(5):
    if i % 2 == 0:  
        print(f'valor: {i}  ') # modo sin continue

for i in range(5):
    if i % 2 != 0: 
        continue 
        print(f'valor: {i}  ') 
        
        
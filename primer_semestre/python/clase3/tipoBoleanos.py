#los boleanos son un tipo de dato que solo puede tener dos valores: True o False
# son utilizados para representar valores de verdad y son muy útiles en la toma de decisiones y en la lógica de programación.
# En Python, los valores booleanos son de tipo bool y se pueden utilizar en expresiones condicionales, 
# bucles y otras estructuras de control.
comparacion1 = 10 > 5 # True
comparacion2 = 10 < 5 # False   
print("el resultado es: ",comparacion1) # True
print("el resultado es: ",comparacion2) # False 

# podemos usar una condicional if para evaluar una expresion booleana
# y ejecutar un bloque de codigo si la condicion es verdadera
# o un bloque de codigo diferente si la condicion es falsa
# en este caso si la condicion es verdadera se ejecuta el bloque de codigo dentro del if
# y si es falsa se ejecuta el bloque de codigo dentro del else  

if comparacion1:
    print("la condicion es verdadera")  
else:
    print("la condicion es falsa")
    

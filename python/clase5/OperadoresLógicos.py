# operadores lógicos

# and: devuelve True si ambos operandos son True, de lo contrario devuelve False
a = True
b = False
result = a and b
print(result)  # False

a = True
b = True
result = a and b # True
print(result)  # True

# or: devuelve True si al menos uno de los operandos es True, de lo contrario devuelve False
a = True
b = False
result = a or b
print(result)  # True

a = False
b = False   
result = a or b
print(result)  # False

# not: devuelve True si el operando es False, de lo contrario devuelve False
a = True
result = not a
print(result)  # False

a = False
result = not a  
print(result)  # True
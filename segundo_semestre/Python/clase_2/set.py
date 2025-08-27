# Conjuntos en Python (set)

# -----------------------------------------------------------
# Un set es una colección de elementos:
# - No tiene un orden específico (los elementos pueden aparecer en cualquier orden).
# - No permite duplicados (cada elemento aparece solo una vez).
# -----------------------------------------------------------

planetas = {'marte', 'jupiter', 'venus'}
print(planetas) # El orden puede cambiar

# -----------------------------------------------------------
# Saber cuántos elementos tiene el set
# La función len() significa "length" (largo en inglés).
# -----------------------------------------------------------

print(len(planetas)) 

# -----------------------------------------------------------
# Verificar si un elemento está dentro del set
# Usamos el operador "in"
# -----------------------------------------------------------

print('marte' in planetas)  # True -> porque 'marte' sí está en el set

# -----------------------------------------------------------
# Verificar si un elemento NO está dentro del set
# Usamos "not in"
# -----------------------------------------------------------

print('jupiter' not in planetas)  # False -> porque 'jupiter' sí está

# -----------------------------------------------------------
# Agregar un nuevo elemento al set
# Importante: no se pueden duplicar elementos.
# Si intentas agregar 'tierra' dos veces, solo se guarda una vez.
# -----------------------------------------------------------

planetas.add('tierra')
print(planetas) 

# -----------------------------------------------------------
# Eliminar un elemento del set
# - Con remove() si el elemento NO existe -> ERROR
# - Con discard() si el elemento NO existe -> NO da error
# -----------------------------------------------------------

planetas.remove('jupiter')  # eliminamos 'jupiter'
print(planetas) 
planetas.discard('urano')
print(planetas)

# -----------------------------------------------------------
# Vaciar un set con clear()
# La función .clear() elimina TODOS los elementos del set,
# pero el set sigue existiendo (queda vacío).
# -----------------------------------------------------------

print(planetas)
planetas.clear()
print(planetas)

# -----------------------------------------------------------
# Eliminar un set completo con del
# La instrucción "del" borra la variable de memoria.
# Después de usar del, el set ya no existe en el programa.
# -----------------------------------------------------------

del planetas

# Si intentamos imprimir después de borrar, da error:
# print(planetas)  # ❌ NameError: name 'planetas' is not defined


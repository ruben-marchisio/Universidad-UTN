# -----------------------------------------------------------
# REPASO DE DICCIONARIOS EN PYTHON
# Un diccionario es una colección de pares "clave: valor".
#  Cada elemento tiene una CLAVE (única) y un VALOR asociado.
#  Se define con llaves {}.
#  Los valores pueden ser de cualquier tipo (números, cadenas,
#  listas, tuplas, otros diccionarios, etc.).


# Crear un diccionario simple con traducciones

diccionario = {'azul': 'blue', 'rojo': 'red', 'verde': 'green'}
print("Diccionario inicial:", diccionario)

# -----------------------------------------------------------
# ELIMINAR ELEMENTOS DE UN DICCIONARIO
# Usamos 'del' con la clave para borrar ese par clave-valor.

del diccionario['rojo']  
print("Después de eliminar 'rojo':", diccionario)

# -----------------------------------------------------------
# DICCIONARIOS CON DIFERENTES TIPOS DE DATOS
# Un diccionario puede almacenar distintos tipos de valores:
#  Otro diccionario
#  Una lista
#  Una tupla
#  Números o cadenas

diccionario2 = {
    'ruben': {      # Valor: otro diccionario
        'edad': 36,
        'altura': 1.75
    },
    'caelos': [38, 1.80],  # Valor: lista
    'marcos': (35, 1.70)   # Valor: tupla
}

print("Diccionario con distintos tipos de valores:", diccionario2)

# ejercicio: operadores or y not

# la preguta es si un padre puede asistir al juego de su hijo
# 1 verificamos si tiene vacaciones
# 2 verificamos si tiene el dia libre
# 3 usar estructura if else con el operador or
# 4 imprimir el resultado

vacaciones = True
diaLibre = False

if not (vacaciones or diaLibre):
    print("El padre puede asistir al juego de su hijo")
else:
    print("El padre no puede asistir al juego de su hijo")
    

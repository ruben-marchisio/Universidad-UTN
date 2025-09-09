# 7.2 Argumentos variables para un diccionario

def listarTerminos(**terminos): # los mas usados son *args y **kwargs
    for llave, valor in terminos.items():
        print(f"{llave}: {valor}")

listarTerminos() # sin argumentos no pasa nada
listarTerminos(IDE="Integrated Development Environment")
listarTerminos(IDE="Integrated Development Environment", PK="Primary Key", DBMS="Database Management System")

listarTerminos(Nombre="Juan", Apellido="Perez", Edad=28, Ciudad="Buenos Aires")
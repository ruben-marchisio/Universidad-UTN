#Dadas las horas trabajadas de 5 personas y la tarifa de pago, calcular el salario y la sumatoria de todos los salarios.
# Inicialización de la suma total de salarios
suma = 0

# Bucle para cada empleado (5 en total)
for i in range(1, 6):
    print(f"Salario del empleado {i}:")
    horas = float(input("Digite las horas trabajadas: "))
    tarifa = float(input("Digite la tarifa por hora: "))
    salario = horas * tarifa
    print(f"El salario es: {salario}")
    suma += salario

# Mostrar la suma total de salarios
print(f"La suma de todos los salarios es: {suma}")

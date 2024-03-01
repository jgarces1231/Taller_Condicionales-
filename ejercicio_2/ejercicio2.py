#input
salario_emp=int(input("Digite el salario del empleado: "))
deudas=input("El empleado tiene deudas: si , no?: ")

#proceso y salida 
if salario_emp>= 945200:
    rta = "APROBADO :D"

else:
    rta = "RECHAZADO :("
#output 
print("Su prestamo ha sido, " + rta)
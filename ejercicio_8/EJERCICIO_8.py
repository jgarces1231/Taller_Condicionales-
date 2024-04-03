#Programa para saber si los dos numeros daos so multiplos 

#input
A = int(input("ingrese porfavor un numero"))
B = int(input("ingrese porfavor un numero"))

# output

if A%B == 0 or B%A ==0:
    print("los numeros",A, "Y" ,B,"son multiplos")

else:
    print("los numeros",A, "Y" ,B,"no son multiplos")
#programa para calcular en que cuadrante esta un punto,de un plano cartesiano 

#entrada 
X = int(input("ingresa la coordenada X:"))
Y = int(input("ignresa la coordenada Y:")) 

#proceso
if X ==0:
    if Y ==0:
        print("La coordenada",(X, Y),"esta en, el origen")
    else:
        print("esta en el eje Y ")
elif Y ==0:
    print("esta en el eje Y ")
elif X > 0:
    if X>0:
        print("La coordenada",(X, Y),"esta en el cuadrante, 1")
    else:
        print("La coordenada",(X, Y),"esta en el caudrante, 4")
elif Y < 0:
    print("La coordenada",(X, Y),"esta en el  cuadrante, 3")
else:
    print("La coordenada",(X, Y),"esta en el cuadrane, 2")
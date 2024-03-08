# programa para calcular el precio de venta de diferentes productos en una tienda 

# entrada 

Precio_Costo = int(input("por favor ingrese el precio que le costo el poducto: "))

# proceso 

if Precio_Costo < 3000:
    GANANCIA = Precio_Costo * 0.15
elif Precio_Costo <= 6000:
    GANANCIA = 500
else:
    GANANCIA = Precio_Costo *0.25
PRECIO_VENTA = Precio_Costo + GANANCIA
#Salida
print ("el producto adquirido se debe vender a",PRECIO_VENTA)

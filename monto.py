total = 0
monto =float(input("Monto de una venta: $"))
while monto !=0 :
    if monto < 0: 
        print("Monto no valido!!!")
    else: 
        total = total + monto
        monto = float(input("Monto de una venta: $"))

    if monto > 1000:
        total = total -(total*0.1)


print("El total a pagar es de: ",total)




opcion = int(input("Ingrese la opcion a realizar por favor: "))

if(opcion == 1):
    print("BIENVENIDOS A LA SUMA!!!")
    a = int(input("ingrese Primer Numero: "))
    b = int(input("ingrese segundo Numero: "))
    b = a+b
    print("El resultado de la suma es: ",b)
elif(opcion ==2):
    print("BIENVENIDOS A LA RESTA!!!")
    a = int(input("ingrese Primer Numero: "))
    b = int(input("ingrese segundo Numero: "))
    b = a-b
    print("El resultado de la suma es: ",b)
elif(opcion ==3):
    print("BIENVENIDOS A LA MULTIPLICACION!!!")
    a = int(input("ingrese Primer Numero: "))
    b = int(input("ingrese segundo Numero: "))
    b = a*b
    print("El resultado de la suma es: ",b)
elif(opcion == 4):
    print("BIENVENIDOS A LA DIVISION!!!")
    a = int(input("ingrese Primer Numero: "))
    b = int(input("ingrese segundo Numero: "))
    b = a/b
    print("El resultado de la suma es: ",b)
 
else: 
    print("OPCION INGRESADA INVALIDA!!!!")
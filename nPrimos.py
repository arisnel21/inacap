num = 1
while num <=10:
    cont = 1
    x = 0

    while cont <= num:
        if num % cont == 0:
            x = x + 1
            cont = cont + 1

    if x == 2:
        print("El numero ",num," es primo")

    num = num + 1


print("")
print("*******************************************************")

"""Numero primo que el usuario lo ingrese"""

usuario = int(input("ingrese numero a evaluar: "))
x1 = 1
contl = 0
while x1 <= usuario:
    if usuario% x1 == 0:
        contl = contl +1
    x1 = x1 +1

if contl== 2: 
    print("El numero ",usuario," Es primo")
else:
    print( "El numero ",usuario," No es primo")
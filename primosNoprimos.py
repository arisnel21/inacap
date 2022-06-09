#numeros primos con while
numb = int(input("ingresa numero para evaluar: "))
x = 1
a = 0
while x <= numb:
    if numb% x == 0:
        a = a + 1

    x= x +1
if a == 2:
    print ("El numero ", numb, "Es primo")
else:
    print("El numero ", numb, " no es primo")

print ("fin.")
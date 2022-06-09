num = int(input("ingrese numeros: "))
totPares = 0
totImpares = 0
while num !=0 :
    if num % 2 == 0 :
        print("el numero ",num," es par")
        totPares += 1
    else:
        totImpares += 1
        print("el numero ",num," es impar")
    num = int(input("ingrese numeros: "))

    
print("total numeros pares :",totPares)
print("Total numeros impares: ",totImpares)

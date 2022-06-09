#ingrese 3 notas y debe evaluar si aprueba o reprueba ojo que cada nota no debe ser mayor a 7 si es mayor a 7 esta mal
notaUno = float(input("Ingrese primera nota porfavor: "))
notaDos = float(input("Ingrese segunda nota porfavor: "))
notaTres = float(input("Ingrese tercera nota porfavor: "))


if(notaUno>7 and notaDos>7 and notaTres>7):
    print("ERROR LA NOTA NO PUEDE SER SUPERIOR A 7")


notaTres = (notaUno + notaDos + notaTres)/3

if(notaTres>4): 
    print("aprobaste el ramo con nota: ",notaTres," Felicidades!!!!")
else:
    print("Reprobaste el ramo con nota: ",notaTres, "Mas suerte para la proxima campeón")
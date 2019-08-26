#Juego de "Adivina el numero

#libreria para generar numeros random
from random import randint

#asignacion de los numeros, mayor y menor, del rango
maximo = 99
minimo = 0
numero = randint(minimo, maximo)
print(numero)

while True:
    propuesta = input("Adivine un numero entre {} y {} incluidos: ".format(minimo, maximo))

    try:
        propuesta = int(propuesta)

    except:
        print("Debe de insertar un numero entero")
        continue

    if propuesta < minimo or propuesta > maximo:
        print("Numero fuera de rango")
        continue

    elif propuesta > numero:
        maximo = propuesta -1
        #numero = randint(minim,maxim) #linea por si se quiere cambiar el numero random en cada intento
        print("El numero es muy alto")

    elif propuesta < numero:
        minimo = propuesta +1
        #numero = randint(minim, maxim) #linea por si se quiere cambiar el numero random en cada intento
        print("El numero es muy bajo")

    elif propuesta == numero:
        break

print("Has Ganado")

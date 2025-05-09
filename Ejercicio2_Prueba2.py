# Desarrolle un programa en Python que permita ingresar dos números enteros que indique un rango numérico. El primer valor debe ser menor que el segundo.
# Luego, debe poder generar un número aleatorio entre ese rango numérico.

import random
rango_min = int(input('Ingrese límite inferior: '))
rango_max = int(input('Ingrese límite superior: '))
numero_aleatorio = random.randint(rango_min, rango_max)

# El juego consta de 3 intentos.
# Si no se adivina en el primer intento, el juego debe permitir dar el segundo intento, sin antes decir si el número a adivinar es mayor o menor.
# Si aún no se adivina en el segundo intento, se debe decir lo mismo que en el primer intento, pero además dar una pista. 
# La pista consta en decir cuál número está más cerca del que queremos adivinar, si el ingresado en el primer intento o el segundo intento
# Luego, si aun no adivina, se dará el tercer y último intento. Si no adivina, deberá mostrar un mensaje diciendo: "Perdiste".
# En caso que se adivine el número, independiente del intento en que se logró, el programa deberá terminar y entregar el mensaje "Felicitaciones, pudiste adivinar"


for intento in range(1, 4):
    respuesta = int(input('Intente adivinar: '))
    if respuesta == numero_aleatorio:
        print('Felicitaciones. Lograste adivinar.')
        break
    elif intento < 3:
        pista_mm = 'mayor' if respuesta < numero_aleatorio else 'menor'
        int(input(f'El número es {pista_mm} \nIntente adivinar de nuevo: '))
else:
    print(f'Perdiste. El número era {numero_aleatorio}')


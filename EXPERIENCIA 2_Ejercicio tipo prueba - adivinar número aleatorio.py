#ejercicio 2
#Desarrolle un programa en Python que permita generar un número aleatorio dentro de un rango definido por el usuario y ajustarlo dividiéndolo entre 4. Luego, el usuario deberá adivinar el número en un máximo de intentos de 3.
#Condiciones del juego:
#1. Ingreso de datos:
#a) El usuario ingresa dos números enteros que representan el rango numérico.
#b) El primero número debe ser menor que el segundo.
#2. Generación de números aleatorios:
#a) Se elige un número aleatorio dentro del rango ingresado.
#b) El número se ajusta dividiéndolo entre 4 y redondeándolo al múltiplo de 4 más cercano.
#3. Intentos del usuario:
#a) Primero intento: si el usuario acierta, se muestra un mensaje de felicitación.
#b) Segundo intento: si el usuario no acierta, se le indica si el número es mayor o menor.
#c) Tercer intento: si no acierta nuevamente, se le da otra pista.
#d) Resultado final: si no acierta en los tres intentos, el programa muestra el mensaje "Perdiste. El número era: ".

import random

print('Bienvenido al juego.')
while True:
    try:
        num1 = int(input('Para comenzar, ingresa un primero número: '))
        num2 = int(input('Ahora, ingresa un segundo número que sea mayor que el primero: '))
        if num1 < num2:
            break
        else:
            print('El primer número debe ser menor al segundo.')
    except ValueError:
        print('Error. Ingresa valores numéricos válidos')

numero_random = random.randint (num1, num2)
numero_secreto = round(numero_random // 4) * 4

intentos = 3
for intento in range(1, intentos + 1):
    while True:
        try:
            respuesta = int(input(f"Intento {intento}: Adivine el número secreto: "))
            break
        except ValueError:
            print("Error: Ingresa un número válido.")

    if respuesta == numero_secreto:
        print('¡Felicitaciones! Adivinaste el número secreto.')
        break
    elif intento == 1:
        print('Incorrecto. Inténtalo de nuevo.')
    elif intento == 2:
        pista = 'mayor' if respuesta < numero_secreto else 'menor'
        print(f'Incorrecto. Aquí te va una pista: el número secreto es {pista}.')
    elif intento == 3:
        print(f'Perdiste. El número secreto era: {numero_secreto}')





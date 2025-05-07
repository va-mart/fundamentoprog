#Desarrolla un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico. El primer valor debe ser menor que el segundo.
# El programa generará un número aleatorio dentro de ese rango. Luego, el usuario intentará adivinar el número generado en tres intentos.

#Si el usuario adivina en el primer intento, el programa mostrará el mensaje: "Felicitaciones, adivinaste en el primer intento."
#Si no acierta en el primer intento, el programa indicará si el número es mayor o menor que el intento del usuario.
#En el segundo intento, si el usuario no acierta, se volverá a indicar si el número es mayor o menor.
#Si el usuario no acierta en el tercer intento, el programa mostrará el mensaje: "Perdiste, el número era [número]."

import random
#pide al usuario que ingrese dos números enteros
numero1 = int(input('Ingresa el primero número: '))
numero2 = int(input('Ingresa el segundo numero (Tiene que ser mayor que el primero): '))
#genera un número aleatorio dentro del rango de los números ingresados por el usuario
num_aleatorio = random.randint(numero1, numero2)

#inicializa la variable "intento"
for intento in range(1, 4):
   respuesta = int(input('¿Cuál es el número secreto? '))
   #adivina el número en el primero intento
   if respuesta == num_aleatorio and intento == 1:
      print('¡Felicitaciones! Adivinaste el número secreto al primer intento')
      break
   #adivina el número y muestra el número de intentos
   elif respuesta == num_aleatorio:
      print(f'¡Felicitaciones! Adivinaste en {intento} intentos')
      break
   #pista en caso de no adivinar el número
   elif intento < 3:
      pista = "mayor" if respuesta < num_aleatorio else "menor"
      print(f'Incorrecto. El número secreto es {pista}. Inténtalo de nuevo.')
else: #si no adivina en los tres intentos
   print(f'Perdiste. El número secreto es {num_aleatorio}')



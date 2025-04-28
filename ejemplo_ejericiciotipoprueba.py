# programa que solicite dos numeros al usuario, A y B
# limite inferior, A, y el superior, B,
# en base a esos dos números, relizar un aleatorio=random import random
# calcular % a ese número aleatorio, usuario ingresa el número del % a calcular
# usuario elije si sumar o resta con el resultado del porcentaje
# resultado

import random #debido a que se van a utilizar funciones del modulo random (random.randint(a,b) es necesario comenzar con import random para que se generen los números aleatorios)

a = int(input('Ingresa un número: '))
b = int(input('Ingresa otro número: '))
num_ale = random.randint(a, b)
print(f'El número aleatorio es: {num_ale}')
porcentaje = int(input('Ingresa el porcentaje del número aleatorio que te gustaría calcular: '))
porcen_calculo = (num_ale * porcentaje) / 100
print(f'El resultado es: {porcen_calculo}')

calculo = input('¿Te gustaría sumar o restar estos números?: ')

if calculo == 'sumar':
    suma = num_ale + porcen_calculo
    print(f'El resultado de la suma es: {suma}')
elif calculo == 'restar':
    resta = num_ale - porcen_calculo
    print(f'El resultado de la resta es: {resta}')
else:
    print('Opción no válida')
import random
print('Bienvenido al juego')
num_1 = int(input('Ingresa el primer número: '))
num_2 = int(input('Ingresa el segundo número (tiene que ser mayor que el primero): '))
num_aleatorio = random.randint(num_1, num_2)

num_secreto = round(num_aleatorio // 4) * 4

respuesta = int(input('Adivina el número secreto: '))

for intento in range(1, 4):
    respuesta = int(input(f"Intento {intento}: Ingresa tu número: "))
    if respuesta == num_secreto:
        print(f"¡Felicitaciones, adivinaste en {intento} intentos!")
        break
    elif intento < 3:
        pista = "mayor" if respuesta < num_secreto else "menor"
        print(f"No acertaste. El número es {pista}. Inténtalo de nuevo.")
    else:
        print(f"Perdiste, el número era {num_secreto}.")





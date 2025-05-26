# Ejercicio 1
# Se solicita desarrollar un programa en Python que permita calcular el área de varios triángulos.
# Para esto, se le solicita al usuario indicar cuántos triángulos desea procesar. Luego, por cada triangulo se debe ingresar la base y la altura,
# ambos valores positivos y reales (números reales = decimales).
# El área de un triangulo se calcula con la siguiente formula: área = base * altura / 2. Si el usuario ingresa un valor inválido, se debe mostrar un mensaje.

print('Bienvenido a la calculadora.')
while True:
    try:
        cantidadTriangulos = int(input('¿Cuántos triángulos deseas procesar?\n'))
        if cantidadTriangulos > 0:
            break
        print('El número debe ser un entero positivo') # Este mensaje es parte de la validación que los número sean enteros positivos
    except ValueError as error:
        print('Debes ingresar un número entero positivo.') # Este mensaje es parte de la validación que sea un número

for i in range(1, cantidadTriangulos + 1):
    while True:
        try:
            base = float(input(f'Ingresa la base del triángulo {i}: '))
            altura = float(input(f'Ingresa la altura del triángulo {i}: '))
            if base <= 0 or altura <= 0:
                print('El valor debe ser real positivo.') # Este mensaje es parte de la validación que los número sean reales positivos
            else:
                area = base * altura / 2
                print(f'El área del triángulo {i} es: {area}')
                break
        except ValueError as error:
            print('Debes ingresar números reales y positivos.') # Este mensaje es parte de la validación que sea un número

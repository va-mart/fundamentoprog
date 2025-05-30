# Se requiere desarrollar un programa que gestione la venta de entradas para un cine mediante un menú interactivo.
# El sistema debe permitir al usuario realizar las siguientes acciones:
# 1. Comprar entradas:
# - Permitir al usuario ingrear la cantidad de entradas que desea comprar (número entero positivo)
# - Validar que la cantidad ingresada sea un número enteros mayor que 0.
# - Agregar las entradas compradas al total acumulado
# 2. Mostrar total de entradas vendidas
# - Mostrar cuántas entradas se han vendido hasta ese momento
# 3. Mostrar total recaudado:
# - Calcular y mostrar el monto total recaudado, considerando que cada entrada cuestra $8.500
# 4. Salir del sistema:
# - Finalizar el programa mostrando un mensaje de despedida

PRECIO_ENTRADA = 8500
entradas_vendidas = 0
total_recaudado = 0

print('Bienvenido a nuestro menú interactivo. ¿Qué deseas hacer?')
while True:
    try:
        print('[1] Comprar entradas')
        print('[2] Mostrar total entradas vendidas')
        print('[3] Mostrar el monto total recaudado')
        print('[4] Salir del menú')
        opcion = int(input('Seleccione la acción que desea realizar\n'))

        if opcion == 1:
            try:
                entradas = int(input('Ingresa la cantidad de entradas que desea comprar:\n'))
                if entradas > 0:
                    entradas_vendidas += entradas
                    total_recaudado += PRECIO_ENTRADA * entradas
                    print(f'Total a pagar: ${PRECIO_ENTRADA * entradas}')
            except ValueError:
                print('Ingresa un número entero positivo.')
        elif opcion == 2:
            print(f'Entradas vendidas: {entradas_vendidas}')
        elif opcion == 3:
            print(f'Total recaudado: ${total_recaudado}')
        elif opcion == 4:
            print('¡Gracias por preferirnos!\nVuelve pronto')
            break
    except ValueError:
        print('Opción inválida. Debes ingresar un número del 1 al 4.')
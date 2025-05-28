# Contexto
# Desarrollar un programa de gestión para estacionamietos que cotrole el flujo de vehículos diferenciando entre tres categorías (autos, motos y camionetas),
# y que aplque tarifas diferenciadas por tipo de vehículo, y garantice que no se exceda la capacidad máxima del establecimiento.

# Objetivo
# Como parte del proceso de operación del sistema de estacionamientos, se debe establecer un máximo de ocupación

# Registrar entrada vehículo
# Registrar salida del vehículo
# Visulizar estado del estacionamiento
# Reporte general del estacionamiento

# Codigo

# Constantes
AUTOS = 3000
MOTOS = 1500
CAMIONETAS = 4000

# Contadores
autos = 0
motos = 0
camionetas = 0

capacidad_estacionamiento = 0
vehiculos_totales_estacionados = 0
recaudacion_total_dia = 0

# Validar la capacidad del estacionamiento
print('*** Adiministración estacionamiento ***')
while True:
    try:
        capacidad_estacionamiento = int(input('Ingrese la capacidad máxima del estacionamiento: '))
        if capacidad_estacionamiento > 0:
            break
        else:
            print('La capacidad del estacionamiento debe ser mayor a 0.')
    except ValueError:
        print('Error, solo se permiten número enteros en la capacidad del estacionamiento.')

# Bucle para una cantidad desconocida de iteraciones
# Menú
while True:
    print('***** M E N Ú*****')
    print('[1] - Registrar entrada vehículo')
    print('[2] - Registrar salida de vehículo')
    print('[3] - Visualizar estado del estaiconamiento')
    print('[4] - Reporte general del estacionamiento')
    print('[5] - Salir')

    try:
         opcion = int(input('Ingrese una opción - 1 al 5: '))
         #if opcion >= 1 or opcion <= 5: # Validar que valor que ingrese usuario ente dentro del rango   
    except:
       print('Debe ingresar solo números enteros en "Opción"')
       continue # Reinicia el ciclo en caso de detectar un error
    
    if opcion == 1:
        
        estacionamientos_utilizados = autos + motos + camionetas
        if estacionamientos_utilizados >= capacidad_estacionamiento:
            print('Lo sentimos, el estacionamiento se encuentra lleno.')
            continue

        print('TIPOS DE VEHÍCULOS')
        print(f'[1] - Autos ${AUTOS}')
        print(f'[2] - Motos ${MOTOS}')
        print(f'[3] - Camionetas ${CAMIONETAS}')

        try:
            tipo_vehiculo = int(input('Ingrese el tipo de vehículo - 1, 2 o 3: '))
            if tipo_vehiculo < 1 or tipo_vehiculo > 3: # esto se cumple cuando el número ingresado está fuera del rango
                print('Solo pueden ingresan las opciones 1, 2 o 3.')
                continue # vuelve arriba
            if tipo_vehiculo == 1:
                autos += 1
            elif tipo_vehiculo == 2:
                motos +=1
            else:
                camionetas += 1
        except ValueError:
            print('Solo se permiten numeros enteros en "Tipo de vehículo".')
    
    elif opcion == 2:
        estacionamientos_utilizados = autos + motos + camionetas
        if estacionamientos_utilizados == 0:
            print('No existen vehículos estacionados.')
            continue

        print('TIPOS DE VEHÍCULOS')
        print(f'[1] - Autos ${AUTOS}')
        print(f'[2] - Motos ${MOTOS}')
        print(f'[3] - Camionetas ${CAMIONETAS}')

        try:
            tipo_vehiculo = int(input('Ingrese tipo de vehículo que sale del estacionamiento - 1, 2 o 3: '))
            if tipo_vehiculo < 1 or tipo_vehiculo > 3:
                print('Solo pueden ingresan las opciones 1, 2 o 3.')
                continue # vuelve arriba

            if tipo_vehiculo == 1 and autos == 0:
                print('No hay autos estacionados.')
            elif tipo_vehiculo == 2 and motos == 0:
                print('No hay camionetas estacionadas.')
            elif tipo_vehiculo == 3 and camionetas == 0:
                print('No hay camionetas estacionadas.')
                continue
        except ValueError:
            print('Solo se aceptan valor enteros en "Tipo de vehículo".')

        try:
            horas_estacionamiento = int(input('Ingrese el tiempo estacionado en horas: '))
            if horas_estacionamiento <= 0:
                print('El tiempo inhgresado debe ser mayor a 0.')
                continue

            if tipo_vehiculo == 1:
                autos -= 1
                pago = horas_estacionamiento * AUTOS
            elif tipo_vehiculo == 2:
                motos -= 1
                pago = horas_estacionamiento * MOTOS
            else:
                camionetas -= 1
                pago = horas_estacionamiento * CAMIONETAS

            vehiculos_totales_estacionados +=1
            recaudacion_total_dia += pago

            print('** BOLETA **')
            if tipo_vehiculo == 1:
                print('Tipo vehículo: AUTO')
            elif tipo_vehiculo == 2:
                print('Tipo vehículo: MOTO')
            else:
                print('Tipo vehículo: CAMIONETA')

            print(f'Total horas estacionado: {horas_estacionamiento}')
            print(f'Total a pagar: ${pago}')
        except:
            print('Error, debe ingresar el tiempo en horas y este debe ser un número entero.')
            continue

    elif opcion == 3:
        estacionamientos_utilizados = autos + motos + camionetas
        estacionamientos_disponibles = capacidad_estacionamiento - estacionamientos_utilizados
        print('***** Reporte estacionamiento *****')
        print(f'Estacionamientos utilizados: {estacionamientos_utilizados}')
        print(f'Estacionamientos disponibles: {estacionamientos_disponibles}')
        print(f'Capacidad máxima del estacionamiento: {capacidad_estacionamiento}')
        print(f'Estacionamientos por tipo de vehículo:\nAutos: {autos}\nMotos: {motos}\nCamionetas: {camionetas}')
    elif opcion == 4:
        print('Reporte general del estacionamiento')
        print(f'Vehículos totales estacionados en el día: {vehiculos_totales_estacionados}')
        print(f'Total recaudado en el día: ${recaudacion_total_dia}')
    elif opcion == 5:
        print('Muchas gracias por utilizar nuestra aplicación. ¡Vuelve pronto!')
        break
    else:
        print('La opción ingresada no es válida.')
    
        
# Sistema de Gestión de Reservas de Hotel
# Eres el desarrollador de un sistema de reservas para un hotel que necesita modernizar su gestión manual. 
# El hotel cuenta con habitaciones de tres categorías (Individual, Doble, Suite) y requiere un sistema eficiente para administrar sus reservas de forma digital.

# Datos solicitados:
# Identificador único de la reserva
# Nombre del huésped
# Número de habitación (entre 101 y 999)
# Tipo de habitación (Individual, Doble, Suite)
# Días de estadía (entero positivo, mínimo 1 día)
# Cálculos automáticos:
# Costo total (Individual: $50/día, Doble: $80/día, Suite: $120/día)
# Validaciones:
# Identificador de reserva (Debe contener letras y números)
# Nombre del huésped (no puede estar vacío)
# Días de estadía válidos (>= 1)
# La habitación debe estar libre al momento de reservar.

"Diccionario dónde se encontrará la lista que almacenará los datos de las reservas"
informacion = { "reservas": [] }


# 2.Buscar reserva
# Búsqueda por:
# ID de reserva
# Muestra:
   # ID: [ID Reserva]
   # Huésped: [Nombre]
   # Habitación: [Nombre]([Tipo])
   # Días: [Cantidad]
   # Total: $[Costo]
def buscar_reserva(id_reserva:str):
    for i in informacion['reservas']:
        if i['id_reserva'] == id_reserva:
            return i

# Validaciones:
# Identificador de reserva (Debe contener letras y números)
def validacion_numero(mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print('Solo se permiten números positivos.')
                continue
            return numero
        except ValueError:
            print('Solo puede ingresar números enteros')
            continue

# Validación para que la cantidad de días de estadía no sean menores a 1
def validacion_dias_estadia(mensaje_input:str):
    while True:
        try:
            dias = int(input(mensaje_input))
            if dias < 1:
                print('La estadía debe ser de al menos 1 día.')
                continue
            return dias
        except ValueError:
            print('Solo puede ingresar números enteros positivos.')

# Validación de texto
# Texto no esté vacío y/o tenga una cantidad de carácteres específica
def validacion_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print('El texto no puede estar vacío.')
            continue
        else:
            return texto
        
# Validar tipo de habitación
def validacion_habitacion():
    while True:
        tipo_habitacion = input('Ingrese el tipo de habitación que desea reservar: ')
        if tipo_habitacion == 'Individual' or tipo_habitacion == 'Doble' or tipo_habitacion == 'Suite':
            return tipo_habitacion
        else:
            print('El tipo de habitación no es válido.')
            continue

# Calcular el costo total según el tipo de habitación y la cantidad de días
def calcular_costo_habitacion(tipo_habitacion:str, cantidad_dias:int):
    if tipo_habitacion == 'Individual':
        return cantidad_dias * 50
    elif tipo_habitacion == 'Doble':
        return cantidad_dias * 80
    else:
        return cantidad_dias * 120
    
# Validar la existencia de números en el ID de la reserva
def validacion_numerica_reserva(id_reserva:str):
    numeros = '0123456789'
    for i in id_reserva:  # recorre cada caracter en id_reserva
        for j in numeros:  # lo compara con los caracteres en el string numeros
            if i == j:
                return True
    return False
        
# Validar la existencia de letras en el ID de la reserva
def validacion_alfabetica_reserva(id_reserva:str):
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    for i in id_reserva:    # recorre cada caracter en id_reserva
        for j in letras:    # lo compara con los caracteres en el string letras
            if i == j:
                return True
    return False
        
# Añadir nueva reserva
def agregar_reserva(id_reserva:str, nombre:str, numero_habitacion:int, tipo_habitacion:str, cantidad_dias:int):
    reserva_generada = { 
    "id_reserva" : id_reserva,
     "nombre_huesped" : nombre,
     "numero_habitacion" : numero_habitacion,
     "tipo_habitacion" : tipo_habitacion,
     "cantidad_dias" : cantidad_dias,
     "costo_total": calcular_costo_habitacion(tipo_habitacion, cantidad_dias)
     }
    informacion['reservas'].append(reserva_generada)


# La habitación debe estar libre al momento de reservar.
def buscar_habitacion(numero_habitacion:int):
    for i in informacion['reservas']:
        if i['numero_habitacion'] == numero_habitacion:
            return True
    return False
    
# Modificar reserva
# Proceso:
# 1.Buscar por ID
# 2.Permitir cambiar:
# Tipo de habitación
# Días de estadía
#Recalcular costo automáticamente
def modificar_reserva(id_reserva:str, tipo_habitacion:str, cantidad_dias:int):
    reserva_encontrada = buscar_reserva(id_reserva)
    if reserva_encontrada == None:
        print('Reserva no encontrada.')
    else:
        reserva_encontrada['tipo_habitacion'] = tipo_habitacion
        reserva_encontrada['cantidad_dias'] = cantidad_dias
        reserva_encontrada['costo_total'] = calcular_costo_habitacion(tipo_habitacion, cantidad_dias)
        print('Reserva modificada con éxito.')

# Cancelar reserva
# Entrada:
# ID de reserva
# Acción:
# Elimina la reserva del sistema
# Confirmación:
# “Reserva cancelada exitosamente”
def cancelar_reserva(id_reserva:str):
    reserva_encontrada = buscar_reserva(id_reserva)
    if reserva_encontrada == None:
        print('Reserva no encontrada.')
    else:
        informacion['reservas'].remove(reserva_encontrada)
        print('Reserva eliminada correctamente.')

# Mostrar todas las reservas
# Formato:
# [ID] – Hab. [Número] – [Huésped] (Días: X, Total: $Y)
def mostrar_reservas():
    for i in informacion['reservas']:
         print(f'ID: {i['id_reserva']} - Habitación: {i['numero_habitacion']} - Nombre: {i['nombre_huesped']} - TOTAL: {i['costo_total']}')

# Menú Principal
# 1.Registrar nueva reserva
# 2.Buscar reserva
# 3.Modificar reserva
# 4.Cancelar reserva
# 5.Mostrar todas las reservas
# 6.Salir
def menu_principal():
    while True:
        print('***** H O T E L *****')
        print('1.- Agregar reserva')
        print('2.- Buscar reserva')
        print('3.- Modificar reserva')
        print('4.- Cancelar reserva')
        print('5.- Mostrar todas las reservas')
        print('6.- Salir')

        opcion = validacion_numero('Ingrese una opción: ')

        if opcion == 1:
            while True:
                id_reserva = validacion_texto('Ingrese el id de su reserva: ')

                if buscar_reserva(id_reserva) != None:
                    print('El id se encuentra registrado.')
                    continue
                elif validacion_alfabetica_reserva(id_reserva) == False:
                    print('El id debe contener al menos 1 letra.')
                    continue
                elif validacion_numerica_reserva(id_reserva) == False:
                    print('El id debe contener al menos 1 número.')
                    continue
                break
            nombre = validacion_texto('Ingrese el nombre del huésped: ')
            while True:
                numero_habitacion = validacion_numero('Ingrese el número de la habitación: ')
                if numero_habitacion < 101 or numero_habitacion > 999:
                    print('El número de habitación no existe.')
                    continue
                if buscar_habitacion(numero_habitacion) == False:
                    break
                else:
                    print('La habitación se encuentra ocupada.')
                    continue
            tipo_habitacion = validacion_habitacion()
            cantidad_dias = validacion_dias_estadia('Ingrese la cantidad de días de su estadía: ')

            agregar_reserva(id_reserva, nombre, numero_habitacion, tipo_habitacion, cantidad_dias)
            print('Reserva registrada existosamente')
            print(informacion['reservas'])

        elif opcion == 2:
            id_reserva = validacion_texto('Ingresa el id de la reserva: ')
            reserva_encontrada = buscar_reserva(id_reserva)
            if reserva_encontrada == None:
                print('No se encontró la reservada ingresada.')
            else:
                print(f'ID: {reserva_encontrada['id_reserva']} - TOTAL: {reserva_encontrada['costo_total']}')
        elif opcion == 3:
            id_reserva = validacion_texto('Ingrese el id de la reserva: ')
            cantidad_dias = validacion_dias_estadia('Ingrese la cantidad de días: ')
            tipo_habitacion = validacion_habitacion()

            modificar_reserva(id_reserva, tipo_habitacion, cantidad_dias)
            print(informacion['reservas'])
        elif opcion == 4:
            id_reserva = validacion_texto('Ingrese el id de la reserva que desea cancelar: ')
            cancelar_reserva(id_reserva)
        elif opcion == 5:
            mostrar_reservas()
        elif opcion == 6:
            print('Saliendo del menú principal. Gracias por visitarnos.')
            break
        else:
            print('La opción ingresada no es válida.')

menu_principal()
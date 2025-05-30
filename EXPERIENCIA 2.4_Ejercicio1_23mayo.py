"Ejercicio 1"
"El programa debe comenzar permitiendo ingresar un número, que correspondería al número de personas que va a registrar."
"Este n° debería ser entero"
"Se debe registrar cada paciente con sus datos. El programa debe solicitar datos como el tipo de vacuna, las vacunas que posee"
"si padece alguna enfermedad, y alergias. En el caso de responder alguna pregunta, debe mostrar esquema incompleto"
"Una vez ingresada toda la información, programa debe mostrar la información obtenida."
"Cada ingreso debe manejarse con una excepción"
"Debe preguntar hasta que se cumpla la entrega de la información correctamente"
"Por último solicitar un número para salir, y al salir mostrar un mensaje de despedida"

# Validar cantidad de pacientes a registrar

while True:
    try:
        cantidad_pacientes = int(input('Bienvenio al portal de ingreso.\nIngrese el cantidad de pacientes a registrar: '))
        if cantidad_pacientes < 0:
            print('Debe ingresar número mayores a 0.')
            continue
        break
    except ValueError:
        print('Debe ingresar un número entero válido.')


for paciente in range(cantidad_pacientes):
    print(f'Registro del paciente {paciente+1}:')

    while True:
        nombre = input('Nombre del paciente: ')
        if nombre.strip() == '':
            print('El nombre no puede estar vacío.')
        else:
            break

    while True:
        try:
            edad = int(input('Edad del paciente: '))
            if edad < 0:
                print('Debe ingresar una edad válida.')
                continue
            break
        except ValueError:
            print('Valor inválido. Ingrese número enteros positivos.')
    
    tipo_vacuna = input('Indique qué vacuna recibirá el paciente: ')
    vacuna_existente = input('Indique las vacunas anteriores del paciente: ')
    enfermedad = input('¿Padece alguna enfermedad? (Si/No): ')
    alergias = input('¿Tiene alergias? (Si/No): ')

    if enfermedad.lower() == 'si' or alergias.lower() == 'si':
        print('Esquema incompleto')
    else:
        print('Esquema completo')

input('\nIngrese cualquier número para salir del programa.\n')
print('Cierre del programa. Hasta luego.')
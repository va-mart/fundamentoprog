"Ejercicio 2"
"Realice un menú que permita realizar la siguientes funcionalidades:"
"Mostrar mensaje que diga 'Menu principal'"
"1- para ingresar un número"
"2. para mostrar el mayor"
"3 para mostrar el promedio"
"4 para salir"
"Descripción de cada una de las opciones:"
"n 1 debe permitir ingresar un número entero entre 0 y 100"
"El usuario puede ingresar cualquier valor dentro del rango por lo que debemos manejar excepciones"
"n 2: debe mostrar el número mayor ingresado hasta ese momento"
"n 3: debe mostrar el promedio ingresado, para ambas opciones si no se ha ingresado ningún número debe indicarlo,"
"mostrar mensaje 'no se ha ingresado ningun intento'"
"n 4: 'Fin del programa.'"

numeros = []

while True:
    print('MENÚ PRINCIPAL')
    print('[1] Ingresar un número')
    print('[2] Número ingresado mayor')
    print('[3] Mostrar promedio de números ingresados')
    print('[4] Salir')
    
    try:
        opcion = int(input('Selecciona una opción\n'))
        if opcion <= 0 or opcion > 4:
            print('Debes ingresar un número entre 1 y 4.')
            continue
    except ValueError:
        print('Debes ingresar un número.')
        continue

    if opcion == 1:
        while True:
            try:
                num = int(input('Ingresa un número: '))
                if 0 <= num <= 100: #  Numero ingresado dentro del rango 0 - 100
                    numeros.append(num) # Se almacena número ingresado a la lista "numeros"
                    break
                else:
                    print('Debe ser un número entre 0 y 100.')
            except ValueError:
                print('Debe ser un número entero y positivo.')
    elif opcion == 2:
        if numeros: # Lista no está vacía
            print('El número ingresado mayor es:', max(numeros))
        else: # Lista está vacía
            print('No se ha ingresado ningún intento.')
    elif opcion == 3:
        if numeros:
            print('El promedio de los números es:', sum(numeros)/len(numeros))
        else:
            print('No se ha ingresado ningún intento.')
    elif opcion == 4:
        print('Fin del programa.')
        break
    else:
        ('Opción no válida.')
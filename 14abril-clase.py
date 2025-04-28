print('\nBienvenido a Tienda Gloria') #\n carácter que representa un salto de línea

perf_mujer = ['Organza', 'Katy Perry', 'Mañana Fresca', 'La mejor noche', 'Sueño Exclusivo']
perf_hombre = ['Ahora Sí Voy', 'Antonio Banderas', 'LaCoste', 'Hugo Boss', 'A que te quito el sueño']

precios = {'50 ml': 10000, '100 ml': 18000} # {} diccionarios que permites almacenar datos clave-valor {clave1 : valor1, clave2: valor2}

subtotal = 0

while True:
    # Categoría
    while True:
        categoria = input('\n¿Qué categoría deseas comprar? (Hombre/Mujer): ').strip().lower()  
        #.strip() sirve para eliminar espacios en blanco al principio y final de una cadena de texto 
        # .lower() convierte todo texto a minúsculas y así evitar fallas por minúsculas o mayúsculas

        if categoria == 'mujer':
            print('Nuestros perfumes para mujer disponibles: ')
            for perfume in perf_mujer:
                print(f'- {perfume}')
            lista_perfumes = perf_mujer
            break

        elif categoria == 'hombre':
            print('Nuestros perfumes para hombres disponibles: ')
            for perfume in perf_hombre:
                print(f'- {perfume}')
            lista_perfumes = perf_hombre
            break

        else:
            print('Categoría inválida. Por favor, ingrese "Mujer" o "Hombre".')

    # Selección de perfume
    while True:
        perf_seleccionado = input('Ingrese el nombre del perfume seleccionado: ').strip()
        if perf_seleccionado in lista_perfumes:
            break
        print('Opción inválida. Por favor, elija un perfume de la lista.')

    # Formato
    while True:
        formato = input('\n¿Qué formato deseas comprar? (50 ml/100 ml): ').strip().lower()

        if formato in precios:
            precio = precios[formato] # precios: diccionario precios  formato: 50 ml o 100 ml -> es lo mismo que precios['50 ml'] o precios ['100 ml']
            subtotal += precio  # manera abreviada de escribir subtotal = subtotal + precio
            print(f'Has seleccionado "{perf_seleccionado}" en formato {formato} - Precio: {precio}')
            break
        else:
            print('Formato inválido. Por favor, ingrese "50 ml" o "100 ml".')

    # Continuar o finalizar compra
    while True:
        continuar = input('¿Desea comprar otro perfume? (sí/no): ').strip().lower()
        if continuar == 'sí':
            break  # Regresa al inicio del bucle principal
        elif continuar == 'no':
            iva = subtotal * 0.19
            total_compra = subtotal + iva
            print('\n---- RESUMEN COMPRA ----')
            print(f'\nSubtotal: ${subtotal}')
            print(f'IVA 19%: ${iva}')        
            print(f'Total: ${total_compra}')
            print('\n¡Muchas gracias por tu compra!')
            exit()  # Finaliza el programa correctamente
        else:
            print('Respuesta inválida. Por favor, ingrese "sí" o "no".')
        

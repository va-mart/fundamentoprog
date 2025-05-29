#El programa debe tener un menú de opciones de donde se pueda realizar el pago
#del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
#una vez sumadas se resten al cupo disponible.
#Las opciones disponibles deben estar construidas de la siguiente forma:
#1. Pago de Tarjeta de Crédito:
#a. El usuario comienza con una deuda de $100.000
#b. El usuario puede ingresar un monto para realizar un pago en la
#tarjeta de crédito.
#c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
#d. Se debe verificar que el monto a pagar no exceda el saldo actual de
#la tarjeta.
#e. Al pagar el sistema debe descontar de la deuda total
#f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
#2. Simulación de Compras:
#a. El usuario puede simular realizar un número ilimitado de compras.
#b. Para cada compra, se solicita al usuario ingresar el monto de la
#compra. El programa suma los montos de cada compra.
#c. Se verifica que el monto de la compra sea mayor o igual a cero.
#d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
#iteración del bucle for.
#3. Salir:
#a. Al seleccionar esta opción, el programa debe cerrarse o finalizar

deuda = 100000
while True:
    print('Bienvenido al portal de pago del Banco\n¿Qué acción desear realizar?')
    print('1. Pagar cupo de la tarjeta')
    print('2. Simular compras nuevas')
    print('3. Ver deuda de la tarjeta')
    print('4. Salir')
    try:
        respuesta = int(input('Ingrese el número de la opción que desea realizar:\n'))
    except ValueError:
        print('Debe ingresar un número del 1 al 4.')
    
    if respuesta == 1:
        print(f'Deuda actual: ${deuda}')
        try:
            pago = float(input('Ingrese el monto a pagar:\n'))
            if pago < 0:
                print('EL monto debe ser mayor o igual a 0.')
            elif pago > deuda:
                print('No puede pagar un monto mayor que la deuda actual.')
            else:
                deuda -= pago
                print(f'Pago realizado. Deuda actual: ${deuda}')
        except ValueError:
            print('Debe ingresar un número válido.')
    elif respuesta == 2:
        while True:
            try:
                compra = float(input('Ingrese el monto de la compra (ingrese 0 para terminar):\n'))
                if compra == 0:
                    break
                elif compra < 0:
                    print('El monto debe ser mayor o igual a cero.')
                else:
                    deuda += compra
                    print(f'Compra realizada. Nueva deuda: ${deuda}')
            except ValueError:
                print('Debe ingresar un número válido.')
    elif respuesta == 3:
        print(f'Deuda actual: ${deuda}')
    elif respuesta == 4:
        print('¡Gracias por utilizar el portal!')
        break
    else:
        print('Debe ingresar un número del 1 al 4.')

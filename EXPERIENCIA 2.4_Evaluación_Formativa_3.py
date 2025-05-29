# En un delivery de Sushi vende 4 tipos de Sushi: 
# 1. Pikachu Roll $4500 2. Otaku Roll $5000 3. Pulpo Venenoso Roll $5200 4. Anguila Eléctrica Roll $4800  
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un cliente el cuál puede ir agregando Rolls 
# a través de un menú uno por uno con solo seleccionar la opción (1 a 4). 
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario decida que su pedido está completo. 
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá ingresarlo. 
# Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso contrario enviar el mensaje “código no válido” 
# y dar al usuario la opción de reingresar el código o volver al menú tecleando “X”  Una vez realizado los pasos anteriores, 
# debe mostrar el detalle del pedido contabilizando el total de productos y la cantidad de cada uno de ellos y si aplica o no el descuento 

# constantes
PIKACHU = 4500
OTAKU = 5000
PULPO = 5200
ANGUILA = 4800

# contadores
pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
while True:
    print('Bienvenid@ al menú de Sushito. \nNuestros rollos disponibles son:')
    print('[1] - Pikachu Roll  $4.500')
    print('[2] - Otaku Roll   $5.000')
    print('[3] - Pulpo Venenoso Roll   $5.200')
    print('[4] - Anguila Eléctrica Roll   $4.800')

    try:
        pedido = int(input('¿Qué roll desea comprar? Ingrese el número del roll correspondiente\n'))

        if pedido == 1:
            pikachu +=1
        elif pedido == 2:
            otaku += 1
        elif pedido == 3:
            pulpo += 1
        elif pedido == 4:
            anguila += 1
        else:
            print('Se debe ingresar un número del 1 al 4.')
    except ValueError:
        print('Se debe ingresar un número entero y positivo.')
    
    continuar_pedido = input('¿Desea agregar más productos? (Si/No)\n').lower()
    if continuar_pedido == 'no':
        break

monto_total = (pikachu * PIKACHU) + (otaku * OTAKU) + (pulpo * PULPO) + (anguila * ANGUILA)
valor_descuento = 0
monto_final = monto_total


while True:
    descuento = input('Ingrese su código de descuento (En caso de no tener uno, ingrese X para continuar al pago)\n')
    if descuento.lower() == 'soyotaku':
        valor_descuento = monto_total * 0.10
        monto_final = monto_total - valor_descuento
        print('¡Descuento aplicado!')
        break
    elif descuento.lower() == 'x':
        print('No se aplica descuento.')
        break
    else:
        print('Código no válido. Intente nuevamente o ingrese X para continuar sin descuento.')

print('*** RESUMEN DE LA VENTA ***')
print('Pikachu Rolls -', pikachu, '- $', pikachu * PIKACHU)
print('Otaku Rolls -', otaku, '- $', otaku * OTAKU)
print('Pulpo Venenoso Rolls -', pulpo, '- $', pulpo * PULPO)
print('Anguila Eléctrica Rolls -', anguila, '- $', anguila * ANGUILA)
print(f'Total: ${monto_total}')
print(f'Descuento: ${valor_descuento}')
print(f'Total a pagar: ${monto_final}')

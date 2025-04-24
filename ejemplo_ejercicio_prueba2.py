# Ejercicio tipo prueba
# tienda falabella necesita desarrollar un programa para saber cuántos puntos tiene acumulado cada usuario
# por cada $1.000 de compra que realice un usuario, recibe 10 puntos
# cuando un usuario alcanza el nivel premium, 1000 puntos, recibe un descuento de 25%
# cuando un usuario alcanza el nivel oro, 500 puntos, recibe un descuento de 10%
# cuando un usuario alcanza el nivel bronce, 250 puntos, no recibe descuento, pero sí grandes premios; audifonos, manos libres, relojesy mucho más
# a continuación los perfiles de 3 tarjeta ???
# Marcos tiene 1500 puntos a canjear, qué niveles le corresponden
# José Luis tiene 2500 puntos, 
# Sebastian solo tiene 300 puntos, 
# mostrar en pantalla la información que corresponde al usuario, el nivel que le corresponde y cuántos el corresponde, o el nivel en el que se encuentra
# mensaje motivándolo a seguir acumulando puntos 

print('Bienvenido/a a Falabella.')
nombre = input('Ingresa tu nombre: ')
puntos = int(input('Ingresa tus puntos acumulados: '))

if puntos >= 1000:
    print('¡Felicitaciones,', nombre, '! Con un total de', puntos, 'puntos te encuentra en el nivel Premium.')
    print('Como agradecimiento de nuestra parte, recibirás un descuento del 25% en tu próxima compra. ¡Disfrutalo y sigue acumulando puntos para más beneficios!')
elif puntos >= 500:
    print('¡Felicitaciones,', nombre, '! Con un total de', puntos, 'puntos te encuentra en el nivel Oro.')
    print('Como agradecimiento de nuestra parte, recibirás un descuento del 10% en tu próxima compra. ¡Disfrutalo y sigue acumulando puntos para más beneficios!')
elif puntos >= 250:
    print('¡Felicitaciones,', nombre, '! Con un total de', puntos, 'puntos te encuentra en el nivel Bronce.')
    print('Como agradecimiento de nuestra parte, puedes elegir un premio entre las opciones disponibles. ¡Disfrutalo! Sigue acumulando puntos para poder obtener mejores beneficios como posibles descuentos en tus futuras compras')
else:
    print('Hola, ', nombre, '. En este momento no estás registrado en ningún nivel. Sigue comprando con nosotros para acumular puntos y obtener beneficios exclusivos.')
    print('¡Recuerda que por cada $1.000 de compra, acumulas 10 puntos!')
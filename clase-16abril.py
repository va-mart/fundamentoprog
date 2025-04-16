# realizar menú que presente las siguiente opciones a un usuario:
# - un saludo al ingresar el n 1
# - despedida al ingresar n 2
# - edad 
# opción de salida (else) opción inválida
#- utilizando if, elif, else"

edad = int(input('Ingrese su edad: '))
if edad >= 18:
    numero =int(input('Ingrese un número del 1 al 2 '))
    if numero == 1:
       print('Bievenido al programa')
    elif numero == 2:
       print('Gracias por visitar el programa. Hasta pronto')
    else:
       print('Opción inválida')
else:
   print('Te esperamos en un año más')
#Ejercicio tipo examen
#Empresa Certefika nos solicita un programa que cumpla con las siguientes condiciones:
#alumnos con calificaciones mayor 6, reciben descuento del 20% en su matricula
#alumnos con calificaciones mayores a 5, reciben descuento del 15%
#alumnos con calificaciones mayores a 4, reciben desciento del 10%
#quien no cumpla con ninguno de los requisitos, lo invitamos a seguir esforzándose 

print('Bienvenido al Portal de Pagos de Certifika')
calificacion_1 = float(input('Ingresa calficación parcial 1: '))
calificacion_2 = float(input('Ingresa calificación parcial 2: '))
calificacion_3 = float(input('Ingresa calificación parcial 3: '))

promedio = float((calificacion_1+calificacion_2+calificacion_3)/3)

if promedio >= 6:
    print('Tu promedio es: ', promedio, 'Debido a tus logros has recibido un descuento del 20% en tu matricula del próximo año')
elif promedio >= 5:
    print('Tu promedio es: ', promedio, 'Debido a tus logros has recibido un descuento del 15% en tu matricula del próximo año')
elif promedio >= 4:
    print('Tu promedio es: ', promedio, 'Debido a tus logros has recibido un descuento del 10% en tu matricula del próximo año')
else:
    print('Tu promedio es: ', promedio, '¡Sigue esforzándote!')
#ejercicio 1
#Desarrolle un programa en Python que permita calcular el subsidio de gas según el quintil de ingreso al que pertenece la familia del solicitante y sus condiciones laborales.
#Condiciones socioeconómicas:
#1. Quintil de ingreso: hay cinco quintiles en total (1 = menos ingreso, 5 = mayor ingreso)
#2. Condiciones laborales: se considera si la persona está desempleada o empleada.
#3. Condiciones del subsidio de gas: 

#quintil       condición laboral      subsidio de gas
#1 o 2           desempleado             $10.000
#1 o 2             empleado              $8.000
#3               desempleado             $6.000
#3                 empleado              $4.000
#4 o 5            cualquiera             $1.500

#bonos adicionales: si el solicitante pertenece al quintil 1 o 2 recibirá un bono adicional de $2.000, si además tiene más de 65 años recibirá un bono extra de $3.000

#código

print('Bienvenido al portal de subsidios. ' \
'A continuación se le solicitarán una serie de datos para poder calcular el subsidio que le correspondería.')
nombre = input('Nombre: ').strip().lower()

while True:
    edad = int(input('Edad: '))
    if edad > 0 and edad < 100:
       break
    else:
        print('Error. Ingrese un número válido')

while True:
    cond_laboral = input('Indique su situación laboral: ').strip().lower()
    if cond_laboral in ['empleado', 'desempleado']:
        break
    else:
        print('Error: Ingrese "empleado" o "desempleado".')

while True:
    quintil = int(input('Indique su quintil socioeconómico ingresando un número del 1 al 5 ' \
'(siendo 1 un ingreso menor y 5 un ingreso mayor): '))
    if quintil >= 1 and quintil <= 5:
        break
    else:
        print("Error: El quintil debe estar entre 1 y 5.")



subsidio = 0
if (quintil == 1 or quintil == 2) and cond_laboral.lower() == 'desempleado':
    subsidio = 10000
elif (quintil == 1 or quintil == 2) and cond_laboral.lower() == 'empleado':
    subsidio = 8000
elif quintil == 3 and cond_laboral.lower() == 'desempleado':
    subsidio = 6000
elif quintil == 3 and cond_laboral.lower() == 'empleado':
    subsidio = 4000
elif quintil == 4 or quintil == 5:
    subsidio = 1500


bono = 0
if quintil == 1 or quintil == 2:
    bono = 2000
    print('Se le ha otorgado un bono extra de $2.000. (Subsidio quintiles 1 y 2).')

bono_2 = 0
if edad >= 65:
    bono_2 = 3000
    print('Se le ha otorgado un bono extra de $3.000 ')


subsidio_final = subsidio + bono + bono_2
print('Su subsidio total es: $', subsidio_final)
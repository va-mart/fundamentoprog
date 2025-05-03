print('Bienvenido al portal de subsidios de la Compañía de Gas')
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
condicion_laboral = input('Indique su condición laboral (Empleado o Desempleado): ').lower()
quintil = int(input('Indique su condición socioecónimica (quintil) ingresando un número del 1 al 5 (1 siendo lo más bajo y 5 lo más alto): '))

subsidio = 0
if condicion_laboral == 'desempleado' and quintil == 1:
    subsidio = 15000
elif condicion_laboral == 'empleado' and quintil == 2:
    subsidio = 10000
elif condicion_laboral == 'desempleado' and quintil == 3:
    subsidio = 8000
elif condicion_laboral == 'empleado' and quintil == 4:
    subsidio = 6000
elif quintil == 5:
    subsidio = 1500

print(f'Su subsidio correspondiente a su quintil es: $ {subsidio}')

bono = 0
if quintil in [1, 2]:
    bono += 2000
    print('Usted recibe un bono adicional de $2.000 (Bono quintiles 1 y 2)')

if edad >= 65:
    bono += 3000
    print ('Usted recibe un bono adicional de $3.000 (Bono tercera edad)')

total_subsidio = subsidio + bono
print(f'Su subsidio total es de: $ {total_subsidio}')

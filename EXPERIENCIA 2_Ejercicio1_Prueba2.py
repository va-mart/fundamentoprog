# Desarrolle un programa en Python que permita calcular los beneficios a los estudiantes de primer año según condición académica y socioeconómica
# Las condiciones académicas basadas en el promedio final con el que salieron del colegio/liceo
# Las condiciones socioeconómicas están basadas según el quintil al que pertenece su grupo familiar (5 quintiles en total)
arancel = 1800000
matricula = 90000

promedio = float(input('Ingrese el promedio final del alumno: '))
quintil = int(input('Ingrese el quintil al que pertenece el grupo familiar (1-5): '))

# Condiciones
# Promedio mayor a 6.0 - Quintil 1 o 2 - 20% descuento arancel
# Promedio mayor a 6.0 - Quintil 3 o 4 - 15% descuento arancel
# Promedio mayor a 5.0 y menor o igual a 6.0 - Quintil 1 o 2 - 13% descuento arancel
# Promedio mayor a 5.0 y menor o igual a 6.0 - Quintil 3 o 4 - 10% descuento arancel

descuento_arancel = 0
if quintil in [1, 2] and promedio > 6.0:
    descuento_arancel = (arancel * 20) / 100
elif quintil in [3, 4] and promedio > 6.0:
    descuento_arancel = (arancel * 15) / 100
elif quintil in [1, 2] and (promedio > 5.0 and promedio <= 6.0):
    descuento_arancel = (arancel * 13) / 100
elif quintil in [3, 4] and (promedio > 5.0 and promedio <= 6.0):
    descuento_arancel = (arancel * 10) / 100
else:
    descuento_arancel = 0

# Solo por el hecho de pertenecer al Quintil 1, 2 o 3 tiene un descuento del 10% en la matrícula
# y si perteneciendo a esos quintiles su promedio es mayor o igual a 5.5 se obtiene un 5% adicional.

descuento_matricula = 0
if quintil in [1, 2, 3]:
    descuento_matricula = (matricula * 10) / 100
else:
    descuento_matricula = 0

descuento_adicional = 0
if quintil in [1, 2, 3] and promedio >= 5.5:
    descuento_adicional = (matricula * 5) / 100
else:
    descuento_adicional = 0

descuentoadicional_total = descuento_matricula + descuento_adicional

# El programa debe entregar el valor final del arancel y matrícula suponiendo que se le entrega el promedio y el quintil del estudiante. 

arancel_final = arancel - descuento_arancel
matricula_final = matricula - descuentoadicional_total
print(f'El valor del arancel es ${arancel_final}')
print(f'El valor de la matrícula es ${matricula_final}')

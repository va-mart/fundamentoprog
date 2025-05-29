# Una empresa de manufactura utiliza códigos numéricos para identificar lotes de producción.
# Para asegurar la calidad y autenticidad de cada lote, se ha definido que solo aquellos
# códigos que son números primos serán considerados válidos para su distribución.
# Se debe desarrollar un programa que permita ingresar una cantidad determinada de códigos numéricos para su evaluación.
# El programa debe comenzar solicitando un número entero positivo N, que indica la cantidad total de códigos que serán ingresados.
# Por cada código ingresado, el programa debe:
# Validar que la entrada sea un numéro entero válido. Si no es así, solicitar la entrada nuavemente hasta que sea correcta.
# Verificar si el código es un número primo
# Mostrar en pantalla "Código válido", si el número es primo.
# Mostrar en pantalla #Código inválido", si el número no es primo
# Al finalizar la evaluación de los N códigos, el programa debe mostrar un resumen indicando:
# Cuántos códigos fueron válidos (primos)
# Cuántos códigos fueron inválidos (no primos)


while True:
    try:
        n = int(input('¿Cuántos códigos serán ingresados?\n'))
        if n > 0:
            break
        else:
            print('Se debe ingresar un número entero positivo.')
    except ValueError:
        print('Se debe ingresar un número.')

def es_primo(num):
    if num < 2: # 0 y 1 no son números primos
        return False
    for i in range(2, int(num ** 0.5) + 1): # genera una lista de números desde el 2 hasta la raíz cuadrada de num - se prueba si num es divisible entre 2 y su raíz cuadrada
        if num % i == 0:   # si num se puede dividir por i, no es primo
            return False
    return True

validos = 0
invalidos = 0

for i in range(n):
    while True:
        try:
            codigo = int(input('Ingresa el código numérico:\n'))
            break
        except ValueError:
            print('Se debe ingresar un número válido.')
        
    if es_primo(codigo):
        print('Código válido')
        validos += 1
    else:
        print('Código inválido')
        invalidos += 1

print('\nResumen:')
print(f'Códigos válidos (primos): {validos}')
print(f'Códigos inválidos (no primos): {invalidos}')



# Registro de temperatura
# El usuario debe ingresar el registro de la temperatura en un rango de -50° a 50° centígrados.
# Dado que el usuario puede ingresar cualquier dato (incluso cadena de texto), se puede usar manejo de excepción (try-except) para evitar que el programa se detenga.
# 1. Si el dato ingresado no es un **número entero** el programa debe mostrar el siguiente mensaje “Error: Debe ingresar un número entero válido” y repetir hasta que sea válido.
# 2. Si el usuario ingresa un número entero **fuera del rango,** informarle al usuario “Error: Temperatura fuera del rango permitido” y se le vuelve a mencionar el rango permitido hasta que le usuario introduzca los datos válidos.
# 3. Si el usuario introduce los datos correctamente: “Temperatura registrada exitosamente”
# 4. Debe tener una opción para solicitar la salida del programa.
# 5. Al salir del programa, mostrar un mensaje que diga “Cierre del programa. Hasta luego.”


while True:
    entrada = input('Ingresa la temperatura que deseas registrar en °C (O escribre "salir" para salir del programa\n').lower()
    if entrada.lower() == "salir":
        print('Cierre del programa. Hasta luego.')
        break

    try:
        temperatura = int(entrada)
        if temperatura >- -50 and temperatura > 50:
            print('Error: Temperatura fuera del rango permitido (-50° - 50°).')
        else:
            print(f'Temperatura registrada exitosamente.\nTemperatura registrada: {temperatura}° C')
            break
    except ValueError:
        print('Error: Debe ingresar un número entero válido.')

# Nombre - Plataforma - Género - Clasificación ESRB - Desarrollador - Año de lanzamiento - Publicador
videojuegos = {
    'GOW001': ['God of War', 'PS5', 'Aventura', 'M', 'Santa Monica Studio', 2022,
'Sony'],
    'ZEL002': ['The Legend of Zelda: Tears of the Kingdom', 'Switch', 'Aventura',
'E10+', 'Nintendo', 2023, 'Nintendo'],
    'ELD003': ['Elden Ring', 'Multiplataforma', 'RPG', 'M', 'FromSoftware', 2022,
'Bandai Namco'],
    'SPD004': ['Spider-Man 2', 'PS5', 'Acción-Aventura', 'T', 'Insomniac Games',
2023, 'Sony'],
    'MNC005': ['Minecraft', 'Multiplataforma', 'Sandbox', 'E', 'Mojang', 2011,
'Microsoft'],
    'FNF006': ['Five Nights at Freddy’s: Security Breach', 'Multiplataforma',
'Terror', 'T', 'Steel Wool Studios', 2021, 'ScottGames'],
    'GT7007': ['Gran Turismo 7', 'PS5', 'Carreras', 'E', 'Polyphony Digital', 2022,
'Sony'],
    'HLY008': ['Hogwarts Legacy', 'Multiplataforma', 'RPG', 'T', 'Avalanche Software', 2023, 'Warner Bros']
}

# Precio en CLP - Cantidad en stock
stock = {
    'GOW001':   [59_990,   12],
    'ZEL002':   [69_990,   8],
    'ELD003':   [49_990,   15],
    'SPD004':   [64_990,   5],
    'MNC005':   [19_990,   30],
    'FNF006':   [34_990,   7],
    'GT7007':   [54_990,   10],
    'HLY008':   [59_990,   6]
}

# Buscar Juego por Nombre
# Crear una función busca_juego_por_nombre(nombre_juego: str) que reciba el nombre de un juego (ignorando mayúsculas/minúsculas) y retorne una lista con todos sus datos, incluyendo el código al inicio. 
# Si no se encuentra, retornar None.
def buscar_juego_por_nombre(nombre_juego:str):
    for i in videojuegos:
        if videojuegos[i][0] == nombre_juego:    # i = códigos de los videojuegos 0 = primer elemento de la lista
            print('¡Juego encontrado!')
        juego_encontrado = videojuegos[i]
        juego_encontrado.insert(0,i)   # Se inserta para agregar el código a la lista y retornarlo de esa manera, como pide la instrucción
        return juego_encontrado
    
# Buscar Stock por Código
# Crear una función buscar_stock_por_juego(codigo_juego: str) que retorne los datos de stock (precio y cantidad) asociados a un código.
def buscar_stock_por_juego(codigo_juego:str):
    for i in stock:
        if i.lower() == codigo_juego.lower():
            print('Juego encontrado')
            return stock[i][1]
    
# Disminuir Stock
# Crear una función disminuir_stock(codigo_juego: str, cantidad: int) que reduzca el stock disponible. Si la cantidad solicitada supera el stock disponible, mostrar: "No hay stock suficiente!".
def disminuir_stock(codigo_juego:str, cantidad:int):
    stock_disponible = buscar_stock_por_juego(codigo_juego)
    if stock_disponible >= cantidad:
        stock[codigo_juego.upper()][1] -= cantidad
        return True
    return False

# Mostrar Todos los Juegos
# Crear una función mostrar_todos_juegos() que imprima el nombre y plataforma de todos los juegos en formato: "NOMBRE: {nombre} || PLATAFORMA: {plataforma}".
def mostras_todos_juegos():
    for i in videojuegos:
        print(f' NOMBRE: {videojuegos[i][0]} || PLATAFORMA: {videojuegos[i][1]}')

# Actualizar Precio de un Juego
# Crear una función actualizar_precio_juego(nombre_juego: str, precio_nuevo: int) que modifique el precio del juego buscado por nombre. Si no existe, mostrar: "El juego que desea actualizar no se encuentra.".
def actualizar_precio_juego(nombre_juego:str, precio_nuevo:int):
    juego_encontrado = buscar_juego_por_nombre(nombre_juego)
    if juego_encontrado != None:
        for i in stock:
            if i.upper() == juego_encontrado[0].upper():
                stock[i][0] = precio_nuevo
                print(f"El nuevo precio de '{nombre_juego}' es: {precio_nuevo}")
    else:
        print('El juego que desea actualizar no se encuentra.')

# Filtrar Juegos por Año de Lanzamiento
# Crear una función buscar_juego_por_anio(rango_minimo: int, rango_maximo: int) que imprima los datos completos de los juegos lanzados dentro del rango especificado (inclusive).
def buscar_juego_por_año(rango_minimo:int, rango_maximo:int):
    for i in videojuegos:
        if videojuegos[i][5] >= rango_minimo and videojuegos[i][5] <= rango_maximo:
            print(videojuegos[i])

def validacion_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print('El texto no puede estar vacío.')
            continue
        else:
            return texto
        
def validacion_numero_entero_positivo(mensaje_input:int):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <= 0:
                print('No se pueden ingresar número negativos ni 0.')
                continue
            else:
                return numero
        except ValueError:
            print('El número debe ser un entero.')
            continue

# Menú principal
def menu_principal():
    while True:
        print('=== Tienda de Videojuegos ===')
        print('1. Vender juego (disminuir stock)')
        print('2. Mostrar todos los juegos')
        print('3. Actualizar precio de un juego')
        print('4. Filtrar juegos por año de lanzamiento')
        print('5. Salir')

        opcion = validacion_numero_entero_positivo('Ingrese una opción: ')
        
        if opcion == 1:
            codigo_juego = validacion_texto('Ingresa el código del juego: ')
            cantidad_a_comprar = validacion_numero_entero_positivo('Ingrese la cantidad que desea comprar: ')
            compra = disminuir_stock(codigo_juego, cantidad_a_comprar)
            if compra == True:
                print('¡Compra realizada con éxito!')
            else:
                print('¡Lo sentimos! No hay stock disponible en este momento.')
        elif opcion == 2:
            mostras_todos_juegos()
        elif opcion == 3:
            nombre_juego = validacion_texto('Ingresa el nombre del juego a actualizar: ')
            precio_nuevo = validacion_numero_entero_positivo('Ingresa el nuevo precio: ')
            actualizar_precio_juego(nombre_juego, precio_nuevo)
        elif opcion == 4:
            rango_minimo = validacion_numero_entero_positivo('Ingrese un rango mínimo: ')
            rango_maximo = validacion_numero_entero_positivo('Ingrese un rango máximo: ')
            buscar_juego_por_año(rango_minimo, rango_maximo)
        elif opcion == 5:
            print('Saliendo del programa.')
            break
        else:
            print('Opción no válida. Ingrese un número del 1-5')

menu_principal()
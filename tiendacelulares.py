#===== TIENDA DE CELULARES =====
#1. Vender producto
#2. Mostrar todos los productos
#3. Actualizar precio
#4. Buscar producto por marca
#5. Salir

productos = {
  'A52S': ['Samsung', 6.5, '6GB', 'Interno', '128GB', 'Snapdragon 778G', 'Triple'],
  'IP12': ['Apple', 6.1, '4GB', 'Interno', '64GB', 'A14 Bionic', 'Dual'],
  'M13': ['Xiaomi', 6.5, '6GB', 'Interno', '128GB', 'MediaTek G80', 'Triple'],
  'NOKG21': ['Nokia', 6.5, '4GB', 'Interno', '64GB', 'Unisoc T606', 'Doble']}


inventario = {
  'A52S': [259990, 15],
  'IP12': [599990, 3],
  'M13': [199990, 0],
  'NOKG21': [149990, 20]}

# Validar texto
def validacion_texto(msj_input:str):
    while True:
        texto = input(msj_input)
        if len(texto) == 0:
            print('El mensaje no puede estar vacío.')
            continue
        else: 
            return texto

# Validar número
def validacion_numerica(msj_input:str):
    while True:
        try:
            numero = int(input(msj_input))
            if numero < 0:
                print('Debe ser un número positivo.')
                continue
            else:
                return numero
        except ValueError:
            print('Debe ser un número entero.')
            continue

# Crear una función buscar_por_marca(marca: str) que retorne una lista con todos los productos de esa marca (ignorando mayúsculas).
def buscar_por_marca(marca:str): 
    for i in productos:         # Recorre cada clave (i) del diccionario productos. Cada clave representa el código de un celular.
        if productos[i][0].lower() == marca.lower():     # Verifica si la marca del celular (primer elemento de la lista de datos) es igual al texto que se busca (marca)
            print('Celular encontrado.')        # Si la marca coincide, muestra el mensaje
        celular_encontrado = productos[i]       # Guarda la lista de datos del celular en la variable celular_encontrado
        celular_encontrado.insert(0, i)         # Agrega el código del celular al inicio de la lista
        return celular_encontrado               # Devuelve la lista con el código y los datos del celular

# Crear una función consultar_stock(codigo_producto: str) que muestre el precio y la cantidad disponible. 
# Si no existe, mostrar un mensaje de error.
def consultar_stock(codigo_producto:str):
    codigo_producto = codigo_producto.upper()
    if codigo_producto in inventario:      # Verifica si el código del producto existe en el diccionario inventario.
            print('Producto encontrado')   # Si el producto existe, muestra el mensaje "Producto encontrado".
            return inventario[codigo_producto]  # Devuelve la lista con el precio y la cantidad disponible de ese producto.
    else:
        print('El producto no existe en el inventario.') # Muestra el mensaje "El producto no existe en el inventario."
        return None    # Devuelve None para indicar que no se encontró el producto
    
# Crear una función vender_producto(codigo_producto: str, cantidad: int) que descuente stock. 
# Si no hay suficiente, mostrar: "No hay stock suficiente!".
def vender_producto(codigo_producto:str, cantidad:int):
     stock_disponible = consultar_stock(codigo_producto)  # Llama a la función consultar_stock para obtener la lista [precio, cantidad] del producto.
     if stock_disponible is None:
         print('El producto no existe en el inventario.')
         return False
     if stock_disponible[1] >= cantidad:  # stock_disponible[1] accede a la cantidad disponible del producto (el segundo elemento de la lista [precio, cantidad]).
          inventario[codigo_producto.upper()][1] -= cantidad # restar la cantidad al stock,
          return True # Venta se realizó
     print('No hay stock suficiente)')
     return False # Venta no se realizó

# Mostrar todos los productos
# Crear una función mostrar_todos_productos() que imprima todos los productos con formato:
# "CÓDIGO: {codigo} || MARCA: {marca} || RAM: {ram} || ALMACENAMIENTO: {almacenamiento}"
def mostrar_todos_productos():
     for i in productos:
          print(f'CÓDIGO: {i} || MARCA: {productos[i][0]} || RAM: {productos[i][2]} || ALMACENAMIENTO: {productos[i][4]} ')

# Actualizar precio
# Crear una función actualizar_precio(codigo_producto: str, nuevo_precio: int) que actualice el precio. 
# Si no se encuentra el código, mostrar un mensaje de error.
def actualizar_precio(codigo_producto: str, nuevo_precio: int):
     if codigo_producto in productos:         # Verifica si el código del producto existe en el diccionario productos.
        inventario[codigo_producto] = nuevo_precio   # Actualiza solo el precio
        print(f"Precio actualizado para {codigo_producto}: ${nuevo_precio}")
     else:
        print(f"Error: el código '{codigo_producto}' no fue encontrado.")

# Filtrar por tamaño de pantalla
def tamaño_pantalla(rango_min:float, rango_max:float):
    for i in productos:   # Recorre cada clave (i) del diccionario productos. Cada clave es el código de un celular.
        if productos[i][1] >= rango_min and productos[i][1] <= rango_max: # Verifica si el tamaño de pantalla del celular (segundo elemento de la lista de datos) está dentro del rango indicado.
            print(productos[i])  # imprime en pantalla la lista de datos del producto cuyo código es i.

        
def menu():
     while True:
        print('===== TIENDA DE CELULARES =====')
        print('1. Vender producto')
        print('2. Mostrar todos los productos')
        print('3. Actualizar precio')
        print('4. Buscar producto por marca')
        print('5. Filtrar por tamaño de pantalla')
        print('6. Salir')


        opcion = validacion_numerica('Ingrese una opción: ')

        if opcion == 1:
            codigo_producto = validacion_texto('Ingrese el código del producto: ')
            cantidad = validacion_numerica('Ingrese la cantidad a comprar: ')
            compra = vender_producto(codigo_producto, cantidad)
            if compra == True:
                print('La venta se realizó con éxito.')
            else:
                print('Lo sentimos. No hay stock disponible.')
        elif opcion == 2:
            mostrar_todos_productos()
        elif opcion == 3:
            codigo_producto = validacion_texto('Ingrese el código del producto: ')
            nuevo_precio = validacion_numerica('Ingrese el nuevo precio: ')
            actualizar_precio(codigo_producto, nuevo_precio)
        elif opcion == 4:
            marca = validacion_texto('Ingrese la marca a buscar: ')
            resultado = buscar_por_marca(marca)
            print(resultado)
        elif opcion == 5:
            rango_min = validacion_numerica('Ingrese el tamaño mínimo de pantalla: ')
            rango_max = validacion_numerica('Ingrese el tamaño máximo de pantalla: ')
            tamaño_pantalla(rango_min, rango_max)
        elif opcion == 6:
            print('Cerrando programa...')
            break
        else:
            print('Opción no válida. Inténtelo de nuevo.')

menu()
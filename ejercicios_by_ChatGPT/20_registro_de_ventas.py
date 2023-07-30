## Mi codigo original ##

'''import json
from random import randint

def acceder_al_inventario(): #retorna un dict con los productos disponible en stock, asi como sus precios

    with open('ejercicios_by_ChatGPT/02_productos/inventario.json','r+',encoding='UTF-8') as inventario:
        return json.load(inventario)


def actualizar_inventario(inventario_post_compra): #actualiza el inventario luego de la compra, asi simula que se llevaron una cantidad de la disponible

    with open('ejercicios_by_ChatGPT/02_productos/inventario.json','w+',encoding='UTF-8') as inventario:
        json.dump(inventario_post_compra,inventario,indent=4)
    

def imprimir_lista_de_productos():
    for nombre,cantidad_precio in inventario.items():
        print(f'----{nombre.capitalize()}----:\nPrecio por unidad ${cantidad_precio["precio"]}\tUnidades {cantidad_precio["cantidad"]}\n')


def seleccionar_productos():
  
    #creamos una lista con todos los nombres de los productos que hay en el inventario
    lista = [i for i in inventario.keys()] 
    #Elige un producto aleatorio de la lista de productos
    productos = lista[randint(0,len(lista)-1)]
    carrito = {} #aqui almacenará el producto elegido y su cantidad a comprar

    #la cantidad de producto es aleatoria y es entre 1 a 10 unidades
    cantidad = randint(1,10)
    if inventario[productos]['cantidad'] == 0: #si no hay cantidades disponibles del producto seleccionado 
        print(f'Cantidad de {productos.capitalize()} agotado :(')

    elif inventario[productos]['cantidad'] < cantidad: #si la cantidad seleccionada supera a la cantidad disponible
        carrito[productos] = inventario[productos]['cantidad'] #solo se podrá llevar la cantidad disponible, almenos
        print(f'Cantidad de {productos.capitalize()} agotado :(')

    else:
        carrito[productos] = cantidad #agrega la cantidad al carrito, le asigna el value al producto
    return carrito #retorna el dict con el porducto seleccionado y la cantidad elegida

    
def comprar_producto(carrito_de_compras,registro):
    #tiene como args los productos y sus cantidades, asi como tambien una variable con el registro de las ganancias

    for producto, cantidad in carrito_de_compras.items(): #separamos el producto y su cantidad
        inventario[producto]['cantidad'] -= cantidad #restamos la cantidad que se está comprando del inventario
        registro += inventario[producto]['precio'] * cantidad #calculamos el precio por la cantidad de producto y guardamos la ganancia resultante
    return registro, carrito_de_compras #retornamos la ganancia aumentada con el dict sin modificar para posteriormente guardar su registro


def imprimir_registro_de_ventas_del_dia(producto_cantidad,registro):
    print('\nRegistro de ventas')
    print('------------------------------')
    for producto, cantidad in producto_cantidad.items(): #tomamos el nombre del producto y su cantidad registrada
        print(f'\n{producto.capitalize()}\nCantidad Vendida: {cantidad}') #imprimimos cada producto con su cantidad vendida
    print('------------------------------')
    print(f'Ganancia total en productos   ${registro}\n') #al final escribimos el total en ganancias por la venta del los productos


def simulacion_automatica(registro_de_ventas): #simula una compra de multiples productos al azar

    for i in range(randint(1,30)): #crea un rango aleatorio para repetir el proceso de compras
        
        #el registro de ventas es la ganancia por la cantidad de producto vendido
        #el registro de productos sirve para saber que productos se vendieron y cuanto fue
        registro_de_ventas, registro_de_productos = comprar_producto(seleccionar_productos(),registro_de_ventas)

        for producto, cantidad in registro_de_productos.items(): #separa el producto vendido con su respectiva cantidad

            if producto in productos_vendidos.keys(): #si el producto ya se registró
                productos_vendidos[producto] += cantidad #se agrega la cantidad adicional

            elif producto in inventario.keys(): #si el producto no se registro aun
                productos_vendidos[producto] = cantidad #crea una nueva clave y le asigna un value

    return registro_de_ventas #retorna la cantidad de ganancia total


def menu(registro_de_ventas,productos_vendidos):
    imprimir_lista_de_productos() #imprime la lista de productos disponibles
    registro_de_ventas = simulacion_automatica(registro_de_ventas) #guarda la cantidad de ganancia
    imprimir_registro_de_ventas_del_dia(productos_vendidos,registro_de_ventas) #imprime los productos que se vendieron y la cantidad de cada uno
    actualizar_inventario(inventario) #sirve para actualizar el inventario descontando la cantidad de productos en las ventas de la simulacion

inventario = acceder_al_inventario() #devuelve un dict que contiene el nombre del producto, cantidad y precio
registro_de_ventas: int = 0 #registro de la cantidad de ganancia
productos_vendidos = {} #dict para almacenar los productos que se hayan vendido y sus cantidades
menu(registro_de_ventas,productos_vendidos)
'''

## Codigo mejorado por ChatGPT
import json
from random import randint

def acceder_al_inventario():
    # Función para acceder al inventario desde el archivo JSON y retornarlo como un diccionario
    with open('ejercicios_by_ChatGPT/02_productos/inventario.json', 'r+', encoding='UTF-8') as inventario:
        return json.load(inventario)

def actualizar_inventario(inventario_post_compra):
    # Función para actualizar el inventario en el archivo JSON después de una compra
    with open('ejercicios_by_ChatGPT/02_productos/inventario.json', 'w+', encoding='UTF-8') as inventario:
        json.dump(inventario_post_compra, inventario, indent=4)

def imprimir_lista_de_productos(inventario):
    # Función para imprimir la lista de productos disponibles en el inventario
    for nombre, cantidad_precio in inventario.items():
        print(f'----{nombre.capitalize()}----:\nPrecio por unidad ${cantidad_precio["precio"]}\tUnidades {cantidad_precio["cantidad"]}\n')

def seleccionar_producto(inventario):
    # Función para seleccionar un producto aleatorio del inventario disponible
    productos_disponibles = [producto for producto, detalles in inventario.items() if detalles['cantidad'] > 0]
    if productos_disponibles:
        producto = productos_disponibles[randint(0, len(productos_disponibles) - 1)]
        cantidad = randint(1, min(10, inventario[producto]['cantidad']))
        return producto, cantidad
    return None, 0

def comprar_producto(producto, cantidad, inventario):
    # Función para comprar un producto del inventario y actualizar la cantidad y el registro de ventas
    if producto:
        precio_unidad = inventario[producto]['precio']
        inventario[producto]['cantidad'] -= cantidad
        return precio_unidad * cantidad
    return 0

def imprimir_registro_de_ventas(productos_vendidos, registro):
    # Función para imprimir el registro de ventas con los productos y las cantidades vendidas
    print('\nRegistro de ventas')
    print('------------------------------')
    for producto, cantidad in productos_vendidos.items():
        print(f'\n{producto.capitalize()}\nCantidad Vendida: {cantidad}')
    print('------------------------------')
    print(f'Ganancia total en productos   ${registro}\n')

def simulacion_automatica(inventario):
    # Función para simular una compra automática de productos aleatorios
    registro_de_ventas = 0
    productos_vendidos = {}

    for _ in range(randint(1, 30)):
        producto, cantidad = seleccionar_producto(inventario)
        ganancia_producto = comprar_producto(producto, cantidad, inventario)

        if producto in productos_vendidos:
            productos_vendidos[producto] += cantidad
        else:
            productos_vendidos[producto] = cantidad

        registro_de_ventas += ganancia_producto

    return registro_de_ventas, productos_vendidos

def menu():
    # Función principal que ejecuta el programa
    inventario = acceder_al_inventario()
    imprimir_lista_de_productos(inventario)
    registro_de_ventas, productos_vendidos = simulacion_automatica(inventario)
    imprimir_registro_de_ventas(productos_vendidos, registro_de_ventas)
    actualizar_inventario(inventario)

menu()

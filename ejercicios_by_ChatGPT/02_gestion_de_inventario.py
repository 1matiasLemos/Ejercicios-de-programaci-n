## Codigo original por mi

import json
def inventario_completo():
    with open('ejercicios_by_ChatGPT/02_productos/inventario.json') as temporal_inventario:
        return temporal_inventario.read() #estamos leyendo el archivo json y retornando esa lectura

dict_inventario = json.load(open('ejercicios_by_ChatGPT/02_productos/inventario.json')) #guardamos el inventario en un dict

def agregar_producto(producto,cantidad):

    try:
        cantidad + 1 #si el usuario introdujo erroneamente un signo o letra en lugar de un numero, dará TypeError
        producto = producto.casefold() #si el usuario introdujo un nombre inadecuado que no sea un str, dará AttributeError
        if cantidad <= 0:
            return 'Error en la cantidad del producto, no puede ser 0 o menor. Intente de nuevo'
    except TypeError:
        return 'Error, la cantidad debe ser en numeros enteros'
    except AttributeError:
        return 'Error, el nombre del producto debe ser escrito como algo legible'
            
    if producto in dict_inventario.keys(): #si el producto está dentro del inventario, que son las claves en el dict
        dict_inventario[producto] = cantidad #actualiza la cantidad de esa clave (producto), no suma sino que reemplaza
        with open('ejercicios_by_ChatGPT/02_productos/inventario.json','w+') as actualizar_invent: #indica que esribiremos de 0
            json.dump(dict_inventario,actualizar_invent,indent=4) #actualizamos el inventario, usando el dict actualizado
        return '---Cantidad de producto actualizado---'
    
    else: #si el producto no está dentro del inventario, que son las claves en el dict
        dict_inventario[producto] = cantidad #agregamos una nueva clave (producto) y la cantidad
        with open('ejercicios_by_ChatGPT/02_productos/inventario.json','w+') as actualizar_invent:
            json.dump(dict_inventario,actualizar_invent,indent=4) #actualizamos el inventario del json con el nuevo producto
        return '---Producto agregado correctamente---'

def eliminar_producto(producto):

    try:
        producto = producto.casefold()
        if producto in dict_inventario.keys():#si el producto está en el inventario (clave del diccionario)
            del dict_inventario[producto] #procedemos a borrar esa clave y su value
            with open('ejercicios_by_ChatGPT/02_productos/inventario.json','w+') as actualizar_invent:
                json.dump(dict_inventario,actualizar_invent,indent=4) #actualizamos el inventario
            return '---El producto fue eliminado del inventario correctamennte---'
        else:
            return 'XX-Ese producto no está en el inventario-XX'
    except:
        return 'Nombre incorrecto'

def consultar_cantidad(nombre):
    try:             #el nombre del producto (parametro de la funcion) #cantidad (value) dentro del inventario (dict)
        return f'---La cantidad disponible de {nombre.casefold()} es {dict_inventario[nombre.casefold()]} unidades---'
    except: 
        return 'XX-No existe este producto en el inventario-XX'

def menu():
    opcion1 = '1_Agregar producto al inventario'
    opcion2 = '2_Eliminar producto del inventario'
    opcion3 = '3_Consultar cantidad de producto en el inventario'
    opcion4 = '4_Mostrar inventario completo'
    opcion5 = '0_Salir del programa'
    return f'\n{opcion1}\n{opcion2}\n{opcion3}\n{opcion4}\n{opcion5}'

opcion = None
while opcion != 'exit':
    print(f'\n****--Bienvenido al inventario--****{menu()}')
    try:
        opcion = int(input()) #opcion recibirá por consola una opcion entre el 0 al 4
        if opcion in [0,1,2,3,4]:
            if opcion == 1:
                print(agregar_producto(input('Escribe el nombre del producto-> '),int(input('Agrega la cantidad de producto-> '))))
            elif opcion == 2:
                print(eliminar_producto(input('Escribe el nombre del producto-> ')))
            elif opcion == 3:
                print(consultar_cantidad(input('Escribe el nombre del producto-> ')))
            elif opcion == 4:
                print(inventario_completo())
            elif opcion == 0:
                print('Saliendo del inventario... ')
                opcion = 'exit'
        else:
            print('XX--Opcion inexistente, intente de nuevo--XX')
    except ValueError:
        print('XX--Opcion erronea, debe usar numeros. Intente de nuevo--XX')


## Codigo "mejorado" por ChatGPT (errores de codigo, no corregidos)
'''
import json

INVENTARIO_FILE = 'ejercicios_by_ChatGPT/02_productos/inventario.json'

def cargar_inventario():
    try:
        with open(INVENTARIO_FILE) as inventario_file:
            inventario = json.load(inventario_file)
        return inventario
    except FileNotFoundError:
        return {}

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, 'w') as inventario_file:
        json.dump(inventario, inventario_file, indent=4)

def agregar_producto(producto, cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            return 'Error en la cantidad del producto, no puede ser 0 o menor. Intente de nuevo'
    except ValueError:
        return 'Error, la cantidad debe ser un número entero'

    inventario = cargar_inventario()
    if producto.casefold() in inventario:
        inventario[producto.casefold()] += cantidad
        guardar_inventario(inventario)
        return '---Cantidad de producto actualizada---'
    else:
        inventario[producto.casefold()] = cantidad
        guardar_inventario(inventario)
        return '---Producto agregado correctamente---'

def eliminar_producto(producto):
    inventario = cargar_inventario()
    if producto.casefold() in inventario:
        del inventario[producto.casefold()]
        guardar_inventario(inventario)
        return '---El producto fue eliminado del inventario correctamente---'
    else:
        return 'XX-Ese producto no está en el inventario-XX'

def consultar_cantidad(producto):
    inventario = cargar_inventario()
    if producto.casefold() in inventario:
        return f'---La cantidad disponible de {producto.casefold()} es {inventario[producto.casefold()]} unidades---'
    else:
        return 'XX-No existe este producto en el inventario-XX'

def mostrar_inventario():
    inventario = cargar_inventario()
    return json.dumps(inventario, indent=4)

def menu():
    opciones = {
        1: {'nombre': 'Agregar producto al inventario', 'funcion': agregar_producto},
        2: {'nombre': 'Eliminar producto del inventario', 'funcion': eliminar_producto},
        3: {'nombre': 'Consultar cantidad de producto en el inventario', 'funcion': consultar_cantidad},
        4: {'nombre': 'Mostrar inventario completo', 'funcion': mostrar_inventario},
        0: {'nombre': 'Salir del programa', 'funcion': None}
    }

    while True:
        print('\n****--Bienvenido al inventario--****')
        for opcion, data in opciones.items():
            print(f'{opcion}_{data["nombre"]}')

        opcion = input()
        if opcion.isdigit() and int(opcion) in opciones:
            opcion = int(opcion)
            if opcion == 0:
                print('Saliendo del inventario...')
                break
            else:
                producto = input('Escribe el nombre del producto -> ')
                cantidad = input('Agrega la cantidad de producto -> ')
                funcion = opciones[opcion]['funcion']
                if funcion is not None:
                    resultado = funcion(producto, cantidad)
                    print(resultado)
        else:
            print('Opción inválida. Intente de nuevo.')

if __name__ == '__main__':
    menu()
'''
#Codigo original por mi
import os 

def acceder_archivo(ruta): #el enconding sirve para que no haya errores en cuanto a las vocales con acentos
    while True:
        try:
            with open(ruta,encoding='utf-8') as abierto:
                return abierto.read()        
        except FileNotFoundError:
            print('Error: ese archivo no existe dentro de la carpeta de archivos\n')
            ruta,nombre = encontrar_archivo()

def separar_las_palabras(archivo):
    return archivo.split()

def contar_palabras(texto,nombre_de_archivo):
    return f'La cantidad de palabras que contiene el archivo "{nombre_de_archivo}" son: {len(texto)} palabras'

def encontrar_archivo():

    print('Aviso: el archivo debe estar en la carpeta de archivos, ademas debe ser un archivo .txt')
    nombre = input('Nombre del archivo de texto-> ')
    ruta = f'ejercicios_by_ChatGPT/carpeta de archivos/{nombre}.txt'
    return ruta,nombre

def menu():

    def mostrar_opciones():
        print('\nOperaciones disponibles:')
        print('1. Imprimir el contenido del archivo')
        print('2. Contar la cantidad de las palabras en el archivo')
        print('3. Cambiar de archivo')
        print('0. Salir del programa')
        return int(input('Escoja la operacion que desea realizar: '))

    def verificar_y_recibir_opcion():
        try:
            opcion = mostrar_opciones()
            if opcion in [0,1,2,3]:
                return opcion
            else:
                print('Opcion no valida')
        except ValueError:
            print('Error: escriba una opcion valida')
            
    print('-----------Bienvenido-----------')
    print('Este programa se encarga de operar con archivos de texto')    
    print('Primero ingrese el nombre del archivo\n')
    ruta,nombre = encontrar_archivo()

    while True:
        opcion = verificar_y_recibir_opcion()

        if opcion == 1:
            print(f'{acceder_archivo(ruta)}')
        elif opcion == 2:
            print(contar_palabras(separar_las_palabras(acceder_archivo(ruta)),nombre))
        elif opcion == 3:
            print('\nIngrese el nombre del nuevo archivo')
            ruta,nombre = encontrar_archivo()
        elif opcion == 0:
            break

    print('Adios :)')


## Codigo mejora por ChatGPT

def acceder_archivo(ruta):
    while True:
        try:
            with open(ruta, encoding='utf-8') as archivo:
                return archivo.read()  # Lee el contenido del archivo
        except FileNotFoundError:
            print('Error: El archivo no existe en la carpeta de archivos.')
            ruta, nombre = encontrar_archivo()  # Vuelve a solicitar el nombre del archivo

def separar_las_palabras(archivo):
    return archivo.split()  # Separa las palabras del archivo en una lista

def contar_palabras(texto, nombre_de_archivo):
    cantidad_palabras = len(texto)  # Obtiene la cantidad de palabras en el texto
    return f'La cantidad de palabras que contiene el archivo "{nombre_de_archivo}" es: {cantidad_palabras} palabras.'

def encontrar_archivo():
    print('Aviso: El archivo debe estar en la carpeta de archivos y tener la extensión .txt')
    nombre = input('Nombre del archivo de texto: ')
    ruta = f'ejercicios_by_ChatGPT/carpeta de archivos/{nombre}.txt'
    return ruta, nombre  # Retorna la ruta y el nombre del archivo

def mostrar_opciones():
    print('\nOperaciones disponibles:')
    print('1. Imprimir el contenido del archivo.')
    print('2. Contar la cantidad de palabras en el archivo.')
    print('3. Cambiar de archivo.')
    print('0. Salir del programa.')
    return int(input('Seleccione la operación que desea realizar: '))  # Solicita la opción al usuario

def verificar_y_recibir_opcion():
    while True:
        try:
            opcion = mostrar_opciones()
            if opcion in [0, 1, 2, 3]:
                return opcion
            else:
                print('Opción no válida.')
        except ValueError:
            print('Error: Ingrese una opción válida.')

def menu():
    print('-----------Bienvenido-----------')
    print('Este programa se encarga de operar con archivos de texto.')
    print('Primero ingrese el nombre del archivo.\n')
    ruta, nombre = encontrar_archivo()  # Solicita el nombre del archivo

    while True:
        opcion = verificar_y_recibir_opcion()  # Verifica y recibe la opción seleccionada

        if opcion == 1:
            contenido = acceder_archivo(ruta)  # Accede al contenido del archivo
            print(contenido)  # Imprime el contenido del archivo
        elif opcion == 2:
            contenido = acceder_archivo(ruta)  # Accede al contenido del archivo
            palabras = separar_las_palabras(contenido)  # Separa las palabras del archivo
            resultado = contar_palabras(palabras, nombre)  # Cuenta las palabras del archivo
            print(resultado)  # Imprime el resultado del conteo de palabras
        elif opcion == 3:
            print('\nIngrese el nombre del nuevo archivo.')
            ruta, nombre = encontrar_archivo()  # Cambia de archivo
        elif opcion == 0:
            break  # Sale del programa

    print('¡Adiós!')

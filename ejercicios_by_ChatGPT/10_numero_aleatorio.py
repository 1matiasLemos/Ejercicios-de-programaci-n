## Numero aleatorio
## Codigo hecho por mi

from random import randint
from functools import reduce

def verificar_range(desde,hasta):
    return desde < hasta


def cantidad_de_numeros_a_generar():
    while True:
        try:
            cantidad = int(input('¿Cuantos numeros desea generar? -> '))
            if cantidad <= 0:
                print('Error: la cantidad no puede ser cero\n')
            else:
                return cantidad
        except ValueError:
            print('Error: ingrese un numero entero para indicar la cantidad de números\n')


def pedir_rango():
    while True:
        print('Ecriba el rango: ')
        try:
            desde = int(input('Desde -> '))
            hasta = int(input('Hasta -> '))
            return desde,hasta
        except ValueError:
            print('Error: escriba números enteros para establecer el rango\n')


def sumar_todos_los_pares(lista):
    lista = [int(i) for i in lista]
    lista = [i for i in lista if i % 2 == 0]
    return sum(lista)


def separar_numeros_impares(lista):
    lista = [int(i) for i in lista]
    lista = [i for i in lista if i % 2 != 0]
    return lista


def producto_de_numeros_impares(lista):
    resultado = reduce(lambda valor1,valor2: valor1 * valor2,lista)
    return resultado


def generar_numero():

    desde, hasta = pedir_rango()

    if verificar_range(desde,hasta):

        numeros = '--'.join(str(randint(desde,hasta)) for i in range(cantidad_de_numeros_a_generar()))

        print(f'\nNúmeros aleatorios entre {desde} a {hasta}:   {numeros}')
        print(f'Resultado de la suma de todos los numeros pares {sumar_todos_los_pares(numeros.split("--"))}')
        print(f'Resultado del producto de los números impares {producto_de_numeros_impares(separar_numeros_impares(numeros.split("--")))}')

    else:
        print('Error: el rango debe empezar desde un número base hasta un máximo rango')

generar_numero()


## Codigo mejorado por ChatGPT

def verificar_range(desde, hasta):
    return desde < hasta

def cantidad_de_numeros_a_generar():
    while True:
        try:
            cantidad = int(input('¿Cuántos números desea generar? -> '))
            if cantidad <= 0:
                print('Error: la cantidad debe ser mayor a cero\n')
            else:
                return cantidad
        except ValueError:
            print('Error: ingrese un número entero para indicar la cantidad de números\n')

def pedir_rango():
    while True:
        print('Escriba el rango: ')
        try:
            desde = int(input('Desde -> '))
            hasta = int(input('Hasta -> '))
            if verificar_range(desde, hasta):
                return desde, hasta
            else:
                print('Error: el rango debe ser válido (desde < hasta)\n')
        except ValueError:
            print('Error: escriba números enteros para establecer el rango\n')

def sumar_todos_los_pares(lista):
    lista = [int(i) for i in lista]
    lista = [i for i in lista if i % 2 == 0]
    return sum(lista)

def separar_numeros_impares(lista):
    lista = [int(i) for i in lista]
    lista = [i for i in lista if i % 2 != 0]
    return lista

def producto_de_numeros_impares(lista):
    resultado = reduce(lambda valor1, valor2: valor1 * valor2, lista)
    return resultado

def generar_numero():
    desde, hasta = pedir_rango()

    numeros = '--'.join(str(randint(desde, hasta)) for i in range(cantidad_de_numeros_a_generar()))

    print(f'\nNúmeros aleatorios entre {desde} y {hasta}:   {numeros}')
    print(f'Resultado de la suma de todos los números pares: {sumar_todos_los_pares(numeros.split("--"))}')
    print(f'Resultado del producto de los números impares: {producto_de_numeros_impares(separar_numeros_impares(numeros.split("--")))}')

generar_numero()

## Codigo original por mi
"""El programa debe convertir unidades de temperatura (Celsius, Fahrenheit y Kelvin); recive valores de una unidad para luego
pasar o convertir a otra unidad, por ejemplo de Celsius a Fahrenheit, etc.
El usuario puede ingresar el valor a convertir mediante la consola.
"""
def grados_celcius(valor,tipo):
    
    if tipo == 'Fahrenheit':
        temperatura = (valor - 32) / 1.8
        if temperatura <= -273.15:
            return f'\nLa temperatura alcanza el 0 absoluto -273.15 Celcius'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Celcius'
    elif tipo == 'Kelvin':
        temperatura = valor - 273.15
        if temperatura <= -273.15:
            return f'\nLa temperatura alcanza el 0 absoluto -273.15 Celcius'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Celcius'
    else:
        return f'\nSon {valor} grados Celcius'
    
def grados_fahrenheit(valor,tipo):

    if tipo == 'Celcius':
        temperatura = (valor * 1.8) + 32
        if temperatura <= -459.67:
            return f'\nLa temperatura alcanza el 0 absoluto -459.67 Fahrenheit'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Fahrenheit'
        
    elif tipo == 'Kelvin':
        temperatura = (valor - 273.15) * 1.8 + 32
        if temperatura <= -459.67:
            return f'\nLa temperatura alcanza el 0 absoluto -459.67 Fahrenheit'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Fahrenheit'
    else:
        return f'\nSon {valor} grados Fahrenheit'

def grados_kelvin(valor,tipo):

    if tipo == 'Celcius':
        temperatura = valor + 273.15
        if temperatura <= 0:
            return f'\nLa temperatura alcanza el 0 absoluto 0 Kelvin'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Kelvin'
        
    elif tipo == 'Fahrenheit':
        temperatura = (valor + 459.67) / 1.8
        if temperatura <= 0:
            return f'\nLa temperatura alcanza el 0 absoluto 0 Kelvin'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura} Kelvin'
    else:
        return f'Son {valor} grados Kelvin'
    
def pedir_datos():
    while True:
        try:
            valor = int(input('Ingrese un valor: '))
            while True:
                try:
                    print('\n1. Grados Celsius')
                    print('2. Grados Fahrenheit')
                    print('3. Grados Kelvin.            0.Cancelar y Salir')
                    tipo_de_unidad = int(input('¿A qué tipo de unidad corresponde el valor? '))
                    if tipo_de_unidad == 0:
                        return valor, tipo_de_unidad
                    elif tipo_de_unidad not in range(1,4):
                        print('Error: opcion no valida')
                    else:
                        return valor, tipo_de_unidad
                except ValueError:
                    print('Error: escriba un numero para seleccionar')
        except ValueError:
            print('Error: escriba un numero')

def menu1():
    print('--- Bienvenido al conversor de unidades de temperaturas ---\n')
    while True:
        unidades_de_grados = ['','Celcius', 'Fahrenheit','Kelvin']
        try:
            valor, tipo_de_unidad = pedir_datos()
            if tipo_de_unidad in [1,2,3]:
                tipo_de_unidad = unidades_de_grados[tipo_de_unidad]
                print('\nAhora escoja a que tipo de unidad desea convertir')
                print('1. Grados Celsius')
                print('2. Grados Fahrenheit')
                print('3. Grados Kelvin.')
                unidad = int(input('Escoja un opcion: '))
                if unidad == 1:
                    print(grados_celcius(valor, tipo_de_unidad))
                elif unidad == 2:
                    print(grados_fahrenheit(valor,tipo_de_unidad))
                elif unidad == 3:
                    print(grados_kelvin(valor,tipo_de_unidad))
            elif tipo_de_unidad == 0:
                print('Programa finalizado.')
                break
            else: 
                print('Opcion no valida')
        except ValueError as e:
            print(e)


## Codigo mejorado por ChatGPT
def convertir_celsius(valor, tipo):
    if tipo == 'Fahrenheit':
        temperatura = (valor - 32) / 1.8
        if temperatura <= -273.15:
            return f'\nLa temperatura alcanza el cero absoluto (-273.15°C)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}°C'
    elif tipo == 'Kelvin':
        temperatura = valor - 273.15
        if temperatura <= -273.15:
            return f'\nLa temperatura alcanza el cero absoluto (-273.15°C)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}°C'
    else:
        return f'\nSon {valor} grados Celsius'


def convertir_fahrenheit(valor, tipo):
    if tipo == 'Celsius':
        temperatura = (valor * 1.8) + 32
        if temperatura <= -459.67:
            return f'\nLa temperatura alcanza el cero absoluto (-459.67°F)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}°F'
    elif tipo == 'Kelvin':
        temperatura = (valor - 273.15) * 1.8 + 32
        if temperatura <= -459.67:
            return f'\nLa temperatura alcanza el cero absoluto (-459.67°F)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}°F'
    else:
        return f'\nSon {valor} grados Fahrenheit'


def convertir_kelvin(valor, tipo):
    if tipo == 'Celsius':
        temperatura = valor + 273.15
        if temperatura <= 0:
            return f'\nLa temperatura alcanza el cero absoluto (0K)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}K'
    elif tipo == 'Fahrenheit':
        temperatura = (valor + 459.67) / 1.8
        if temperatura <= 0:
            return f'\nLa temperatura alcanza el cero absoluto (0K)'
        else:
            return f'\n{valor} grados {tipo} es igual a {temperatura:.2f}K'
    else:
        return f'\nSon {valor} grados Kelvin'


def pedir_datos():
    while True:
        try:
            valor = float(input('Ingrese un valor: '))
            while True:
                print('\n1. Grados Celsius')
                print('2. Grados Fahrenheit')
                print('3. Grados Kelvin')
                print('0. Cancelar y salir')
                tipo_de_unidad = int(input('¿A qué tipo de unidad corresponde el valor? '))
                if tipo_de_unidad == 0:
                    return valor, tipo_de_unidad
                elif tipo_de_unidad not in range(1, 4):
                    print('Error: opción no válida')
                else:
                    return valor, tipo_de_unidad
        except ValueError:
            print('Error: ingrese un valor numérico')


def menu2():
    print('--- Bienvenido al conversor de unidades de temperaturas ---\n')
    while True:
        unidades_de_grados = ['', 'Celsius', 'Fahrenheit', 'Kelvin']
        valor, tipo_de_unidad = pedir_datos()
        if tipo_de_unidad == 0:
            print('Programa finalizado.')
            break
        elif tipo_de_unidad in range(1, 4):
            tipo_de_unidad = unidades_de_grados[tipo_de_unidad]
            print('\nAhora elija a qué tipo de unidad desea convertir')
            print('1. Grados Celsius')
            print('2. Grados Fahrenheit')
            print('3. Grados Kelvin')
            unidad = int(input('Seleccione una opción: '))
            if unidad in range(1, 4):
                if unidad == 1:
                    print(convertir_celsius(valor, tipo_de_unidad))
                elif unidad == 2:
                    print(convertir_fahrenheit(valor, tipo_de_unidad))
                elif unidad == 3:
                    print(convertir_kelvin(valor, tipo_de_unidad))
            else:
                print('Error: opción no válida')
        else:
            print('Error: opción no válida')


menu2()

from functools import reduce

def factorial(numero):

    factorial = reduce(lambda value1, value2: value1 * value2,[unidad for unidad in range(1,numero+1)])
    print(f'El factorial de {numero} es: {factorial}')

def menu():

    salir = False
    print('++++++++++++++++++++++++++++++++++')
    print('+---Calculadora de factoriales---+')
    print('++++++++++++++++++++++++++++++++++\n')
    print('Nota: Para salir del programa solo presiones Enter cuando le pida un número\n')

    while True:
        try:
            numero = int(input('Ingrese un numero: '))
            if numero < 0:
                print('Ingrese un número no negativo ')
            else:
                factorial(numero) 
        except ValueError:
            return 'Error: ingrese un numero entero\n'

print(menu())
print('El programa finalizó, ¡¡Adios!!')
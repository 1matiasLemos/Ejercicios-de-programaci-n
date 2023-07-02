## Codigo original por mi
'''import random
def lista_aleatoria():
    return [random.randint(0,100) for i in range(13)]

def imprimir_lista_ordenada():
    lista_aleatoria = sorted(lista_de_numeros)
    return lista_aleatoria

def ingresar_numero():
    while True: #el while true significa hasta que se retorne algo, de lo contrario seguirá
        try:
            numero_a_agregar = int(input('Escriba el numero -> '))
            return numero_a_agregar
        except ValueError:
            print('Por favor ingrese un numero, ya sea entero o decimal')

def agregar_numero():
    def verificar_duplicado() -> int:
        while True:
            imprimir_lista_ordenada()
            numero_a_examinar = ingresar_numero()
            if numero_a_examinar in lista_de_numeros:
                print('Este numero ya existe en la lista. Intente de nuevo')
            else:
                return numero_a_examinar
            
    numero = verificar_duplicado()
    lista_de_numeros.append(numero)
    return 'Numero agregado a la lista'

def existe_o_no(eliminar):
    return eliminar in lista_de_numeros  
      
def eliminar_elemento():
    imprimir_lista_ordenada()
    a_eliminar = ingresar_numero()
    if existe_o_no(a_eliminar):
        lista_de_numeros.remove(a_eliminar)
        return 'Se borró el numero de la lista'
    else:
        return 'Ese numero no existe en la lista'
    
def operaciones_matematicas():

    suma = lambda num1, num2: f'El resultado de la suma es: {(num1 + num2)}\n'
    resta = lambda num1, num2: f'El resultado de la resta es: {(num1 - num2)}\n'
    multiplicacion = lambda num1, num2: f'El resultado de la multiplicación es: {(num1 * num2)}\n'
    division = lambda num1, num2: f'El resultado de la división es: {(num1 / num2)}\n'

    def numeros_de_lista(numero1, numero2):
        while True:
            if existe_o_no(numero1) and existe_o_no(numero2):
                return numero1, numero2
            else:
                print(f'Error: ambos numeros deben ser de la lista. Intenta de nuevo\n{imprimir_lista_ordenada()}')
                numero1,numero2 = ingresar_numero(), ingresar_numero()

    while True:
        try:
            operaciones = ['Saliendo de operaciones...',suma,resta,multiplicacion,division]

            print('\nElige una operación:')
            print('1) Sumar')
            print('2) Restar')
            print('3) Multiplicar')
            print('4) Dividir')
            print('0) Salir')
            eleccion = int(input())

            if eleccion in [1,2,3,4]:
                print('Aviso: solo se podrá operar con dos numeros de la lista. Puede operar con el mismo numero')
                num1, num2 = numeros_de_lista(ingresar_numero(),ingresar_numero())
                print(operaciones[eleccion](num1,num2))

            elif eleccion == 0:
                return operaciones[eleccion]
            
            else:
                print('No existe esa opción, intente de nuevo')

        except ValueError:
            print('Error: no puede ingresar signos de puntuacion o letras, use numeros para elegir una opcion')
        except ZeroDivisionError:
            print('Error: no se puede dividir entre 0')

def menu():
    lista_de_numeros = lista_aleatoria()
    print('****Bienvenido a Manipulacion de listas****\n\nA continuacion verá un lista con números aleatorios:',end=' ')
    print(f'{lista_de_numeros}\nUsted elige que es lo que quiere hacer con esta lista\n')
    operaciones_para_la_lista = ['1) Agregar un nuevo número a la lista',
                                '2) Eliminar algun número de la lista',
                                '3) Ordenar la lista en orden de menor a mayor',
                                '4) Generar una nueva lista',
                                '5) Realizar operaciones matematicas con los números de la lista',
                                '0) Salir del programa']
    todas_las_operaciones = ['Adios :)',agregar_numero,eliminar_elemento,imprimir_lista_ordenada,lista_aleatoria,operaciones_matematicas]
    
    try: 
        while True:
            for i in operaciones_para_la_lista:
                print(i)
            eleccion_de_operaciones = int(input('Escoja su opción: '))
            if eleccion_de_operaciones in [1,2,3,4,5]:
                print(f'{todas_las_operaciones[eleccion_de_operaciones]()}\n')
            elif eleccion_de_operaciones == 0:
                return todas_las_operaciones[eleccion_de_operaciones]
            else:
                print('Error: esa opcion no existe, escoja una de las mostradas\n')

    except Exception as e:
        print(e)

print(menu())'''

## Codigo mejorado por ChatGPT

import random

def generar_lista_aleatoria():
    return [random.randint(0, 100) for _ in range(13)]

def imprimir_lista_ordenada(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

def ingresar_numero():
    while True:
        try:
            numero_a_agregar = int(input('Escriba el número -> '))
            return numero_a_agregar
        except ValueError:
            print('Por favor ingrese un número entero válido.')

def agregar_numero(lista):
    numero = ingresar_numero()
    if numero in lista:
        print('Este número ya existe en la lista. Intente de nuevo.')
    else:
        lista.append(numero)
        print('Número agregado a la lista.')

def eliminar_numero(lista):
    a_eliminar = ingresar_numero()
    if a_eliminar in lista:
        lista.remove(a_eliminar)
        print('Se eliminó el número de la lista.')
    else:
        print('Ese número no existe en la lista.')

def realizar_operaciones_matematicas(lista):
    suma = lambda num1, num2: num1 + num2
    resta = lambda num1, num2: num1 - num2
    multiplicacion = lambda num1, num2: num1 * num2
    division = lambda num1, num2: num1 / num2

    def obtener_numeros_de_lista():
        while True:
            num1 = ingresar_numero()
            num2 = ingresar_numero()
            if num1 in lista and num2 in lista:
                return num1, num2
            else:
                print('Ambos números deben estar en la lista. Intente de nuevo.')

    while True:
        print('\nElige una operación:')
        print('1) Sumar')
        print('2) Restar')
        print('3) Multiplicar')
        print('4) Dividir')
        print('0) Salir')

        eleccion = int(input())

        if eleccion == 1:
            num1, num2 = obtener_numeros_de_lista()
            resultado = suma(num1, num2)
            print(f'El resultado de la suma es: {resultado}')
        elif eleccion == 2:
            num1, num2 = obtener_numeros_de_lista()
            resultado = resta(num1, num2)
            print(f'El resultado de la resta es: {resultado}')
        elif eleccion == 3:
            num1, num2 = obtener_numeros_de_lista()
            resultado = multiplicacion(num1, num2)
            print(f'El resultado de la multiplicación es: {resultado}')
        elif eleccion == 4:
            num1, num2 = obtener_numeros_de_lista()
            if num2 == 0:
                print('Error: No se puede dividir entre 0.')
            else:
                resultado = division(num1, num2)
                print(f'El resultado de la división es: {resultado}')
        elif eleccion == 0:
            break
        else:
            print('No existe esa opción. Intente de nuevo.')

def menu():
    lista_numeros = generar_lista_aleatoria()
    print('**** Bienvenido a Manipulación de Listas ****\n')
    print('A continuación, verás una lista con números aleatorios:')
    print(lista_numeros)

    while True:
        print('\n¿Qué deseas hacer con esta lista?')
        print('1) Agregar un nuevo número a la lista')
        print('2) Eliminar un número de la lista')
        print('3) Ordenar la lista en orden de menor a mayor')
        print('4) Generar una nueva lista')
        print('5) Realizar operaciones matemáticas con los números de la lista')
        print('0) Salir del programa')

        eleccion = int(input('Escoja una opción: '))

        if eleccion == 1:
            agregar_numero(lista_numeros)
        elif eleccion == 2:
            eliminar_numero(lista_numeros)
        elif eleccion == 3:
            lista_ordenada = imprimir_lista_ordenada(lista_numeros)
            print('Lista ordenada:', lista_ordenada)
        elif eleccion == 4:
            lista_numeros = generar_lista_aleatoria()
            print('Nueva lista generada:', lista_numeros)
        elif eleccion == 5:
            realizar_operaciones_matematicas(lista_numeros)
        elif eleccion == 0:
            print('Adiós.')
            break
        else:
            print('Error: esa opción no existe. Por favor, elija una opción válida.')

menu()

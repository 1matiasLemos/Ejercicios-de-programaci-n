'''import random
import string

def generar_contraseña_aleatoria(longitud_caracteres = 0):#Funcion que retorna una contraseña aleatoria con simbolos
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        if longitud_caracteres == 0:
            contraseña = ''.join(random.choice(caracteres) for _ in range(random.randint(8,20)))
            return contraseña
        else:
            contraseña = ''.join(random.choice(caracteres) for _ in range(longitud_caracteres))
            return contraseña

def cantidad_de_caracteres_permitidos(): #funcion que se encarga de devolver un contraseña con 8 caracteres minimo
        while True:
            try:
                longitud = 0
                while longitud < 8: #si o si debe tener minimo 8 caracteres

                    longitud = int(input('Escriba un numero entre el 8/20-> '))
                    
                    if longitud in range(0,8):
                        print('Error: la longitud de la contraseña debe ser de 8 caracteres minimo')
                    else:
                        return longitud

            except ValueError:
                print('Error: debe escribir numeros enteros')

def agregar_caracter_especial(caracteres): #funcion para agregar caracteres especificos por el usuario, pero sin orden 

    #selecciona una o varias posiciones dentro de la contraseña para colocar ahi los caracteres que dio el usuario
    def posiciones_aleatorias(longitud_contraseña,cantidad_de_especiales):
        posiciones = []

        while len(posiciones) < len(cantidad_de_especiales): 
            #Toma en cuenta cuantos caracteres tiene la contraseña y genera un numero dentro de ese rango
            numero_random = random.randint(0,len(longitud_contraseña)-1) 
            #Si el numero se repite vuelve a generar otro hasta que no se repita
            if numero_random in posiciones: 
                pass
            else:
                #Si el numero no ha sido generado antes se agrega a la lista
                posiciones.append(numero_random)

        return posiciones #Todos los numeros son distintos, no hay iguales
    
    #la contraseña es una lista para facilitar la sobreescritura de los caracteres especiales del arg
    contraseña = list(generar_contraseña_aleatoria(cantidad_de_caracteres_permitidos()))
    
    #dentro de la funcion se agregan los caracteres y se devuelve la cotraseña modificada con los caracteres incluidos
    def escribir_caracteres(contraseña):
    
        #La lista posiciones contiene numeros aleatorios que serviran como indice o ubicaciones dentro de la list contraseña
        posiciones = posiciones_aleatorias(contraseña,caracteres) 
        index = 0
    
        #las repeticiones dependen de la cantidad de caracteres del arg
        for i in caracteres: #Se encarga de agregar los caracteres especiales que se le dieron como args
            #Toma una ubicacion aleatoria de algun caracter de la contraseña y lo reemplaza por uno de los caracteres especiales
            contraseña[posiciones[index]] = i 
            index += 1 

        #como bien dice la misma funcion
        def convertir_list_a_str(contraseña):
            contraseña_personalizada = ''
            #Transforma la lista a un str
            for i in contraseña:
                contraseña_personalizada += i
            return contraseña_personalizada
        
        return convertir_list_a_str(contraseña)

    return f'Tu nueva contraseña contiene los caracteres especiales que solicitaste: {escribir_caracteres(contraseña)}\n'


def menu():

    print('----Bienvenido al generador de contraseñas aleatorias----')
    while True:
        print('Seleccione que desea hacer: ')
        print('1. Generar contraseña aleatoria')
        print('2. Generar contraseña aleatoria con tal cantidad de caracteres')
        print('0. Salir')
        eleccion_operacion = int(input('Eleccion -> '))

        if eleccion_operacion == 1:
            print(f'Su contraseña es: {generar_contraseña_aleatoria()}\n')

        elif eleccion_operacion == 2:
            while eleccion_operacion == 2:
                try:
                    print('\nAviso: la contraseña debe tener minimo 8 caracteres!')
                    print('Agregar caracteres especiales?')
                    si_o_no = int(input('¿si(1) / no(0)? '))

                    if si_o_no == 1:
                
                        try:
                            print('\nLos caracteres deben escribirse sin espacios')
                            caracteres = input('Escriba que caracteres quiere que tenga su contraseña -> ')
                            print(agregar_caracter_especial(caracteres))
                            eleccion_operacion = 0

                        except TypeError:
                            print('Intente de nuevo')

                    elif si_o_no == 0:

                        contraseña_aleatoria = generar_contraseña_aleatoria(cantidad_de_caracteres_permitidos())
                        print(f'Su nueva contraseña: {contraseña_aleatoria}\n')
                        eleccion_operacion = 0

                    else:
                        print('Opción no valida')
                except ValueError:
                    print('Error: la eleccion debe ser 1 o 0')
        elif eleccion_operacion == 0:
            break
        else:
            print('Opcion no valida\n')
    return 'Adios :)'
'''

##Codigo mejorado por ChatGPT (Aclaracion: este codigo no toma en cuenta el manejo de excepciones)

import random
import string

def generar_contraseña_aleatoria(longitud_caracteres=0):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    if longitud_caracteres == 0:
        longitud_caracteres = random.randint(8, 20)
    return ''.join(random.choice(caracteres) for _ in range(longitud_caracteres))

def obtener_longitud_contraseña():
    while True:
        try:
            longitud = int(input('Escriba un número entre 8 y 20: '))
            if 8 <= longitud <= 20:
                return longitud
            print('Error: la longitud de la contraseña debe estar entre 8 y 20 caracteres.')
        except ValueError:
            print('Error: debe escribir un número entero.')

def agregar_caracter_especial(contraseña):
    caracteres_especiales = input('Escriba los caracteres especiales que desea incluir en la contraseña: ')
    for caracter in caracteres_especiales:
        posicion = random.randint(0, len(contraseña) - 1)
        contraseña = contraseña[:posicion] + caracter + contraseña[posicion+1:]
    return contraseña

def generar_contraseña_personalizada():
    longitud_contraseña = obtener_longitud_contraseña()
    contraseña = generar_contraseña_aleatoria(longitud_contraseña)
    agregar_especiales = input('¿Desea agregar caracteres especiales? (si/no): ')
    if agregar_especiales.lower() == 'si':
        contraseña = agregar_caracter_especial(contraseña)
    return contraseña

def menu():
    print('----Bienvenido al generador de contraseñas aleatorias----')
    while True:
        print('Seleccione qué desea hacer:')
        print('1. Generar contraseña aleatoria')
        print('2. Generar contraseña personalizada')
        print('0. Salir')
        opcion = input('Eleccion -> ')

        if opcion == '1':
            contraseña = generar_contraseña_aleatoria()
            print(f'Su contraseña es: {contraseña}\n')

        elif opcion == '2':
            contraseña = generar_contraseña_personalizada()
            print(f'Su nueva contraseña es: {contraseña}\n')

        elif opcion == '0':
            break

        else:
            print('Opción no válida\n')
    
    return 'Adiós :)'

print(menu())

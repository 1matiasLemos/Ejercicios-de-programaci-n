from math import sqrt, pow

suma = lambda num1, num2: num1 + num2
resta = lambda num1, num2: num1 - num2
multiplicacion = lambda num1, num2: num1 * num2
division = lambda num1, num2: num1 / num2
potencia = lambda num1, num2: pow(num1,num2)
raiz = lambda num: sqrt(num)

signo_operacion = {'+':suma,'-':resta,'*':multiplicacion,'/':division,'^':potencia,'V':raiz}

def obtener_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Ingresa un número entero válido")

def menu():
    
    nombre_operacion = {'+':'suma','-':'resta','*':'multiplicación','/':'división','^':'potenciación','V':'radicación'}
    lista_menu = ['Ingrese el primer número: ',
    'Ingrese el segundo número: ',
    'Ingrese la operación (+, -, *, /, ^, V): ',
    'El resultado de la']

    try:
        salir = 0
        while salir != 1:

            num1 = obtener_numero(lista_menu[0])
            num2 = obtener_numero(lista_menu[1])
            signo = input(lista_menu[2])
            if signo in signo_operacion.keys():
                if signo == 'V':
                    print('Al operar con raíces solo se tomará el primer número')
                    print( f'{lista_menu[3]} {nombre_operacion[signo]} es de {signo_operacion[signo](num1)}')
                    salir = obtener_numero('Salir? 1(si)/0(no) ')

                else:
                    print(f'{lista_menu[3]} {nombre_operacion[signo]} es de {signo_operacion[signo](num1, num2)}')
                    salir = obtener_numero('Salir? 1(si)/0(no) ')
            else:
                return 'Esa operación no está disponible en la calculadora XX'
        return 'Cerró el programa correctamente'
    except ValueError:
        return 'Error: Los números ingresados deben ser enteros'
    except ZeroDivisionError:
        return 'Error: No se puede dividir entre 0'
print(menu())
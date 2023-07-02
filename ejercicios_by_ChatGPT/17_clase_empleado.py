# Mi codigo :)

import re

class Empleado: 
    def __init__(self,formulario) -> None: #pide como arg un dict con todos los datos
        self.nombre = formulario['nombre']
        self.apellido = formulario['apellido']
        self.edad = formulario['edad']
        self.salario = formulario['salario']
        self.correo = formulario['correo']

    def datos_del_empleado(self): #imprime el nombre, apellido, edad, salario y correo

        print(f'\nNombre del empleado: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Salario en USD: {self.salario:.2f}')
        print(f'Correo electronico: {self.correo}')
        

    def salario_anual(self): #hace un calculo de cuanto gana el empleado con su sueldo en un año y lo imprime
        print(f'Salario anual aproximado {self.salario * 12} USD')


    def actualizar_datos(self): #actualiza todos los datos

        self.nombre = input('Nombre: ').capitalize() #solicita el nombre
        self.apellido = input('Apellido: ').capitalize() #solicita el apellido
        
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$' #RE para validar correo

        while True:
            try:
                edad = int(input('Edad: '))

                if edad < 18: #debe ser mayor de edad
                    print('No es posible ingresar los datos, edad insuficiente para trabajar')
                else:
                    self.edad = edad
                    break
            except ValueError:
                print('Ingrese la edad')

        while True:
            try:
                salario = int(input('Salario en USD: '))
                self.salario = salario
                break
            except ValueError:
                print('Ingrese un número entero para asignar su salario')

        while True:
            correo = input('Correo: ')

            if re.match(patron,correo): #utiliza una expresion regular para validar el correo
                self.correo = correo
                break
            print('Ingrese un correo válido')            

    
    def actualizar_email(self): #actualiza solo el correo del empleado
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$' #ER para validar correo
        
        while True:
            correo = input('Correo: ')
            if re.match(patron,correo):
                self.correo = correo
                break
            print('Ingrese un correo válido')


    def aplicar_aumento(self): #hace un calculo utilizando porcentaje (0%) que determina cuanto aumenta el sueldo con ese porcentaje y lo imprime

        while True:
            try:#calcula el 1% del salario; lo multiplica por el porcentaje ingresado y lo suma al salario actual
                self.salario = self.salario + ((self.salario / 100) * float(input('\nEscriba el porcentaje de aumento que recibirá el empleado\nPorcentaje: ')))
                break
            except ValueError:
                print('Error: ingrese un número, puede ser entero o decimal')
        print(f'Aumento de sueldo aplicado +{self.salario:.2f} USD') #para evitar imprimir decimales largos solo se limita a 2 luego de un punto (.)


def crear_archivo_de_empleado(): #pide el nombre, apellido, edad, salario y correo

    formulario = {'nombre':input('Nombre: ').capitalize(),'apellido':input('Apellido: ').capitalize(),'edad':int,'salario':int,'correo':str}

    while True:
        try:
            formulario['edad'] = int(input('Edad: '))

            if formulario['edad'] < 18:
                print('No es posible ingresar los datos, edad insuficiente para trabajar')
            else:
                break
        except ValueError:
            print('Ingrese la edad')

    while True:
        try:
            formulario['salario'] = float(input('Salario: '))
            break
        except ValueError:
            print('Ingrese un valor de salario')

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$' #ER para validar correo
    while True:
        formulario['correo'] = input('Ingrese un correo electrónico: ')

        if re.match(patron, formulario['correo']):
            break

        print('Por favor ingrese una dirección de correo válido')
        
    return formulario #devuelve un dict con todos los datos 


def inicio():
    
    print('Ingrese los datos del nuevo empleado')
    empleado = Empleado(crear_archivo_de_empleado()) #crea una clase
    print('\n¡Nuevo empleado agregado al personal!')

    while True:

        empleado.datos_del_empleado() #imprime los datos ingresados
        #dict de las funciones dentro de la clase Empleado, cada funcion tiene un entero como key
        dict_opciones = {1:empleado.salario_anual,2:empleado.aplicar_aumento,3:empleado.actualizar_email,4:empleado.actualizar_datos}

        while True: #solicita abrir o no la lista de opciones
            print('\n¿Desplegar lista de opciones?')
            abrir_o_no = input('s/n: ') #s (si)/ n (no)

            if abrir_o_no.casefold() == 's':
                while True: #se mantendrá dentro de la lista de opciones hasta que se seleccione "Cerrar lista"
                    print('\nLista de opciones')
                    print('1. Obtener salario anual')
                    print('2. Aplicar aumento')
                    print('3. Actualizar email')
                    print('4. Actualizar datos del empleado')
                    print('5. Cerrar lista')
                    try: #evita que se genere un ValueError por ingresar un dato no int
                        eleccion = int(input('Ecoja una opción: ')) 
                        if eleccion in [1,2,3,4]: 
                            dict_opciones[eleccion]() #llama al dict y usa la variable eleccion como key para acceder a la funcion dentro
                        elif eleccion == 5:
                            break #detiene el bucle de la lista de opciones l_133
                    except ValueError:
                        print('Intente de nuevo')

                break #detiene el bucle que solicita abrir la lista de opciones l_128

            elif abrir_o_no.casefold() == 'n':
                break #detiene el bucle que solicita abrir la lista de opciones l_128

        salir = input('\nSalir? s/n ') #salir del programa?
        if salir.casefold() == 's':
            break #detiene el bucle principal l_123



## Codigo mejorado por ChatGPT

class Empleado:
    def __init__(self, formulario):
        self.nombre = formulario['nombre']
        self.apellido = formulario['apellido']
        self.edad = formulario['edad']
        self.salario = formulario['salario']
        self.correo = formulario['correo']

    def datos_del_empleado(self):
        print(f'\nNombre del empleado: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Salario en USD: {self.salario:.2f}')
        print(f'Correo electrónico: {self.correo}')

    def salario_anual(self):
        print(f'Salario anual aproximado: {self.salario * 12:.2f} USD')

    def actualizar_datos(self):
        self.nombre = input('Nombre: ').capitalize()
        self.apellido = input('Apellido: ').capitalize()
        
        while True:
            try:
                self.edad = int(input('Edad: '))
                if self.edad < 18:
                    print('No es posible ingresar los datos, edad insuficiente para trabajar')
                else:
                    break
            except ValueError:
                print('Ingrese una edad válida')

        while True:
            try:
                self.salario = float(input('Salario en USD: '))
                break
            except ValueError:
                print('Ingrese un valor numérico para el salario')

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        while True:
            correo = input('Correo electrónico: ')
            if re.match(patron, correo):
                self.correo = correo
                break
            print('Ingrese un correo válido')

    def actualizar_email(self):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        while True:
            correo = input('Correo electrónico: ')
            if re.match(patron, correo):
                self.correo = correo
                break
            print('Ingrese un correo válido')

    def aplicar_aumento(self, porcentaje):
        self.salario += (self.salario * porcentaje) / 100
        print(f'Aumento de sueldo aplicado: {self.salario:.2f} USD')


def crear_formulario_empleado():
    # Crear un diccionario para almacenar los datos del formulario
    formulario = {
        'nombre': input('Nombre: ').capitalize(),
        'apellido': input('Apellido: ').capitalize(),
        'edad': None,
        'salario': None,
        'correo': None
    }

    while True:
        try:
            # Solicitar al usuario que ingrese la edad
            formulario['edad'] = int(input('Edad: '))

            if formulario['edad'] < 18:
                print('No es posible ingresar los datos, edad insuficiente para trabajar')
            else:
                break
        except ValueError:
            print('Ingrese una edad válida')

    while True:
        try:
            # Solicitar al usuario que ingrese el salario
            formulario['salario'] = float(input('Salario: '))
            break
        except ValueError:
            print('Ingrese un valor de salario válido')

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$' # ER para validar el correo electrónico

    while True:
        formulario['correo'] = input('Ingrese un correo electrónico: ')

        if re.match(patron, formulario['correo']):
            break

        print('Por favor ingrese una dirección de correo válida')

    return formulario


def inicio():
    # Imprimir mensaje para ingresar los datos del nuevo empleado
    print('Ingrese los datos del nuevo empleado')

    # Crear una instancia de la clase Empleado y pasar el formulario como argumento
    empleado = Empleado(crear_formulario_empleado())

    # Imprimir mensaje confirmando que el nuevo empleado ha sido agregado al personal
    print('\n¡Nuevo empleado agregado al personal!')

    while True:
        # Mostrar los datos del empleado
        empleado.datos_del_empleado()

        # Crear un diccionario con las opciones y los métodos correspondientes
        dict_opciones = {
            1: empleado.salario_anual,
            2: empleado.aplicar_aumento,
            3: empleado.actualizar_email,
            4: empleado.actualizar_datos
        }

        while True:
            # Preguntar al usuario si desea desplegar la lista de opciones
            print('\n¿Desplegar lista de opciones?')
            abrir_o_no = input('s/n: ').lower()

            if abrir_o_no == 's':
                while True:
                    # Mostrar el menú de opciones
                    print('\nLista de opciones')
                    print('1. Obtener salario anual')
                    print('2. Aplicar aumento')
                    print('3. Actualizar correo electrónico')
                    print('4. Actualizar datos del empleado')
                    print('5. Cerrar lista')

                    try:
                        # Solicitar al usuario que elija una opción
                        eleccion = int(input('Elija una opción: '))

                        if eleccion in [1, 2, 3, 4]:
                            if eleccion == 2:
                                # Si se elige la opción 2, solicitar el porcentaje de aumento
                                porcentaje = float(input('\nIngrese el porcentaje de aumento: '))
                                dict_opciones[eleccion](porcentaje)
                            else:
                                # Ejecutar el método correspondiente a la opción elegida
                                dict_opciones[eleccion]()
                        elif eleccion == 5:
                            # Salir del bucle interno si se elige la opción 5
                            break
                    except ValueError:
                        print('Ingrese un número válido')

                break
            elif abrir_o_no == 'n':
                break

        # Preguntar al usuario si desea salir del programa
        salir = input('\n¿Salir? s/n: ').lower()
        if salir == 's':
            break

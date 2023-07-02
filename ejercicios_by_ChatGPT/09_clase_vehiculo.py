class Vehiculo:
    def __init__(self,marca,modelo,año,color):
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.color = color
        self.velocimetro = 0
        self.posicion_de_cambio_de_marcha = 'N'
        self.motor = False

    def get_caracteristicas(self): #imprime las caracteristicas del auto
        print(f'Marca del vehiculo: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Año: {self.año}')
        print(f'Color: {self.color}')


    def set_nuevas_caracteristicas(self,marca1,modelo1,año1,color1): #cambia las caracteristicas del auto con los args que se le mandan
        self.marca = marca1
        self.modelo = modelo1
        self.año = año1
        self.color = color1


    def encender(self): #enciende el motor, True = motor encendido
        self.motor = True #indica que el motor está encendido
        print('El motor está en marcha')


    def apagar(self): #apaga el motor, False = motor apagado

        self.motor = False #indica que el motor está apagado
        print('Motor apagado')


    def cambiar_de_marcha(self): #esto sirve como si fuera la caja de cambios
        if self.posicion_de_cambio_de_marcha == 'N': #si está en neutro
            self.posicion_de_cambio_de_marcha = 1
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha}')
            print('Empieza a acelerar')
        elif self.posicion_de_cambio_de_marcha == 6: #si está en el ultimo cambio de la caja de cambios, no hará nada
            pass
        else:
            self.posicion_de_cambio_de_marcha += 1 #subirá un cambio
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha}')
    

    def bajar_marcha(self): #caja de cambios, toma en cuenta la velocidad y la reduce cada que baja un cambio
        if self.posicion_de_cambio_de_marcha == 1:
            self.posicion_de_cambio_de_marcha = 'N'

        elif self.posicion_de_cambio_de_marcha == 'N':
            pass
        else:
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha-1}')
            self.posicion_de_cambio_de_marcha -= 1 
            self.velocimetro -= 20


    def acelerar(self): #agrega velocidad al velocimetro, representado como numeros enteros
        if self.motor == True:
            if self.velocimetro <= 160: #si se pasa ese limite, no se puede acelerar mas

                if self.posicion_de_cambio_de_marcha == 'N':
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 1:
                    self.velocimetro += 5
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 2:
                    self.velocimetro += 8
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 3:
                    self.velocimetro += 12
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 4:
                    self.velocimetro += 15
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 5:
                    self.velocimetro += 18
                    print('\nAcelerando...')
                elif self.posicion_de_cambio_de_marcha == 6:
                    self.velocimetro += 20
                    print('\nAcelerando...') 

        else:
            print('El motor está pagado')


    def desacelerar(self): #quita velocidad al velocimetro, tambien baja un cambio cada que desaceleras
        if self.motor == False and self.velocimetro > 0: #en caso de que se apague el motor cuando está andando
            print(f'\nDesacelerando... ')
            desaceleracion = 'km-> '.join(str(velocidad) for velocidad in range(self.velocimetro,0,-4))
            print(f'{desaceleracion}') #representa la velocidad bajando
            self.velocimetro = 0
        else:
            print(f'\nDesacelerando... ')
            print(f'{self.velocimetro}km-> {self.velocimetro-10}km')
            self.velocimetro -= 15
            self.posicion_de_cambio_de_marcha -= 1


    def estado_del_motor(self): #imprime el velocimetro y la caja de cambios
        print(f'\nPosicion {self.posicion_de_cambio_de_marcha}')
        print(f'Velocimetro-> {self.velocimetro}km\n')


def pedir_caracteristicas(): #pide la marca, modelo, año y color, para cambiar los valores por defecto
    print('\nEscriba el nombra de la marca:')
    marca = input('Marca: ')
    print('\nEscriba el nombra del modelo de auto:')
    modelo = input('Modelo: ')
    print('\nEscriba el año del modelo:')
    año = int(input('Año: '))
    print('\nEscriba el color del auto:')
    color = input('Color: ')
    print('Cargando datos....\n')
    return marca, modelo, año, color


def cambio_de_caracteristicas(): #como dice, envia los nuevos valores y los actualiza
    cambiar_caracteristicas = ''
    while cambiar_caracteristicas != 'no': #Si el usuario quiere cambiarle los atributos
        print('\nEscriba si o no: ')
        cambiar_caracteristicas = input('Desea cambiar las caracteristicas de tu auto? ')

        if cambiar_caracteristicas == 'si':
            marca, modelo, año, color = pedir_caracteristicas()
            vehiculo.set_nuevas_caracteristicas(marca,modelo,año,color) 
            vehiculo.get_caracteristicas()


def menu_inicial():

    print('Auto por defecto:\n')
    vehiculo.get_caracteristicas()


def interfaz_del_auto():

    menu_inicial()
    cambio_de_caracteristicas()

    llave_de_encendido = int(input('Encender (1)/ apagar (0) '))

    if llave_de_encendido == 1:
        vehiculo.encender()
    else:
        vehiculo.apagar() #al apagar el vehiculo termina la operacion y se sale de la funcion

    if vehiculo.motor == True: #si el motor está encendido
        vehiculo.estado_del_motor()
        while True:
            print('1. Acelerar  2. Poner marcha  3.Bajar marcha  4. Desacelerar 5. Apagar motor')
            opcion = int(input('Acción -> '))

            if opcion in [1,2,3,4,5]:
                if opcion == 1:
                    vehiculo.acelerar()
                    vehiculo.estado_del_motor()

                elif opcion == 2:
                    vehiculo.cambiar_de_marcha()
                    vehiculo.estado_del_motor()

                elif opcion == 3:    
                    vehiculo.bajar_marcha()
                    vehiculo.estado_del_motor()

                elif opcion == 4:
                    vehiculo.desacelerar()
                    vehiculo.estado_del_motor()

                elif opcion == 5:
                    if vehiculo.velocimetro != 0: #si el motor se apaga cuando se está moviendo
                        vehiculo.apagar()
                        vehiculo.desacelerar() 
                        vehiculo.estado_del_motor()
                        print('El vehiculo se detuvo')
                    else:
                        vehiculo.apagar()
                        vehiculo.estado_del_motor()
                    break
            else:
                print('No existe esa opción\n')


vehiculo = Vehiculo('Toyota','Corolla',2015,'Negro') #vehiculo por defecto
interfaz_del_auto()
print('El programa finalizó, ¡Adios!')


## Codigo por ChatGPT

class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        # Constructor que inicializa los atributos del vehículo
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.color = color
        self.velocimetro = 0
        self.posicion_de_cambio_de_marcha = 'N'
        self.motor = False

    def get_caracteristicas(self):
        # Imprime las características del vehículo
        print(f'Marca del vehículo: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Año: {self.año}')
        print(f'Color: {self.color}')

    def set_nuevas_caracteristicas(self, marca, modelo, año, color):
        # Actualiza las características del vehículo con los nuevos valores
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def encender(self):
        # Enciende el motor
        self.motor = True
        print('El motor está en marcha')

    def apagar(self):
        # Apaga el motor
        self.motor = False
        print('Motor apagado')

    def cambiar_de_marcha(self):
        # Cambia la marcha del vehículo
        if self.posicion_de_cambio_de_marcha == 'N':
            self.posicion_de_cambio_de_marcha = 1
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha}')
            print('Empieza a acelerar')
        elif self.posicion_de_cambio_de_marcha == 6:
            pass
        else:
            self.posicion_de_cambio_de_marcha += 1
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha}')

    def bajar_marcha(self):
        # Baja la marcha del vehículo
        if self.posicion_de_cambio_de_marcha == 1:
            self.posicion_de_cambio_de_marcha = 'N'
        elif self.posicion_de_cambio_de_marcha == 'N':
            pass
        else:
            self.posicion_de_cambio_de_marcha -= 1 
            self.velocimetro -= 20
            print(f'\nCambio de marcha -> {self.posicion_de_cambio_de_marcha}')

    def acelerar(self):
        # Acelera el vehículo
        if self.motor:
            if self.velocimetro <= 160:
                cambios = {
                    'N': 0,
                    1: 5,
                    2: 8,
                    3: 12,
                    4: 15,
                    5: 18,
                    6: 20
                }
                self.velocimetro += cambios[self.posicion_de_cambio_de_marcha]
                print('\nAcelerando...')
        else:
            print('El motor está apagado')

    def desacelerar(self):
        # Desacelera el vehículo
        if self.velocimetro > 0:
            print(f'\nDesacelerando... ')
            if self.motor:
                desaceleracion = 'km-> '.join(str(velocidad) for velocidad in range(self.velocimetro, 0, -4))
                print(f'{desaceleracion}')
                self.posicion_de_cambio_de_marcha -= 1
            self.velocimetro = 0
        else:
            print('El vehículo ya está detenido')

    def estado_del_motor(self):
        # Imprime el estado del motor y el velocímetro
        print(f'\nPosición {self.posicion_de_cambio_de_marcha}')
        print(f'Velocímetro -> {self.velocimetro} km/h')


def pedir_caracteristicas():
    # Pide al usuario las características del vehículo
    print('\nEscriba el nombre de la marca:')
    marca = input('Marca: ')
    print('\nEscriba el nombre del modelo de auto:')
    modelo = input('Modelo: ')
    print('\nEscriba el año del modelo:')
    año = int(input('Año: '))
    print('\nEscriba el color del auto:')
    color = input('Color: ')
    print('Cargando datos....\n')
    return marca, modelo, año, color


def cambio_de_caracteristicas(vehiculo):
    # Permite al usuario cambiar las características del vehículo
    cambiar_caracteristicas = ''
    while cambiar_caracteristicas != 'no':
        print('\nEscriba si o no: ')
        cambiar_caracteristicas = input('¿Desea cambiar las características de su auto? ')

        if cambiar_caracteristicas == 'si':
            marca, modelo, año, color = pedir_caracteristicas()
            vehiculo.set_nuevas_caracteristicas(marca, modelo, año, color)
            vehiculo.get_caracteristicas()


def menu_inicial(vehiculo):
    # Muestra las características del vehículo por defecto
    print('Auto por defecto:\n')
    vehiculo.get_caracteristicas()


def interfaz_del_auto():
    vehiculo = Vehiculo('Toyota', 'Corolla', 2015, 'Negro')
    menu_inicial(vehiculo)
    cambio_de_caracteristicas(vehiculo)

    llave_de_encendido = int(input('Encender (1) / Apagar (0): '))

    if llave_de_encendido == 1:
        vehiculo.encender()
    else:
        vehiculo.apagar()

    if vehiculo.motor:
        vehiculo.estado_del_motor()
        while True:
            print('1. Acelerar  2. Poner marcha  3. Bajar marcha  4. Desacelerar  5. Apagar motor  6. Salir')
            opcion = int(input('Acción -> '))

            if opcion in [1, 2, 3, 4, 5, 6]:
                if opcion == 1:
                    vehiculo.acelerar()
                elif opcion == 2:
                    vehiculo.cambiar_de_marcha()
                elif opcion == 3:
                    vehiculo.bajar_marcha()
                elif opcion == 4:
                    vehiculo.desacelerar()
                elif opcion == 5:
                    vehiculo.apagar()
                    if vehiculo.velocimetro != 0:
                        vehiculo.desacelerar()
                        print('El vehículo se detuvo')
                    break
                elif opcion == 6:
                    break
                vehiculo.estado_del_motor()
            else:
                print('No existe esa opción')

    print('El programa finalizó. ¡Adiós!')


interfaz_del_auto()

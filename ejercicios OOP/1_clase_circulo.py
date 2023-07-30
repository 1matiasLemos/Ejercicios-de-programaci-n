from math import pi

class Circle():
    def __init__(self,radio,) -> None:
        self.radio = radio

    def calcular_perimetro(self):
        print(f'\nEl perimetro de un circulo con {self.radio}cm de radio es: {2*pi*self.radio:.2f}cm')
    
    def calcular_diametro(self):
        print(f'\nEl diametro de un circulo con {self.radio}cm de radio es: {self.radio/pi:.2f}')

    def cambiar_radio(self):

        while True:
            try:
                self.radio = float(input('Ingrese el valor del radio: '))
                break
            except ValueError:
                print('Error: ingrese un valor correspondiente')


def escojer_operaciones():

    print('\nEscoja una de las siguiente operaciones que desee hacer con el circulo')
    print('1.Calcular el perimetro')
    print('2.Calcular el diametro')
    print('3.Cambiar el radio del circulo')
    while True:
        try:
            opcion = int(input('Elija una opción__ '))
            if opcion not in [1,2,3]:
                raise ValueError
            else:
                break
        except ValueError as e:
            print('Error: opción no valida')
    return opcion

try:
    my_circle = Circle(float(input('Valor del radio: ')))
except ValueError as e:
    print('Error: ingrese un número', e)

operaciones = {1:my_circle.calcular_perimetro,2:my_circle.calcular_diametro,3:my_circle.cambiar_radio}

intentos: int = 0
while intentos < 3:
    operaciones[escojer_operaciones()]()
    intentos+=1
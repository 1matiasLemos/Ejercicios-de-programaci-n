num_uno = int(input('1er numero: '))
num_dos = int(input('2do numero: '))
print('1) Suma\n2) Resta\n3) Multiplicación\n4) División')
eleccion = int(input())

def suma(num_uno, num_dos):
    return num_uno + num_dos

def resta(num_uno, num_dos):
    return num_uno - num_dos

def multiplicacion(num_uno, num_dos):
    return num_uno * num_dos

def division(num_uno, num_dos):
    return num_uno / num_dos

if eleccion == 1:
    print(f'{num_uno} + {num_dos} = {suma(num_uno,num_dos)}')
elif eleccion == 2:
    print(f'{num_uno} - {num_dos} = {resta(num_uno,num_dos)}')
elif eleccion == 3:
    print(f'{num_uno} x {num_dos} = {multiplicacion(num_uno, num_dos)}')
elif eleccion == 4:
    print(f'{num_uno} % {num_dos} = {division(num_uno, num_dos)}')
else:
    print('La opción elegida no existe')


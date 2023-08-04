
import random
import subprocess
import re

def limpiar_consola_windows():
    subprocess.call('cls', shell=True)


class Roullette():
    def __init__(self,saldo) -> None:
        self.saldo:float = saldo #Saldo en fichas para hacer apuestas
        self.numeros_color:dict = { #cada numero tiene su respectivo color (r: Rojo) (n: Negro) y (v:Verde)
            3:'r', 6:'n', 9:'r', 12:'r', 15:'n', 18:'r', 21:'r', 24:'n', 27:'r', 30:'r', 33:'n', 36:'r',
            2:'n', 5:'r', 8:'n', 11:'n', 14:'r', 17:'n', 20:'n', 23:'r', 26:'n', 29:'n', 32:'r', 35:'n',
            1:'r', 4:'n', 7:'r', 10:'n', 13:'n', 16:'r', 19:'r', 22:'n', 25:'r', 28:'n', 31:'n', 34:'r',
            0:'v'
        }

        self.tablero= ('  _________________________________________________________________\n' +
                        ' |   | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |_1:3|\n' +
                        '{  0 | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |_1:3|\n' +
                        ' |___| 1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 |_1:3|\n' + 
                        '     |_____1ro 12_____|______2do 12_______|______3ro 12_______|  \n'+
                        '     |__1-18_|___par__|___rojo__|__negro__|__impar__|__19-36__|\n'   
                         )


        self.filas_de_doce = {
            1:range(3,37,3),#'fila1' 3,6,9,...,36
            2:range(2,36,3),#'fila2' 2,5,8,11,...,35
            3:range(1,35,3)#'fila3' 1,4,7,10,...,34
        }
        
        self.columnas_de_seis ={
            1:range(1,7),#'1ra fila' 1 al 6
            2:range(7,13),#'2da fila' 7 al 12
            3:range(13,19),#'3ra fila 13 al 18
            4:range(19,25),#'4ta fila 19 al 25
            5:range(25,31), #'5ta fila' 25 al 31
            6:range(31,37) #'6ta fila' 31 al 37
        }
        
        self.colores = {'r':'Rojo','n':'Negro','v':'verde'}

        self.columnas_de_doce:dict = {
            1: range(1,13), #primera columna de doce (1 al 12)
            2: range(13,25), #segunda columna de doce (13 al 24)
            3: range(25,37) #tercera columna de doce (25 al 36)
        }


    def girar_ruleta(self,numeros_apostados:list): #recibe una lista con los números escogidos por el usuario

        numero_random = random.randint(0,36) #genera un numero aleatorio entre 0 al 36
        print(f'Nro: {numero_random}-{self.colores[self.numeros_color[numero_random]]}') #imprime el numero y el color correspondiente

        if numero_random in numeros_apostados: #si el número que salió es uno de los números que apostaste
            print('¡Tu ganas!') #mensaje de salida
            return True #Ganador
        else:
            return False #Perdedor


    def apuesta(self,tipo_de_apuesta:int,monto_apostado:int): #recibe un int(1-5) y otro int que es la cantidad en fichas
        
        def escoger_numeros_por_columnas(tipo_de_juego:int):

            rango_por_tipo_de_apuesta = {
                1:range(1,4), #rango para escojer una de las tres columnas de 12 numeros
                2:range(1,7), #rango para escojer una de las seis columnas de 6 numeros
                3:range(1,4)  #rango para escojer una de las tres filas de 12 numeros
            }
            tipo_de_columna = {
                1:self.columnas_de_doce, 
                2:self.columnas_de_seis,
                3:self.filas_de_doce
            }

            while True:
                try:
                    numeros = int(input('Columna nro: -> ')) 
                    if numeros in rango_por_tipo_de_apuesta[tipo_de_juego]: #esto da un range, dependiendo el tipo de apuesta
                        return tipo_de_columna[tipo_de_juego][numeros] #retorna una lista de numeros que pertecen a una columna escogida
                    else:
                        raise ValueError
                except ValueError:
                    print('Intente de nuevo')

        def escoger_numero_o_numeros() -> list[int]:

            while True:

                print('\nPara apostar a mas de un número, escriba de la siguiente manera: 3 5 o 12, 4, 23')

                #Se usa una expresion regular con un patron para solo detecte numeros
                numero_s = [int(num) for num in re.findall(r'\d+',input('Numero/s: -> '))] #convierte a int elementos de la lista findall
                if numero_s == []: #si no escribió ningun numero
                    print('No se puede realizar esta apuesta. Ingrese un número o varios')
                else:
                    numero_s = [num for num in numero_s if num <= 36 and num >= 0] #verifica que no sean numeros que excedan el limite
                    return numero_s      
        
        def escojer_color() -> str:
            while True:
                color = input('Color ->  ').casefold()
                if color not in self.numeros_color.values():
                    print('No se puede hacer esa apuesta. Escoja (r) Rojo o (n) Negro')
                else:
                    return color
        

        dict_de_tipo_de_apuesta:dict = {1:{'mensaje':'Escoja una columna de 12 números','paga':monto_apostado * 3},
                                    2:{'mensaje':'Escoja una columna de 6 números','paga':monto_apostado * 6},
                                    3:{'mensaje':'Escoja una de las tres filas de 12','paga':monto_apostado * 3},
                                    4:{'mensaje': 'Escoja uno o varios números', 'paga': monto_apostado * 36},
                                    5:{'mensaje': 'Escoja Rojo (r) o Negro (n)', 'paga': monto_apostado * 2}
                                    }
        
        print(f'{dict_de_tipo_de_apuesta[tipo_de_apuesta]["mensaje"]}')

        if tipo_de_apuesta == 5: # 5 es apostar al color
            color = escojer_color()
            numeros = sorted([n for n, c in self.numeros_color.items() if c == color ]) #ordena los numeros del color escogido
 
        elif tipo_de_apuesta == 4: #6 es para apostar a numeros individuales

            while True:
                numeros = escoger_numero_o_numeros()
                apuesta_total = (monto_apostado * len(numeros)) - monto_apostado #dependiendo de la cantidad de numeros la apuesta total es mayor
                
                if apuesta_total > self.saldo: 
                    print('!Saldo Insuficiente para hacer esta apuesta¡. Intente con menos números')
                else:
                    self.saldo -= apuesta_total
                    break

        else:
            numeros = escoger_numeros_por_columnas(tipo_de_apuesta)

        limpiar_consola_windows() #limpia sólo la parte visible de la consola, no elimina el historial

        if self.girar_ruleta(numeros):
            print(f'Tus números apostados: {[num for num in numeros]}')
            print(f'Ganaste ${dict_de_tipo_de_apuesta[tipo_de_apuesta]["paga"]}')
            self.saldo += dict_de_tipo_de_apuesta[tipo_de_apuesta]["paga"]
        else:
            print(f'Tus números apostados: {[num for num in numeros]}')
            print('No hay ganancia')


    def verificador_de_saldo(self) -> bool: #se asegura de que haya al menos 1 ficha para seguir ejecutando el programa
        if self.saldo == 0: #si el saldo es igual a 0
            print('\n¡Su saldo es insuficiente para realizar apuestas!')
            return False 
        else:
            return True


    def escojer_monto(self) -> int: #retorna la cantidad elegida por el usuario sin sobrepasar su saldo

        if self.verificador_de_saldo(): #retorna bool
            print('\nEscoja la cantidad que desea apostar')

            while True:
                try:
                    monto = int(input(f'Saldo: ${self.saldo:.1f}\t\tApuesta: $'))
                    if monto > 0: #la apuesta no puede ser menor que 0

                        if monto <= self.saldo:
                            self.saldo -= monto
                            print('$$$---   Apuesta realizada   ---$$$\n')
                            return monto
                                
                        elif monto > self.saldo:
                            print('¡Saldo insuficiente para hacer esta apuesta!\n')

                    else:
                        print('Intente de nuevo') #mensaje de salida
                        
                except ValueError:
                    print('Apuesta inadecuada\n')
        else:
            return False


    def elegir_tipo_de_apuesta(self) -> int: #retorna un int (1-5) que simboliza el estilo de juego que se usará

        while True:
            print('\nEscoja su tipo de apuesta')
            print('\t1. Columnas de Doces')
            print('\t2. Columnas de seis')
            print('\t3. Filas de doce')
            print('\t4. Número individual')            
            print('\t5. Apostar por color\n')

            try:
                apuesta_escojida:int = int(input('Tipo de apuesta -> '))
                if apuesta_escojida in range(1,6):
                    return apuesta_escojida
                else:
                    raise ValueError
            except ValueError:
                print('No se admiten ese tipo de apuestas')


    def menu_de_apuestas(self): #ejecuta 
        print('----- Bienvenido a Roullete -----')
        print('\tHaga su apuesta:')
        print(self.tablero) #solo imprime el tablero al incio

        while self.verificador_de_saldo(): #mientras aun tengas saldo, seguirá ejecutandose
        
            print(f'Saldo: ${self.saldo}') #imprime el saldo disponible
            
            tipo_de_apuesta = self.elegir_tipo_de_apuesta()
            monto = self.escojer_monto()

            self.apuesta(tipo_de_apuesta,monto) #ejecuta la apuesta

            print(self.tablero) #imprime el tablero en cada vuelta porque se limpia la consola luego de ejecutar "apuesta"

        print('\n___El programa se cerró correctamente___')

ruleta = Roullette(2000)
ruleta.menu_de_apuestas()        






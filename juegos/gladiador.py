class Gladiator:

    def __init__(self) -> any: #cuando no quieres pasar parametros y crearlos directamente en la funcion init
        self.__altura = 189
        self.__habilidad = 'Guerrero novato'
        self.__edad = 21
        self.durabilidad = 120
        self.poder_de_combate = 120
        self.money = 100

    def get_attribute(self):
        
        altura = f'Altura:  {self.__altura}cm'   
        nivel = f'Nivel de habilidad: {self.__habilidad}'
        edad = f'Edad: {self.__edad}'
        durabilidad = f'Durabilidad en minutos: {self.durabilidad}min'
        poder = f'Poder de combate: {self.poder_de_combate}'
        money = f'Dinero disponible ${self.money}'
        return f'{altura}\n{nivel}\n{edad}\n{durabilidad}\n{poder}\n{money}'
            
    def set_damage(self, daño):

        self.poder_de_combate = self.poder_de_combate - daño
        self.durabilidad = self.durabilidad - (daño/10)
        self.money = self.money + daño*2

        def daño_recibido(daño_rec = daño): #le pasamos como parametro el valor del daño recibido de el objeto Gladiador
            if daño_rec in range (0,10):
                print('\n🏹➵Recibiste un flechazo')
                print(f'Daño recibido -{daño_rec}')          
            elif daño_rec in range(11,35):
                print('\n🔫Recibiste un disparo')
                print(f'Daño recibido -{daño_rec}') 
            elif daño_rec in range (36,70):
                print('\n🔪🩸Recibiste una puñalada de un sable')
                print(f'Daño recibido -{daño_rec}')
            elif daño_rec in range(71,135):
                print('\n💣  Recibiste daño por una bomba')
                print('Daño critico!!🩸🩸🩸')
                print(f'Daño recibido -{daño_rec}')
        
        if self.poder_de_combate <= 0:
            daño_recibido()
            return (f'Poder de combate {self.poder_de_combate}\nYou´re dead')
        elif self.poder_de_combate >= 1 and self.poder_de_combate <= 100: #si esta niveles muy bajos
            daño_recibido()
            return (f'Peligro❌ tus niveles están muy bajos\nPoder de combate {self.poder_de_combate}'+
                    f'\nDurabilidad en minutos {self.durabilidad}min\nDinero disponible ${self.money}')
        else:
            daño_recibido()
            return (f'Poder de combate {self.poder_de_combate}'+
                f'\nDurabilidad en minutos {self.durabilidad}min\nDinero disponible ${self.money}')
class Store:
    def __init__(self) -> any:
        self.pocion_simple = 150
        self.escudo = 300
        self.pocion_de_resurreccion = 800
        self.level_complete = 2500
        self.money = 0
        self.salud = 0

    def tienda(self,money,salud): #le pasamos como parametro la cantidad de dinero del objeto gladiador
        self.money = money 
        self.salud = salud
        eleccion_de_objeto = 1

        def posicion_simple():
            print('\n----Posición simple----\n --Restaura 100 de poder de combate')
            print('Comprar por $150? (si/no)')
            eleccion = str(input())
            if self.money >= self.pocion_simple:
                if eleccion == "si":
                    self.money = self.money - self.pocion_simple
                    self.salud = self.salud + 100
            else:
                print('Dinero insuficiente')
        def escudo():
            print('----Escudo----\n --Recibe tres ataques seguidos sin daño')
            print('Comprar por $300? (si/no)')
            eleccion = str(input())
            if self.money >= self.escudo:
                if eleccion == "si":
                    self.money = self.money - self.escudo
                    self.salud = self.salud + 250
            else:
                print('Dinero insuficiente')          
        def posicion_de_resurrecion():
            print('----Posición de Resurrección----\n --Restaura todo el poder de combate(480) y lo suma' +
                  '\n ----------al poder de combate actual')
            print('Comprar por $800? (si/no)')
            eleccion = str(input())
            if self.money >= self.pocion_de_resurreccion:
                if eleccion == "si":
                    self.money = self.money - self.pocion_de_resurreccion
                    self.salud = self.salud + 480
            else:
                print('Dinero insuficiente')
        def level_complete():
            print('----Level Complete----\n --Restaura 100 de poder de combate')
            print('Comprar por $2500? (si/no)')
            eleccion = str(input())
            if self.money >= self.level_complete:
                if eleccion == "si":
                    self.money = self.money - self.level_complete
                    self.salud = self.salud + 250
            else:
                print('Dinero insuficiente')
        while eleccion_de_objeto != 0:
            print('\n*****Bienvenido a la tienda de items*****\n')
            print(f'Dinero disponible: ${self.money}\n')
            print(f'1)Primer item: Pocion simple ${self.pocion_simple}')
            print(f'2)Segundo item: Escudo ${self.escudo}')
            print(f'3)Tercer item: Pocion de resurreción ${self.pocion_de_resurreccion}')
            print(f'4)Cuarto item: Level Complete ${self.level_complete}')
            print('0) Salir')

            try:
                eleccion_de_objeto = int(input('\nElija una para ver sus atributos '))
                
                if eleccion_de_objeto == 1:
                    posicion_simple()   
                elif eleccion_de_objeto == 2:
                    escudo()
                elif eleccion_de_objeto == 3:
                    posicion_de_resurrecion()
                elif eleccion_de_objeto == 4:
                    level_complete()
                elif eleccion_de_objeto == 0:
                    print('Gracias por su compra\n')
            except:
                print('❌❌❌Opcion no valida, elija otra❌❌❌')

tienda = Store()
gladiador = Gladiator()

print(gladiador.get_attribute())
import random
yes_no = ''

while yes_no != 'no':

    if gladiador.poder_de_combate <= 0:
            break
    elif gladiador.poder_de_combate >= 1 and gladiador.poder_de_combate <= 100:
            
        print('⚔️   Desea pelear?⚔️  (z) o deseas ir a la tienda? (x)') 
        yes_no = str(input())
        if yes_no == 'x':
            tienda.tienda(gladiador.money,gladiador.poder_de_combate) #le paso el valor del dinero y porcentaje de poder que tiene mi objeto gladiador
            ##Despues de hacer las compras devolvemos los valores de money y poder, los pasamos al personaje##
            gladiador.money = tienda.money
            gladiador.poder_de_combate = tienda.salud
            print(gladiador.get_attribute()) #vemos los valores modificados
        elif yes_no == 'z':
            print(gladiador.set_damage(random.randint(0,135)))
        elif yes_no == 'no':
            break
    else:
        print('⚔️   Desea pelear?⚔️   ' )
        yes_no = str(input())
        if yes_no != 'si':
            break
        else:
            print(gladiador.set_damage(random.randint(0,135)))
if yes_no != 'si':
    print('❌Game over❌')


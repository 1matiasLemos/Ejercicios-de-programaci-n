from random import choice

class Perro():
    
    def __init__(self,nombre:str,raza:str,edad:int,comida_fav:str,juguete_fav:str) -> None:
        self.raza = raza
        self.edad = edad
        self.name = nombre
        self.comida_fav = comida_fav
        self.juguete_fav = juguete_fav
        self.estado_de_animo = 50
        self.hambre = 40
        self.indicador_de_hambre = 0
        self.sed = 40
        self.sueño = 30


    def comer(self,comida_elegida):
        #dict donde contiene diferentes comidas, incluyendo la comida fav
        #cada comida quita un porcentaje diferente de hambre, siendo la comida fav la que quita mayor nivel de hambre
        comidas = {'comida normal':30,'comida sabrosa': 50,f'{self.comida_fav}':80,'bocadillo':15,'croqueta':20}

        if self.hambre <= 20: #el nivel de hambre debe ser mayor que 20%
            print(f'\n{self.name} no tiene hambre') #mensaje de salida

        else: #Al comer...
            #la comida hace bajar el nivel de hambre
            print(f'\n{self.name} comió {comida_elegida}') #mensaje que indica que fue lo que comió
            self.hambre -= comidas[comida_elegida] #reduce o resta los niveles de hambre, dependiendo de la comida elegida

            if self.hambre < 0: #en caso de que alguna comida baje los niveles de hambre, menor que 0
                self.hambre = 0 #deja los niveles de hambre en cero, que es el limite
                print(f'\n{self.name} ya no tiene hambre') #mensaje de salida

            self.indicador_de_hambre = 0 #el indicador se reinicia
            self.sed += 20 #aumenta la sed...
            self.sueño += 7 #aumenta el sueño...
            self.barrera_de_limite() #evita que algun atributo supere el limite que es 100%


    def beber(self):
        while True: #el bucle se ejecutará hasta que el nivel de sed sea <= 30
            if self.sed > 30: #condicional que indica que siga ejecutandose el bucle
                self.sed -= 30 #reduce el nivel de sed (simula beber agua)
                print(f'\n{self.name} está bebiendo agua...') #mensaje de salida
                self.sueño -= 5 #reduce levemente el nivel de sueño
                if self.sueño < 0: #en caso de que el nivel de sueño sea menro que 0
                    self.sueño = 0 #deja el nivel en 0 para evitar numeros negativos
            elif self.sed <= 30: #condicional que cierra el bucle
                print(f'\n{self.name} no tiene sed') #mensaje de salida del bucle
                break #cierra el bucle


    def indicadores(self): #retorna el nivel mas alto, entre todos
    
        return max([self.hambre,self.sed,self.sueño])


    def indicador_del_problema(self,problema):
            
        #dict que tiene un mensaje diferente para cada problema
        problemas = {
            self.estado_de_animo:f'{self.name} esta desanimado', #mesaje del estado de animo
            self.hambre:f'{self.name} tiene hambre', #mensaje del nivel de hambre
            self.sed:f'{self.name} tiene sed', #mensaje del nivel de sed
            self.sueño:f'{self.name} tiene sueño' #mensaje del nivel de sueño
        }
        
      
        if problema >= 80 and self.estado_de_animo <= 30: #este condicional sirve para indicar un estado de animo bajo
            print(problemas[self.estado_de_animo])
        
        if self.hambre == problema: #si el problema es de hambre 
            #el indicador de hambre sirve para saber si se ha ingnorado el problema, asi incrementar hasta un max de 3
            self.indicador_de_hambre += 1
            #al llegar a tres, significa que la mascota Murio por ignorar el indicador de hambre
        
        print(problemas[problema]) #mensaje de salida que indica el problema especifico


    def jugar(self,juguete:str): #recibe como arg un juguete

        #dict que contiene distintos tipos de juguetes, cada uno tiene un porcentaje diferente
                                                    #el juguete favorito es el de mayor porcentaje 
        juguetes = {'pelota':20,'hueso':10,'palo':15,'juguete plastico':13,'muñeco':25,self.juguete_fav:33}

        if self.indicadores() >= 80: #en caso de detectar un problema...
            #mensaje de salida que indica que no se hará la accion de jugar hasta que el problema se solucione
            print(f'\n{self.name} no quiere jugar')        
        else:#en caso contrario...
            self.estado_de_animo += juguetes[juguete] #el juguete aumenta el estado de animo, dependiendo su valor
            print(f'\n{self.name} esta jugando con {juguete}...') #mensaje de salida que dice que juguete esta usando
            self.sueño += 8 #aumenta el sueño (porque al jugar te cansas)
            self.hambre += 7 #aumenta el hambre (la perdida de energia en calorias)
            self.sed += 10 #aumenta la sed (perdida de liquidos)
            if self.estado_de_animo > 100: #evita que el estado de animo sobrepase el limite de 100%
                self.estado_de_animo = 100
 

    def dormir(self): 
        if self.sueño >= 80: #el nivel de sueño debe ser mayor que 80% para poder dormir
            print('\n') #salto de linea

            while self.sueño > 0: #Se repetirá el bucle hasta que el nivel de sueño sea menor que 0
                print('Zzz, Zzz, ZZZ', end='....') #mensaje de salida (durmiendo)
                self.sueño -= 30 #reduce el sueño...
                self.hambre += 7 #aumenta el hambre...
                self.sed += 5 #aumenta la sed...
                self.estado_de_animo -= 15 #disminuye el estado de animo
                self.barrera_de_limite() #evita que los valores superen el 100%

            print(f'\n{self.name} ya despertó de su siesta') #mensaje de salida al finalizar el bucle 
            self.sueño = 0 #colocamos 0 al nivel de sueño para evitar numeros negativos
        else:
            print(f'\n{self.name} no tiene sueño aún') #mensaje de salida si el nivel de sueño no es mayor que 80%
    

    def estadisticas(self): #imprime el porcentaje de los niveles
        print(f'\nHambre {self.hambre}%')
        print(f'Sed {self.sed}%')
        print(f'Nivel de somnolencia {self.sueño}%')
        print(f'Estado de animo {self.estado_de_animo}%')


    def barrera_de_limite(self):
        limite:int = 100 
        indicador = self.indicadores() #toma el valor mas alto
        if indicador >= limite: #si hay un estadistica que supera los 100
            for i in list(self.sed,self.hambre,self.sueño,self.estado_de_animo):
                
                if i >= limite:
                    self.i = 100



def crear_perro():
    n = 'Nombre del perro: '
    r = 'Tipo de raza: '
    e = 'Edad: '
    cf = 'Comida favorita: '
    jf = 'Juguete favorito: '
    
    while True:
        try:
            return Perro(input(n),input(r),int(input(e)),input(cf),input(jf))
        except ValueError:
            print('Error: ingrese los valores adecuados')

def mostrar_acciones(nombre):
    print(f'\nEscoje una acción que quieres que haga {nombre}')
    print('1. Beber agua\t2. Comer\t3. Dormir\t4. Jugar\t5. Terminar el juego')

def escojer():
    while True:
        try:
            opcion = int(input('Acción ->   '))
            if opcion in [1,2,3,4,5]:
                return opcion
            else:
                print('Escoja una acción de las mostradas\n')
        except ValueError:
            print('Opción no válida')

def menu():
    perro = crear_perro()  

    opciones = {1:perro.beber,2:perro.comer,3:perro.dormir,4:perro.jugar}
    juguetes:list = ['pelota','hueso','palo','juguete plastico','muñeco',perro.juguete_fav]
    comidas:list = ['comida normal','comida sabrosa','bocadillo','croqueta',perro.comida_fav]

    print(f'Bienvenido ahora eres el dueño de {perro.name}')
    print('Cuida bien de tu nueva mascota :D')

    while perro.indicador_de_hambre != 3:
        mostrar_acciones(perro.name)
        accion = escojer()
        if accion == 2:
            opciones[accion](choice(comidas))
        elif accion == 4:
            opciones[accion](choice(juguetes))
        elif accion == 5:
            break
        else:
            opciones[accion]()

        indicador_de_niveles = perro.indicadores()
        if indicador_de_niveles >= 80:
            perro.indicador_del_problema(indicador_de_niveles)
            perro.estadisticas()
    else:
        print(f'\n{perro.name} Murio :(\nXXX-Game Over-XXX')

menu()


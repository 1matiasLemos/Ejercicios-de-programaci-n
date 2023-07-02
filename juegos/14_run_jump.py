## funcion que calcula el recorrido de un atleta en una carrera de obstaculos ##
## los obstaculos se representan con '|' (valla) y '_' (suelo)
## el atleta puede saltar (jump) y correr (run)

run = 'run'
jump = 'jump'

def pista_de_obstaculos(run_jump,pista) -> bool:
    accion = 0
    recorrido = '' #esto es el recorrido que hizo el atleta

    for i in pista:
        if i == '_' and run_jump[accion] == 'run': #si esta en suelo y corre, entonces esta correcto
            recorrido += pista[accion:accion+1]
        elif i == '|' and run_jump[accion] == 'jump': #si hay una valla y salta, entonces es correcto
            recorrido += pista[accion:accion+1]
        elif i == '|' and run_jump[accion] == 'run': #si corre cuando hay una valla, indica un error (/)
            recorrido += '/'
        elif i == '_' and run_jump[accion] == 'jump': #si salta sin que haya una valla, indica un error (x)
            recorrido += 'x'
        elif i != '|' and i != '_': #si se ingresa un dato que no sea suelo y valla, retorna un ValueError
            return ValueError, 'error en la pista, no existe este obstaculo'

        accion +=1

        if accion == run_jump.__len__(): #esto es en caso de que las acciones que haga el atleta sean menos que la pista
            recorrido += pista[accion::] #lo interpretará como correcto a lo sobrante de la pista
            break
    return recorrido == pista

print(pista_de_obstaculos([run,jump,run,jump,run], pista='_|_|_|_|_'))
print(pista_de_obstaculos([run,run,jump,run], pista='_|_|__|_'))
print(pista_de_obstaculos([run,jump,jump,run], pista='_|3_|__|_'))
print(pista_de_obstaculos([run,jump,run,jump,run,run,run], pista='_|_|___'))
print(pista_de_obstaculos([run,jump,jump,jump,run,jump], pista='_|||_|__|_'))
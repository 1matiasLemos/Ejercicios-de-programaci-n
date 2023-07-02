from conceptos import lista,Trivia,questions
from random import randint

opciones = [0,1,2]
lista = list(set(lista)) #esto desordena las respuestas asi no aparezcan en el mismo orden

while str(input('¿Quieres jugar la trivia? ')) != 'no':  
    question = questions[randint(0,1)]
    print(question)
    for i in opciones:
        print(f'{i+1}) {lista[i]}')

    print('escoje una opcion')

    respuesta = int(input()) - 1

    if lista[respuesta] == Trivia.get(question):
        print(True)
    else:
        print(False)
        break

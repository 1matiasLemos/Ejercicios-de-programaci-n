## Este programa verifica que los parentesis, llaves y corchetes esten equilibrados y en orden correcto ##

def verificador(cadena):
    signos_de_puntuacion = {
        'abierto':{'(','[','{'},
        'cerrado':{')',']','}'},
        'parentesis':{'(',')'},
        'corchetes':{'[',']'},
        'llaves':{'{','}'}
    }
    signos_abiertos = [] #iremos agregando todos los signos abiertos que nos encontremos en toda la cadena
    signo_final = 0 #este indice servirá para trasladarno a los signos abiertos para compararlos
    true_or_no = True #declaramos como True 
    for i in cadena:

        if i in signos_de_puntuacion['abierto']:
            signos_abiertos.append(i) #agregamos el signo a la lista 
            signo_final+=1 #indicamos al indice que se agregó un elemento a la lista
    for i in cadena:
        if i in signos_de_puntuacion['cerrado']: #al momento de encontrarse con un signo cerrado
            #se tomará en cuenta el ultimo signo abierto para ver si corresponde a ese signo cerrado
            if i in signos_de_puntuacion['parentesis'] and signos_abiertos[signo_final-1] in signos_de_puntuacion['parentesis']:
                signo_final-=1 #decrementamos el indice para 
                #cuando se encuentra un signo cerrado, automaticamente nos iremos fijando en los anteriores abiertos, hasta el inicio
            elif i in signos_de_puntuacion['corchetes'] and signos_abiertos[signo_final-1] in signos_de_puntuacion['corchetes']:          
                signo_final-=1      
            elif i in signos_de_puntuacion['llaves'] and signos_abiertos[signo_final-1] in signos_de_puntuacion['llaves']:
                signo_final-=1           
            else:
                #si el programa detecta que no coinciden los signos, se detendrá el for, indicando un error en el orden
                true_or_no = False #indicador del error encontrado
                break
    if true_or_no == False: 
        print('los signos no están equilibrados')
    else:
        print('los signos están equilibrados')

verificador('{{{{{{)}}}}}')

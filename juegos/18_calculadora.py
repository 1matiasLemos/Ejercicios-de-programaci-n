import os

def calculadora(ruta):

    archivo = open(ruta,'r+')

    dict_signos = {'suma':'+','resta':'-','multiplicacion':'*','division':'/'}
    def suma(value1, value2):
        return value1 + value2

    def resta(value1, value2):
        return value1 - value2

    def multiplicacion(value1, value2):
        return value1 * value2

    def division(value1, value2):
        return value1 / value2

    try:
        inicio = 1
        value1 = 0
        signo = ''
        for i in archivo.readlines():
            if inicio == 1:
                value1 = int(i)
                inicio+=1
            
            elif i.strip() in dict_signos.values():
                if i.strip() == dict_signos['suma']:
                    signo = dict_signos['suma']
                elif i.strip() == dict_signos['resta']:
                    signo = dict_signos['resta']
                elif i.strip() == dict_signos['multiplicacion']:
                    signo = dict_signos['multiplicacion']
                elif i.strip() == dict_signos['division']:
                    signo = dict_signos['division']

            elif i.strip() not in dict_signos.values() and signo != '':
                if signo == dict_signos['suma']:
                    value1 = suma(value1,int(i))
                    signo = ''
                elif signo == dict_signos['resta']:
                    value1 = resta(value1,int(i))
                    signo = ''
                elif signo == dict_signos['multiplicacion']:
                    value1 = multiplicacion(value1,int(i))
                    signo = ''
                elif signo == dict_signos['division']:
                    value1 = division(value1,int(i))
                    signo = ''
            else:
                return 'Error, no se pudo operar los numeros'
        archivo.close()
        return value1
    except Exception as e:
        return 'Error, no se pudo operar los numeros', e

print(calculadora('juegos/archivo.txt'))
## Este programa devuelve una cadena de texto con caracteres que no se encuentran en los parametros opuestos ##
def impresion(cadena1,cadena2):

    out1 = out2 = '' 
    for i in cadena1:
        if i in cadena2:
            pass
        else:
            out1 = out1 + i
    for i in cadena2:
        if i in cadena1:
            pass
        else:
            out2 = out2 + i

    return out1,out2

print(impresion('jugar', 'futbol'))
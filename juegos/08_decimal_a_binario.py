## condicion: no usar funciones del sistema ##

def binario(decimal:int):

    numero_decimal = decimal
    num_bin = ''

    while numero_decimal > 1:

        if numero_decimal % 2 == 0:
            num_bin = '0' + num_bin
        elif numero_decimal % 2 == 1:
            num_bin = '1' + num_bin
        numero_decimal = numero_decimal // 2 
        if numero_decimal == 1:
            num_bin = '1' + num_bin
    
    return  f"{decimal} = { num_bin}"
        
print(binario(323))
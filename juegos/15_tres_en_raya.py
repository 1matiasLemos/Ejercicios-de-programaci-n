## Esta funcion retorna si ganó X, si ganó O o si hubo empate ##
def tres_en_raya(tablero) -> str:
    def print_tablero():
        return f'\n{lista_bi[0]}\n{lista_bi[1]}\n{lista_bi[2]}'
    def contar_XyO():
        X_cantidad = [i.count('x') for i in tablero]
        O_cantidad = [i.count('o') for i in tablero]
        sumar = lambda numeros: numeros[0] + numeros[1] + numeros[2]

        X_cantidad = sumar(X_cantidad)
        O_cantidad = sumar(O_cantidad)
        if X_cantidad - O_cantidad == 1 or O_cantidad - X_cantidad == 1:
            return None
        else:
            return ValueError
       
    def horizontal():
        fila = 0
        tres_en_linea_X = 0
        tres_en_linea_O = 0
        Winner = ''
        for horizontal in tablero:
            
            if 'x' in horizontal[0] and 'x' in horizontal[1] and 'x' in horizontal[2]:
                tres_en_linea_X += 1
                Winner = 'X'
                if tres_en_linea_X > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
                
            elif 'o' in horizontal[0] and 'o' in horizontal[1] and 'o' in horizontal[2]:
                tres_en_linea_O += 1
                Winner = 'O'
                if tres_en_linea_O > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
            fila +=1
        return Winner
    
    def vertical():
        fila = 0
        columna = 0
        tres_en_linea_O = 0
        tres_en_linea_X = 0
        Winner = ''

        for vertical in tablero:
            
            if 'o' in tablero[fila][columna] and 'o' in tablero[fila+1][columna] and 'o' in tablero[fila+2][columna]:

                tres_en_linea_O += 1
                Winner = 'O'
                if tres_en_linea_O > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
            elif 'x' in tablero[fila][columna] and 'x' in tablero[fila+1][columna] and 'x' in tablero[fila+2][columna]:

                tres_en_linea_X += 1
                Winner = 'X'
                if tres_en_linea_X > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
                
            columna +=1
        return Winner

    def cruzado():
        tres_en_linea_O = 0
        tres_en_linea_X = 0
        Winner = ''
        if tablero[0][0] == 'x' and tablero[1][1] == 'x' and tablero[2][2] == 'x':
            tres_en_linea_X += 1
            Winner = 'X'
            if tres_en_linea_X > 1:
                return ValueError
            elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
        elif tablero[0][0] == 'o' and tablero[1][1] == 'o' and tablero[2][2] == 'o':
                tres_en_linea_O += 1
                Winner = 'O'
                if tres_en_linea_O > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
        elif tablero[2][0] == 'x' and tablero[1][1] == 'x' and tablero[0][2] == 'x':
                tres_en_linea_X += 1
                Winner = 'X'
                if tres_en_linea_X > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
        elif tablero[2][0] == 'o' and tablero[1][1] == 'o' and tablero[0][2] == 'o':
                tres_en_linea_O += 1
                Winner = 'O'
                if tres_en_linea_O > 1:
                    return ValueError
                elif tres_en_linea_O == 1 and tres_en_linea_X == 1:
                    return IndexError
        return Winner
                
    if contar_XyO() == ValueError:
        return 'Error en la cantidad de X y O'
    else:

        if horizontal() == ValueError or horizontal() == IndexError:
            return 'Error: ambos no pueden ganar' + print_tablero()
        
        elif horizontal() == vertical() == 'X' or horizontal() == vertical() == 'O':
            return f'No es posible hacer raya en ambas direcciones {print_tablero()}'
        elif horizontal() == cruzado() == 'X' or horizontal() == cruzado() == 'O':
            return f'No es posible hacer raya en ambas direcciones {print_tablero()}'
        elif vertical() == cruzado() == 'X':
            return f'No es posible hacer raya en ambas direcciones {print_tablero()}'
        
        elif horizontal() == 'X' or horizontal() == 'O':
            return horizontal()        
        elif vertical() == ValueError or vertical() == IndexError:
            return 'Error: ambos no pueden ganar' + print_tablero()
        elif vertical() == 'X' or vertical() == 'O':
            return vertical()
        elif cruzado() == 'X' or cruzado() == 'O':
            return cruzado()
        else:
            return 'Empate'

lista_bi = [['x','x','o'],
            ['x','o','x'],
            ['o','o','x']]
print(tres_en_raya(lista_bi)) #gana O (cruzado)

lista_bi = [['o','x','x'],
            ['x','o','x'],
            ['o','o','x']]
print(tres_en_raya(lista_bi)) #gana X (verical)

lista_bi = [['x','o','x'],
            ['x','o','x'],
            ['o','x','o']]
print(tres_en_raya(lista_bi)) #Empate

lista_bi = [['x','x','o'],
            ['o','o','x'],
            ['x','x','o']]
print(tres_en_raya(lista_bi)) #Empate

lista_bi = [['x','x','x'],
            ['x','o','o'],
            ['o','o','x']]
print(tres_en_raya(lista_bi)) #gana X

lista_bi = [['x','x','x'],
            ['o','o','x'],
            ['o','o','x']]
print(tres_en_raya(lista_bi)) #No es posible hacer raya en ambas direcciones

lista_bi = [['x','o','x'],
            ['x','o','o'],
            ['x','o','x']]
print(tres_en_raya(lista_bi)) #Error: ambos no pueden ganar

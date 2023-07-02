'''Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.'''

def function(list1,list2, bool) -> list:

    list_high = []
    list_down = []
    if list2.__len__() <= list1.__len__():
        list_high = list1
        list_down = list2
    else:
        list_high = list2
        list_down = list1

    list_resultante = []
    if bool: 
        for i in list_high:
            if i in list_down and i not in list_resultante:
                list_resultante.append(i)
    else:

        for i in list_high:
            if i not in list_down:
                list_resultante.append(i)
        for i in list_down:
            if i not in list_high:
                list_resultante.append(i)
    return list_resultante

print(function([1,2,3,4,5,7],[1,2,4,6,5,7],True))
print(function([1,2,3,4],[2,2,3,3,3,4,6],True))
print(function([1,2,3,4],[2,2,3,3,3,4,6],False))

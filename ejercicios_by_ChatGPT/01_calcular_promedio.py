### Codigo original por mi
'''def calcular_promedio(numeros):

    letrero1 = 'El promedio de la lista es:'
    letrero2 = 'Los numeros mayores que el promedio son'
    letrero3 = 'La suma de los numeros mayores al promedio es:'
    letrero4 = 'La desviación estándar del promedio es de, aproximadamente'
    if len(numeros) == 0:
        return 0
    
    suma = sum(numeros)
    promedio = suma / len(numeros)

    def numbers_bigger_than_average(number):

        if number > promedio:
            return True
        else:
            return False
        
    def desviacion(number):
        return (number-promedio) ** 2
    
    # numeros mayores que el promedio
    filtro = list(filter(numbers_bigger_than_average,numeros))

    # calcular desviacion
    from math import sqrt

    promedio2 = sum(list(map(desviacion,numeros)))
    desviacion_estandar = sqrt(promedio2 / len(numeros))

    if filtro != []:
        return f'{letrero1} {promedio}\n{letrero2} {filtro}\n{letrero3} {sum(filtro)}\n{letrero4} {desviacion_estandar}'
    else:
        return f'{letrero1} {promedio}'
        
numeros = [4, 7, 9, 12, 5]
print(calcular_promedio(numeros))
'''

## Codigo mejorado por Chat GPT
from math import sqrt

def calcular_promedio(numeros):
    letrero1 = 'El promedio de la lista es:'
    letrero2 = 'Los numeros mayores que el promedio son'
    letrero3 = 'La suma de los numeros mayores al promedio es:'
    letrero4 = 'La desviación estándar del promedio es de, aproximadamente'

    if len(numeros) == 0:
        return 'La lista está vacía.'

    promedio = sum(numeros) / len(numeros)

    # Utilizar comprensión de listas en lugar de filter
    filtro = [num for num in numeros if num > promedio]

    # Calcular la desviación estándar utilizando directamente la fórmula
    desviacion_estandar = sqrt(sum((num - promedio) ** 2 for num in numeros) / len(numeros))

    if filtro:
        return f'{letrero1} {promedio}\n{letrero2} {filtro}\n{letrero3} {sum(filtro)}\n{letrero4} {desviacion_estandar}'
    else:
        return f'{letrero1} {promedio}'

numeros = [4, 7, 9, 12, 5]
print(calcular_promedio(numeros))

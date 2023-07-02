import json

# Carga el archivo JSON que contiene los valores de cambio de monedas
valor_monedas = json.load(open('ejercicios_by_ChatGPT\monedas.json', 'r'))

# Diccionario que mapea los números de opción de monedas permitidas a sus códigos
dict_monedas_permitidas = {
    1: 'USD',
    2: 'EUR',
    3: 'JPY',
    4: 'GBP',
    5: 'AUD',
    6: 'CAD',
    7: 'CHF',
    8: 'CNY',
    9: 'NZD',
    10: 'MXN'
}


def calcular_cambio(cantidad, moneda_de_origen, moneda_de_cambio):
    """
    Calcula el cambio de una cantidad de una moneda a otra y llama a la función para imprimir el resultado.
    :param cantidad: Cantidad a convertir.
    :param moneda_de_origen: Moneda de origen.
    :param moneda_de_cambio: Moneda de cambio.
    """
    cambio = cantidad * valor_monedas[moneda_de_origen][moneda_de_cambio]
    imprimir_cambio_realizado(cantidad, cambio, moneda_de_origen, moneda_de_cambio)


def imprimir_cambio_realizado(valor_entrada, valor_cambio, moneda_ori, moneda_cam):
    """
    Imprime el resultado del cambio realizado.
    :param valor_entrada: Valor de entrada.
    :param valor_cambio: Valor convertido.
    :param moneda_ori: Moneda de origen.
    :param moneda_cam: Moneda de cambio.
    """

    print('\n+________________________________________+')
    print('+     Cambio realizado exitosamente      +')
    print('+________________________________________+')#.2f indica si hay un punto, seguido, que solo imprima dos caracteres siguientes
    print(f'+______{valor_entrada} {moneda_ori}_____=====>_____{valor_cambio:.2f} {moneda_cam}______+')
    print('+________________________________________+\n')


def seleccioonar_moneda_de_origen():
    """
    Permite al usuario seleccionar la moneda de origen.
    :return: Código de moneda seleccionada.
    """
    while True:
        print('\nMonedas permitidas:')
        imprimir_monedas()
        try:
            moneda_de_origen = int(input('Seleccione su moneda (1-10): '))

            if moneda_de_origen < 0 or moneda_de_origen > 10:
                print('Opcion no valida')
            else:
                return dict_monedas_permitidas[moneda_de_origen]

        except ValueError:
            print('Error: ingrese una opcion válida')


def seleccionar_moneda_de_cambio():
    """
    Permite al usuario seleccionar la moneda de cambio.
    :return: Código de moneda seleccionada.
    """
    while True:
        print('\nMonedas permitidas:')
        imprimir_monedas()
        try:
            moneda_de_cambio = int(input('Seleccione su moneda de cambio (1-10): '))
            if moneda_de_cambio < 0 or moneda_de_cambio > 10:
                print('Opcion no valida')
            else:
                return dict_monedas_permitidas[moneda_de_cambio]

        except ValueError:
            print('Error: ingrese una opcion válida')


def imprimir_monedas():
    """
    Imprime la lista de monedas permitidas con sus números de opción.
    """
    print('1. Dólar estadounidense (USD)\t' +
          '2. Euro (EUR)\t\t\t' +
          '3. Yen japonés (JPY)\n'
          '4. Libra esterlina (GBP)\t'
          '5. Dólar australiano (AUD) \t' +
          '6. Dólar canadiense (CAD)\n' +
          '7. Franco suizo (CHF)\t\t'
          '8. Yuan chino (CNY)\t\t' +
          '9. Dólar neozelandés (NZD) \n' +
          '10. Peso mexicano (MXN)\n'
          )


def menu():
    """
    Función principal que muestra el menú al usuario y solicita la cantidad y las monedas a convertir.
    """
    print('********************************************')
    print('***Bienvenido a la Caja de Cambio Oficial***')
    print('********************************************\n')
    print('Ingrese una cantidad o monto para hacer el cambio: \n')

    while True:
        try:
            calcular_cambio(
                int(input('Ingrese una cantidad: ')),
                seleccioonar_moneda_de_origen(),
                seleccionar_moneda_de_cambio()
            )
            break
        except ValueError:
            print('Error: Ingrese una cantidad o monto para hacer el cambio: ')


menu()


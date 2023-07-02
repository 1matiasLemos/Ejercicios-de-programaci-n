## funcion que calcula cuantos dias de diferencia hay entre dos fechas ##
from datetime import datetime,date

def calcular_dias(fecha1 = '',fecha2 = '') -> int:
    '''manera de convertir un str en date, primero se debe convertir a datetime y luego retornar como date
    respetando el formate de la funcion strptime(str,%(d)ay/%(m)onth/%(Y)ear)'''
    covertidor = lambda fecha_lambda: datetime.strptime(fecha_lambda,'%d/%m/%Y').date()
    try:
        fecha1 = covertidor(fecha1)
        fecha2 = covertidor(fecha2)
        if fecha1 < fecha2:
            return f'{(fecha2 - fecha1).days} days'
        else:
            return f'{(fecha1 - fecha2).days} days'
    except Exception as e:
        return e

print(calcular_dias('24/06/2026','24/03/2024'))
print(calcular_dias("18/05/2022", "29/05/2022"))
print(calcular_dias("mouredev", "29/04/2022"))
print(calcular_dias("18/5/2022", "29/04/2022"))
print(calcular_dias())
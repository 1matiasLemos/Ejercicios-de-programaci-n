## Funcion que convierte dias, horas, minutos y segundos a milisegundos ##

def conversor_de_tiempo(dias: int, horas: int, minutos: int, segundos: int):
    
    microsegundos_dias = dias *24 * 60 * 60 * 1000
    microsegundos_horas = horas * 60 * 60 * 1000
    microsegundos_minutos = minutos * 60 * 1000
    microsegundos_segundos = segundos * 1000

    return microsegundos_dias + microsegundos_horas + microsegundos_minutos + microsegundos_segundos
 
print(conversor_de_tiempo(0,0,0,10))
print(conversor_de_tiempo(2,5,-45,10))
print(conversor_de_tiempo(2000000000, 5, 45, 10))


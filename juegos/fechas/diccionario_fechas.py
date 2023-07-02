from datetime import date

fechas = {'dia de la independencia': date(2023,5,25)}

fecha = date(2023,5,25)
llave = 'dia de la independencia'
if fecha in fechas.values():
    print(fecha)

print(fechas['dia de la independencia'])
lados = 'Cuantos lados tiene el pologono?'
perimetro = 'Cuantos centimetros miden los lados del poligono?'
apotema = 'De cuanto es el apotema del poligono?'

def area_de_un_poligono(lados,perimetro,apotema):

    perimetro = lados * perimetro
    area = (perimetro * apotema) / 2
    return area

my_area = area_de_un_poligono(float(input(f"{lados} ")),float(input(f"{perimetro} ")),float(input(f"{apotema} ")))
print(f"El area del poligono es de {my_area}cm^2")
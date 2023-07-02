import random

print("Hazme una pregunta")
Question = input()
magic_ball8 = random.randint(1,9)

if magic_ball8 == 1:
    print("Si, definitivamente")
elif magic_ball8 == 2:
    print("Es decididamnete asi")
elif magic_ball8 == 3:
    print('Sin ninguna duda')
elif magic_ball8 == 4:
    print('Respuesta confusa, intenta otra vez')
elif magic_ball8 == 5:
    print('Pregunta de nuevo mas tarde')
elif magic_ball8 == 6:
    print('Mejor no decirte ahora')
elif magic_ball8 == 7:
    print('Mis fuentes dicen que no')
elif magic_ball8 == 8:
    print('Las perspectivas no son tan buenas')
elif magic_ball8 == 9:
    print('Muy dudoso')
else:
    print("Error")

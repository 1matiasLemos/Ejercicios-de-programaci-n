'''
CN = float(input('Cuantos yuanes tienes? '))
JP = float(input('Cuantos yenes tienes? '))
KR = float(input('Cuantos wons tienes? '))

dolares = (CN * 0.15) + (JP * 0.0074) + (KR * 0.00077)
print(str(dolares)) 
'''
#estructura condicional


import random #libreria o modulo para utilizar la funcion random
'''
num = random.randint(0, 1)
num2 = random.randint(0,6) #esta funcion otorga un valor int aleatorio, entre 0 a 6

if num2 >= 4:
  print('Heads')
  print(num2)
else:
  print('Tails')
  print(num2)
  '''

num1 = random.randint(0,100) #un numero random enntre 0 a 100

if num1 <= 9:
    print("You are in plant 0 n° " + str(num1))
elif num1 <= 19 and num1 >= 10:
    print("You are in plant 1 n° " + str(num1))
elif num1 <= 29 and num1 >= 20:
    print("You are in plant 2 n° " + str(num1))
elif num1 <= 39 and num1 >= 30:
    print("You are in plant 3 n° " + str(num1))
else:
    print("Error", num1)
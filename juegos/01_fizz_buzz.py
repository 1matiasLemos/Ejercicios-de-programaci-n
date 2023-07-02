#imprime Fizz si i es multiplo de 3, Buzz si es multiplo de 5 y FizzBuzz si ocurren ambos casos
for i in range(1,101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    
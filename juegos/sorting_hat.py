respuesta = [0,0,0]
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#------Question 1 ------
print('Q1) Do you like Dawn or Dusk?')
print(' 1) Draw')
print(' 2) Dusk') 
respuesta[0] = int(input())

if respuesta[0] == 1:
    gryffindor+=1
    ravenclaw+=1
elif respuesta[0] == 2:
    hufflepuff+=1
    slytherin+=1
else:
    print('Worng input')

#------Question 2 ------

print('Q2) When I’m dead, I want people to remember me as:')
print(' 1) The Good')
print(' 2) The Great')
print(' 3) The Wise')
print(' 4) The Bold')
respuesta[1] = int(input())

if respuesta[1] == 1:
    hufflepuff+=1
elif respuesta[1] == 2:
    slytherin+=1
elif respuesta[1] == 3:
    ravenclaw+=1
elif respuesta[1] == 4:
    gryffindor+=1
else:
    print('Wrong input')

#------Question 3 -------
print('Q3) Which kind of instrument most pleases your ear?')
print(' 1) The violin')
print(' 2) The trumpet')
print(' 3) The piano')
print(' 4) The drum')
respuesta[2] = int(input())

if respuesta[2] == 1:
    slytherin += 1
elif respuesta[2] == 2:
    hufflepuff+=1
elif respuesta[2] == 3:
    ravenclaw+=1
elif respuesta[2] == 4:
    gryffindor+=1
else:
    print('Wrong input')

print('Gryffindor:', gryffindor)
print('Ravenclaw:', ravenclaw)
print('Hufflepuff:', hufflepuff)
print('Slytherin:', slytherin)

max_point = max(hufflepuff,gryffindor,slytherin,ravenclaw) #toma el valor mas alto de todas las variables

if gryffindor == max_point:
    print('🦁 House Gryffindor')
elif slytherin == max_point:
    print('🐍 House Slytherin')
elif ravenclaw == max_point:
    print('🦅 House Ravenclaw')
elif hufflepuff == max_point:
    print('🦡 House Hufflepuff')
else:
    print('Error')
guess = 0
tries = 0

while guess != 16 and tries < 5:
  
  guess = int(input('Guess the number between 10-20: '))
  tries += 1 
  if guess < 10 or guess > 20:
    print('\ni told "number between 10-20"')


if guess == 16:
  print("You got it!")
else:
  print("You ran out of tries")

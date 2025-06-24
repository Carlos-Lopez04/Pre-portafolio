# Guess the number
#todo 1 Generate a random number
#todo 2 Give some hints to the user


import random

secret_number = random.randint(1,5)
tries = int(input('''\nGuess a number between 1 to 5
'''))

if tries == secret_number:
    print("\nIt's correct")
else:
    print("\nIt's incorrect\n")
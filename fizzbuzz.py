# FizzBuzz

# todo 1 Use a loop to iterate through from 1 to 100
# todo 2 Use conditions to verify the following:
# ? if is a multiple of 3 and 5 -> Will be replace by FizzBuzz
# ? if is multiple of 3 -> Will be replace by Fizz
# ? if is multiple of 5 -> Will be replace by Buzz
# ? If doesn't apply any condition -> print the number

# * Remember that the module operator (%) helps to determine if one number is a multiple of another.
# * number % 2 == 0 -> even or multiple of 2
# * number % 2 != 0 -> odd
# * number % 3 == 0 -> multiple of 3


numbers = 100

for number in range(numbers):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

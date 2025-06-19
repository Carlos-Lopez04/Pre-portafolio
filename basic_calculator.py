#Basic Calculator
#todo 1 Ask for two numbers
#todo 2 Do the math operations
#todo 3 Show the results

# Asking for a number
num1 = float(input('\nInsert a number '))
num2 = float(input('Insert another number '))

# Basic math operations
addition = num1 + num2
substraction = num1 - num2
multiplication = num2 * num1
division = num1 / num2

# Showing the results
print(f'''\nThese are the results:
    Adition ==> {num1} + {num2} = {addition}
    Substraction ==> {num1} - {num2} = {substraction}
    Multiplication ==> {num1} x {num2} = {multiplication}
    Division ==> {num1} / {num2} = {division}
''')
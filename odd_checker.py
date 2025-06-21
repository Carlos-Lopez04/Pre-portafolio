#Converter
#todo 1 Ask the user to write a numbeer
#todo 2 Identify if the number is an odd or an even
#todo 3 Show the result

def even_odd():
    num = float(input('\nIntroduce a number '))

    if num % 2 == 0:
        print(f'\nThe number {num} is even\n')
    else:
        print(f'\nThe number {num} is odd\n')

if __name__ == '__main__':
    even_odd()
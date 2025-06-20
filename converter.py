#Converter
#todo 1 Ask the user to choose an option to convert degrees or distance
#todo 2 Separate into different functions
#todo 3 Show the results
#todo 4 Do the math operations

from tkinter import simpledialog as sd, messagebox as mb

# Main menu
def menu():
    opc = True
    while opc == True:
        op = sd.askinteger('Menu',
'''Choose an opcion

1) Convert from degrees Celsius to degrees Fahrenheit
2) Convert from degrees Fahrenheit to degrees Celsius
3) Convert from miles to kilometers
4) Convert from kilometer to miles
5) Close
''')
        if op == 1 :
            celsius_fahrenheit()
        elif op == 2 :
            fahrenheit_celsius()
        elif op == 3 :
            miles_km()
        elif op == 4 :
            km_miles()
        elif op == 5 :
            mb.showinfo('Menu',
'Closing the window')
            opc = False
            break
        else:
            mb.showerror('Error',
'Introduce a valid number')

def celsius_fahrenheit():
    # Asking for a number to convert
    celsius = sd.askfloat('Converter',
'Introduce the degree in Celsius to convert ')
    
    #Formula to convert from C to F
    fahrenheit = (celsius * (9/5)) + 32

    #Showing the result
    mb.showinfo('Converter',
f'{celsius} Celsius degree are {round(fahrenheit,1)} Fahrenheit degree')

def fahrenheit_celsius():
    # Asking for a number to convert
    fahrenheit = sd.askfloat('Converter',
'Introduce the degree in Fahrenheit to convert ')
    
    # Formula to convert from F to C
    celsius = (fahrenheit - 32) * (5/9)

    # Showing the result
    mb.showinfo('Converter',
f'{fahrenheit} Fahrenheit degree are {round(celsius,1)} Celsius degree')

def miles_km():
    # Asking a number to convert
    miles = sd.askfloat('Converter',
'Introduce the miles to convert')
    
    # Formula to convert
    km = miles * 1.60934

    # Showing the result
    mb.showinfo('Converter',
f'{miles} miles are {round(km,3)} km')

def km_miles():
    # Asking a number to convert
    km = sd.askfloat('Converter',
'Introduce the miles to convert')
    
    # Formula to convert
    miles = km * 0.621371

    # Showing the result
    mb.showinfo('Converter',
f'{km} km are {round(miles,3)} miles')

if __name__ == '__main__':
    menu()
from menu_designer import *
import os

temperature_list = list(("Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Réamur", "Romer"))

def convert(unit, value):
    if unit == 0:
        print(str(value) + "° Kelvin")
    elif unit == 1:
        converted_value = value - 273.15
        print(str(round(converted_value, 2)) + "° Celsius")
    elif unit == 2:
        converted_value = (value*(9/5))-459.67
        print(str(round(converted_value, 2)) + "° Fahrenheit")
    elif unit == 3:
        converted_value = value * (9/5)
        print(str(round(converted_value, 2)) + "° Rakine")
    elif unit == 4:
        converted_value = (373.15-value)*(3/2)
        print(str(round(converted_value, 2)) + "° Delisle")
    elif unit == 5:
        converted_value = (value-273.15) * (33/100)
        print(str(round(converted_value, 2)) + "° Newton")
    elif unit == 6:
        converted_value = (value-273.15) * (4/5)
        print(str(round(converted_value, 2)) + "° Réamur")
    elif unit == 7:
        converted_value = ((value-273.15) * (21/40))+7.5
        print(str(round(converted_value, 2)) + "° Romer")

def printCalc(value, selection):
    os.system('cls' if os.name == 'nt' else 'clear')
    if selection == 0:
        converted_value = value
    elif selection == 1:
        converted_value = value + 273.15
    elif selection == 2:
        converted_value = (value+459.67) * (5/9)
    elif selection == 3:
        converted_value = (value) * (5/9)
    elif selection == 4:
        converted_value = 373.15 - (value * (2/3))
    elif selection == 5:
        converted_value = (value*(100/33)) + 273.15
    elif selection == 6:
        converted_value = (value*(5/4)) + 273.15
    elif selection == 7:
        converted_value = (value-7.5)*(40/21)+273.15
    print("Temperature is: " + str(value) + "° " + str(temperature_list[selection]))
    print("───────────────────")
    print("Equivalents")
    print("───────────────────")
    for x in range(len(temperature_list)):
        convert(x, converted_value)
    print("───────────────────")

def run():
    correct = 0
    while correct == 0:
        menu("Temperature converter", "Select the temperature to convert from", temperature_list)
        selection = input("Select the temperature unit: ")
        if selection != '':
            if int(selection) <= 8:
                if int(selection) > 0:
                    correct = 1
        os.system('cls' if os.name == 'nt' else 'clear')
    correct = 0
    while correct == 0:
        value = input("Enter the temperature value: ")
        if value != '':
            correct = 1
    printCalc(int(value), int(selection)-1)
    input("Press enter to exit...")

run()
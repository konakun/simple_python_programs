from menu_designer import *
import random

PROJECT_PATH = os.path.dirname(__file__)
optionList = ["Yes", "No"]

def generateLowerCase():
    random.seed()
    keychar = chr(random.randint(97,122))
    return keychar

def generateUpperCase():
    random.seed()
	keychar = chr(random.randint(65,90))
    return keychar

def generateNumber():
	random.seed()
    keychar = chr(random.randint(48,57))
    return keychar

def generateSymbol():
    random.seed()
    symbol_part = random.randint(1,4)
    if symbol_part == 1:
        return chr(random.randint(33,47))
    elif symbol_part == 2:
        return chr(random.randint(58,64))
    elif symbol_part == 3:
        return chr(random.randint(91,95))
    elif symbol_part == 4:
        return chr(random.randint(123,126))

def generator(length, numbers, symbols):
    key = ''
    if numbers == 0:
        if symbols == 0:
            for i in range (length):
                random.seed()
                val = random.randint(1,4)
                if val == 1:
                    ##lower case letter
                    key += generateLowerCase()
                elif val == 2:
                    ##Upper case letter
                    key += generateUpperCase()
                elif val == 3:
                    ##Number
                    key += generateNumber()
                elif val == 4:
                    ##Symbols
                    key += generateSymbol()
        else:
            for i in range (length):
                random.seed()
                val = random.randint(1,3)
                if val == 1:
                    ##lower case letter
                    key += generateLowerCase()
                elif val == 2:
                    ##Upper case letter
                    key += generateUpperCase()
                elif val == 3:
                    ##Number
                    key += generateNumber()
    else:
        if symbols == 0:
            for i in range (length):
                random.seed()
                val = random.randint(1,3)
                if val == 1:
                    ##lower case letter
                    key += generateLowerCase()
                elif val == 2:
                    ##Upper case letter
                    key += generateUpperCase()
                elif val == 3:
                    ##Symbols
                    key += generateSymbol()
        else:
            for i in range (length):
                random.seed()
                val = random.randint(1,2)
                if val == 1:
                    ##lower case letter
                    key += generateLowerCase()
                elif val == 2:
                    ##Upper case letter
                    key += generateUpperCase()

    clear()
    print("Your generated password is: " + key)
    with open('password.txt', 'a') as file:
        file.write(key + '\n')
    print("It will be saved in plain text file passwords.txt")

def run():
    correct = False
    while correct != True:
        window("Password Generator - Password Length", "Select a password length")
        length = int(input("Insert the password length: "))
        print(length)
        if length > 0 & length != '':
            correct = True
        clear()
    correct = False
    while correct != True:
        menu("Password Generator - Numbers", "Choose if you want numbers inside your password", optionList)
        numbers = int(input("Insert the option: "))
        if numbers > 0 & numbers < 3 & numbers != '':
            correct = True
        clear()
    correct = False
    while correct != True:
        menu("Password Generator - Symbols", "Choose if you want symbols inside your password", optionList)
        symbols = int(input("Insert the option: "))
        if symbols > 0 & symbols < 3 & symbols != '':
            correct = True
        clear()
    correct = False
    generator(length, numbers-1, symbols-1)

def main():
    clear()
    run()

if __name__ == "__main__":
    main()
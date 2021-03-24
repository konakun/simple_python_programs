import os

def menu(title, message, optionList):
    count = 0
    print(title)
    print("──────────────────────────────────────")
    print(message)
    print("──────────────────────────────────────")
    print("──────────────────────────────────────")
    for option in optionList:
        count+=1
        print(str(count)+'.- '+option)
    print("──────────────────────────────────────")

def window(title, message):
    print(title)
    print("──────────────────────────────────────")
    print(message)
    print("──────────────────────────────────────")
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
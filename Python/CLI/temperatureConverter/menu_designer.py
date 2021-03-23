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
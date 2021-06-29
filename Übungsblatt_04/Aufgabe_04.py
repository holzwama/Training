import string

buchstabenListeLower = list(string.ascii_lowercase)
buchstabenListeUpper = list(string.ascii_uppercase)

userinput = list(input("Geben Sie den Text ein \n"))

def buchstabenSwap(lis):
    position = 13
    i = 1
    decodedList = []
    for buchstabe in lis:
        if buchstabe == buchstabenListeLower:
            decodedList.append(buchstabenListeLower)

    return decodedList

result = buchstabenSwap(userinput)
print(result)
import string

CHARSLOWER = list(string.ascii_lowercase)
CHARSUPPER = list(string.ascii_uppercase)

def rot13(text):
    result = '' 

    for letter in text:
        #Kleinbuchstaben herausfinden
        if letter.islower() & letter.isalpha():
            text = text.lower()
            result += CHARSLOWER[(CHARSLOWER.index(letter) + 13) % 26]
        ##Großbuchstaben herausfinden
        elif letter.isupper() & letter.isalpha():
            text = text.upper()
            result += CHARSUPPER[(CHARSUPPER.index(letter) + 13) % 26]

    return result

def saveFile(text):
    f = open("Test_swap.txt", "w")
    f.write(text)
    f.close()

try:
    userinput = input('"Welche Datei wollen sie öffnen?"')
    with open(userinput, 'r') as f2:
        data = f2.read()
    encData = rot13(data)
    print(encData)
    saveFile(encData)

except FileNotFoundError:
    print("Falscher Dateiname")
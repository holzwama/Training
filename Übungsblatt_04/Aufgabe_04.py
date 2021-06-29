import string

buchstabenListeLower = list(string.ascii_lowercase)
buchstabenListeUpper = list(string.ascii_uppercase)
try:
    userinput = input('"Welche Datei wollen sie öffnen?"')

    with open(userinput, 'r') as f2:
        data = f2.read()


    def rot13(text):
        result = '' 

        for letter in text:
            #Kleinbuchstaben herausfinden
            if letter.islower() & letter.isalpha():
                text = text.lower()
                result += buchstabenListeLower[(buchstabenListeLower.index(letter) + 13) % 26]
            ##roßbuchstaben herausfinden
            elif letter.isupper() & letter.isalpha():
                text = text.upper()
                result += buchstabenListeUpper[(buchstabenListeUpper.index(letter) + 13) % 26]
    
        return result

    def saveFile(text):
       f = open("Test_swap.txt", "w")
       f.write(text)
       f.close()

    print(rot13(data))
    saveFile(rot13(data))
except FileNotFoundError:
    print("Falscher Dateiname")
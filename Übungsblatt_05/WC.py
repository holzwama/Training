# funktion um Anzahl der Wörter zu bestimmen
def wordsFunc(userlang):
    with open('Test_python.txt') as infile:
        words=0
        for line in infile:
            wordslist=line.split()
            words=words+len(wordslist)
    if userlang == "de":
        print(words, "Wörter")
    else:
        print(words, "words")

# funktion um Anzahl der Buchstaben zu bestimmen
def charsFunc(userlang):
    with open('Test_python.txt') as infile:
        words=0
        characters=0
        for line in infile:
            wordslist=line.split()

            words=words+len(wordslist)
            characters += sum(len(Word) for Word in wordslist)
    if userlang == "de":
        print(characters, "Buchstaben")
    else:
        print(characters, "letters")

# funktion um Anzahl der Linien zu bestimmen
def linesFunc(userlang):
    with open('Test_python.txt') as infile:
        lines=0
        for line in infile:
            lines=lines+1
    if userlang == "de":
        print(lines, "Linien")
    else:
        print(lines, "lines")
        


def main():
    lang = input("Welche Sprache möchten Sie ausgegeben bekommen? (de | en) \n")
    linesFunc(lang)
    wordsFunc(lang)
    charsFunc(lang)

if __name__ == "__main__":
    main()
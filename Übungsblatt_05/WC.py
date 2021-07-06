from collections import Counter

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
        chars=0
        for line in infile:
            wordslist=line.split()
            words=words+len(wordslist)
            chars += sum(len(Word) for Word in wordslist)
    if userlang == "de":
        print(chars, "Buchstaben")
    else:
        print(chars, "letters")

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
# funktion um Anzahl der verschiedenen Wörter zu bestimmen     
def word_counter(file):
    with open(file) as f:
        return print(Counter(f.read().split()))
# funktion um Anzahl der verschiedenen Buchstaben zu bestimmen  
def char_counter(file):
    with open(file) as file:
        charcount = {} 
        validchars = "abcdefghijklmnopqrstuvwxyz" 
        
        for i in range(97,123):
            c = (chr(i)) 
            charcount[c] = 0 
        
        for line in file:
            words = line.split(" ") 
            for word in words:  
                chars = list(word) 
            for c in chars:  
                if c.isalpha(): 
                    if c.isupper():
                        c = c.lower()  
                    if c in validchars: 
                        charcount[c] += 1 
    print(charcount) 

def main():
    textData = 'Test_python.txt'
    lang = input("Welche Sprache möchten Sie ausgegeben bekommen? (de | en) \n")
    linesFunc(lang)
    wordsFunc(lang)
    charsFunc(lang)
    word_counter(textData)
    char_counter(textData)

if __name__ == "__main__":
    main()
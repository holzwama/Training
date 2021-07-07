#Soundex
def soundex(userWord):
    counter = 1
    encodedWord = userWord
    result = [userWord[0], "0", "0", "0", "0", "0"]
    if counter <= 6:
        for i in range(1, len(encodedWord)):
            letter = encodedWord[i]
            if letter in ['B','F','P','V']:
                result[counter] = 1
                counter += 1
            elif letter in ['C','G','J','K','Q','S','X','Z']:
                result[counter] = 2
                counter += 1
            elif letter in ['D','T']:
                result[counter] = 3
                counter += 1
            elif letter in ['L']:
                result[counter] = 4
                counter += 1
            elif letter in ['M','N']:
                result[counter] = 5
                counter += 1
            elif letter in ['R']:
                result[counter] = 6
                counter += 1
    return result

def fillList(encWord):
    unique = []
    sorted_encodedWord = encWord
    for letters in sorted_encodedWord:
            if letters not in unique:
                unique.append(letters)

    while len(unique) <=5:
            i = len(unique) 
            temp = i
            unique.append("0")
    return unique

def main():
    decodedWord = input("Enter a word to decipher \n")
    encodedWord = decodedWord.upper()
    sorted_encodedWord = soundex(encodedWord)
    print(fillList(sorted_encodedWord))

if __name__ == "__main__":
    main()
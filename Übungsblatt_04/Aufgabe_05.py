# Soundex

def addDigit(list, place, number):
    if place != 0 and place == 1:
        list[place] = number
        return 1
    elif place != 0 and place < 6:
        if list[place - 1] != number:
            list[place] = number
            return 1
    return 0


def soundex(userWord):
    counter = 1
    encodedWord = userWord
    result = [userWord[0], 0, 0, 0, 0, 0]
    for letter in encodedWord[1:]:
        if letter in ['B', 'F', 'P', 'V']:
            counter += addDigit(result, counter, 1)
        elif letter in ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z']:
            counter += addDigit(result, counter, 2)
        elif letter in ['D', 'T']:
            counter += addDigit(result, counter, 3)
        elif letter in ['L']:
            counter += addDigit(result, counter, 4)
        elif letter in ['M', 'N']:
            counter += addDigit(result, counter, 5)
        elif letter in ['R']:
            counter += addDigit(result, counter, 6)
    return result

# def fillList(encWord):
#     unique = []
#     sorted_encodedWord = encWord
#     for letters in sorted_encodedWord:
#             if letters not in unique:
#                 unique.append(letters)

#     while len(unique) <=5:
#             i = len(unique)
#             temp = i
#             unique.append(0)
#     return unique


def main():
    decodedWord = input("Enter a word to decipher \n")
    encodedWord = decodedWord.upper()
    sorted_encodedWord = soundex(encodedWord)
    print(sorted_encodedWord)


if __name__ == "__main__":
    main()

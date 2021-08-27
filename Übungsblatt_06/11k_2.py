#!/usr/bin/python3
import sys

def compress(word):
    last_chr = word[0]
    counter = 1
    compressed = ""

    # Vergleiche aktuellen Buchstaben mit letzten Buchstaben
    for c in word[1:]:
        if c == last_chr:
            counter += 1
        elif c != last_chr and counter == 1:
            compressed += last_chr
            last_chr = c
        else:
            compressed += last_chr + str(counter)
            last_chr = c
            counter = 1

    # Letzte Buchstaben des Wortes noch ausgeben
    if counter == 1:
        compressed += last_chr
    else:
        compressed += last_chr + str(counter)

    return compressed

def main(args):
    for arg in ["abbccc", "aaabbc", "aaaabbbccdefg", "aaaaaaaaaaaaaaaaaaaabb"]:
        print(compress(arg))
    # for arg in args:
    #     print(compress(arg))
        

if __name__ == '__main__':
    main(sys.argv[1:])
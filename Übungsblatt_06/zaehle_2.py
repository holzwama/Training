#!/usr/bin/python3
import sys

def zaehle(words):
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    top = []
    for k in sorted(dic, key=dic.get, reverse=True):
        if (top == []) or (dic[k] == top[0][1]):
            top.append((k, dic[k]))

    return sorted(top)
    

def main(args):
    lis = (zaehle(["ein", "Text", "wird", "ein", "Beispiel", "das", "danach", "weggeworfen", "wird"]))
    # lis = (zaehle(args))

    for tup in lis:
        print(str(tup[1]) + ": " + str(tup[0]))


if __name__ == '__main__':
    main(sys.argv[1:])
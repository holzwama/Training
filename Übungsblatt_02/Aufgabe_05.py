germanDic = { 1 : "Eins", 2: "Zwei" , 3 : "Drei"}
englishDic = { 1 : "One", 2: "Two" , 3 : "Three"}

def translation(german, english):
    untranslated = german
    translated = english
    swapped = 1
    while swapped <= len(translated):
        untranslated[swapped] = translated [swapped]
        print (untranslated[swapped])
        swapped += 1
translation(germanDic, englishDic)

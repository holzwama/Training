import sys

Input1 = ['f', 'b', 'c']
Input2 = ['what', 'doin', "sdada"]

def combinedList(list1, list2):

    result = [None]*len(list1)+len(list2)
    result[::2] = list1
    result[1::2] = list2
    print(result)

combinedList(Input1,Input2)
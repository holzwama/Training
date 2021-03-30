import sys

Input1 = sys.argv[1]
Input2 = sys.argv[2]

def combineList(list1,list2):
    combinedList = list1 + list2
    combinedList_sorted = sorted(combinedList)
    print(combinedList_sorted)


combineList(Input1, Input2)
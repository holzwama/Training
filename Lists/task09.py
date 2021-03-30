import sys

InputList1 = sys.argv[1]
InputList2 = sys.argv[2]

def combineList(list1,list2):
    combinedList = list1 + list2
    print(combinedList)

combineList(InputList1, InputList2)

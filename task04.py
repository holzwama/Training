import sys

InputList = [20,6,6,5,4,3,2,1,0]

def odd_position(list):
    for idx, value in enumerate(list):
        if idx % 2 != 0:
            print(value)

odd_position(InputList)
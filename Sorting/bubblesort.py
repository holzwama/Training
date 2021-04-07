import random

LIST_SIZE = 20
MAX = 100
MIN = 0


def bubblesort(lis):
    size = len(lis)
    
    if size < 2:
        return lis

    for _ in range(len(lis)):
        for i in range(len(lis) - 1):
            if lis[i] > lis[i +1]:
                lis[i], lis[i +1] = lis[i+1], lis[i]


random_list = [random.randint(MIN,MAX) for i in range(LIST_SIZE)]
print(random_list)
bubblesort(random_list)
print(random_list)
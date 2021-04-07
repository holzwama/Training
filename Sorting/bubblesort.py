import random
LIST_SIZE = 10
MAX = 10
MIN = 0
random_list = [random.randint(MIN,MAX) for i in range(LIST_SIZE)]

def bubblesort(lis):

    size = len(lis)
    
    if size < 2:
        return lis

    for j in range(len(lis)):
        for i in range(len(lis) - 1):
            if lis[i] > lis[i +1]:
                lis[i], lis[i +1] = lis[j+1], lis[j]
print(random_list)
bubblesort(random_list)
print(random_list)
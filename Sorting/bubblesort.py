import random
LIST_SIZE = 10
MAX = 10
MIN = 0
random_list = [random.randint(MIN,MAX) for i in range(LIST_SIZE)]

def bubblesort(lis):
    Sorted = False
    temp = 0
    element_1 = 0
    element_2 = 1
    while not Sorted:
        temp = random_list[element_2]
        if random_list[element_1] > random_list[element_2]:
            random_list[element_2] = random_list[element_1]
            random_list[element_1] = temp
            element_1 +=1
            element_2 +=1


bubblesort(random_list)
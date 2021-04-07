import random
LIST_SIZE = 10
MAX = 10
MIN = 0
random_list = [random.randint(MIN,MAX) for i in range(LIST_SIZE)]

def quicksort(lis):
    size = len(lis)
    
    if size < 2:
        return lis
    
    position = 0


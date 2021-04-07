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

    for x in range(1, size):
        if lis[x] <= lis[0]:
            position += 1
            temp = lis[x]
            lis[x] = lis[position]
            lis[position] = temp
    
    temp = lis[0]
    lis[0] = lis[position] 
    lis[position] = temp 
    
    left = quicksort(lis[0:position]) 
    right = quicksort(lis[position+1:size]) 

    lis = left + [lis[position]] + right 
    
    return lis

print(random_list)
quicksort(random_list)
print(random_list)
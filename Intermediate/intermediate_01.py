numbers_list = []
max_value = 9 
list_year = []
def fill_list(empty_list):
    counter = 1
    while len(empty_list) != max_value:
        empty_list.append(counter)
        counter += 1

fill_list(numbers_list)
print(numbers_list)
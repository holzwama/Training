numbers_list = []
max_value = 100 + 1
list_year = []
def fill_list(empty_list):
    counter = 0
    while len(empty_list) != max_value:
        empty_list.append(counter)
        counter += 1


def until_100(list_):
    result = 0
    count_one = 0
    count_two = 1
    temp = 0
    while result != 100:
        temp = list_[count_one] + list_[count_two]
        result = result + temp
        count_one += 1
        count_two += 1
        print(result)



fill_list(numbers_list)
until_100(numbers_list)


MIN = 0
MAX = 100
first_max = 10
list_extract = range(MIN, MAX + 1)

def first_ten(lis):
    counter = 0
    while counter <= first_max:
        print(lis[counter])
        counter += 1
    if counter <= first_max + 1:
        print("-------, Above are the first", first_max, ("numbers from the list"))

def last_ten(lis):
    counter = MAX - 10
    while counter <= MAX:
        print(lis[counter])
        counter += 1
    if counter <= MAX +1:
        print("-------, Above are the last", first_max  ,"numbers from the list")

def every_tenth(lis):
    counter = 0
    while counter <= MAX:
        print(lis[counter])
        counter += 10
    if counter <= MAX +10:
        print("-------, Every tenth number from the list")

def mid_number(lis):
    value = int(len(lis) /2 )
    print(lis[value], "<- This is the middle number")

def every_third_one(lis):
    counter = 3
    while counter <= MAX - 5:
        print(lis[counter + 1])
        counter +=3
    if counter <= MAX +3:
        print('------, Ever third number from the list is above')

def main():
    first_ten(list_extract)
    last_ten(list_extract)
    every_tenth(list_extract)
    mid_number(list_extract)
    every_third_one(list_extract)

if __name__ == "__main__":
    main()
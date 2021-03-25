
next_years = 20
print("Type a year")
users_year = int(input())

list_year = []

def fill_list(empty_list):
    counter = 1
    while len(empty_list) != 20:
        list_year.append(users_year + counter)
        counter += 1

def leap_year(list_):
    for x in list_:
        if x % 100 == 0:
            print(x, "No leap year")
        elif x % 400 == 0:
             print(x, "is a leap year")
        elif x %   4 == 0:
            print(x, "Is a leap year")
        else:
            print(x, "No leap year")

fill_list(list_year)
leap_year(list_year)
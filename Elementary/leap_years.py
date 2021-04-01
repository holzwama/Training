
next_years = 20
print("Type a year")
year_input = int(input())
list_year = range(year_input, year_input+next_years+1)

def leap_year(years):
    for year in years:
        if year % 400 == 0:
            print(year, "is a leap year")
        elif year % 100 == 0:
            print(year, "No leap year")        
        elif year %   4 == 0:
            print(year, "Is a leap year")
        else:
            print(year, "No leap year")

leap_year(list_year)
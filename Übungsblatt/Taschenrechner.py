import sys

number_one = int(sys.argv[1])
sign = sys.argv[2]
number_two = int(sys.argv[3])

def calculator(value_one, value_two):
    if sign == "+":
        result = value_one + value_two
        print(result)
    if sign == "-":
        result = value_one - value_two
        print(result)
    if sign == "*":
        result = value_one * value_two
        print(result)
    if sign == "/":
        result = value_one / value_two
        print(result)

calculator(number_one, number_two)


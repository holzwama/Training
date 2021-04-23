import sys

number_one = int(sys.argv[1])
sign = sys.argv[2]
number_two = int(sys.argv[3])

def calculator(value_one, value_two):
    if sign == "+":
        result = value_one + value_two
    elif sign == "-":
        result = value_one - value_two
    elif sign == "*":
        result = value_one * value_two
    elif sign == "/":
        result = value_one / value_two
    return result

print(calculator(number_one, number_two))


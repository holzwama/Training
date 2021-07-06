def add(elem):
    if elem is not stack:
        stack.append(elem)


while user_input != 4:
    user_input = input("Was wollen Sie zum Stack hinzufügen??\n", "1 - Element hinzufügen, 4 - Beenden")
    
stack = []
user_input = 0
add(user_input)
print(stack)

import string
stack = []

def add(elem):
    if elem not in stack:
        stack.append(elem)
    return stack


def union_update(seq):
    stack = seq
    stack = "".join(stack)
    print(stack)

def union(seq):
    stack = seq
    union_update(stack)
    print(stack)

def size(stack):
    x = len(stack)
    print("Anzahl der Elemente >>>>>> ", x)
    

def clear(stack):
    print("Stack wird geleert")   
    stack.clear()

user_choice = 0
print("Was möchten sie tun?`\n")
while user_choice == 0:
    user_choice = int(input("Element hinzufügen - 1, Elemente einer Sequenz hinzufügen - 2, Menge der Seq zurückgeben - 3"
    ", Element löschen? -4, Differenz ausgeben - 5, Menge reset - 6, Anzahl der Elemente ausgeben -7 \n "))
    
    if user_choice == 1:
        element = input("Wie lautet das Element, welches sie hinzufügen möchten?`\n")
        add(element)
        print(stack)
        user_choice = 0
    
    if user_choice == 2:
        union_update(stack)
        user_choice = 0
    
    if user_choice == 3:
        union(stack)
        user_choice = 0
    
    if user_choice == 4:
        user_pop = int(input("Das Element an welcher Stelle möchten sie löschen?\n"))
        stack_len = len(stack)
        if stack_len > user_pop:
            del_elem = stack.pop(user_pop)
            print("Folgendes Element wurde gelöscht >>>>>>", del_elem)
            print("Aktueller Stack:", stack)
            user_choice = 0
        else:
            print("Kein Element im Stack gefunden")
            user_choice = 0

    if user_choice == 5:
        user_choice = 0

    if user_choice == 6:
        clear(stack)
        user_choice = 0
    
    if user_choice == 7:
        size(stack)
        user_choice = 0

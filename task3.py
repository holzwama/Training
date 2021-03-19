import sys

checkarg = sys.argv[1]
mylist = ["5", "banana", "cherry", "test"]
counter = False

for x in mylist:
    if x == checkarg:
        print("You were right, it's one of the correct arguments!")
        counter = True

if counter == False:
    print("Not given!")



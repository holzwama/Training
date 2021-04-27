
def teiler(num_one, num_two):
    counter = 1
    lis_one = []
    lis_two = []
    while counter <= num_one:
        if num_one % counter == 0:
            lis_one.append(counter)
        if num_two % counter == 0:
            lis_two.append(counter)
        else:
            counter +=1
    print(lis_one)
def main():
    print("Geben Sie zwei Zahlen ein, um den größten Gemeinsamen Teiler zu berechnen")
    x = print(input("Zahl 1: \n"))
    y = print(input("Zahl 2: \n"))
    teiler(x,y)
    
if __name__ == "__main__":
    main()
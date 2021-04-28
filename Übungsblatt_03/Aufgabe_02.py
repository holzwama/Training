
def teiler(num_one, num_two):
    counter = 0
    big_num = num_one
    lis_one = []
    lis_two = []
    if big_num <= num_two:
        big_num = num_two
    while counter < big_num:
        counter +=1
        if num_one % counter == 0:
             lis_one.append(counter)
        if num_two % counter == 0:
            lis_two.append(counter) 
    print(set(lis_one).intersection(lis_two)) # Vergleicht die Werte von zwei Listen miteinander & gibt diese aus

def main():
    print("Geben Sie zwei Zahlen ein, um den größten Gemeinsamen Teiler zu berechnen")
    x = int(input("Zahl 1: \n"))
    y = int(input("Zahl 2: \n"))
    teiler(x,y)
    
if __name__ == "__main__":
    main()
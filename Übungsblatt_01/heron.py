user_root = float(input("Quadratwurzel: "))
starting_value = float(input("Startwert: ")) 

def heron(start, root):
    for i in range(1,9):
        x = 0.5*(start+root/start)
        print ('   ',i,'    ',x)

def main():
    heron(starting_value, user_root)

if __name__ == "__main__":
    main()
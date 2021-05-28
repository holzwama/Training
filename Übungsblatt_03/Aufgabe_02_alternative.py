
# Iterative Funktion ggT mit 2 Parametern x | y
# X | Y sortieren nach Größen -> X > Y
# while ggT = 0
# if x % y == 0 then ggT = y
# else x,y = y, x % y

#It. Funktion ggTL die den größten ggT von einer Liste berechnet
# Jeden Teiler jeder Zahl herausfinden
# result = ggT(erste Zahl, zweite Zahl)
# for next in lis[2:]
#   result = ggT(result, next)

def ggT(x, y):
    if y > x:
        x,y = y,x
    if y == 0:
        print("Null ist durch eine beliebige Ganzzahl teilbar.")
        return x
    else:
        return ggT(y, x % y)

def ggT_list(lis):
	for i in range(0, len(lis)-1):
		while lis[1]:      
			lis[0], lis[1] = lis[1], lis[0] % lis[1]
		lis[1] = lis[i+1]
		return lis[0]

def main():
    print("Geben Sie zwei Zahlen ein, um den größten Gemeinsamen Teiler zu berechnen")
    x = int(input("Zahl 1: \n"))
    y = int(input("Zahl 2: \n"))
    print(ggT(x,y))
    test_list = [25, 20, 10,  75, 80]
    print(ggT_list(test_list))
    
if __name__ == "__main__":
    main()
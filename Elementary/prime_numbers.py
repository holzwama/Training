max_value = int(input("Maximalwert eingeben, bis zu welchem die Primzahlen ausgegeben werden sollen: "))
print(max_value)

list_numbers = range(1, max_value+1)



def primes(prime_list):
   
    for x in prime_list:
        if x % 1 == 0:
            print(x, "ist keine Primzahl")            
        elif x % x == 0:
            print(x,"ist eine Primzahl")
            

primes(list_numbers)
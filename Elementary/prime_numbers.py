max_value = int(input("Maximalwert eingeben, bis zu welchem die Primzahlen ausgegeben werden sollen: "))
print(max_value)
list_numbers = []

def fill_list(empty_list):
    counter = 1
    while counter <= max_value:
        list_numbers.append(counter)
        counter += 1


def primes(prime_list):
   
    for x in prime_list:
        if x % 1 == 0:
            print(x, "ist keine Primzahl")
            
        elif x % x == 0:
            print(x,"ist eine Primzahl")
            

fill_list(list_numbers)
primes(list_numbers)
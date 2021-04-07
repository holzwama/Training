def primes():
    n = 1
    prim = True
    max_value = int(input("Maximalwert eingeben, bis zu welchem die Primzahlen ausgegeben werden sollen: "))
    while n < max_value:
        prim = True
        if n == 1:
              prim = False      
        else:
            i = 2
            while i <= n - 1:
                if n % i == 0:
                    prim = False
                i += 1
        if prim == True:
            print(n)
        n += 1

primes()
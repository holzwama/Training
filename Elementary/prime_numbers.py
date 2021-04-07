def primes(max_value=100):
    start = 2
    prim = True
    primes = []
    for n in range(start, max_value+1):
        prim = True
        for i in range(2, n):
            if n % i == 0:
                prim = False
        if prim == True:
            primes.append(n)
    return primes

def primes2(n):
    """ Returns  a list of primes < n """
    # Stichwort Sieb des Erastothenes
    # https://www.youtube.com/watch?v=Cg8P4GNPe0I
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def main():
    max_value = int(input("Maximalwert eingeben, bis zu welchem die Primzahlen ausgegeben werden sollen: "))
    my_primes = primes(max_value)
    print(my_primes)
    # print(primes(1000))
    # primes2(1000000)

if __name__ == "__main__":
    main()
##Kubikzahlen
print("GERADE KUBIKZAHLEN")
basic_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kubik_list = [x ** 3 for x in basic_numbers if x ** 3 % 2 == 0]
kubik_list_a = list(filter(lambda y: y % 2 == 0, map(lambda x: x ** 3, basic_numbers)))
print(kubik_list)
print(kubik_list_a)

##Teiler
<<<<<<< HEAD
print("ALLE TEILER / List Comprehension")

=======
teiler_numbers = []
print(teiler_numbers)
>>>>>>> c677e842b09952b5cc8b4b3de3d517289aa42842

def teilerVonZ(z):
    return [x for x in range(2, z // 2 + 1) if z % x == 0]


print(teilerVonZ(123))
print(teilerVonZ(12345))
print(teilerVonZ(123456))

print("ALLE TEILER / primitive")


def funTeilerVonZ(z):
    return list(filter(lambda x: z % x == 0, range(2, z // 2 + 1)))


print(funTeilerVonZ(123))
print(funTeilerVonZ(12345))
print(funTeilerVonZ(123456))

##Primzahlen
print("Primzahlen")


def checkPrime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


primzahlen = [x for x in range(10000, 10100 + 1) if checkPrime(x)]
primzahlen_a = list(filter(lambda x: checkPrime(x), range(10000, 10100 + 1)))

print(primzahlen)
print(primzahlen_a)

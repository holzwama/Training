import math

MAX = 100
PAIRS_DIF = 2

def prim_gen(prim):

    i = prim
    while True:
        for x in range(2, int(math.sqrt(i) + 1)):
            if i%x==0:
                break
        else:
            if i >= MAX:
                break
            print(i)
        i += 1

def is_prime(prim):
        for x in range(2,prim):
            if prim % x == 0:
                return False
        return True

def pairs_gen(first, last):
   for num_one in range(first, last):
      num_two = num_one + PAIRS_DIF
      if(is_prime(num_one) and is_prime(num_two)):
         print("{:d} {:d}".format(num_one, num_two))

pairs_gen(2, 100)
# 1. 4 Zahlen
# 2. Müssen alle unterschiedlich sein (1,3,4)
# 3. Kubikzahlen von diesen berechnen
# 4. a^3 + b^3 = c^3 + d^3 
# 5. keine doppelten Ergebnisse
# Ergebniss soll aussehen wie folgt: [(1729, 1,12,9,10), (????, ?,?,?,?)] -> Tipp: sortieren

import math
 
def printTaxicab2(N):
 
    # Starting from 1, check every number if
    # it is Taxicab until count reaches N.
    i, count = 1, 0
    while (count < N):
     
        int_count = 0
        for j in range(1, math.ceil(\
                   pow(i, 1.0 / 3)) + 1):
             
            for k in range(j + 1,\
              math.ceil(pow(i, 1.0 / 3)) + 1):
                if (j * j * j + k * k * k == i):
                    int_count += 1
         
        # Taxicab(2) found
        if (int_count == 2):
         
            count += 1
            print(count, " ", i)
 
        i += 1
     
# Driver code
N = 10
printTaxicab2(N)
 
counter = 1
lis_one = []
x = 20
while counter <= 20:
    if x % counter == 0:
        lis_one.append(counter)
        counter += 1
print (lis_one)

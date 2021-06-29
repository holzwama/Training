Zahlen = [1,2,3,4]
Buchstaben = ["a","b","c"]
print(list(zip(Zahlen, Buchstaben)))

print(list(zip((1,2,3,4), (5,6), (7,8))))

def unzip(lis):
    return list(zip(*lis))

zipped = list(zip((1,2,3), (4,5), (6,7,8)))
unzipped = list(unzip(zipped))

print(zipped)
print(unzipped)
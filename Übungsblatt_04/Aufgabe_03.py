#Zahlen = [1,2,3,4]
#Buchstaben = ["a","b","c"]
#print(list(zip(Zahlen, Buchstaben)))

#print(list(zip((1,2,3,4), (5,6), (7,8))))

def unzip(lis):
    return list(zip(*lis))


print(list(unzip(list(zip((1,2,3,4), (5,6), (7,8))))) == [(1,2), (5,6), (7,8)])
t = [(1,2), (3,4), (5,6)]
print(list(unzip(list(unzip(t)))) == t)
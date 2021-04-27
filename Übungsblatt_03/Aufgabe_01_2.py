dic = {1: "eins", 2: "zwei", 3: "drei"}
lis = list(dic.keys())
idx = 0
while idx < len(lis):
    key = lis[idx]
    print(key, dic[key])
    idx = idx + 1

for key in dic:
    print(key, dic[key])

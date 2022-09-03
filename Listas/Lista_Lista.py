lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(lista)
print("---------")

print(lista[0])
print("---------")

print(lista[0][0])
print("---------")

for x in range(len(lista[0])):
    print(lista[0][x])
print("---------")               

for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])

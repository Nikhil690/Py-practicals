print('hello world')
a = [[2,5,7],
    [4,2,9],
    [11,12,13]]
print (a)
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[j][i]=a[i][j]

for r in result:
    print(r)
A = [[1,4,5,],
    [5,8,9],
    [6,7,11]]
B = [[8,7,5],
    [11,14,15],
    [6,9,3]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
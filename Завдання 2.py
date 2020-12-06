coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 4) for j in range(row)] for i in range(coulmn)]

B = [[random.randint(0, 4) for j in range(row)] for i in range(coulmn)]

print(A)
print(B)

for i in range(coulmn):
    for j in range(row):
        if A[i][j] == 0:
            A[i][j] = B[i][j]

print('\n')
print(A)

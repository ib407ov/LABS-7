coulmn = int(input('coulmn : '))
row = int(input('row : '))

import math
import random
A = [[random.randint(0, 0) for j in range(row)] for i in range(coulmn)]

for i in range(coulmn):
    for j in range(row):
        if i * j % 2 == 0:
            A[i][j] = math.factorial(j)
        else:
            A[i][j] = i * (i + 1) / 2
print(A)

B = []
for i in range(coulmn):
    for j in range(row):
        B.append(A[i][j])
print(B)
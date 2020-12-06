coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 100) for j in range(row)] for i in range(coulmn)]

Summ = 0

for i in range(coulmn):
    for j in range(row):
        if i == j:
            Summ += A[i][j]

print(Summ)
print(A)
coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(-10, 10) for j in range(row)] for i in range(coulmn)]

Summ = 0
for i in range(coulmn):
    for j in range(row):
        if i % 2 == 0 and j % 2 == 0 and A[i][j] < 0:
            Summ += A[i][j]

print(A)
print(Summ)
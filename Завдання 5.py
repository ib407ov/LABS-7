coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 20) for j in range(row)] for i in range(coulmn)]

k = 1
sumRow = 0
for i in range(coulmn):
    for j in range(row):
        if A[i][j] == False:
            k = False
    if k == True:
        sumRow += 1
    k = 1

print(A)
print(sumRow)
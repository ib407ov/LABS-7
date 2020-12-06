coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 100) for j in range(row)] for i in range(coulmn)]

print(A)

for i in range(coulmn):
   for j in range(row):
        if j % 2 == 0:
            A[j].sort()

print('\n')
print(A)

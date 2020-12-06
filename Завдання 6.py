coulmn = int(input('coulmn : '))
row = int(input('row : '))

import random
A = [[random.randint(0, 10) for j in range(row)] for i in range(coulmn)]
print(A)


b=[]
for row in A:
    b+=row
print(b)

z=[el for el in b if b.count(el)>1]
print(z)

print('Res=', max(z))


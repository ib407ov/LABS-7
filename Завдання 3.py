import random
A = [[random.randint(-10, 10) for j in range(2)] for i in range(2)]

print(A)

Determinant = A[0][0] * A[1][1] - A[1][0] * A[0][1]
print(Determinant)
import numpy as np

A = np.array([[2, 1, -1],
              [3, -2, 1],
              [1, -1, -1]])

b = np.array([-3, 9, 0])

result = np.linalg.solve(A, b)

print(f"x = {result[0]}")
print(f"y = {result[1]}")
print(f"z = {result[2]}")
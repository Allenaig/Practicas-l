'''
    |2  2|      B =|4  9  0 6|
A = |3  0|         |2  7  9 2|
    |1  7|
'''

import numpy as np
A = np.array([
    [2, 2],
    [3, 0],
    [1, 7]
])

B = np.array([
    [4, 9, 0, 6],
    [2, 7, 9, 2]
])

#Multiplicación C= A x B
C = np.dot(A, B)
print(C)
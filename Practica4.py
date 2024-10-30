#/1  2  3/
#/4  5  6/
#/7  8  9/

import numpy as np
element=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Acceder a un elemento
element = arr[1, 2]
print(element)

#Rebanar una matriz
slice_arr = arr[:, 1:]
print(slice_arr)
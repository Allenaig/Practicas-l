#/1  2  3/
#/4  5  6/
#/7  8  9/

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

#Acceder a un elemento
element = arr[0, 1] # Accede al elemento en la primera fila, segunda columna
print(element)

#Rebanar una matriz
slice_arr = arr[:, 1:] # Rebanar todas las filas, desde la segunda columna en
print(slice_arr)
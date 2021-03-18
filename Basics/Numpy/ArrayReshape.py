import numpy as np
#reshape will work on original data
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


#1d to 2d
newarr = arr.reshape(4, 3)

print(newarr)

#2d to 3d
newarr = arr.reshape(2, 3, 2)

print(newarr)

#flattening

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
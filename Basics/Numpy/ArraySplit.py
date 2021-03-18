import numpy as np
#will work on original data

#Splitting breaks one array into multiple arrays
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
newarr[1][1]=22
print(newarr)
print(arr)



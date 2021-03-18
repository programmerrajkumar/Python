import numpy as np

#creates copy of array
#axis=1 will join array columns at same  index
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
arr[1][1]=22
print(arr)
print(arr1)
print(arr2)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
arr[1][1]=22
print(arr)

arr = np.hstack((arr1, arr2)) #hstack() to stack along rows.

print(arr)
arr = np.vstack((arr1, arr2)) #vstack() to stack along columns.

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))
print(np.dstack((arr1, arr2)))
from numpy import *
# datatypes in numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# For i, u, f, S and U we can define size as well.
a1=[1,2,3,100,20]

print(array(["1","2","3"],dtype="i4"))
print(array(['q','w']))
print(array(["1","2","3"],int))

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
v = arr.view()
arr[0] = 42

print(arr)
print(x)
print(v)



print(linspace(1,100,3))
print(a1)
print(sort(a1))
print(min(a1)," ",max(a1))
print(sin(a1)," ",cos(a1))
print(log(a1)," ",log2(a1))
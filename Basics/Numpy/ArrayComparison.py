from numpy import *

a1 = array([1, 2, 3, 4, 5, 16])
a2 = array([11, 12, 13, 14, 15, 6])
a3 = array([11, 12, 13, 14, 15, 16])

print(a1 > a2)
print(a1 < a2)
print(any(a1 > a2))
print(all(a1 > a2))

print(logical_and(a1 > 3,a1))
print(where(a1%2==0,a1,0))
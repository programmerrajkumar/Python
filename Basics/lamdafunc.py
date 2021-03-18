# lamda function

# Use lambda functions when an anonymous function is required for a short period of time.

# syntax lambda arguments : expression


x = lambda a, b: a + b

print(x(11, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

lst = [10, 20, 21, 22, 23, 25]

print(list(filter(lambda x: x % 2 == 0, lst))) #predicate

print(list(map(lambda x: x * 2, lst))) #func

from functools import  reduce
print(reduce(lambda x,y:x+y,lst)) #returns scalar

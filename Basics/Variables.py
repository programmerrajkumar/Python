x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Variable Scopes


x = "global"
y = "global"


def myfunc():
    x = "local"
    global y, z
    y = "global overridden"
    print(x)


myfunc()
print(x, y)

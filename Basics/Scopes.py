x = 300  # global variable
z = 500


def myfunc():
    x = 200  # local variable
    global y
    y = 100
    global z
    z = 400
    print("local :", x)
    print("global x from func:",globals()["x"])


myfunc()

print("global :", x)
print("global :", y)
print("global :", z)

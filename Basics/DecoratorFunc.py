def decoratorfunc(func):
    def inner(num):
        res = func(num)
        return res * 10
    return inner


def getnumber(num):
    return num


print(decoratorfunc(getnumber)(10))


@decoratorfunc
def getnumberfromuser(num):
    return num


print(getnumberfromuser(int(input("Enter a number:"))))

def log(msg):
    log(msg)


# receives args as tuple
def add(*nums):
    result = 0
    for num in nums:
        result += num


add(1, 2, 3, 4)


# receives args as dictionary
def printInfo(**args):
    for arg in args:
        print(arg)
    # print(arg["age"])


printInfo(name="raj", age=26)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     -----------    ----------     ----------
#         |             |             |
#   Positional Only |(Positional   |  (Keyword Only)
#   placed before(/)|  or keyword) |
#                   |              |


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):  # arg name can't be used in func call
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
# pos_only_arg(arg=1) #this one will throw error

# kwd_only_arg(3) #this one will throw error
kwd_only_arg(arg=3)

#combined_example(1, 2, 3) #this one will throw error
combined_example(1, 2, kwd_only=3)

# combined_example(pos_only=1, standard=2, kwd_only=3) #this one will throw error

# Unpacking Argument Lists

args = [3, 6]
list(range(*args))  # array unpacking


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  # unpacking dictionary


# Documentation Strings

def docstring(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    pass


def typedparam(strparam: str, intparam: int) -> str:
    print(typedparam.__annotations__)
    return 0

typedparam(1,"kk") #doesn't throw error because it is ducktyping

# function with no body

def myfunction():
    pass


def myfunctuple():
    a = 1
    b = 2
    c = 3
    return a, b, c


res = myfunctuple()


def nestedfunc():
    def sayhi():
        return "hi"

    print(sayhi(), "world", sep=" ")


print(nestedfunc())


def funcparam(param):
    print("hello", param)


def getname():
    return "world"


print(funcparam(getname()))


def funcreturn():
    def greet(name):
        return "congrats " + name

    return greet


res = funcreturn()
print(res("muthu"))

# The default values are evaluated at the point of function definition in the defining scope, so that
i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

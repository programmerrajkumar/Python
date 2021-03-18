import CustomModule as cm
from CustomModule import person1
import datetime
import math
import json

cm.greetings("raj")

# to list all the function names (or variable names) in a module

dir(cm)

# import only parts from a module
# while using from keyword do not use the module name Ex:person1["age"], not mymodule.person1["age"]


print(person1["name"])

print(datetime.datetime.now())

print(min(1, 5, -9, 0))
print(math.pow(2, 4))

x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# convert to json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# default seperator separators=(",",":")
print(json.dumps(x, indent=1, separators=(";", "="), sort_keys=True))

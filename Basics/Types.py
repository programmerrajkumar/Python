# Text Type

stringVariable = "Hi"
stringVariable1 = 'Hello'

strVarTemp = stringVariable[0]  # nth character

strVarTemp = """multi
line
string
"""

print(len(strVarTemp))

print("hi!" * 2)  # repeat twice

if "string" not in strVarTemp:
    print(1)
# slicing
print(strVarTemp[2:5])  # from 2 to 4(5 not included) i.e 2,3,4 (5 not included)
print(strVarTemp[:5])  # from start
print(strVarTemp[2:])  # from end
print(strVarTemp[-5:-2])  # to slice from end Hello=-5 -4 -3 -2 -1
print(strVarTemp[0:5:2])  # returns by jumping index+2 elements. default is index+1
print(strVarTemp[0:5:-1])  # reversing the string

# strip - trim

print(" hi ".strip())
print("hi ".strip("h"))

myorder = "I want to pay {2:.2f} dollars for {0} pieces of item {1}."
print(myorder.format(1, 2, 3))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))

print("Name : stringVariable \nType : ", type(stringVariable), "\nValue : ", stringVariable)
print("Name : stringVariable1 \nType : ", type(stringVariable1), "\nValue : ", stringVariable1)

# Numeric Type
intVar = int(10)  # int() casting. float() str()
floatVar = 22.22
floatVar = 22e3  # 22 * 10^3
c = 2 + 2j

print("Name : a \nType : ", type(a), "\nValue : ", a)
print("Name : b \nType : ", type(b), "\nValue : ", b)
print("Name : c \nType : ", type(c), "\nValue : ", c)

# Boolean

boolVar = True | False
boolVar = bool(2)

# returns false for below values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myClass():
    def __len__(self):
        return 0


myobj = myClass()
print(bool(myobj))

# end returns false

# Sequence Types
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.




# Mapping Type

dictionaryVar = {"name": 'raj', 'job': 'se'}

# SetTypes

setVar = {"a", "b", "c"}
frozenSet = frozenset({"a", "b", "c"})

# Binary Type

binaryVar = 0B1010

bytesVar = b"Hello"

byteArrayVar = bytearray(5)

memoryViewVar = memoryview(bytes(5))

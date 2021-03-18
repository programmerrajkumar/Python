listVar = ["a", 2, 33.3, True]

listVar = list((1, 2, 2))

listVar[1:3] = [1, 2]
listVar[1:3] = [1, 2, 3]  # add additional element - 3 also and shift other elements accordingly
listVar[1:3] = [1]  # from range 1 to 2 replace with 1 i.e ["a",1,True]
listVar.insert(1, "ss")
listVar.append("www")

listVar1 = [1, 2]

listVar.extend(listVar1)  # merging two iterable objects i.e tuple or set or dic
#or
listVar2 = listVar+listVar1

listVar.remove("a")  # reove element
listVar.pop(1)  # remove@index
listVar.pop()  # remove last  element
del listVar[1]  # remove element @ index 1
del listVar1  # remove entire list i.e removes variable declaration also

listVar.clear()  # clears all values

tupleVar = ('aa', 33.4)
tupleVar = tuple(('aa', 33.4))

rangeVar = range(1, 20, 2)  # start,end,step

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

for item in listVar:
    print(item)

# List Comprehension

# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]
newlist = [x.upper() for x in fruits if "a" in x]
newlist = [x if x != "banana" else "orange" for x in fruits if "a" in x]

# Sorting

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#by default it is case sensitive sort
thislist1 = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thislist.sort(reverse=True)  # descending
print(thislist)


#Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


thislist.reverse()

#copy List

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#or

mylist = list(thislist)
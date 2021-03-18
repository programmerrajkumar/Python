#Tuple items are indexed
#indexed,Ordered,Unchangeable(no add,update,remove),allow duplicate
mytuple = ("apple", "banana", "cherry")  #packing
mytuple = tuple((1,2,1))
print(mytuple[0])
print(mytuple.count(1)) #counts no of 1


#direct update is not possible. but by converting to list and back to tuple will work
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# deleting whole tuple is possible

del x


#packing and unpacking

fruits = ("apple", "banana", "cherry") # packing

(green, yellow, red) = fruits #unpacking

print(green)
print(yellow)
print(red)


#using *


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #print except first two - return type is array


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic) #print except first and last - return type is array
print(red)


#looping

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#join
thistuple = thistuple + fruits
thistuple = thistuple *2

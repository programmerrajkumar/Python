#Hash set
#Unordered, update is not allowed ,unindexed,no duplicates

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) #duplicates ar ignored

#Accessing items

# no index or a key.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#adding items

thisset.add("mango")

thisset.update({"pineapple", "mango", "papaya"}) #adding from another iterable to existing set

#remove items

thisset.remove("mango") #throws error if item not exists
thisset.discard("mango") #no error if item not exists
thisset.pop("mango") #since unordered , doesn't know which element wil be removed
thisset.clear() #rmoves all values
del thisset

#join sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #excludes duplicate items
print(set3)


#Keep ONLY the Duplicates


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
z=x.intersection(y)
print(x)  #prints only apple

#Keep All, But NOT the Duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
z=x.symmetric_difference(y)
print(z) # prints excpet apple.not intersect items



#Get all from set1,But not duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference(y)
x.difference_update(y)


#others

z = x.isdisjoint(y) #returns bool. check if sets has common items
z = x.issubset(y) #returns bool. check if set y contains set x
z = x.issuperset(y) #returns bool. check if set x contains set y


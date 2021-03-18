#stores key value pair
#non indexed, unordered,changeable,no duplicate

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Accessing Items

#throws error if key not found
x = thisdict["model"]
x = thisdict.get("model")

x= thisdict.keys()
x= thisdict.values()
x= thisdict.items() #Key value pair


if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Add items
thisdict["color"] = 'red'
thisdict.update({"color": 'red'}) #if not exists it will add


#update items
thisdict["year"] = 2018
thisdict.update({"year": 2018})

#remove
thisdict.pop("model")
del thisdict["model"]
thisdict.clear()
del thisdict


#looping
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x) #prints key


#copy

newdict=thisdict.copy()
newdict=dict(thisdict)

for x, y in thisdict.items():
  print(x, y)

#insert many keys with same value

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x) #with no values

print(thisdict) #['key1': None, 'key2': None, 'key3': None]


#Get value of key. if not exists insert it


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco") #since model key exists it will not set the value to Bronco

print(x)
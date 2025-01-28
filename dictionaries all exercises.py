#ACCESSING ITEMS
print("ACCESSING ITEMS")
thisdict =	{"brand": "Ford","model": "Mustang","year": 1964}
x = thisdict["model"]
print("value of the 'model' key:\n",x)
#get method
print("get method")
y = thisdict.get("model")
print("value of the 'model' key using get method:\n",y)
#keys method
print("keys method")
z = thisdict.keys()
print("keys of dictionary:\n",z) #before the change
thisdict["color"] = "white"
print("keys of dictionary after change:\n",z) #after the change
#values method
print("values method")
value= thisdict.values()
print("values of dictionary:\n",value) #before the change
thisdict["year"] = 2020
print("values of dictionary after change:\n",value) #after the change
#Get Items
print("Get Items")
item = thisdict.items()
print("Displaying all items in dictionary:\n",item) #before the change
thisdict["color"] = "red"
print("Displaying all items in dictionary after change:\n",item) #after the change
#Check if Key Exists
print("Check if Key Exists")
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Change Values
print("Change Values")
thisdict["year"] = 2018
print("after changing value:\n",thisdict)
#changing Values using update()
print("changing Values using update()")
thisdict.update({"year": 2020})
print("after changing value using update():\n",thisdict)
#Adding Items
print("Adding Items")
thisdict["price"] = "1 Lakh"
print("after adding value:\n",thisdict)
#Adding Items using update()
print("Adding Items using update()")
thisdict.update({"price": "1 Lakh"})
print("after adding value using update():\n",thisdict)
#Removing Items
print("Removing Items using pop():")
thisdict.pop("model")
print("updated dictionary:\n",thisdict)
print("Removing Items using pop item():")
thisdict.popitem()
print("updated dictionary:\n",thisdict)#removes last entry
print("Removing Items using del keyword:")
mydict =	{"brand": "Ford","model": "Mustang","year": 1964}
del mydict["model"]
print("updated dictionary:\n",mydict)
print("Deleting dictionary using del keyword:")
#del mydict
#print("dictionary:",mydict)#it throws error dicitionary is not defined
print("Deleting dictionary using clear():")
mydict.clear()
print("dictionary:",mydict)
#Loop Through a Dictionary
print("Loop Through a Dictionary:")
for x in thisdict:
    print("Dictionary:",x,thisdict[x])
for x in thisdict.values():
    print("printing values using values():",x)
for x in thisdict.keys():
    print("printing values using keys():",x)
for x, y in thisdict.items():
    print("printing values using items():",x, y)
#Copy Dictionaries
print("copy dictionaries")
mydict = thisdict.copy()
print("copying dictionary:\n",mydict)
mydict = dict(thisdict)
print("copying dictionary using dict():\n",mydict)
#Nested Dictionaries
print("Nested Dictionaries")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("Nested Dictionaries\n",myfamily)
#creating one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#Loop Through Nested Dictionaries
for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

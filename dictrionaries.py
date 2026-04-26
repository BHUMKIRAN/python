#Dictionaries stores data in key value pairs
#dictionaries are ordered (since Python 3.7)
#dictionaries are changable
#dictionaries donot  contain duplicate values

a = {"name": "John", "age": 36, "country": "Norway"}
print(a)

#get values

print(a["name"])
print(a["age"])
print(a["country"])

print(a.get("name"))
print(a.get("age"))
print(a.get("country"))

print(a.keys())
print(a.values())
print(a.items())

#update dictionary

a["age"] = 37
print(a)

a.update({"country": "India"})
print(a)

#remove items

a.pop("age")
print(a)

a.popitem()
print(a)

del a["name"]
print(a)

#copy dictionary

b = a.copy()
print(b)

#use del keyword to delete the dictionary

del a

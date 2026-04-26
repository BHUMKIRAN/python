#sets can store multiple values in a single variable
#sets are unordered
#sets are unchangeable
#sets can contain duplicate values
#sets are mutable

a = {1, 2, 3, 4, 5}
print(a)
print(len(a))
print(type(a))

#add items to the set using add() method
a.add(6)
print(a)

#add multiple items to the set using update() method
a.update([7, 8, 9])
print(a)

#remove items from the set using remove() method
a.remove(9)
print(a)

#remove items from the set using discard() method
a.discard(8)
print(a)

#remove items from the set using pop() method
a.pop()
print(a)

#remove all items from the set using clear() method
a.clear()
print(a)

#delete the set using del keyword
del a
# print(a)

#union of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a | b)

#intersection of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a & b)

#difference of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a - b)

#symmetric difference of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a ^ b)

#subset of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a <= b)

#superset of sets
a = {1, 2, 3}
b = {4, 5, 6}
print(a >= b)

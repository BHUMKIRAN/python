# list are used to store multiples variables in a single variable

a = [10, 20, 30, 40, 50]
print(a)

print(len(a))

a.append(200)

print(a)

if 200 in a:
    print("200 is in the list")

a.append(a[0:2])
print(a)

a.extend([300, 400])
print(a)

# use list() to create the list

b = list(range(1, 10))
print(b)

# Access the list

print(b[1])
print(b[1:3])

if 9 in b:
    print(b.index(9))
    print(b.count(9))

# insert () method at the specific position

b.insert(2, 99)
print(b)

# append() method at the end
b.append(99)
print(b)


# extend() method to add multiple items
b.extend([300, 400])
print(b)

# removing methods
# using remove() - remove the specific value

b.remove(400)
print(b)

# using pop() - remove the last item (by default) or specific index

b.pop()
print(b)

# using  del - remove the specific index

del b[1]
print(b)

# using clear() - remove all the items

b.clear()
print(b)


# looping the items

c = ["kiran", "ram", "shyam", "sita", "laxman"]
print(c)

for i in c:
    print(i)

# sorting the list

c.sort()  # alphabetical order (ascending )
print(c)

# reverse the list

c.reverse()  # revers the alphabetical order (descending )
print(c)

c.sort()

# sorting function


def sorting(a):
    a.sort()
    return a


print(sorting(c))


# copy lists

a = list((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(a)

v = a.copy()
print(v)

# use slice operator to copy specific range

x = a[1:3]
print(x)


# join lists use extent() , + , loop

a = [1, 2, 3, 4, 5, ["kiran", "ram", "shyam", "sita", "laxman"]]
b = [6, 7, 8, 9, 10]

print(a + b)

for i in b:

    a.append(i)

print(a)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

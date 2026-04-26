# tuples can be ordered, unchangeable, and can contain duplicate values
a = (1, 2, 3, 4, 5)
print(a)

# Tuples are ordered, meaning they have a defined order that will not change.
# Tuples are unchangeable, meaning you cannot change the values of the elements in a tuple.
# Tuples can contain duplicate values, meaning you can have the same value multiple times in a tuple.

b = ("jrab", "arab", "bhum", 5)
c=((1,23,4,5,5,4))

d=["ram","hari"]
print(b)

#sorting 
#use tuple() constructor to create the tuples
#accessing elements in tuple 

print(len(b))
print(type(a))
print(type(c))
print(type(d))

#access tuples 

print (b[1])
#convert tuples to list and change the value

q = list(b)
print(q)

q.append("gita")
print(q)
#Unpack tuples , using asterisk(*) operator to assign the value 

fruits = ("apple", "banana", "cherry")

(*green, yellow) = fruits 

(w,z)= (1,2)
print(w)
print(z)


print(green)
print(yellow)





#loop through the tuples

for i in fruits:
    print(i)
#multiply tuples 

z=fruits * 2 + a
print(z)


#use tuple() method to create the tuples

v=tuple(("kiran","hari","sita","laxman","kiran","hari","sita","laxman"))
print(v)    

#tuple methods

print(v.count("kiran"))
print(v.index("kiran"))


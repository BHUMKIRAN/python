#iterator in python

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#it works with the next() function that will give the values one by one. it also remember the last value used 
#iter() function returns an iterator object.

mytext = "banana"
iterator = iter(mytext)

print(next(iterator))

#we can use the for loop to iterator through the iterable objects


#iterator in class

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
## _iter_  methods allows you to make an object iterable and can also make initialization of the object 
## and always return the iterator object from the method itself.

## __next__  method allows you to iterate through the object and always return the next value from the method.
## it's basically the doing operation of the next value from the object.
    def __next__(self):
       if( self.a <20) :
        x = self.a
        self.a += 1
        return x
       else:
        raise StopIteration
## StopIteration is an exception that is raised when the iterator is exhausted.

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#_init_methods is used to assign values to object properties

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

x = car("Toyota", "Corolla", 2022)
print(x.make)
print(x.model)
print(x.year)

# self is used to access the object properties

class kiran:
    def __init__(self ,age):
        self.age = age
    def display(self):
        print(self.age)

y=kiran(25)
y.display()

# _str_() method -> The _str_() method is used to return a string representation of the object.

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

x=car("Toyota", "Corolla", 2022)
print(x)    

# _del_() method -> The _del_() method is used to delete the object.

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __del__(self):
        print(f"{self.make} {self.model} {self.year} is deleted")


x=car("Toyota", "Corolla", 2022)
del x

# _repr_() method -> The _repr_() method is used to return a string representation of the object.

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __repr__(self):
        return f"{self.make} {self.model} {self.year}"

x=car("Toyota", "Corolla", 2022)
print(x)

# _add_() method -> The _add_() method is used to add two objects.      

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __add__(self, other):
        return self.year + other.year

x=car("Toyota", "Corolla", 2022)
y=car("Honda", "Civic", 2023)
print(x+y)    


# class and object


class student:
    a = tuple(("ram", "harish", "sita", "laxman"))


b = student()
print(b.a)

# built in method  _init_() method -> The __init__() method is used to assign values to object properties,
# or to perform operations that are necessary when the object is being created.


class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


t = teacher("kiran", 25)
t.display()
t = teacher("ram ", 23)
t.display()


# self parameter -> Without self, Python would not know which object's properties you want to access
class calculator:
    def add(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b

    def multiply(self, a, b):
        self.a = a
        self.b = b
        return self.a * self.b

    def divide(self, a, b):
        self.a = a
        self.b = b
        return self.a / self.b

    def subtract(self, a, b):
        self.a = a
        self.b = b
        return self.a - self.b

    def sqare(self, a):
        return a * a


y = calculator()

print(y.add(2, 3))
print(y.multiply(2, 3))
print(y.divide(2, 3))
print(y.subtract(2, 3))
print(y.sqare(5))

# class porperties
##Accessing class porperties using dot() method


class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(self.make, self.model, self.year)

    def add_car(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


x = car("Toyota", "Corolla", 2022)
x.display()

##Adding class porperties
x.add_car("Honda", "Civic", 2023)
x.display()


##Updating class porperties

x.__init__("ram", "civic", 2023)
print(x.make)
print(x.model)
print(x.year)

##Deleting class porperties
# class methods
# inheritance
# polymorphism
# encapsulation
# abstration

import random

# Global variable

x = 10
y = "kiran "


def printVariable():
    print("Value of x: " + str(x))
    print("Value of y: " + y)


printVariable()

# Local variable


def localVar():
    x = 20
    y = "Nitesh "
    print("Value of x: " + str(x))
    print("Value of y: " + y)
    print(type(y))


localVar()

# Global keyword


def globalVar():
    global x
    global y
    x = 100
    y = "Kiran "
    print("Value of x: " + str(x))
    print("Value of y: " + y)


globalVar()


# concatination


a = "ram"
b = "kumar"

print(a + b)
print(f"my name is {a} and my last name is {b}")  # f-string
print(2 + 3)


# type casting

x = int(10)
print(type(x))
print(x)

y = str(10)
print(type(y))
print(y)


z = float(10)
print(type(z))
print(z)


print(random.randint(5, 9))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = "hello world boys"
print(b[0])


for loop in b:
    print(loop)

if "hello" in b:
    print("hello is present in b")

print(b[2:5])
print(b[2:7:2])
print(b[:1])

# upper case
print(b.upper())
# lower case
print(b.lower())
# strip removes spaces from both sides
print(b.strip())
# replace replaces the word
print(b.replace("hello", "hi"))
# split splits the string into a list
print(b.split())

# concatinate

print("hello " + "kiran")

# format string
print(f"my name is {a} and my last name is {b}")
# type casting

print(type(a))
# random

print(random.randint(1, 10))

print(bool("kiran"))
print(bool(12) )
print(bool(["apple", "cherry", "banana"]))
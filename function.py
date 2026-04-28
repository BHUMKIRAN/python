# 1. Basic Function

# Function definition
# function name must start with letter or underscore


def tyrePressure(air, tyreSize):
    Pressure = air * tyreSize  # multiply values
    return Pressure  # return result


# function call
print(tyrePressure(10, 5))  # Output: 50


### Explanation:

# * `def` → defines a function
# * `air, tyreSize` → parameters
# * `return` → sends value back


# 2. Arbitrary Arguments (*args)

# Used when you don’t know how many arguments will be passed.


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(10, 20, 30))  # Output: 60


### Explanation:

# * `*args` collects values into a tuple
# * You can loop through it

# 3. Keyword Arguments (**kwargs)

# Used to pass named arguments.


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(display_info(name="John", age=30, city="New York"))


### Explanation:

# * `**kwargs` collects values into a dictionary
# * Access using `key` and `value`


# 4. Argument Unpacking


def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


list1 = range(1, 10)

print(sum_all(*list1))  # unpack list


### Explanation:

# * `*list1` → unpack values
# * Same as writing: `sum_all(1,2,3,...)`


# 5. Global Keyword


def update_global():
    global counter
    counter += 1
    print("Inside function:", counter)


counter = 0
update_global()
print("Outside function:", counter)


### Explanation:

# * `global` allows modifying global variable inside function

# 6. Nonlocal Keyword


def outer_function():
    counter = 0

    def inner_function():
        nonlocal counter
        counter += 1
        print("Inside function:", counter)

    inner_function()
    print("Outside function:", counter)


outer_function()


### Explanation:

# * `nonlocal` → used for variables in enclosing scope


# 7. Lambda Functions

# One-line anonymous functions.

sum = lambda a, b: a + b
print(sum(1, 2))  # Output: 3


### With map()


print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))


### With filter()


print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))


### Explanation:

# * `lambda` → quick function
# * Used for short operations


# 8. Decorators

# Used to modify existing functions.


def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


### Output:


# Before function
# Hello!
# After function


# 9. Recursion

# Function calling itself.


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120


### Explanation:

# * Must have **base case**
# * Used in problems like factorial, tree traversal


# 10. Generators

# Used to generate values one by one.


def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for num in count_up(5):
    print(num)


### Explanation:

# * `yield` → returns value but pauses function
# * Memory efficient


# | Concept   | Purpose                        |
# | --------- | ------------------------------ |
# | Function  | Reuse code                     |
# | *args     | Multiple inputs                |
# | **kwargs  | Named inputs                   |
# | global    | Modify global variable         |
# | nonlocal  | Modify outer function variable |
# | lambda    | Short function                 |
# | decorator | Modify function behavior       |
# | recursion | Self-calling function          |
# | generator | Efficient iteration            |


# Use:

# * **normal functions** → most cases
# * **lambda** → small quick tasks
# * **decorators** → advanced (web frameworks like Flask/Django)
# * **generators** → large data handling

#range (start,end,step)

print(list(range(1,10,2)))
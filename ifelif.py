# Conditions and statments

a = 20
b = 30

# Equal
# Not equal
# Greater then
# Less then
# Greater then or equal to
# Less then or equal to

if a == b:
    print("Equal")
elif a > b:
    print("a is greater")
else:
    print("b is greater")

if a != b:
    print("Not Equal")

if a >= b:
    print("Greater than or Equal to")

if a <= b:
    print("Less than or Equal to")

if a < b:
    print("Less than")

if a == b:
    print("a and b are equal")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are not equal")


# logical operators

# and
# or
# not

if a > b and a == b:
    print("a is greater than or equal to b")

elif a > b or a == b:
    print("a is greater than or equal to b")

if not (a > b):
    print("a is not greater than b")

# pass statment in if and elif and else

value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass  # Zero case - no action needed
else:
    print("Positive value")

# The pass statement is useful in several situations:

# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement l

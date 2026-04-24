from variable import localVar


def kiran():
    print("Hello Kiran")


def echo():
    try:
        kiran()
    except Exception as e:
        print(f"Error: {e}")


# Calling the function
echo()

print("Welcome to Python Practice 🚀")

name = "Kiran"
print("Hello", name)


print(localVar())

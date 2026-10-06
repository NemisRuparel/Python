# None

# Assigning None
value = None

print("Value:", value)
print("Type:", type(value))


# Checking for None
name = None

if name is None:
    print("Name is not set")


# Checking for a Value
name = "Nemis"

if name is not None:
    print("Name:", name)


# None in Functions
def greet():
    print("Hello")


result = greet()

print("Return value:", result)


# None vs 0
a = None
b = 0

print("None == 0:", a == b)


# None vs Empty String
a = None
b = ""

print("None == Empty String:", a == b)
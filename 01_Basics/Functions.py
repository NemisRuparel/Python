# Functions

def add(a, b):
    return a + b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add(a, b)

print("Sum =", result)



# Another way

def difference(a, b):
    return a - b

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = difference(a, b)

    print("Difference =", result)


main()
# Input and Output

# Taking inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Normal Print
print("\nHello", name)
print("Your age is", age,end="\n\n")
print("Hello " + name + ", you are " + str(age) + " years old.",end="\n\n")

# printing " " inside print statement 
print("Hello \"World\"")
print("Hello 'World'")
print('Hello "World"',end='\n\n')

#format-String print
print(f"Hello {name}, you are {age} years old.")


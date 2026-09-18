# String Formatting, F-String and String Methods

name = "Nemis"
course = "Python"
age = 20

# String Formatting using format()
print("My name is {} and I am {} years old.".format(name, age))

# F-String
print(f"I am learning {course}.")

# F-String with expression
a = 10
b = 20
print(f"Sum of {a} and {b} = {a + b}")

# String Methods
text = "  python programming  "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title:", text.title())
print("Without spaces:", text.strip())
print("Replace:", text.replace("python", "Java"))
print("Split:", text.split())

# Other string methods
language = "Python Programming"

print("Find:", language.find("Programming"))
print("Count:", language.count("m"))
print("Starts with Python:", language.startswith("Python"))
print("Ends with Programming:", language.endswith("Programming"))
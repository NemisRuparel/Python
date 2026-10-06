# Lists

# Creating a List
fruits = ["Apple", "Banana", "Mango"]

print("Fruits:", fruits)

# Accessing List Items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Changing an Item
fruits[1] = "Orange"
print("After changing:", fruits)

# Adding Items
fruits.append("Grapes")
print("After adding:", fruits)

# Removing an Item
fruits.remove("Orange")
print("After removing:", fruits)

# List Length
print("Number of fruits:", len(fruits))

# Checking an Item
print("Apple" in fruits)

# Iterating Through a List
for fruit in fruits:
    print(fruit)